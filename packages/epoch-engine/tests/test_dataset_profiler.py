
from pathlib import Path

import pytest

from epoch_engine.profiling.dataset_profiler import profile_dataset


def test_profile_dataset_counts_classes_and_images(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    tulsi = tmp_path / "Tulsi"

    aloe.mkdir()
    tulsi.mkdir()

    (aloe / "image1.jpg").write_bytes(b"image-data")
    (aloe / "image2.png").write_bytes(b"image-data")
    (tulsi / "image1.jpeg").write_bytes(b"image-data")

    result = profile_dataset(tmp_path)

    assert result["class_count"] == 2
    assert result["total_images"] == 3
    assert result["classes"]["Aloe_Vera"]["image_count"] == 2
    assert result["classes"]["Tulsi"]["image_count"] == 1


def test_profile_dataset_detects_empty_files(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    aloe.mkdir()

    (aloe / "empty.jpg").write_bytes(b"")
    (aloe / "valid.jpg").write_bytes(b"image-data")

    result = profile_dataset(tmp_path)

    assert result["total_images"] == 2
    assert result["empty_files"] == 1


def test_profile_dataset_detects_unsupported_files(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    aloe.mkdir()

    (aloe / "notes.txt").write_text("not an image")

    result = profile_dataset(tmp_path)

    assert result["unsupported_files"] == 1
    assert result["total_images"] == 0


def test_profile_dataset_rejects_missing_directory(tmp_path: Path):
    missing_path = tmp_path / "missing"

    with pytest.raises(FileNotFoundError):
        profile_dataset(missing_path)
