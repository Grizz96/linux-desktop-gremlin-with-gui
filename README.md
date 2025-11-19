# Linux Desktop Gremlins

Desktop companions for your Linux desktop, based on the wonderful project by [iluvgirlswithglasses](https://github.com/iluvgirlswithglasses/linux-desktop-gremlin), which is a PySide6 rewrite of [KurtVelasco's Desktop Gremlin](https://github.com/KurtVelasco/Desktop_Gremlin).

A huge thank you to them for creating these amazing desktop friends!

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

---

## ✨ How to Add a New Character

To add your own character:

1.  **Create Directories**:
    *   Create a new folder with the character's name inside `spritesheet/`. Example: `spritesheet/my-char/`.
    *   Create another folder with the same name inside `sounds/`. Example: `sounds/my-char/`.

2.  **Prepare Sprite Assets**:
    *   Place all your `*.png` files (spritesheets) for your character's animations inside the `spritesheet/my-char/` directory.

3.  **Configure `sprite-map.json`**:
    *   Create a `sprite-map.json` file inside `spritesheet/my-char/`.
    *   This file defines the frame dimensions (`FrameWidth`, `FrameHeight`) and maps action names (like `Idle`, `Walk`, `Pat`) to their corresponding `.png` filenames.
    *   You can copy and modify this file from an existing character (e.g., `spritesheet/agnes/sprite-map.json`).

4.  **Configure `emote-config.json`**:
    *   (Optional) If you want the character to have an "annoy emote" (a random emote when idle), create an `emote-config.json` file in its sprite directory. Set `AnnoyEmote` to `true` and adjust the timings.

5.  **Add Sounds**:
    *   Place all your sound files (`*.wav`) inside the `sounds/my-char/` directory you created. The filenames should correspond to the actions that trigger them (e.g., `pat.wav`, `grab.wav`, etc.).

After all the files are in place, your new character will automatically appear in the GUI picker.
