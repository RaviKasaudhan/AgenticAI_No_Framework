from .agent_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, name="WriteArticleTool", max_retries=4, verbose=True):
        super().__init__(name, max_retries, verbose)

    def execute(self, topic, outline=None):
        messages = [
            {"role": "system", "content": "You are an expert academic writer."},
            {"role": "user", "content": (
                f"Please write a research article on the following topic: {topic}" +
                (f"\nOutline:\n{outline}" if outline else "")
            )}
        ]
        article = self.call_openai(messages)
        return article