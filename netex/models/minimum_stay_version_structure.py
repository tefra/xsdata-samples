from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .day_of_week_enumeration import DayOfWeekEnumeration
from .minimum_stay_type_enumeration import MinimumStayTypeEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MinimumStayVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "MinimumStay_VersionStructure"

    minimum_stay_type: None | MinimumStayTypeEnumeration = field(
        default=None,
        metadata={
            "name": "MinimumStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_nights_away: Iterable[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RequiresNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    minimum_number_of_nights_away: None | int = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_nights_away: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNightsAway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
