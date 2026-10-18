#!/bin/bash
# Vistella Image API - cURL Quickstart

# 1. Replace with your actual API key
export VISTELLA_API_KEY="your_api_key_here"

# 2. Submit task
echo "Submitting task..."
RESPONSE=$(curl -s -X POST "https://www.vistella.xyz/api/v1/tasks" \
  -H "Authorization: Bearer ${VISTELLA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "Cinematic portrait of a cyberpunk wanderer in rainy Neo-Tokyo, 8k",
    "aspect_ratio": "16:9"
  }')

echo "Task Response: $RESPONSE"

# Extract task_id using python or jq
TASK_ID=$(echo $RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['data']['task_id'])")
echo "Created Task ID: $TASK_ID"

# 3. Poll for result
echo "Polling for result..."
while true; do
  POLL_RESPONSE=$(curl -s "https://www.vistella.xyz/api/v1/tasks/${TASK_ID}" \
    -H "Authorization: Bearer ${VISTELLA_API_KEY}")
  
  STATUS=$(echo $POLL_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
  echo "Current status: $STATUS"

  if [ "$STATUS" = "succeeded" ]; then
    IMAGE_URL=$(echo $POLL_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['data']['output']['url'])")
    echo "Success! Image URL: $IMAGE_URL"
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Task failed!"
    break
  fi

  sleep 2
done
