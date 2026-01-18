from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.time_period_range_type import TimePeriodRangeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TimeRangeValueType:
    """
    TimeRangeValueType allows a time period value to be expressed as a
    range.

    It can be expressed as the period before a period, after a period, or
    between two periods. Each of these properties can specify their
    inclusion in regards to the range.
    """

    choice: tuple[
        TimeRangeValueType.BeforePeriod
        | TimeRangeValueType.AfterPeriod
        | TimeRangeValueType.StartPeriod
        | TimeRangeValueType.EndPeriod,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BeforePeriod",
                    "type": ForwardRef("TimeRangeValueType.BeforePeriod"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "AfterPeriod",
                    "type": ForwardRef("TimeRangeValueType.AfterPeriod"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "StartPeriod",
                    "type": ForwardRef("TimeRangeValueType.StartPeriod"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "EndPeriod",
                    "type": ForwardRef("TimeRangeValueType.EndPeriod"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
            "max_occurs": 2,
        },
    )
    valid_from: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    valid_to: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )

    @dataclass(frozen=True)
    class BeforePeriod(TimePeriodRangeType):
        pass

    @dataclass(frozen=True)
    class AfterPeriod(TimePeriodRangeType):
        pass

    @dataclass(frozen=True)
    class StartPeriod(TimePeriodRangeType):
        pass

    @dataclass(frozen=True)
    class EndPeriod(TimePeriodRangeType):
        pass
