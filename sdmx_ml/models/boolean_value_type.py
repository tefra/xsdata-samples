from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class BooleanValueType(ValueType):
    """
    BooleanValueType is a refinement of SimpleValueType limiting the
    content to be a boolean.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: bool = field()
