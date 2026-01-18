from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class DoubleValueType(ValueType):
    """
    DoubleValueType is a refinement of SimpleValueType limiting the content
    to be a double.

    This can be further refined ranges, etc.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: float | None = field(default=None)
