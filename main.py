import streamlit as st
from backend import chat_with_ollama

st.set_page_config(page_title="Gemma3 Chatbot", layout="centered")

st.title("💬 Gemma3 Chatbot (Ollama)")
st.markdown("Chat with `gemma3:1b` model locally using **Ollama**")

# Store chat history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.conversation.append(f"You: {user_input}")
    bot_reply = chat_with_ollama(st.session_state.conversation)
    st.session_state.conversation.append(f"Bot: {bot_reply}")

# Display chat history
for message in st.session_state.conversation:
    if message.startswith("You:"):
        st.chat_message("user").write(message.replace("You: ", ""))
    else:
        st.chat_message("assistant").write(message.replace("Bot: ", ""))