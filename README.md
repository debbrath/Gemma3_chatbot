# Chatbot (Gemma3+ Ollama + Streamlit)

A simple chatbot built with **Ollama** running the `gemma3:1b` model and a **Streamlit UI**.  
This project lets you run a local chatbot with conversation history, multi-chat support, and an interactive interface.

## 🚀 Features
- Chat with the `gemma3:1b` model locally
- Conversation history (saved per chat)
- Multiple chat sessions (switch between them in the sidebar)
- Clear or create new chat sessions easily
- Scrollable chat UI
- Docker support for deployment

---

##  Project Structure

```
Gemma3_chatbot/
│── __pycache__/
│── Image/
│── venv/
│── backend.py
│── Dockerfile
│── main.py
│── README.md
│── requirements.txt

```

## Technologies

- Python 3.10+

- Streamlit

- Ollama

- Requests / httpx (for API calls)

## ⚙️ Installation

### 1. Install Python and VS Code

Make sure you have Python 3.10+ installed.

Install VS Code and open the project folder.

### 2. Install Ollama CLI

Ollama provides CLI tools to interact with their models.

Install Ollama:
Follow instructions at https://ollama.com/docs
 for your OS.

### 3.	Open VS Code
	Create a new folder named gemma3_chatbot.

### 4.	Create a requirements.txt with:
    subprocess-tee
    ollama
### 5.  Create a virtual environment 
    Open a terminal in the folder and run:
    python -m venv venv
    source venv/bin/activate       # Linux/macOS
    venv\Scripts\activate          # Windows
### 6.  Install dependencies:

    pip install -r requirements.txt
### 7. Run the App

    Local

    streamlit run main.py

    💬 Chatbot using Ollama Gemma3:1b. Type 'exit' to quit.

    You: Hello!
    Bot: Hello! How can I assist you today?

    Docker

    docker build -t gemma3-chatbot .
    docker run -p 8501:8501 gemma3-chatbot


## 📸 Screenshots

![Screenshot](https://github.com/debbrath/Gemma3_chatbot/blob/main/Image/chatbot_imgae2.png)
![Screenshot](https://github.com/debbrath/Gemma3_chatbot/blob/main/Image/chatbot_imgae3.png)
![Screenshot](https://github.com/debbrath/Gemma3_chatbot/blob/main/Image/chatbot_imgae4.png)

<br/>

---

✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath)
