from main import read_file, save_file, display_menu, main
from unittest.mock import mock_open, patch

# Testa två scenarion:
# Filen exiterar och innehåll returneras som en lista

# Filen finns inte och en tom lista returneras

def test_read_file_exists():
    mock_data = "Alice\nBob\nCharlie\n" # Använder mock för att simulera filinnehåll
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_file("contacts.txt")
    assert result == ["Alice", "Bob", "Charlie"]

def test_read_file_not_exists():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_file("contacts.txt")
    assert result == []

def test_save_file_success():
    contacts = ["Ada", "Grace"]
    mock = mock_open()
    with patch("builtins.open", mock):
        save_file("contacts.txt", contacts)
    mock.assert_called_once_with("contacts.txt", "w")

def test_should_display_menu(capsys):
    display_menu()
    captured = capsys.readouterr()
    assert "--- Kontaktlista ---" in captured.out
    assert "1. Visa kontakter" in captured.out

def test_should_show_contacts_and_then_exit(capsys):
    inputs = ["1", "4"]
    with patch("builtins.input", side_effect=inputs):
        with patch("main.read_file", return_value=["Alice"]), \
        patch("main.save_file") as mock_save:
            main()
        captured = capsys.readouterr()
        assert "- Alice" in captured.out
        mock_save.assert_called_once()

def test_should_add_contact_and_then_exit(capsys):
    inputs = ["2", "Grace", "4"]
    with patch("builtins.input", side_effect=inputs):
        with patch("main.read_file", return_value=["Alice"]), \
        patch("main.save_file") as mock_save:
            main()
        captured = capsys.readouterr()
        assert "Grace har lagts till" in captured.out
        mock_save.assert_called_once()