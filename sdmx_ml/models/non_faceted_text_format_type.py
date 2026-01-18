from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.simple_component_text_format_type import (
    SimpleComponentTextFormatType,
)
from sdmx_ml.models.simple_data_type import SimpleDataType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class NonFacetedTextFormatType(SimpleComponentTextFormatType):
    """
    NonFacetedTextFormatType is a restricted version of the
    SimpleComponentTextFormatType that does not allow for any facets.

    :ivar sentinel_value: SentinelValue defines a value that has a
        special meaning within the text format representation of a
        component.
    :ivar text_type:
    :ivar is_sequence:
    :ivar interval:
    :ivar start_value:
    :ivar end_value:
    :ivar time_interval:
    :ivar start_time:
    :ivar end_time:
    :ivar min_length:
    :ivar max_length:
    :ivar min_value:
    :ivar max_value:
    :ivar decimals:
    :ivar pattern:
    """

    sentinel_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    text_type: SimpleDataType | None = field(
        default=None,
        metadata={
            "name": "textType",
            "type": "Attribute",
        },
    )
    is_sequence: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    interval: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    start_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    end_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
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
    min_length: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_length: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    min_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    max_value: Any = field(
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
    pattern: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
