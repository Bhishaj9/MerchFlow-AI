import sys
import subprocess
import re

def patch_dashboard():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Locate the setTimeout block inside startBtn.addEventListener and replace it with fetch logic
    pattern = re.compile(r"setTimeout\(\(\) => \{[\s\S]*?\}, 1500\);", re.DOTALL)
    
    new_block = """try {
                const formData = new FormData();
                formData.append('file', fileInput.files[0]);
                
                const response = await fetch('/generate-catalog', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                jsonOutput.textContent = JSON.stringify(data, null, 2);
                isCatalogGenerated = true;
            } catch (error) {
                console.error("Error generating catalog:", error);
            } finally {
                startBtn.innerHTML = '<div class="absolute inset-0 flex items-center justify-center gap-2 lg:gap-3 relative z-10"><span class="text-white text-base lg:text-lg font-bold tracking-wide group-hover:scale-105 transition-transform">Start Agent Workflow</span><span class="material-symbols-outlined text-white text-lg lg:text-xl group-hover:translate-x-1 transition-transform">arrow_forward</span></div>';
                startBtn.disabled = false;
                startBtn.classList.add('animate-pulse-slow', 'animate-glow-pulse');
            }"""

    if not pattern.search(content):
        print("Error: Could not find the target setTimeout block in dashboard.html.")
        return False

    new_content = pattern.sub(new_block, content)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully patched dashboard.html")
    return True

def run_git_commands():
    commands = [
        ['git', 'add', 'dashboard.html'],
        ['git', 'commit', '-m', 'Bugfix: Restore real API connection to Glassmorphism UI'],
        ['git', 'push', '--force', 'space', 'HEAD:main']
    ]
    
    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Command failed with {result.returncode}: \\n{result.stderr}")
            # Don't break here, let it try the other commands just in case, though push might fail if commit fails.
            if cmd[1] == 'commit' and "nothing to commit" in result.stdout + result.stderr:
                continue
            if cmd[1] == 'push':
                pass
        else:
            print(f"Success!\\n{result.stdout}")

if __name__ == '__main__':
    if patch_dashboard():
        run_git_commands()
