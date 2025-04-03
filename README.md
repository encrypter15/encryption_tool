# Encryption Tool

## Overview
The Encryption Tool is a Python script that encrypts files using the `cryptography` library’s Fernet symmetric encryption. It generates a key, encrypts the specified file, and saves both the encrypted file and the key.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- `cryptography` library (`pip install cryptography`)

## Usage
Run the script with the following arguments:

```bash
python3 encryption_tool.py --file <INPUT_FILE> --output <OUTPUT_FILE> [--config <CONFIG_FILE>]
