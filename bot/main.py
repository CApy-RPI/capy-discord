"""Main entrypoint for the application."""

from bot.config import settings


def main() -> None:
    """Main function to run the application."""
    settings.__sizeof__()
    while True:
        pass


def ping() -> str:
    """Return pong to test."""
    return "Pong!"


if __name__ == "__main__":
    main()
