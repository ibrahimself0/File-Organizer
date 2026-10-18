import shutil
from pathlib import Path

TARGET_DIR = Path.home() / "Downloads"


FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"},
    "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
    "Audio_Video": {".mp3", ".wav", ".mp4", ".mkv", ".mov"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".sql"},
    "Installers": {".exe", ".msi", ".dmg", ".pkg", ".deb"},
}


def organize_folder(directory: Path):
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return

    moved_count = 0

    for item in directory.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue

        ext = item.suffix.lower()

        destination_folder = "Misc"
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                destination_folder = category
                break

        target_path = directory / destination_folder
        target_path.mkdir(exist_ok=True)

        final_file_path = target_path / item.name
        counter = 1
        while final_file_path.exists():
            final_file_path = target_path / f"{item.stem}_{counter}{item.suffix}"
            counter += 1

        shutil.move(str(item), str(final_file_path))
        print(f"Moved: {item.name} -> {destination_folder}/")
        moved_count += 1

    print(f"\nDone! Organized {moved_count} files.")


if __name__ == "__main__":
    print(f"Organizing: {TARGET_DIR}...")
    organize_folder(TARGET_DIR)
