from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataComponentValueType(SimpleComponentValueType):
    """
    DataComponentValueType derives from the SimpleValueType, but does not
    allow for validity dates.
    """

    valid_from: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_to: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
