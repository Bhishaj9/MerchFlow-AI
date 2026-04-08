## 2025-04-08 - [Path Traversal Fix]
**Vulnerability:** A path traversal vulnerability was discovered in the `/generate-catalog` endpoint of `main.py`. The uploaded file's original name `file.filename` was directly concatenated into the temporary file path `f"uploads/{file.filename}"`. This could allow an attacker to send a manipulated filename (e.g., `../../../etc/passwd` or `../../../root/.bashrc`) resulting in file writes to arbitrary locations on the host.
**Learning:** This codebase relies on temporary saving of user uploads before passing them to the visual analysis agent. Blindly trusting `file.filename` without sanitation is inherently unsafe because FastAPI does not guarantee `file.filename` is purely a basename; it reflects whatever the client provided.
**Prevention:** Always discard the client-provided filename entirely (or heavily sanitize it via `os.path.basename` and regex) when writing files to the filesystem. In this scenario, we use `uuid.uuid4().hex` to generate a completely randomized, safe filename while preserving only the file extension.

## 2025-05-15 - [Missing CORS Configuration]
**Vulnerability:** The FastAPI application was initialized without `CORSMiddleware`. This means that by default, it didn't have a defined Cross-Origin Resource Sharing policy, which could lead to issues when accessed from different frontends or potentially expose it to certain CSRF-related risks if not properly configured.
**Learning:** FastAPI requires explicit middleware attachment to handle CORS. Without it, the application lacks standard web security headers that control which domains can access the API.
**Prevention:** Always configure `CORSMiddleware` immediately after FastAPI instantiation. Use `allow_origins=["*"]` with `allow_credentials=False` for public APIs, or specify explicit origins if the consumer domains are known.

## 2025-06-10 - [Unsafe Subprocess Execution Fix]
**Vulnerability:** The `create_dockerfile.py` script used `subprocess.run(command, shell=True)`, which is vulnerable to shell injection if any part of the command string is derived from untrusted input. While the current commands were hardcoded, this pattern is inherently risky.
**Learning:** Using `shell=True` allows the shell to interpret special characters like `;`, `&`, and `|`, which can be exploited to execute arbitrary commands.
**Prevention:** Avoid `shell=True` whenever possible. Instead, pass the command as a list of arguments. Use `shlex.split()` to safely parse command strings into argument lists if needed.

### Fixed Path Traversal via Unsanitized File Extension

*   **Date:** $(date +%Y-%m-%d)
*   **Vulnerability:** A path traversal vulnerability was present in the `main.py` application file upload handling. The application extracted the file extension from user-submitted file names using `os.path.splitext()`. However, `os.path.splitext()` does not properly strip path traversal characters (such as `\..\`) if the path is evaluated on a Linux backend that considers `\` as part of the filename. This allowed an attacker to inject paths directly into the extension part of the filename (e.g. `file_extension` could become `.\\etc\\passwd`).
*   **Fix:** Instead of trusting the parsed extension directly, the extraction logic was rewritten to check the extracted extension against a strict whitelist of known-safe extensions (`ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".heic"}`). If the extracted extension does not exactly match one of the allowed extensions, it defaults to an empty string. The `ALLOWED_EXTENSIONS` set was also moved to the module level to optimize memory allocations during requests.
*   **Recommendation:** Never trust or construct filesystem paths directly from user input. Always use secure whitelisting when handling uploaded file metadata (including file names and extensions), as cross-platform discrepancies in path handling APIs (like `os.path.splitext()`) can be abused to bypass naïve sanitization.
