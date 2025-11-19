# Linux Desktop Gremlins

Desktop companions for your Linux desktop, based on the wonderful project by [iluvgirlswithglasses](https://github.com/iluvgirlswithglasses/linux-desktop-gremlin), which is a PySide6 rewrite of [KurtVelasco's Desktop Gremlin](https://github.com/KurtVelasco/Desktop_Gremlin).

A huge thank you to them for creating these amazing desktop friends!

## Changelog
- **2025-11-19**: Added GUI Picker and new characters: Agnes, Goldship, and Oguri.

---

## ⚙️ Installation

1.  **Dependencies**:
    *   Ensure you have `git` and `curl`.
    *   This project uses `uv` for Python package management.
    *   You will need **PySide6** and **Qt6**. For Arch Linux users, you can install them with: `yay -S pyside6 qt6-base`.
    *   For background transparency, your compositor must be configured (e.g., `picom` for X11).

2.  **Clone the Repository**:
    ```sh
    git clone <your-fork-url>
    cd linux-desktop-gremlin
    ```

3.  **Install Python Packages**:
    Use `uv` to sync the dependencies.
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv sync
    ```

---

## 🚀 Running the Gremlins

There are multiple ways to run the gremlins.

### Method 1: Graphical Picker (Recommended)

This is the easiest way to select and run a character.

1.  **Make the scripts executable**:
    ```sh
    chmod +x run-gui.sh run-uv-xwayland.sh
    ```
2.  **Run the GUI**:
    ```sh
    ./run-gui.sh
    ```

### Method 2: Command Line (XWayland)

You can run a specific character directly using the `run-uv-xwayland.sh` script. If no name is provided, it will use the default from `config.json`.

```sh
# Run a specific character
./run-uv-xwayland.sh agnes

# Run the default character
./run-uv-xwayland.sh
```

### Method 3: Unified Script

The project also includes a unified `run.sh` script from a previous refactor.

```sh
./run.sh <character-name>
```