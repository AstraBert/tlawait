from tlawait import run_script_with_top_level_await


def test_disk_io() -> None:
    run_script_with_top_level_await("tests/scripts/disk_io.py")


def test_network_io() -> None:
    run_script_with_top_level_await("tests/scripts/network_io.py")


def test_db_io() -> None:
    run_script_with_top_level_await("tests/scripts/db_io.py")
