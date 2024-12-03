# RAG Model with Llama and SHAP Interpretability

## Prerequisites
- Python 3.8+
- pip (Python Package Manager)
- Virtual Environment (recommended)

## Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/gober9/Rag-Creation-Python-Llama.git
cd Rag-Creation-Python-Llama
```

### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Llama Model
- Visit Hugging Face: https://huggingface.co/models
- Search for and download a Llama model
- Place the model in a `models/` directory

### 5. Run the RAG Model
```bash
python rag_model.py
```

## Troubleshooting
- Ensure all dependencies are installed
- Check Python version compatibility
- Verify model file paths

## Project Structure
- `rag_model.py`: Main RAG model implementation
- `requirements.txt`: Project dependencies
- `models/`: Directory for storing Llama models
- `data/`: Directory for input/output data

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request