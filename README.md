# Listing Scripts Setup Guide

## Prerequisites
- Python 3.7+ (for Python script)
- Ruby 2.7+ (for Ruby script)
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

## Ruby Script Setup

### 1. Check Ruby Version
```bash
# Verify Ruby installation and version
ruby -v
```

### 2. Run the Ruby Script
```bash
# Execute the Ruby script
ruby listings.rb
```

## Troubleshooting
- Ensure you have Python and Ruby installed
- Check that you're using compatible versions
- Verify internet connection for dependency installation
- Make sure you're in the correct directory when running scripts

## Notes
- The Python script requires the `requests` library
- The Ruby script can be run directly if all dependencies are met