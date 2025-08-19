# filepath: /Users/ravi.kasaudhan/Documents/My Projects/YT Project/agents/summary_validator_agent.py
from .agent_base import AgentBase

class SummaryValidatorAgent(AgentBase):
    def __init__(self, max_retries=4, verbose=True):
        super().__init__(name="SummaryValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_text, summary):
        system_message = "You are an expert assistant that validates medical text summaries."
        user_content = (
            "Please review the original medical text and its summary. "
            "Assess whether the summary accurately and concisely captures the key points of the original text. "
            "List any missing or incorrect information, and rate the summary's quality on a scale of 1 to 5.\n\n"
            f"Original Text:\n{original_text}\n\n"
            f"Summary:\n{summary}\n\n"
            "Validation:"
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
        validation = self.call_openai(messages, max_tokens=400)
        return validation