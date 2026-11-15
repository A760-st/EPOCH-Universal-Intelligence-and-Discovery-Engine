from pathlib import Path

from PIL import Image

from epoch_engine.profiling.integrity_report import (
    generate_integrity_report,
)


def test_clean_dataset_report(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    aloe.mkdir()

    Image.new("RGB", (50, 50)).save(aloe / "valid.png")

    report = generate_integrity_report(tmp_path)

    assert report["integrity_status"] == "CLEAN"
    assert report["class_count"] == 1
    assert report["total_image_candidates"] == 1
    assert report["valid_images"] == 1
    assert report["issue_count"] == 0


def test_report_detects_dataset_issues(tmp_path: Path):
    aloe = tmp_path / "Aloe_Vera"
    aloe.mkdir()

    Image.new("RGB", (50, 50)).save(aloe / "valid.png")
    (aloe / "broken.jpg").write_bytes(b"not a real image")
    (aloe / "empty.jpg").write_bytes(b"")
    (aloe / "notes.txt").write_text("unsupported file")

    report = generate_integrity_report(tmp_path)

    assert report["integrity_status"] == "ISSUES_FOUND"
    assert report["valid_images"] == 1
    assert report["corrupted_images"] == 1
    assert report["empty_files"] == 1
    assert report["unsupported_files"] == 1
    assert report["issue_count"] == 3


def test_report_contains_per_class_statistics(tmp_path: Path):
    tulsi = tmp_path / "Tulsi"
    tulsi.mkdir()

    Image.new("RGB", (30, 30)).save(tulsi / "leaf.png")
    (tulsi / "broken.jpg").write_bytes(b"invalid")

    report = generate_integrity_report(tmp_path)

    tulsi_stats = report["classes"]["Tulsi"]

    assert tulsi_stats["image_candidates"] == 2
    assert tulsi_stats["valid_images"] == 1
    assert tulsi_stats["corrupted_images"] == 1


def test_report_identifies_empty_dataset(tmp_path: Path):
    report = generate_integrity_report(tmp_path)

    assert report["integrity_status"] == "EMPTY_DATASET"
    assert report["class_count"] == 0
    assert report["total_image_candidates"] == 0