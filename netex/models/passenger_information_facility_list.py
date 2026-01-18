from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
