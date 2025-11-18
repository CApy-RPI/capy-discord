from bot.main import ping


def test_ping() -> None:
    """Test that ping returns 'Pong!'."""
    assert ping() == "Pong!"
