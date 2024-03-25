from dataclasses import dataclass, field
from typing import Optional, Tuple, Type, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.time_period_range_type import TimePeriodRangeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TimeRangeValueType:
    """TimeRangeValueType allows a time period value to be expressed as a range.

    It can be expressed as the period before a period, after a period,
    or between two periods. Each of these properties can specify their
    inclusion in regards to the range.
    """

    choice: Tuple[
        Union[
            "TimeRangeValueType.BeforePeriod",
            "TimeRangeValueType.AfterPeriod",
            "TimeRangeValueType.StartPeriod",
            "TimeRangeValueType.EndPeriod",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BeforePeriod",
                    "type": Type["TimeRangeValueType.BeforePeriod"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "AfterPeriod",
                    "type": Type["TimeRangeValueType.AfterPeriod"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "StartPeriod",
                    "type": Type["TimeRangeValueType.StartPeriod"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "EndPeriod",
                    "type": Type["TimeRangeValueType.EndPeriod"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
            "max_occurs": 2,
        },
    )
    valid_from: Optional[Union[XmlPeriod, XmlDate, XmlDateTime, str]] = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    valid_to: Optional[Union[XmlPeriod, XmlDate, XmlDateTime, str]] = field(
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
