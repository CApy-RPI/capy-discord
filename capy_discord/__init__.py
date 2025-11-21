from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from capy_discord.bot import Bot

instance: Optional["Bot"] = None
