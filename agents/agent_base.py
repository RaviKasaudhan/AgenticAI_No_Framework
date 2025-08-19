from groq import Groq
from abc import ABC, abstractmethod 
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"), 
)

class AgentBase(ABC):
    def __init__(self, name, max_retries=4, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_openai(self, messages, temperature=0.7, max_tokens=400):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"Calling Groq API with messages: {messages}")
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                reply = response.choices[0].message
                if self.verbose:
                    logger.info(f"[{self.name}] Received response: {reply}")
                return reply
            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during OpenAI call: {e}. Retry {retries}/{self.max_retries}")
        raise Exception(f"[{self.name}] Failed to get response from OpenAI after {self.max_retries} retries.")