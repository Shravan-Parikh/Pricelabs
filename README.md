# Listing Scripts Setup Guide

## Prerequisites
- Python 3.7+ (for Python script)
- pip (Python package manager)

## Python Script Setup

### 1. Set Up Virtual Environment
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Required Dependencies
```bash
# Install requests library
pip install requests
```

### 3. Run the Python Script
```bash
# Run the listings script
python listings.py
```

## Troubleshooting
- Ensure you have Python installed
- Check that you're using compatible versions
- Verify internet connection for dependency installation
- Make sure you're in the correct directory when running scripts

## Notes
- The Python script requires the `requests` library