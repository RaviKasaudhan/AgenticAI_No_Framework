from .summarize_tool import SummarizeTool
from .write_article_tool import WriteArticleTool
from .sanitize_data_tool import SanitizeDataTool
from .write_artcile_validator_agent import WriteArticleValidatorAgent
from .refiner_agent import RefinerAgent
from .summary_validator_agent import SummaryValidatorAgent
from .sanitze_data_validator_agent import SanitizeDataValidatorAgent
from .agent_base import AgentBase


class AgentManager:
    def __init__(self, max_retries=4, verbose=True):
        self.agents = {
            "SummarizeTool": SummarizeTool(max_retries=max_retries, verbose=verbose),
            "WriteArticleTool": WriteArticleTool(max_retries=max_retries, verbose=verbose),
            "SanitizeDataTool": SanitizeDataTool(max_retries=max_retries, verbose=verbose),
            "WriteArticleValidatorAgent": WriteArticleValidatorAgent(max_retries=max_retries, verbose=verbose),
            "RefinerAgent": RefinerAgent(max_retries=max_retries, verbose=verbose),
            "SummaryValidatorAgent": SummaryValidatorAgent(max_retries=max_retries, verbose=verbose),
            "SanitizeDataValidatorAgent": SanitizeDataValidatorAgent(max_retries=max_retries, verbose=verbose)
        }

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found.")
        return agent