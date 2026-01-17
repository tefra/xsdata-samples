from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.simple_component_text_format_type import (
    SimpleComponentTextFormatType,
)
from sdmx_ml.models.time_data_type import TimeDataType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TimeTextFormatType(SimpleComponentTextFormatType):
    """
    TimeTextFormat is a restricted version of the
    SimpleComponentTextFormatType that only allows time based format and
    specifies a default ObservationalTimePeriod representation and facets
    of a start and end time.
    """

    text_type: TimeDataType = field(
        default=TimeDataType.OBSERVATIONAL_TIME_PERIOD,
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
