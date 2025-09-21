# Simple Text Summarization with Ollama

A Python project that demonstrates text summarization and AI chat capabilities using Ollama's local language models. This project includes web scraping functionality and showcases both direct API calls and the Ollama Python SDK.

## Features

- 🤖 Integration with Ollama local language models (Llama 3.2)
- 🌐 Web scraping capabilities using BeautifulSoup
- 📝 Text summarization and AI chat functionality
- 🔄 Support for both REST API and Python SDK approaches
- 🐍 Python 3.13 environment with conda

## Prerequisites

Before running this project, make sure you have:

1. **Ollama installed and running**: Download from [ollama.ai](https://ollama.ai)
2. **Conda or Miniconda**: For environment management
3. **Llama 3.2 model pulled**: Run `ollama pull llama3.2` in your terminal

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ollama-text-summarization
```

### 2. Create the conda environment

```bash
conda env create -f environment.yml
```

### 3. Activate the environment

```bash
conda activate ollama-text-summarization
```

### 4. Verify Ollama is running

```bash
ollama serve
```

Make sure Ollama is accessible at `http://localhost:11434`

## Usage

### Basic AI Chat

Run the main script to interact with the Llama 3.2 model:

```bash
python src/main.py
```

This will demonstrate a simple AI conversation about business applications of Generative AI.

### Code Structure

- `src/main.py`: Main application file with AI chat functionality
- `environment.yml`: Conda environment specification
- Dependencies include:
  - `requests`: For HTTP API calls
  - `beautifulsoup4`: For web scraping
  - `ollama`: Official Ollama Python SDK

### API Methods

The project demonstrates two ways to interact with Ollama:

1. **Direct REST API calls** (commented out in main.py):

```python
payload = {
    "model": "llama3.2",
    "messages": messages,
    "stream": False
}
response = requests.post("http://localhost:11434/api/chat", json=payload)
```

2. **Ollama Python SDK** (current implementation):

```python
response = ollama.chat(model="llama3.2", messages=messages)
```

## Configuration

### Model Selection

Change the model by updating the `MODEL` variable in `src/main.py`:

```python
MODEL = "llama3.2"  # or any other model you have pulled
```

### Ollama API Endpoint

If Ollama is running on a different host/port, update the `OLLAMA_API` variable:

```python
OLLAMA_API = "http://localhost:11434/api/chat"
```

## Dependencies

The project uses Python 3.13 with the following key packages:

- `ollama`: Official Ollama Python client
- `requests`: HTTP library for API calls
- `beautifulsoup4`: HTML/XML parsing for web scraping
- `typing-extensions`: Enhanced type hints

## Development

### Adding New Features

1. Extend `src/main.py` with additional functionality
2. Add new dependencies to `environment.yml` if needed
3. Update this README with usage instructions

### Environment Management

Export current environment after adding new packages:

```bash
conda env export > environment.yml
```

## Troubleshooting

### Common Issues

1. **Ollama not responding**: Ensure Ollama service is running with `ollama serve`
2. **Model not found**: Pull the required model with `ollama pull llama3.2`
3. **Environment issues**: Recreate the conda environment:
   ```bash
   conda env remove -n ollama-text-summarization
   conda env create -f environment.yml
   ```

### Checking Ollama Status

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# List available models
ollama list
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please check individual package licenses for production use.

## Resources

- [Ollama Documentation](https://github.com/jmorganca/ollama)
- [Ollama Python SDK](https://github.com/ollama/ollama-python)
- [Llama Models](https://ollama.ai/library)
