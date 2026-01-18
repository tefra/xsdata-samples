from __future__ import annotations

from dataclasses import dataclass

from .rental_availability_version_structure import (
    RentalAvailabilityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RentalAvailability(RentalAvailabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
