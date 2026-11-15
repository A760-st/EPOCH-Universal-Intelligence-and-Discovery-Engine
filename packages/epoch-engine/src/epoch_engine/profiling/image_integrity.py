
"""Image integrity validation for EPOCH datasets."""

from pathlib import Path
from typing import Any

from PIL import Image, UnidentifiedImageError

from epoch_engine.profiling.dataset_profiler import SUPPORTED_EXTENSIONS


def validate_image(image_path: str | Path) -> dict[str, Any]:
    """
    Validate an image by checking its file size and decoding its contents.

    Returns a structured validation result.
    """

    path = Path(image_path)

    result = {
        "file_path": str(path),
        "is_valid": False,
        "status": "INVALID",
        "format": None,
        "width": None,
        "height": None,
        "file_size_bytes": None,
        "error": None,
    }

    if not path.exists():
        result["status"] = "MISSING"
        result["error"] = "File does not exist"
        return result

    if not path.is_file():
        result["error"] = "Path is not a file"
        return result

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        result["status"] = "UNSUPPORTED"
        result["error"] = "Unsupported image extension"
        return result

    result["file_size_bytes"] = path.stat().st_size

    if result["file_size_bytes"] == 0:
        result["status"] = "EMPTY"
        result["error"] = "File is empty"
        return result

    try:
        with Image.open(path) as image:
            image.verify()

        # Reopen the file because verify() invalidates the image object.
        with Image.open(path) as image:
            image.load()

            result["format"] = image.format
            result["width"], result["height"] = image.size

        result["is_valid"] = True
        result["status"] = "VALID"

    except (UnidentifiedImageError, OSError, ValueError) as exc:
        result["status"] = "CORRUPTED"
        result["error"] = str(exc)

    return result


def validate_dataset_images(
    dataset_path: str | Path,
) -> dict[str, Any]:
    """Validate every supported image candidate in class folders."""

    root = Path(dataset_path)

    if not root.exists():
        raise FileNotFoundError(f"Dataset directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    results = []
    class_directories = sorted(
        path for path in root.iterdir() if path.is_dir()
    )

    for class_dir in class_directories:
        for file_path in sorted(class_dir.rglob("*")):
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                results.append(validate_image(file_path))

    valid_count = sum(item["is_valid"] for item in results)

    status_counts = {}
    for item in results:
        status = item["status"]
        status_counts[status] = status_counts.get(status, 0) + 1

    return {
        "dataset_path": str(root.resolve()),
        "total_candidates": len(results),
        "valid_images": valid_count,
        "invalid_images": len(results) - valid_count,
        "status_counts": status_counts,
        "results": results,
    }
