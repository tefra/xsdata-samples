from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TimePeriodByHour(TimePeriodOfDay):
    """
    Specification of a continuous period within a 24 hour period by times.

    :ivar start_time_of_period: Start of time period.
    :ivar end_time_of_period: End of time period.
    :ivar time_period_by_hour_extension:
    """

    start_time_of_period: XmlTime | None = field(
        default=None,
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    end_time_of_period: XmlTime | None = field(
        default=None,
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    time_period_by_hour_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "timePeriodByHourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
