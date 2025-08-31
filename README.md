# Project Overview

##  Project Structure

```
chatbot_ollama/
│
├── main.py       # Main script for running chatbot
├── requirements.txt  # Required Python packages
└── README.md     # Project description and instructions

```
## Technologies

## Getting Started

1.	Install Python and VS Code

Make sure you have Python 3.10+ installed.

Install VS Code and open the project folder.

2.	Install Ollama CLI

Ollama provides CLI tools to interact with their models.

Install Ollama:
Follow instructions at https://ollama.com/docs
 for your OS.

3.	Open VS Code
o	Create a new folder named gemma3_chatbot.

3.	Create a requirements.txt with:
    subprocess-tee
    ollama
4.  Initialize a Python Project 
    Open a terminal in the folder and run:
    python -m venv venv
    source venv/bin/activate       # Linux/macOS
    venv\Scripts\activate          # Windows
5.  Then run:

    pip install -r requirements.txt
6.  Create main.py
7.  Run the Chatbot

    python main.py

    💬 Chatbot using Ollama Gemma3:1b. Type 'exit' to quit.

    You: Hello!
    Bot: Hello! How can I assist you today?

    streamlit run main.py