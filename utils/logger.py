from loguru import logger
import os
import sys

if not os.path.exists("logs"):
    os.makedirs("logs")

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
logger.add("logs/multi_agent_system.log", level="DEBUG", rotation="10 MB", retention="10 days", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")