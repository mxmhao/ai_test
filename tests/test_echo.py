"""echo 公开接口的行为规格。

seam：从仓库根 echo 模块导入的 echo(name) 函数。
期望值取自 ticket 规格给出的已知示例，独立于实现方式。
"""

from echo import echo


def test_echo_world() -> None:
    # 规格示例：echo("World") == "echo: World"
    assert echo("World") == "echo: World"


def test_echo_other_name_is_interpolated() -> None:
    # 三角化：确认 name 被插值而非硬编码
    assert echo("Ada") == "echo: Ada"
