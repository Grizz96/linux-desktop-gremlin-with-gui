# Linux Desktop Gremlins

Desktop companions for your Linux desktop, rewritten in PySide6.

![Gremlin Preview](https://github.com/user-attachments/assets/eeb75510-9725-4f3a-a259-0959ddc22603)

---

## ⚙️ Installation

1.  **Dependencies**:
    *   Pastikan Anda memiliki `git` dan `curl`.
    *   Proyek ini menggunakan `uv` untuk manajemen package Python.
    *   Anda memerlukan **PySide6** dan **Qt6**. Untuk pengguna Arch Linux, Anda bisa install dengan: `yay -S pyside6 qt6-base`.
    *   Untuk background transparan, compositor Anda harus dikonfigurasi. Pengguna X11 perlu `picom`, dan pengguna Hyprland perlu menambahkan beberapa rules window (lihat `hyprland.conf` di repo asli untuk contoh).

2.  **Clone Repository**:
    ```sh
    git clone https://github.com/iluvgirlswithglasses/linux-desktop-gremlin
    cd linux-desktop-gremlin
    ```

3.  **Install Python Packages**:
    Gunakan `uv` untuk sinkronisasi dependencies.
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv sync
    ```

---

## 🚀 Running the Gremlins

Cara termudah untuk menjalankan dan memilih gremlin adalah menggunakan GUI.

1.  **Jalankan GUI Picker**:
    ```sh
    ./run-gui.sh
    ```
    GUI ini memungkinkan Anda melihat pratinjau karakter dan menjalankannya dengan satu klik.

2.  **Alternatif (Command Line)**:
    Anda juga bisa menjalankan gremlin langsung dari terminal dengan menyebutkan namanya:
    ```sh
    ./run.sh <character-name>
    ```
    Contoh: `./run.sh agnes`

---

## ✨ How to Add a New Character

Untuk menambahkan karakter Anda sendiri:

1.  **Buat Direktori**:
    *   Buat folder baru dengan nama karakter di dalam `spritesheet/`. Contoh: `spritesheet/my-char/`.
    *   Buat folder baru dengan nama yang sama di dalam `sounds/`. Contoh: `sounds/my-char/`.

2.  **Siapkan Aset Sprite**:
    *   Letakkan semua file `*.png` (spritesheets) untuk animasi karakter Anda di dalam direktori `spritesheet/my-char/`.

3.  **Konfigurasi `sprite-map.json`**:
    *   Buat file `sprite-map.json` di dalam `spritesheet/my-char/`.
    *   File ini mendefinisikan ukuran frame (`FrameWidth`, `FrameHeight`) dan memetakan nama aksi (seperti `Idle`, `Walk`, `Pat`) ke nama file `.png` yang sesuai.
    *   Anda bisa menyalin dan memodifikasi file ini dari karakter yang sudah ada (misal, `spritesheet/agnes/sprite-map.json`).

4.  **Konfigurasi `emote-config.json`**:
    *   (Opsional) Jika Anda ingin karakter memiliki "annoy emote" (emote acak saat idle), buat file `emote-config.json` di direktori sprite-nya. Atur `AnnoyEmote` ke `true` dan sesuaikan durasinya.

5.  **Tambahkan Suara**:
    *   Letakkan semua file suara (`*.wav`) di dalam direktori `sounds/my-char/` yang telah Anda buat. Nama file harus cocok dengan yang akan direferensikan oleh logika program (misal, `pat.wav`, `grab.wav`, dll).

Setelah semua file berada di tempatnya, karakter baru Anda akan secara otomatis muncul di GUI picker.