Write-Host "🚀 Killing stuck Node.js processes..." -ForegroundColor Yellow
Stop-Process -Name "node" -Force -ErrorAction SilentlyContinue
Write-Host "✅ Ports cleared." -ForegroundColor Green

Write-Host "🚀 Starting n8n with Tunnel..." -ForegroundColor Yellow
# This starts n8n and keeps the window open
npx n8n start --tunnel