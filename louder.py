"""返回名称的大写回显。"""

from echo import echo


def louder(name: str) -> str:
    """复用 echo(name) 后整体大写，例如 louder("World") == "ECHO: WORLD"。"""
    return echo(name).upper()
