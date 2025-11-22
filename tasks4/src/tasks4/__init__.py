import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Please add it as a user environment variable and restart VS Code.")

client = OpenAI(api_key=api_key)


def summarize_text(paragraph: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the following task in 3–6 words."},
            {"role": "user", "content": paragraph},
        ],
    )
    return response.choices[0].message.content.strip()

def main() -> None:
    paragraphs = [
        "I need to clean my room. It has been messy for a week because I've been busy with work and school. I want to put away my clothes, vacuum the floor, and reorganize my desk.",
        "Finish writing the introduction of my Buddhism paper. It must mention the historical origins, explain why the text is important, and connect to my thesis.",
    ]

    for p in paragraphs:
        summary = summarize_text(p)
        print("Paragraph:", p)
        print("Summary:", summary)
        print("-" * 40)
