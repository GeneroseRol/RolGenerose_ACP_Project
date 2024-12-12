import pytest
import csv
from unittest.mock import patch, mock_open
from project import (
    load_names_from_csv,
    add_names,
    pick_random,
    pick_multiple,
    display_all_names,
    display_available_names,
    display_pick_history,
    reset_names,
    clear_data,
)

@pytest.fixture
def setup_csv_file(tmp_path):
    csv_file = tmp_path / "test_names.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Gen"])
        writer.writerow(["Eldon"])
        writer.writerow(["Rol"])
        writer.writerow(["Paquera"])
    return csv_file


def test_load_names_from_csv(setup_csv_file):
    csv_file = setup_csv_file
    all_names, available_names = load_names_from_csv(str(csv_file))
    assert all_names == ["Gen", "Eldon", "Rol", "Paquera"]
    assert available_names == ["Gen", "Eldon", "Rol", "Paquera"]


@pytest.mark.parametrize("input_data, expected_all_names, expected_available_names", [
    (["Gen", "Eldon", "done"], ["Gen", "Eldon"], ["Gen", "Eldon"]),
    (["Rol", "Paquera", "done"], ["Rol", "Paquera"], ["Rol", "Paquera"]),
])
def test_add_names(input_data, expected_all_names, expected_available_names):
    mock_csv = mock_open()
    all_names = []
    available_names = []
    with patch("builtins.open", mock_csv):
        with patch("builtins.input", side_effect=input_data):
            all_names, available_names = add_names(all_names, available_names, "mock.csv")
    assert all_names == expected_all_names
    assert available_names == expected_available_names


def test_pick_random():
    available_names = ["Gen", "Eldon", "Rol", "Paquera"]
    pick_history = []

    pick_random(available_names, pick_history)

    assert len(available_names) == 3
    assert len(pick_history) == 1
    assert pick_history[0] not in available_names


def test_pick_multiple():
    available_names = ["Gen", "Eldon", "Rol", "Paquera"]
    pick_history = []

    with patch("builtins.input", return_value="2"):
        pick_multiple(available_names, pick_history)

    assert len(available_names) == 2
    assert len(pick_history) == 2
    assert all(name not in available_names for name in pick_history)


def test_display_all_names(capsys):
    all_names = ["Gen", "Eldon", "Rol", "Paquera"]

    display_all_names(all_names)
    captured = capsys.readouterr()
    assert "Gen" in captured.out
    assert "Eldon" in captured.out
    assert "Rol" in captured.out
    assert "Paquera" in captured.out


def test_display_available_names(capsys):
    available_names = ["Gen", "Eldon"]

    display_available_names(available_names)
    captured = capsys.readouterr()
    assert "Gen" in captured.out
    assert "Eldon" in captured.out


def test_display_pick_history(capsys):
    pick_history = ["Rol", "Paquera"]

    display_pick_history(pick_history)
    captured = capsys.readouterr()
    assert "Rol" in captured.out
    assert "Paquera" in captured.out


def test_reset_names():
    all_names = ["Gen", "Eldon", "Rol", "Paquera"]
    available_names = []
    pick_history = ["Rol"]

    with patch("builtins.input", return_value="yes"):
        reset_names(all_names, available_names, pick_history)

    assert available_names == all_names
    assert len(pick_history) == 0


def test_clear_data():
    all_names = ["Gen", "Eldon", "Rol", "Paquera"]
    available_names = ["Gen", "Eldon"]
    pick_history = ["Rol"]

    with patch("builtins.input", return_value="yes"):
        clear_data(all_names, available_names, pick_history)

    assert len(all_names) == 0
    assert len(available_names) == 0
    assert len(pick_history) == 0
