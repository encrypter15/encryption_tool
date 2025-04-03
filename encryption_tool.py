#!/usr/bin/env python3
# Encryption Tool
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Requires cryptography. Encrypts files and saves the key.

import argparse
import logging
import json
from cryptography.fernet import Fernet
from pathlib import Path

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='encryption_tool.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"key_path": "encryption_key.key"}

def encrypt_file(file_path: str, output_path: str, key_path: str) -> bool:
    """Encrypt a file and save the key."""
    try:
        key = Fernet.generate_key()
        cipher = Fernet(key)

        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)

        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
        with open(key_path, 'wb') as f:
            f.write(key)

        return True
    except (IOError, Exception) as e:
        logging.error(f"Encryption failed: {e}")
        return False

def main():
    """Main function to parse args and encrypt a file."""
    parser = argparse.ArgumentParser(description="Encryption Tool")
    parser.add_argument("--file", required=True, help="File to encrypt")
    parser.add_argument("--output", required=True, help="Encrypted output file path")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    logging.info(f"Encrypting {args.file} to {args.output}")
    if encrypt_file(args.file, args.output, config["key_path"]):
        logging.info(f"File encrypted successfully. Key saved to {config['key_path']}")
        print(f"Success: Encrypted file saved to {args.output}, key saved to {config['key_path']}")
    else:
        print("Error: Encryption failed")

if __name__ == "__main__":
    main()
