# Llama-Chat
A simple terminal based chat app between you and AI. Handles just one conversation at a time.

## Instructions
1. Download the packages necessary.
```
pip install -r requirements.txt
```

### Running Llama Locally
2. Download Llama Model from HuggingFace. I used <a href="https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf">TheBloke/llama-2-7b-chat.Q2_K.gguf</a>. 
```
> wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf
```

3. Run `heavy_app.py` 
```
> python heavy_app.py
```
### Using OpenAI
2. Set up `.env` file with `OPENAI_API_KEY`.

3. Run `openai_app.py`
```
> python openai_app.py
```