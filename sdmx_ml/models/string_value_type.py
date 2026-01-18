from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.value_type import ValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class StringValueType(ValueType):
    """
    StringValueType is a refinement of SimpleValueType limiting the content
    to be a string.

    This can be further refined with facets, patterns, etc.
    """

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")
