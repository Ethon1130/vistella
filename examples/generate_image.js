/**
 * Vistella AI Image Generation - Node.js Fetch Quickstart
 * Docs: https://www.vistella.xyz/docs
 */

const API_KEY = process.env.VISTELLA_API_KEY;
const BASE_URL = "https://www.vistella.xyz/api/v1";

async function generateImage({ prompt, model = "gpt-image-2", aspectRatio = "16:9" }) {
  if (!API_KEY) {
    console.error("[Error] VISTELLA_API_KEY environment variable is not set.");
    console.error("Obtain your key from https://www.vistella.xyz/dashboard/settings");
    process.exit(1);
  }

  const headers = {
    Authorization: `Bearer ${API_KEY}`,
    "Content-Type": "application/json",
  };

  // 1. Submit task
  console.log(`Submitting task to Vistella (${model})...`);
  const createRes = await fetch(`${BASE_URL}/tasks`, {
    method: "POST",
    headers,
    body: JSON.stringify({
      model,
      prompt,
      aspect_ratio: aspectRatio,
    }),
  });

  const createJson = await createRes.json();
  if (!createRes.ok || createJson.code !== 200) {
    throw new Error(`Task submission failed: ${JSON.stringify(createJson)}`);
  }

  const taskId = createJson.data.task_id;
  console.log(`Task submitted successfully. ID: ${taskId}`);

  // 2. Poll for completion
  while (true) {
    await new Promise((r) => setTimeout(r, 2000));
    const pollRes = await fetch(`${BASE_URL}/tasks/${taskId}`, { headers });
    const pollJson = await pollRes.json();

    const status = pollJson.data.status;
    if (status === "succeeded") {
      console.log("Generation complete!");
      return pollJson.data.output.url;
    } else if (status === "failed") {
      throw new Error(`Generation failed: ${pollJson.data.error || "Unknown"}`);
    }
    process.stdout.write("Waiting for output...\r");
  }
}

// Run example
generateImage({
  prompt: "Minimalist glowing geometric crystal sculpture on wet dark stone, volumetric beam of blue light, 8k",
  model: "flux-schnell",
  aspectRatio: "1:1",
})
  .then((url) => console.log("\nImage output URL:", url))
  .catch(console.error);
