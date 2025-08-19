from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, name="SanitizeDataTool", max_retries=4, verbose=True):
        super().__init__(name, max_retries, verbose)

    # ...existing code...
    def execute(self, data):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that sanitizes data by removing all Personally Identifiable Information (PII) and Protected Health Information (PHI)."},
            {"role": "user", "content": (
                "Please carefully review the following data and remove any PII or PHI present. "
                "Ensure that names, addresses, contact details, medical information, and any other sensitive identifiers are fully removed or anonymized. "
                "Return only the sanitized version of the data, suitable for public use.\n\n"
                f"Data:\n{data}\n\n"
                "Sanitized Data:"
            )}
        ]
        sanitized_data = self.call_openai(messages)
        return sanitized_data