import OpenAI from "openai";
import "dotenv/config";

const client = new OpenAI({
  apiKey: process.env.DEEPSEEK_API_KEY,
  baseURL: "https://api.deepseek.com",
});

const MODEL = process.env.LLM_MODEL ?? "deepseek-chat";

const response = await client.chat.completions.create({
  model: MODEL,
  max_tokens: 256,
  messages: [{ role: "user", content: "Что такое нейросеть в одном предложении?" }],
});

const content = response.choices[0].message.content;

process.stdout.write((response.choices[0].message.content ?? "") + "\n");
