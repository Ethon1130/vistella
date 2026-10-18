"""
Vistella AI Image Generation - Python SDK Quickstart
Docs: https://www.vistella.xyz/docs
"""

import os
import sys
import time
import requests

API_KEY = os.getenv("VISTELLA_API_KEY")
BASE_URL = "https://www.vistella.xyz/api/v1"


def generate_image(prompt: str, model: str = "gpt-image-2", aspect_ratio: str = "16:9") -> str:
    if not API_KEY:
        print("[Error] VISTELLA_API_KEY environment variable is not set.")
        print("Obtain your key from https://www.vistella.xyz/dashboard/settings")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 1. Submit async task
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio
    }

    print(f"Submitting task to Vistella (model: {model})...")
    res = requests.post(f"{BASE_URL}/tasks", json=payload, headers=headers)
    if res.status_code != 200:
        raise RuntimeError(f"Submission failed: {res.status_code} {res.text}")

    data = res.json()["data"]
    task_id = data["task_id"]
    print(f"Task accepted: {task_id}")

    # 2. Poll until terminal state
    start_time = time.time()
    while True:
        status_res = requests.get(f"{BASE_URL}/tasks/{task_id}", headers=headers)
        if status_res.status_code != 200:
            raise RuntimeError(f"Poll error: {status_res.status_code} {status_res.text}")

        res_data = status_res.json()["data"]
        status = res_data["status"]

        if status == "succeeded":
            elapsed = time.time() - start_time
            image_url = res_data["output"]["url"]
            print(f"Done in {elapsed:.1f}s! Image URL: {image_url}")
            return image_url
        elif status == "failed":
            error_msg = res_data.get("error", "Unknown error")
            raise RuntimeError(f"Task failed: {error_msg}")

        print("Waiting for generation...", end="\r")
        time.sleep(2)


if __name__ == "__main__":
    prompt = "A futuristic eco-city built into a lush canyon, solar glass bridges, hanging botanical gardens, 8k"
    url = generate_image(prompt=prompt, model="gpt-image-2", aspect_ratio="16:9")
    print("\nView your result at:", url)
