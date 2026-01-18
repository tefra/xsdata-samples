from __future__ import annotations

from dataclasses import dataclass, field

from .passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: PassengerInformationFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
