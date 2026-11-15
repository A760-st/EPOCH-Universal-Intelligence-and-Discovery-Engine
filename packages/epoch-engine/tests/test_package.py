from epoch_engine import __version__


def test_package_version():
    assert __version__ == "0.1.0"


def test_package_import():
    import epoch_engine

    assert epoch_engine is not None