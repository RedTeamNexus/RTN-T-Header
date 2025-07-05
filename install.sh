#!/bin/bash
echo "Updating packages..."
apt update && apt upgrade -y

echo "Installing dependencies..."
pkg install python git -y
pip install pyfiglet termcolor

echo "Setup complete. Run the tool with:"
echo "python3 t-header.py"
