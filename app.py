# app.py

import streamlit as st
from agents import AgentManager
from utils.logger import logger
import os
from dotenv import load_dotenv

print(f"Logger {logger}")
# Load environment variables from .env if present
load_dotenv()

def main():
    st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
    st.title("Multi-Agent AI System with Collaboration and Validation")

    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox("Choose a task:", [
        "Summarize Text",
        "Write and Refine Research Article",
        "Sanitize Data (PHI)"
    ])

    agent_manager = AgentManager(max_retries=4, verbose=True)

    if task == "Summarize Text":
        summarize_section(agent_manager)
    elif task == "Write and Refine Research Article":
        write_and_refine_article_section(agent_manager)
    elif task == "Sanitize Data (PHI)":
        sanitize_data_section(agent_manager)

def summarize_section(agent_manager):
    st.header("Summarize Text")
    text = st.text_area("Enter text to summarize:", height=200)
    if st.button("Summarize"):
        if text:
            main_agent = agent_manager.get_agent("SummarizeTool")
            validator_agent = agent_manager.get_agent("SummaryValidatorAgent")
            with st.spinner("Summarizing..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary.content)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SummarizeAgent Error: {e}")
                    return

            with st.spinner("Validating summary..."):
                try:
                    validation = validator_agent.execute(original_text=text, summary=summary)
                    st.subheader("Validation:")
                    st.write(validation.content)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"SummarizeValidatorAgent Error: {e}")
        else:
            st.warning("Please enter some text to summarize.")

def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)
    if st.button("Write and Refine Article"):
        if topic:
            writer_agent = agent_manager.get_agent("WriteArticleTool")
            refiner_agent = agent_manager.get_agent("RefinerAgent")
            validator_agent = agent_manager.get_agent("WriteArticleValidatorAgent")
            with st.spinner("Writing article..."):
                try:
                    draft = writer_agent.execute(topic, outline)
                    st.subheader("Draft Article:")
                    st.write(draft.content)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"WriteArticleAgent Error: {e}")
                    return

            with st.spinner("Refining article..."):
                try:
                    refined_article = refiner_agent.execute(draft)
                    st.subheader("Refined Article:")
                    st.write(refined_article.content)
                except Exception as e:
                    st.error(f"Refinement Error: {e}")
                    logger.error(f"RefinerAgent Error: {e}")
                    return

            with st.spinner("Validating article..."):
                try:
                    validation = validator_agent.execute(topic=topic, article=refined_article)
                    st.subheader("Validation:")
                    st.write(validation.content)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"ValidatorAgent Error: {e}")
        else:
            st.warning("Please enter a topic for the research article.")

def sanitize_data_section(agent_manager):
    st.header("Sanitize Data (PHI)")
    medical_data = st.text_area("Enter data to sanitize:", height=200)
    if st.button("Sanitize Data"):
        if medical_data:
            main_agent = agent_manager.get_agent("SanitizeDataTool")
            validator_agent = agent_manager.get_agent("SanitizeDataValidatorAgent")
            with st.spinner("Sanitizing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data.content)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SanitizeDataAgent Error: {e}")
                    return

            with st.spinner("Validating sanitized data..."):
                try:
                    validation = validator_agent.execute(original_data=medical_data, sanitized_data=sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation.content)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"SanitizeDataValidatorAgent Error: {e}")
        else:
            st.warning("Please enter data to sanitize.")

if __name__ == "__main__":
    main()