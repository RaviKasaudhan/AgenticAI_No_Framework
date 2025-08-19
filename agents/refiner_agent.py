from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, name="RefinerAgent", max_retries=4, verbose=True):
        super().__init__(name, max_retries, verbose)

    def execute(self, text):
        messages = [
            {"role": "system", "content": "You are an expert editor who refines and enhances articles for clarity, coherence, and professionalism."},
            {"role": "user", "content": (
                "Please carefully review and refine the following article draft. "
                "Improve its language, clarity, logical flow, grammar, and overall quality. "
                "Ensure the article is well-structured, concise, and suitable for publication. "
                "Do not add new information; only enhance what is present.\n\n"
                f"Article Draft:\n{text}\n\n"
                "Refined Article:"
            )}
        ]
        refined_text = self.call_openai(messages, temperature=0.3, max_tokens=400)
        return refined_text
