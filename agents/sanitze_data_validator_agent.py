from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, max_retries=4, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)


    def execute(self, original_data, sanitized_data):
        system_message = "You are an expert AI assistant that validates the sanitization of data by checking that all PHI (Protected Health Information) is removed."

        user_content = (
            "Please review the original data and the sanitized version. "
            "Assess whether all Protected Health Information (PHI) has been properly removed from the sanitized data. "
            "List any instances where PHI may still be present, and provide suggestions for further sanitization if necessary. "
            "Confirm if the sanitized data is free from PHI and safe for public use.\n\n"
            f"Original Data:\n{original_data}\n\n"
            f"Sanitized Data:\n{sanitized_data}\n\n"
            "Validation:"
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        validation = self.call_openai(messages, max_tokens=400)
        return validation
