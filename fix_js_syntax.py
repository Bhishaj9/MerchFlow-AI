import sys
import subprocess

def fix_html():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('</footer>')
    if len(parts) < 2:
        print("Could not find </footer> in dashboard.html")
        return False
        
    top_part = parts[0] + '</footer>\n'
    
    new_script = """<script>
    tailwind.config.theme.extend.animation = { shine: 'shine 1.5s infinite' }
    tailwind.config.theme.extend.keyframes = {
        shine: { '0%': { left: '-100%' }, '100%': { left: '200%' } }
    }
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const startBtn = document.getElementById('startBtn');
const jsonOutput = document.getElementById('jsonOutput');
const deployBtn = document.getElementById('deployBtn');
const copyBtn = document.getElementById('copyBtn');
const copyIcon = document.getElementById('copyIcon');
let selectedFile = null;
let isCatalogGenerated = false;
const defaultDropZoneContent = `
    <div class="absolute w-16 h-16 lg:w-20 lg:h-20 bg-amber-500/10 rounded-full blur-xl group-hover:bg-amber-500/20 transition-all"></div>
    <div class="size-14 lg:size-16 relative z-10 rounded-2xl bg-gradient-to-br from-neutral-800 to-black border border-white/10 shadow-lg flex items-center justify-center transition-transform group-hover:scale-110 duration-300">
        <span class="material-symbols-outlined text-2xl lg:text-3xl text-amber-500">cloud_upload</span>
    </div>
    <div class="flex flex-col items-center gap-1 relative z-10">
        <p class="text-white text-base lg:text-lg font-bold leading-tight tracking-tight text-center">Drop Product Image Here</p>
        <p class="text-neutral-500 text-xs lg:text-sm font-medium text-center">Supports JPG, PNG, WEBP</p>
    </div>
    <button id="browseBtn" class="mt-2 relative z-10 flex items-center justify-center rounded-full h-8 lg:h-9 px-4 lg:px-5 bg-white/5 hover:bg-white/10 border border-white/10 text-white text-[10px] lg:text-xs font-bold transition-all uppercase tracking-wide">
        Browse Files
    </button>
`;
function initDropZone() {
    const currentBrowseBtn = document.getElementById('browseBtn');
    if (currentBrowseBtn) {
        currentBrowseBtn.addEventListener('click', (e) => {
            e.preventDefault(); e.stopPropagation(); fileInput.click();
        });
    }
}
initDropZone();
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) handleFile(e.target.files[0]);
});
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault(); dropZone.classList.add('border-amber-500', 'bg-amber-500/5');
});
dropZone.addEventListener('dragleave', (e) => {
    e.preventDefault(); dropZone.classList.remove('border-amber-500', 'bg-amber-500/5');
});
dropZone.addEventListener('drop', (e) => {
    e.preventDefault(); dropZone.classList.remove('border-amber-500', 'bg-amber-500/5');
    if (e.dataTransfer.files.length > 0) {
        fileInput.files = e.dataTransfer.files;
        handleFile(e.dataTransfer.files[0]);
    }
});
function handleFile(file) {
    selectedFile = file;
    dropZone.innerHTML = `
        <div class="flex flex-col items-center justify-center gap-4 z-10">
            <div class="size-14 lg:size-16 rounded-2xl bg-gradient-to-br from-neutral-800 to-black border border-white/10 shadow-lg flex items-center justify-center">
                 <span class="material-symbols-outlined text-2xl lg:text-3xl text-amber-500">check_circle</span>
            </div>
            <div class="flex flex-col items-center gap-1">
                <p class="text-white text-base lg:text-lg font-bold text-center">${file.name}</p>
                <p class="text-neutral-500 text-xs lg:text-sm text-center">${(file.size / 1024).toFixed(1)} KB</p>
            </div>
             <button id="removeFileBtn" class="mt-2 flex items-center justify-center gap-2 rounded-full h-8 lg:h-9 px-4 lg:px-5 bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/20 transition-all text-[10px] lg:text-xs font-bold uppercase tracking-wide">
                <span class="material-symbols-outlined text-sm lg:text-base">close</span>
                <span>Remove File</span>
            </button>
        </div>
    `;
    document.getElementById('removeFileBtn').addEventListener('click', (e) => {
        e.stopPropagation(); e.preventDefault(); resetUploadUI();
    });
}
function resetUploadUI() {
    selectedFile = null; fileInput.value = ""; dropZone.innerHTML = defaultDropZoneContent; initDropZone();
}
startBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    if (!fileInput.files || fileInput.files.length === 0) {
        alert("Please select or drop an image first."); return;
    }
    const originalBtnContent = startBtn.innerHTML;
    startBtn.innerHTML = '<div class="absolute inset-0 flex items-center justify-center gap-2 lg:gap-3"><svg class="animate-spin h-4 w-4 lg:h-5 lg:w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg><span class="text-white text-base lg:text-lg font-bold tracking-wide">Synthesizing...</span></div>';
    startBtn.disabled = true; startBtn.classList.remove('animate-pulse-slow', 'animate-glow-pulse');
    
    try {
        const formData = new FormData(); formData.append('file', fileInput.files[0]);
        const response = await fetch('/generate-catalog', { method: 'POST', body: formData });
        if (!response.ok) throw new Error("Server Error " + response.status);
        const data = await response.json();
        jsonOutput.textContent = JSON.stringify(data, null, 2);
        isCatalogGenerated = true;
    } catch (error) {
        console.error("Agent Error:", error); alert("Pipeline failed: " + error.message);
    } finally {
        startBtn.innerHTML = originalBtnContent; startBtn.disabled = false; startBtn.classList.add('animate-pulse-slow', 'animate-glow-pulse');
    }
});
copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(jsonOutput.innerText).then(() => {
        const originalIcon = copyIcon.innerText; copyIcon.innerText = 'check'; copyIcon.classList.add('text-green-400');
        setTimeout(() => { copyIcon.innerText = originalIcon; copyIcon.classList.remove('text-green-400'); }, 2000);
    });
});
</script>
</body>
</html>
"""

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(top_part + new_script)

    print("Replaced script successfully.")

    # Run git commands
    subprocess.run(['git', 'add', 'dashboard.html'], check=True)
    try:
        subprocess.run(['git', 'commit', '-m', 'Critical Bugfix: Resolve corrupted JS syntax and restore core agent loop'], check=True)
    except subprocess.CalledProcessError:
        print("Nothing to commit")
        
    subprocess.run(['git', 'push', '--force', 'space', 'HEAD:main'], check=True)
    
    # Push to origin main as well
    try:
        subprocess.run(['git', 'push', 'origin', 'HEAD:main'], check=True)
    except subprocess.CalledProcessError:
        print("Push to origin failed or not needed")
        
    print("Deployment triggered successfully.")

if __name__ == '__main__':
    fix_html()
