---
name: vistella-image-gen
description: Generate and edit high-fidelity AI images using Vistella's unified visual cloud API.
version: 1.0.0
author: Ethon1130
repository: https://github.com/Ethon1130/vistella
---

# Vistella Image Generation Skill for AI Agents

Equips AI coding assistants and autonomous agents (such as Claude Code, Cursor, OpenClaw, and AutoGen) with the ability to synthesize, edit, and orchestrate AI visual generation tasks via the Vistella platform.

## 🔑 Authentication

Set the API Key in your environment:

```bash
export VISTELLA_API_KEY="your_vistella_api_key"
```

Keys can be generated from the [Vistella Developer Dashboard](https://www.vistella.xyz/dashboard/settings?utm_source=github&utm_medium=agent_skill).

---

## 🛠️ Tool Schema: `generate_image`

### Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `prompt` | string | Yes | Detailed natural language prompt describing the image. |
| `aspect_ratio` | string | No | Desired image aspect ratio. Options: `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`. Default: `1:1`. |
| `negative_prompt` | string | No | Elements to exclude or diminish in the generated visual. |

---

## 💻 Workflow Example (HTTP REST)

### 1. Submit Generation Task
```http
POST https://www.vistella.xyz/api/v1/tasks
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

{
  "prompt": "Minimalist geometric logo of an origami hummingbird in flight, pure white background, vector style",
  "aspect_ratio": "1:1"
}
```

Response:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "task_id": "tsk_8f9104b2a",
    "status": "pending"
  }
}
```

### 2. Poll for Result
```http
GET https://www.vistella.xyz/api/v1/tasks/tsk_8f9104b2a
Authorization: Bearer YOUR_API_KEY
```

Response:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "task_id": "tsk_8f9104b2a",
    "status": "succeeded",
    "output": {
      "url": "https://cdn.vistella.xyz/outputs/tsk_8f9104b2a.png",
      "width": 1024,
      "height": 1024
    }
  }
}
```
