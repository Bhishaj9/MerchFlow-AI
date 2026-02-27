import sys
import subprocess
import re

def fix_html():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_snippet = """
        const browseBtn = document.getElementById('browseBtn');
        browseBtn.addEventListener('click', (e) => {
            e.preventDefault();
            fileInput.click();
        });
        fileInput.addEventListener('change', () => {
            if (fileInput.files.length > 0) {
                // Provide a visual cue that a file was selected
                const fileName = fileInput.files[0].name;
                browseBtn.innerHTML = `<span class="material-symbols-outlined text-xl">check_circle</span> ${fileName}`;
            }
        });
"""

    if "browseBtn.addEventListener('click', (e) => {" in content and "Provide a visual cue that a file was selected" in content:
        print("Snippet already exists. Skipping injection.")
    else:
        # Find where the DOM elements are defined
        target = "const downloadBtn = document.getElementById('downloadBtn');"
        if target in content:
            new_content = content.replace(target, target + "\n" + js_snippet)
            with open('dashboard.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Injected JS successfully.")
        else:
            print("Could not find insertion point!")
            return False
            
    # Run git commands
    subprocess.run(['git', 'add', 'dashboard.html'], check=True)
    try:
        subprocess.run(['git', 'commit', '-m', 'Bugfix: Wire up Browse Files button to hidden input'], check=True)
    except subprocess.CalledProcessError:
        print("Nothing to commit")
        
    subprocess.run(['git', 'push', '--force', 'space', 'HEAD:main'], check=True)
    
    # Push to origin main as well
    try:
        subprocess.run(['git', 'push', 'origin', 'HEAD:main'], check=True)
    except subprocess.CalledProcessError:
        print("Push to origin failed or not needed")
        
    print("Deployment triggered successfully.")
    return True

if __name__ == '__main__':
    fix_html()
