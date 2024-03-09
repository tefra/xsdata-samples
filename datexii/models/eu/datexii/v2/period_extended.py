from dataclasses import dataclass, field
from typing import List

from datexii.models.eu.datexii.v2.special_day import SpecialDay

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PeriodExtended:
    """
    An extension point for Period offering the possibility to describe special days
    and public holidays.

    :ivar recurring_special_day: A recurring period in terms of special
        days.
    """

    recurring_special_day: List[SpecialDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringSpecialDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
