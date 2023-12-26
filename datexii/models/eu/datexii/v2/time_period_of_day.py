from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TimePeriodOfDay:
    """
    Specification of a continuous period of time within a 24 hour period.
    """

    time_period_of_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodOfDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
