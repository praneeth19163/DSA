# Daily DSA Commit Script
# This script automatically commits and pushes daily DSA practice to GitHub

Set-Location "C:\Users\praneeth\Downloads\praneeth1\DSA"

# Get current date in format: Jun 11, 2026
$date = Get-Date -Format "MMM dd, yyyy"

# Check if there are any changes
$status = git status --porcelain
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "No changes to commit." -ForegroundColor Yellow
    exit
}

# Add all changes
git add .

# Create commit with date
git commit -m "Daily DSA practice - $date"

# Push to GitHub
git push

Write-Host "✓ Daily commit pushed successfully!" -ForegroundColor Green
Write-Host "Date: $date" -ForegroundColor Cyan
