# typing.Any removed to avoid using dynamic typing in metaclass __call__

from discord.ext.commands import AutoShardedBot


class Bot(AutoShardedBot):
    """Bot class for Capy Discord."""

    pass
