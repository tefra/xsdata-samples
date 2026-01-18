from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.simple_data_structure_representation_type import (
    SimpleDataStructureRepresentationType,
)
from sdmx_ml.models.time_text_format_type import TimeTextFormatType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class TimeDimensionRepresentationType(SimpleDataStructureRepresentationType):
    """
    TimeDimensionRepresentationType defines the representation for the time
    dimension.

    Enumerated values are not allowed.
    """

    enumeration_or_enumeration_format: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    text_format: TimeTextFormatType = field(
        metadata={
            "name": "TextFormat",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        }
    )
