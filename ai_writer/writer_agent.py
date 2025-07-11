from openai import OpenAI

class WriterAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def spin_chapter(self, content):
        prompt = f"Rewrite this content in a modern, engaging way:\n{content}"
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content