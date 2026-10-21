"""greeter 公开接口的行为规格。

seam：从仓库根 greeter 模块导入的 greet(name) 函数。
期望值取自 ticket 规格给出的已知示例，独立于实现方式。
"""

from greeter import greet


def test_greet_world() -> None:
    # 规格示例：greet("World") == "Hello, World!"
    assert greet("World") == "Hello, World!"


def test_greet_other_name_is_interpolated() -> None:
    # 三角化：确认 name 被插值而非硬编码
    assert greet("Ada") == "Hello, Ada!"
