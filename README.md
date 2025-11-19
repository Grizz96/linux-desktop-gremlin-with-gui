# Linux Desktop Gremlins

Desktop companions for your Linux desktop, based on the wonderful project by [iluvgirlswithglasses](https://github.com/iluvgirlswithglasses/linux-desktop-gremlin), which is a PySide6 rewrite of [KurtVelasco's Desktop Gremlin](https://github.com/KurtVelasco/Desktop_Gremlin).

A huge thank you to them for creating these amazing desktop friends!

## Changelog
- **2025-11-19**: Added new characters: Agnes, Goldship, and Oguri.

![Gremlin Preview](https://github.com/user-attachments/assets/eeb75510-9725-4f3a-a259-0959ddc22603)

---

## ⚙️ Installation

1.  **Dependencies**:
    *   Ensure you have `git` and `curl`.
    *   This project uses `uv` for Python package management.
    *   You will need **PySide6** and **Qt6**. For Arch Linux users, you can install them with: `yay -S pyside6 qt6-base`.
    *   For background transparency, your compositor must be configured. X11 users will need `picom`, and Hyprland users need to add a few window rules (see the original repo's `hyprland.conf` for examples).

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

The easiest way to run and select a gremlin is by using the GUI.

1.  **Run the GUI Picker**:
    Make the script executable first:
    ```sh
    chmod +x run-gui.sh
    ```
    Then run it:
    ```sh
    ./run-gui.sh
    ```
    This GUI allows you to preview characters and run them with a single click.

2.  **Alternative (Command Line)**:
    You can also run a gremlin directly from the terminal by specifying its name:
    ```sh
    ./run.sh <character-name>
    ```
    Example: `./run.sh agnes`

