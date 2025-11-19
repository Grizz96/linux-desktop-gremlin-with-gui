import json
import os
import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class GremlinPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gremlin Picker")
        self.setWindowIcon(QIcon.fromTheme("applications-games"))
        self.process = None

        # Main layout
        main_layout = QGridLayout(self)

        # --- Left Side: Gremlin List ---
        list_group_box = QGroupBox("Select a Gremlin")
        list_layout = QVBoxLayout()
        self.gremlin_list = QListWidget()
        self.gremlin_list.itemSelectionChanged.connect(self.update_preview)
        list_layout.addWidget(self.gremlin_list)
        list_group_box.setLayout(list_layout)
        main_layout.addWidget(list_group_box, 0, 0)

        # --- Right Side: Preview and Controls ---
        right_panel_layout = QVBoxLayout()

        # Preview Box
        preview_group_box = QGroupBox("Preview")
        preview_layout = QVBoxLayout()
        self.preview_label = QLabel("Select a character to see a preview")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setMinimumSize(256, 256)
        preview_layout.addWidget(self.preview_label)
        preview_group_box.setLayout(preview_layout)
        right_panel_layout.addWidget(preview_group_box)

        # Controls Box
        controls_group_box = QGroupBox("Controls")
        controls_layout = QVBoxLayout()
        self.run_button = QPushButton("▶️ Run Gremlin")
        self.run_button.clicked.connect(self.run_gremlin)
        self.stop_button = QPushButton("⏹️ Stop Gremlin")
        self.stop_button.clicked.connect(self.stop_gremlin)
        controls_layout.addWidget(self.run_button)
        controls_layout.addWidget(self.stop_button)
        controls_group_box.setLayout(controls_layout)
        right_panel_layout.addWidget(controls_group_box)

        main_layout.addLayout(right_panel_layout, 0, 1)

        # Set column stretch
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 2)

        self.load_gremlins()
        self.update_button_states()

        # Apply some basic styling
        self.setStyleSheet("""
            QWidget {
                font-size: 11pt;
            }
            QGroupBox {
                font-weight: bold;
            }
            QPushButton {
                padding: 8px;
            }
        """)

    def load_gremlins(self):
        spritesheet_dir = "spritesheet"
        if not os.path.isdir(spritesheet_dir):
            self.preview_label.setText("Error: 'spritesheet' directory not found.")
            return

        for gremlin_name in sorted(os.listdir(spritesheet_dir)):
            if os.path.isdir(os.path.join(spritesheet_dir, gremlin_name)):
                item = QListWidgetItem(gremlin_name)
                icon_pixmap = self.get_single_frame_pixmap(gremlin_name)
                if icon_pixmap:
                    item.setIcon(QIcon(icon_pixmap))
                self.gremlin_list.addItem(item)

        if self.gremlin_list.count() > 0:
            self.gremlin_list.setCurrentRow(0)

    def get_preview_path(self, gremlin_name):
        base_path = os.path.join("spritesheet", gremlin_name)
        # Prefer a specific, representative image if available
        for img_name in [
            "idle.png",
            "intro.png",
            "forward.png",
            "walkR.png",
            "icon.png",
        ]:
            preview_path = os.path.join(base_path, img_name)
            if os.path.exists(preview_path):
                return preview_path
        return None

    def get_single_frame_pixmap(self, gremlin_name):
        preview_path = self.get_preview_path(gremlin_name)
        if not preview_path:
            return None

        # Load the entire spritesheet
        spritesheet = QPixmap(preview_path)
        if spritesheet.isNull():
            return None

        # Find and read the sprite map to get frame dimensions
        sprite_map_path = os.path.join("spritesheet", gremlin_name, "sprite-map.json")
        if os.path.exists(sprite_map_path):
            try:
                with open(sprite_map_path, "r") as f:
                    sprite_map = json.load(f)

                frame_width = sprite_map.get("FrameWidth")
                frame_height = sprite_map.get("FrameHeight")

                if frame_width and frame_height:
                    # Crop the pixmap to the first frame
                    return spritesheet.copy(0, 0, frame_width, frame_height)
            except (json.JSONDecodeError, KeyError):
                # If JSON is bad or keys are missing, fall through to returning the full sheet
                pass

        # Fallback: return the whole (uncropped) spritesheet
        return spritesheet

    def update_preview(self):
        current_item = self.gremlin_list.currentItem()
        if not current_item:
            self.preview_label.setText("No character selected")
            self.preview_label.setPixmap(QPixmap())
            return

        gremlin_name = current_item.text()
        frame_pixmap = self.get_single_frame_pixmap(gremlin_name)

        if frame_pixmap:
            self.preview_label.setPixmap(
                frame_pixmap.scaled(
                    256, 256, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
        else:
            self.preview_label.setText("No preview available")
            self.preview_label.setPixmap(QPixmap())  # Clear any existing pixmap

    def run_gremlin(self):
        if self.process is not None and self.process.poll() is None:
            return

        selected_item = self.gremlin_list.currentItem()
        if selected_item:
            gremlin_name = selected_item.text()
            command = ["./run-uv-xwayland.sh", gremlin_name]
            try:
                self.process = subprocess.Popen(command)
            except FileNotFoundError:
                self.preview_label.setText("Error: './run-uv-xwayland.sh' not found.")
                return
            self.update_button_states()

    def stop_gremlin(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
        self.update_button_states()

    def update_button_states(self):
        is_running = self.process is not None and self.process.poll() is None
        self.run_button.setEnabled(not is_running)
        self.stop_button.setEnabled(is_running)

    def closeEvent(self, event):
        self.stop_gremlin()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    picker = GremlinPicker()
    picker.resize(600, 400)
    picker.show()
    sys.exit(app.exec())
