"""louder 公开接口的行为规格。

seam：从仓库根 louder 模块导入的 louder(name) 函数。
期望值取自 ticket 规格给出的已知示例（复用 echo 后 .upper()），独立于实现方式。
"""

from louder import louder


def test_louder_world() -> None:
    # 规格示例：louder("World") == "ECHO: WORLD"
    assert louder("World") == "ECHO: WORLD"


def test_louder_other_name_is_interpolated() -> None:
    # 三角化：确认 name 经 echo 插值后整体大写，而非硬编码
    assert louder("Ada") == "ECHO: ADA"
