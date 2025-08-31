import subprocess

def chat_with_ollama(conversation):
    """Send conversation history to Ollama and return bot reply."""
    full_prompt = "\n".join(conversation) + "\nBot:"

    try:
        process = subprocess.Popen(
            ["ollama", "run", "gemma3:1b"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",   # 🔹 Add this
            errors="ignore"     # 🔹 Avoid crash on weird chars
        )

        # Send prompt to Ollama
        process.stdin.write(full_prompt)
        process.stdin.close()

        bot_reply = ""
        for line in process.stdout:
            bot_reply += line

        process.wait()
        return bot_reply.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"