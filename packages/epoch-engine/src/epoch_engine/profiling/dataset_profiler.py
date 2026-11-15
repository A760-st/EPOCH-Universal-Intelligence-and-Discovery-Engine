
"""Dataset profiling utilities for EPOCH."""

from pathlib import Path
from typing import Any


SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp",
    ".gif", ".webp", ".tif", ".tiff",
}


def profile_dataset(dataset_path: str | Path) -> dict[str, Any]:
    """Profile an image dataset organised into class folders."""

    root = Path(dataset_path)

    if not root.exists():
        raise FileNotFoundError(f"Dataset directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    class_directories = sorted(
        path for path in root.iterdir() if path.is_dir()
    )

    classes = {}
    total_images = 0
    total_empty_files = 0
    total_unsupported_files = 0
    unassigned_files = 0

    for class_dir in class_directories:
        image_count = 0
        empty_files = 0
        unsupported_files = 0

        for file_path in class_dir.rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                image_count += 1

                if file_path.stat().st_size == 0:
                    empty_files += 1
            else:
                unsupported_files += 1

        classes[class_dir.name] = {
            "image_count": image_count,
            "empty_files": empty_files,
            "unsupported_files": unsupported_files,
        }

        total_images += image_count
        total_empty_files += empty_files
        total_unsupported_files += unsupported_files

    for file_path in root.iterdir():
        if file_path.is_file():
            unassigned_files += 1

    return {
        "dataset_path": str(root.resolve()),
        "class_count": len(classes),
        "total_images": total_images,
        "empty_files": total_empty_files,
        "unsupported_files": total_unsupported_files,
        "unassigned_files": unassigned_files,
        "classes": classes,
    }
