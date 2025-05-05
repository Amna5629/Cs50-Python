import json
from project import read_birthstone_data, get_birthstone_character, display_birthstone_info, save_user_info

# Test reading the CSV data
def test_read_birthstone_data():
    data = read_birthstone_data()
    assert data[1]["name"] == "Garnet"
    assert data[12]["name"] == "Turquoise"

# Test getting the character description
def test_get_birthstone_character():
    data = read_birthstone_data()
    assert get_birthstone_character(data[1]) == "Adventurous and determined, Garnet is a leader who always strives for success."
    assert get_birthstone_character({}) == "Unknown"

# Test displaying birthstone info
def test_display_birthstone_info(capsys):
    display_birthstone_info("Garnet", "A deep red gemstone symbolizing protection, strength, and vitality.",
                            ["Oprah Winfrey", "Muhammad Ali"],
                            "Adventurous and determined")
    captured = capsys.readouterr()
    assert "Your birthstone is Garnet!" in captured.out

# Test saving user info
def test_save_user_info(tmpdir):
    save_user_info("TestUser", 1, {"name": "Garnet"})
    with open("TestUser.json", "r") as f:
        saved_data = json.load(f)
    assert saved_data["name"] == "TestUser"
