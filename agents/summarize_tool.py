from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, name="SummarizeTool", max_retries=4, verbose=True):
        super().__init__(name, max_retries, verbose)

    def execute(self, text):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Please summarize the following text: {text}"}
        ]
        summary = self.call_openai(messages)
        return summary