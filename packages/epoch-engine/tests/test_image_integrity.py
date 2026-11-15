
from pathlib import Path

import pytest
from PIL import Image

from epoch_engine.profiling.image_integrity import (
    validate_image,
    validate_dataset_images,
)


def test_valid_image_is_detected(tmp_path: Path):
    image_path = tmp_path / "valid.png"
    Image.new("RGB", (100, 80)).save(image_path)

    result = validate_image(image_path)

    assert result["is_valid"] is True
    assert result["status"] == "VALID"
    assert result["format"] == "PNG"
    assert result["width"] == 100
    assert result["height"] == 80


def test_corrupted_image_is_detected(tmp_path: Path):
    image_path = tmp_path / "corrupted.jpg"
    image_path.write_bytes(b"This is not a real image")

    result = validate_image(image_path)

    assert result["is_valid"] is False
    assert result["status"] == "CORRUPTED"


def test_empty_image_is_detected(tmp_path: Path):
    image_path = tmp_path / "empty.jpg"
    image_path.write_bytes(b"")

    result = validate_image(image_path)

    assert result["status"] == "EMPTY"
    assert result["is_valid"] is False


def test_unsupported_file_is_detected(tmp_path: Path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Not an image")

    result = validate_image(file_path)

    assert result["status"] == "UNSUPPORTED"


def test_missing_image_is_detected(tmp_path: Path):
    result = validate_image(tmp_path / "missing.jpg")

    assert result["status"] == "MISSING"


def test_dataset_validation_summary(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    aloe.mkdir()

    Image.new("RGB", (50, 50)).save(aloe / "valid.png")
    (aloe / "broken.jpg").write_bytes(b"broken data")
    (aloe / "empty.jpg").write_bytes(b"")

    result = validate_dataset_images(tmp_path)

    assert result["total_candidates"] == 3
    assert result["valid_images"] == 1
    assert result["invalid_images"] == 2
    assert result["status_counts"]["VALID"] == 1
    assert result["status_counts"]["CORRUPTED"] == 1
    assert result["status_counts"]["EMPTY"] == 1


def test_dataset_validation_rejects_missing_directory(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        validate_dataset_images(tmp_path / "missing")
