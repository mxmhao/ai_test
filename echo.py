"""回显指定名称。"""


def echo(name: str) -> str:
    """返回 name 的回显，例如 echo("World") == "echo: World"。"""
    return f"echo: {name}"
