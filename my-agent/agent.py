import os
import sys
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

question = " ".join(sys.argv[1:]) or "In two sentences, what is Docker and why do AI engineers use it?"

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": question}],
)

print(response.content[0].text)