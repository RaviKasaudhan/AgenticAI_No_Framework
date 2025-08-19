# Task Management Agent System from Scratch
![Alt text](logo.png "Project Screenshot")
## **Overview**
This project implements a **simple agentic AI system** in Python for task management, built from scratch **without external frameworks**. The system enables an agent to **prioritize and execute tasks** based on urgency and importance, with optional integration of **Groq's Large Language Model (LLM)** for enhanced prioritization and reflection. The agent demonstrates basic **autonomous decision-making** and **reflection capabilities**.

## **Features**
- **Task Management**: Add tasks with urgency (1-10) and importance (1-10) scores.
- **Prioritization**: Tasks are prioritized using a weighted scoring mechanism or **Groq's LLM** for intelligent ranking.
- **Execution**: The agent executes tasks in order of priority.
- **Reflection**: Post-execution reflection summarizes completed tasks or uses **Groq's LLM** for deeper insights.
- **No Frameworks**: Built entirely with native Python, with optional LLM integration via **Groq's API**.

## **Requirements**
- **Python 3.8+**
- **`groq` library** for LLM integration (`pip install groq`)


## **Installation**
1. **Clone the repository**:
   ```bash
   git clone hhttps://github.com/RaviKasaudhan/AgenticAI_No_Framework.git
   cd AgenticAI_No_Framework
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your Groq API key**:
   ```bash
   export GROQ_API_KEY='your-api-key-here'
   ```
   Alternatively, modify the code to include your API key directly (**not recommended** for security).

## **Usage**
1. **Run the main script**:
   ```bash
   streamlit run app.py
   ```
2. The script includes **example tasks**:
   - **Reply to email** (Urgency: 8, Importance: 6)
   - **Write report** (Urgency: 5, Importance: 9)
   - **Attend meeting** (Urgency: 7, Importance: 7)
   - **Debug code** (Urgency: 9, Importance: 8)
3. The agent will **prioritize**, **execute**, and **reflect** on the tasks. If **Groq's LLM** is configured, it will use it for prioritization and reflection; otherwise, it falls back to a simple scoring mechanism.

## **Code Structure**
- **`task_agent_with_llm.py`**: Main script containing the `Task` and `TaskAgent` classes.
  - **`Task`**: Represents a task with name, urgency, and importance.
  - **`TaskAgent`**: Manages tasks, prioritizes them, executes them, and reflects on completion.
- **No external frameworks** are used, keeping the implementation lightweight.



## **Customization**
- **Change Groq Model**: Modify the `model` parameter in `agent_base.py` (e.g., `"llama3-70b-8192"` or other **Groq models**).

## **Notes**
- The system is designed to be **lightweight** and **extensible** for other agentic use cases.
- The system is not using any agentic frameworks. It is in plain python.
- **Rendering Markdown**: To see bold and larger fonts, view this README in a markdown-supported environment like **GitHub**, **VS Code** (with markdown preview), or a markdown renderer. Plain text editors (e.g., Notepad) will show raw markdown (e.g., `**` or `#`) without formatting.

## **License**
**MIT License**. See `LICENSE` for details.

## **Contributing**
Feel free to submit **issues** or **pull requests** to enhance the agent’s functionality, such as adding new prioritization algorithms or reflection methods.