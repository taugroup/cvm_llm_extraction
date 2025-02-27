# Veterinary Medical Data Extraction Tool with LLMs

A user-friendly tool for extracting structured data from veterinary medical documents using AI.

## Features ✨
- **PDF Document Processing**: Works with standard veterinary report formats
- **AI-Powered Extraction**: Uses local LLM (Deepseek-r1) for data understanding
- **Structured Output**: Generates clean CSV files with organized results
- **Simple Setup**: Minimal configuration required

## Requirements 📋
- Python 3.11 or more
- [Ollama](https://ollama.com/) running locally
- 8GB+ available RAM (16GB+ recommended)

## Quick Start 🚀

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/taugroup/cvm_llm_extraction.git
cd cvm_llm_extraction
```

#### Create virtual environment (recommended)

> using Anaconda
```bash
conda create -n "cvm" python=3.11
conda activate cvm
```
> using venv
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Documents
Create a data folder in your project directory

Place your PDF files in the data folder with these exact names:

- signalment_physical.pdf
- cbc.pdf
- chem.pdf
- cpli.pdf
- aus.pdf

### 3. Configure AI Model
You can pull any of the models from [here](https://ollama.com/search). If the device you are going to run this code on, has RAM >= 16gb, you can run smaller models (that are 2gb - 8gb in size) with no overhead. \
\
If you have a GPU set up, then you can run stronger models like `deepseek-r1:14b` or `qwen2.5:14b`.
I would suggest starting with `llama3.2` or `llama3.1:8b`. 
This is the format to load the model (needs to be done once only, and never again):
```bash
# Download the required AI model
ollama pull deepseek-r1:14b
```

### 4. Run the Application
```bash
python main.py
```

The processed data will be saved as extracted_data.csv in the output folder.

## File Structure 📂
```tree
.
└── project/
    ├── data/               # PDF documents go here
    ├── config/             # Configuration settings
    ├── llm/                # AI model integration
    ├── data_processing/    # Core processing logic
    ├── utils/              # Helper functions
    ├── main.py             # Start here
    └── output/             # Output CSV file will be stored here
```

## Customization ⚙️

### Change Input Folder

Edit `config/settings.py`:

```python
class Settings:
    DATA_DIR = "your/new/path"  # ← Change this line
    # ... rest remains the same
```

### Using Different Models
Check available models by running this command in the terminal: `ollama list`

Update `config/settings.py`:

```python
LLM_MODEL = "your-model-name"  # e.g., "llama3.2:latest"
```

## Troubleshooting 🔧

> "Ollama not responding"
- Ensure Ollama is running
- Check ollama serve output

> Missing PDF files
- Verify filenames match exactly in `data/`

> JSON parsing errors
- Check if documents contain expected data formats

## Support & Contact 📬
For assistance, reach out to `dheeraj.reddy@tamu.edu`

Note: Ensure Ollama service is running before starting the application. 
