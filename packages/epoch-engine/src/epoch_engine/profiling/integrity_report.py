"""Unified dataset profiling and image integrity reporting."""

from pathlib import Path
from typing import Any

from epoch_engine.profiling.dataset_profiler import profile_dataset
from epoch_engine.profiling.image_integrity import validate_dataset_images


def generate_integrity_report(
    dataset_path: str | Path,
) -> dict[str, Any]:
    """Generate a unified structural and image-integrity report."""

    root = Path(dataset_path)

    # Run both existing inspection modules.
    profile = profile_dataset(root)
    image_report = validate_dataset_images(root)

    # Prepare per-class integrity statistics.
    per_class = {}

    for class_name, stats in profile["classes"].items():
        per_class[class_name] = {
            "image_candidates": stats["image_count"],
            "valid_images": 0,
            "corrupted_images": 0,
            "empty_files": 0,
            "unsupported_files": stats["unsupported_files"],
        }

    # Aggregate image validation results by class.
    for item in image_report["results"]:
        image_path = Path(item["file_path"])

        try:
            relative_path = image_path.resolve().relative_to(root.resolve())
            class_name = relative_path.parts[0]
        except (ValueError, IndexError):
            continue

        if class_name not in per_class:
            continue

        status = item["status"]

        if status == "VALID":
            per_class[class_name]["valid_images"] += 1
        elif status == "CORRUPTED":
            per_class[class_name]["corrupted_images"] += 1
        elif status == "EMPTY":
            per_class[class_name]["empty_files"] += 1

    corrupted_count = image_report["status_counts"].get(
        "CORRUPTED", 0
    )
    empty_count = image_report["status_counts"].get("EMPTY", 0)
    unsupported_count = profile["unsupported_files"]
    unassigned_count = profile["unassigned_files"]

    issue_count = (
        corrupted_count
        + empty_count
        + unsupported_count
        + unassigned_count
    )

    if profile["class_count"] == 0:
        integrity_status = "EMPTY_DATASET"
    elif issue_count > 0:
        integrity_status = "ISSUES_FOUND"
    else:
        integrity_status = "CLEAN"

    return {
        "dataset_path": profile["dataset_path"],
        "integrity_status": integrity_status,
        "class_count": profile["class_count"],
        "total_image_candidates": profile["total_images"],
        "valid_images": image_report["valid_images"],
        "corrupted_images": corrupted_count,
        "empty_files": empty_count,
        "unsupported_files": unsupported_count,
        "unassigned_files": unassigned_count,
        "issue_count": issue_count,
        "classes": per_class,
    }