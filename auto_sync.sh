#!/bin/bash

# This script will continuously monitor the folder and auto-commit/push changes.
# It runs a sync loop every 10 seconds.

echo "Starting realtime synchronization with GitHub..."

while true; do
    # Fetch changes from remote
    git fetch origin main > /dev/null 2>&1
    
    # Check if there are any local changes
    if ! git diff-index --quiet HEAD --; then
        echo "Changes detected. Syncing..."
        git add .
        git commit -m "Auto-sync update: $(date)" > /dev/null 2>&1
        
        # Try to rebase/pull to avoid conflicts, then push
        git pull --rebase origin main > /dev/null 2>&1
        git push origin main > /dev/null 2>&1
        echo "Sync complete."
    fi
    
    sleep 10
done
