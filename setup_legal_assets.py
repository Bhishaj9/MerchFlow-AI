import os
import subprocess
from pathlib import Path

def create_legal_assets():
    # Create legal directory
    os.makedirs("legal", exist_ok=True)
    
    # Define MSA content
    msa_content = """# Master Service Agreement

**Parties:** "Bhishaj Technologies (MSME URN: UDYAM-UP-02-0108589)" (The Consultant) AND "[Client Name]" (The Client).

## Clause 1: Payment & MSME Protection
Strict adherence to the Micro, Small and Medium Enterprises Development (MSMED) Act, 2006. Pursuant to Section 15, all payments must be settled within forty-five (45) days of invoice date. Delayed payments shall attract compound interest at three times (3x) the bank rate notified by the Reserve Bank of India, as mandated by Section 16 of the Act.

## Clause 2: Intellectual Property Rights
Background IP (including pre-existing code, libraries, and agents) remains the sole property of the Consultant. Custom deliverables become Client property only upon full and final settlement of all dues.

## Clause 3: Future Transfer (Successor Entity)
Assignment of Rights: Bhishaj Technologies (The Consultant) reserves the right to assign or transfer all rights, duties, and intellectual property created under this agreement to a successor corporate entity or affiliate (e.g., Bhishaj Labs Pvt Ltd) upon formal incorporation, without requiring further consent from the Client.

## Clause 4: Confidentiality
Both parties agree to hold in strict confidence any proprietary or confidential information, including trade secrets, disclosed during the course of this agreement. Such information shall not be used for any purpose other than the performance of obligations under this agreement, nor disclosed to any third party without prior written consent.
"""

    # Write MSA_TEMPLATE.md
    Path("legal/MSA_TEMPLATE.md").write_text(msa_content, encoding="utf-8")

def deploy_assets():
    commands = [
        ["git", "add", "legal/"],
        ["git", "commit", "-m", "Add Master Service Agreement template with MSME & Successor clauses"],
        ["git", "push", "space", "clean_deploy:main"]
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

if __name__ == "__main__":
    create_legal_assets()
    deploy_assets()
