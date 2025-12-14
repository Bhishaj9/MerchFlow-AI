import csv
import time
import os
import datetime
from agents.trend_spotter import TrendSpotter
from agents.visionary import Visionary

class MerchManager:
    def __init__(self):
        self.trend_spotter = TrendSpotter()
        self.visionary = Visionary()
        self.results_dir = "results"
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

    def generate_batch(self, niche: str) -> str:
        # Step 1: Get slogans
        print(f"🔍 Analyzing trends for niche: {niche}...")
        slogans = self.trend_spotter.get_trends(niche)
        
        results = []
        
        # Step 2: Generate art prompts
        print(f"🎨 Generating designs for {len(slogans)} slogans...")
        for i, slogan in enumerate(slogans):
            print(f"Generating design {i+1}/{len(slogans)}...")
            prompt = self.visionary.generate_art_prompt(slogan, niche)
            results.append({
                "Niche": niche,
                "Slogan": slogan,
                "Art Prompt": prompt
            })
            time.sleep(10)

        # Step 3 & 4: Save to CSV
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"merch_batch_{niche}_{timestamp}.csv"
        filepath = os.path.join(self.results_dir, filename)

        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Niche", "Slogan", "Art Prompt"])
            writer.writeheader()
            writer.writerows(results)
            
        print(f"✅ Batch complete! Saved to {filepath}")
        return filename
