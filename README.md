# AI chat application
### For OPENAI USE:
1. Install Python 3.11+ by Using Homebrew:\
   ```brew install python``` 
2. Check python version with: \
   ```python3 --version```
3. Clone the repo: https://...
4. Create the virtual environment:\
   ```python3 -m venv .venv``` \
   ```source .venv/bin/activate```
5. Install dependencies: \
   ```pip install -r requirements.txt```
6. Verify .env file contains \
   ```OPENAI_API_KEY=your-api-key-here```\
   ```USE_OLLAMA=false```
7. Run command: \
   ```python main.py "{Your question}" | python main.py --interactive``` 

### FOR OLLAMA USE
1. Install Python 3.11+ by Using Homebrew:\
   ```brew install python```
2. Install ollama (if we want to use free version):\
   ```ollama pull llama3``` and verify with this: ```ollama list```
3. Clone the repo: https://...
4. Create the virtual environment:\
   ```python3 -m venv .venv```\
   ```source .venv/bin/activate```
5. Install dependencies:\
   ```pip install -r requirements.txt```
6. Verify .env file contains\
   ```USE_OLLAMA=true```
7. Run command: \
   ```python main.py "{Your question}" | python main.py --interactive``` 

### Project Structure
#### Key Files:
- **`.env`**: Stores API keys and runtime configurations (ensure this is in `.gitignore`!)  
- **`main.py`**: Launch the CLI or interactive chat mode  
- **`config.py`**: Centralizes environment variables and settings  
- **`client_factory.py`**: Dynamically selects between OpenAI or Ollama clients  
- **`chat.py`**: Handles streaming responses (e.g., for real-time chat)  
- **`chat_session.py`**: Manages conversation history and context flow  
