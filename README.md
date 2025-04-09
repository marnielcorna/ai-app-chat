## For OPENAI USE: ##
1. Install Python 3.11+ by Using Homebrew:
```brew install python```
2. Check python version with: ```python3 --version```
3. Clone the repo: https://...
4. Create the virtual environment:
   ```python3 -m venv .venv```
   ```source .venv/bin/activate```
5. Install dependencies: ```pip install -r requirements.txt```
6. Verify .env file contains ```OPENAI_API_KEY=your-api-key-here``` and ```USE_OLLAMA=false```
7. Run command: ```python main.py``` 

## FOR OLLAMA USE ##
1. Install Python 3.11+ by Using Homebrew:
```brew install python```
2. Install ollama (if we want to use free version): ```ollama pull llama3``` and verify with this: ```ollama list```
3. Clone the repo: https://...
4. Create the virtual environment:
   ```python3 -m venv .venv```
   ```source .venv/bin/activate```
5. Install dependencies: ```pip install -r requirements.txt```
6. Verify .env file contains ```USE_OLLAMA=false```
7. Run command: ```python main.py``` 