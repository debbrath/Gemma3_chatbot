import streamlit as st
from backend import chat_with_ollama

st.set_page_config(page_title="Gemma3 Chatbot", layout="wide")

st.title("💬 Gemma3 Chatbot (Ollama)")
st.markdown("Chat with `gemma3:1b` model locally using **Ollama**")

# --- Sidebar: Conversation List ---
if "conversations" not in st.session_state:
    st.session_state.conversations = {"Default": []}
if "active_chat" not in st.session_state:
    st.session_state.active_chat = "Default"

st.sidebar.header("🗂️ Conversations")

chat_names = list(st.session_state.conversations.keys())
selected_chat = st.sidebar.radio("Select chat:", chat_names, index=chat_names.index(st.session_state.active_chat))
if selected_chat != st.session_state.active_chat:
    st.session_state.active_chat = selected_chat

new_chat_name = st.sidebar.text_input("➕ New chat name")
if st.sidebar.button("Create Chat") and new_chat_name.strip():
    if new_chat_name not in st.session_state.conversations:
        st.session_state.conversations[new_chat_name] = []
        st.session_state.active_chat = new_chat_name

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.conversations[st.session_state.active_chat] = []

# --- Main Chat UI ---
conversation = st.session_state.conversations[st.session_state.active_chat]
user_input = st.chat_input("Type your message...")

if user_input:
    conversation.append(f"You: {user_input}")
    bot_reply = chat_with_ollama(conversation)
    conversation.append(f"Bot: {bot_reply}")

# ----- Scrollable chat area (vertical) -----
try:
    chat_box = st.container(height=520, border=True)  # creates a vertical scroll area automatically
    with chat_box:
        for message in conversation:
            if message.startswith("You:"):
                st.chat_message("user").write(message[5:])  # strip "You: "
            else:
                st.chat_message("assistant").write(message[5:])  # strip "Bot: "
except TypeError:
    # Fallback below if your Streamlit doesn't support height/border args
    pass