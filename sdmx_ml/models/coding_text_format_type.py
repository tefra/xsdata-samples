from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.simple_code_data_type import SimpleCodeDataType
from sdmx_ml.models.simple_component_text_format_type import (
    SimpleComponentTextFormatType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class CodingTextFormatType(SimpleComponentTextFormatType):
    """
    :ivar sentinel_value: SentinelValue defines a value that has a
        special meaning within the text format representation of a
        component.
    :ivar text_type:
    :ivar time_interval:
    :ivar start_time:
    :ivar end_time:
    :ivar decimals:
    """

    sentinel_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    text_type: None | SimpleCodeDataType = field(
        default=None,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
    time_interval: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    start_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    end_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    decimals: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
