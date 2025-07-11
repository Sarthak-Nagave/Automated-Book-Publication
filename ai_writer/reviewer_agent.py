from openai import OpenAI

class ReviewerAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def review_chapter(self, content):
        prompt = f"Proofread and improve the clarity and flow:\n{content}"
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content