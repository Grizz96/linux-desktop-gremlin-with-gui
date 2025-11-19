#!/bin/bash
# This script launches the Gremlin Picker GUI

# Navigate to the script's directory to ensure relative paths work correctly
cd "$(dirname "$0")"

# Run the GUI using the uv virtual environment
uv run python gui.py
