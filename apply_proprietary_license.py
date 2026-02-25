#!/usr/bin/env python3
"""Apply proprietary licensing updates and deploy git changes."""

from __future__ import annotations

import subprocess
from pathlib import Path

LICENSE_TEXT = """Copyright © 2026 Bhishaj Technologies.
This software and its documentation are the confidential and proprietary
information of Bhishaj Technologies (URN: UDYAM-UP-02-0108589).
Unauthorized copying, distribution, or use of this source code
is strictly prohibited. Use is governed by the signed Master Service Agreement.
All Rights Reserved.
"""

MIT_BADGE_LINE = "![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)"
FOOTER = "---\n**🛡️ Maintained by Bhishaj Technologies (UDYAM-UP-02-0108589). All Rights Reserved.**\n"


def overwrite_license_file() -> None:
    Path("LICENSE").write_text(LICENSE_TEXT, encoding="utf-8")


def sanitize_readme() -> None:
    readme_path = Path("README.md")
    readme = readme_path.read_text(encoding="utf-8")

    filtered_lines = [line for line in readme.splitlines() if line.strip() != MIT_BADGE_LINE]
    sanitized = "\n".join(filtered_lines).rstrip("\n")

    if FOOTER.strip() not in sanitized:
        sanitized = f"{sanitized}\n\n{FOOTER}"
    else:
        sanitized = f"{sanitized}\n"

    readme_path.write_text(sanitized, encoding="utf-8")


def run_git_commands() -> None:
    commands = [
        ["git", "add", "LICENSE", "README.md"],
        ["git", "commit", "-m", "Switch to Proprietary License (Bhishaj Technologies)"],
        ["git", "push", "space", "clean_deploy:main"],
    ]
    for command in commands:
        subprocess.run(command, check=True)


def main() -> None:
    overwrite_license_file()
    sanitize_readme()
    run_git_commands()


if __name__ == "__main__":
    main()
