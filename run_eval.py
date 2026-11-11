import json
import os
from anthropic import Anthropic

MODEL = os.environ.get("MODEL", "claude-sonnet-5-5")

client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

os.makedirs("results", exist_ok=True)

with open("data/prompts.jsonl") as f:
    prompts = [json.loads(line) for line in f if line.strip()]

with open("results/responses.jsonl", "w") as out:
    for p in prompts:
        reply = client.messages.create(
            model=MODEL,
            max_tokens=300,
            temperature=0,
            messages=[{"role": "user", "content": p["question"]}],
        )
        text = reply.content[0].text
        record = {**p, "model": MODEL, "response": text}
        out.write(json.dumps(record) + "\n")
        print(f"[{p['id']}] {p['type']}: {text[:80]}...")

print(f"\nSaved {len(prompts)} replies to results/responses.jsonl")
