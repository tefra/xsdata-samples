from __future__ import annotations

from dataclasses import dataclass, field

from .log_entry_version_structure import LogEntryVersionStructure
from .parking_ref import ParkingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RentalAvailabilityVersionStructure(LogEntryVersionStructure):
    class Meta:
        name = "RentalAvailability_VersionStructure"

    parking_ref: None | ParkingRef = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    is_operational: None | bool = field(
        default=None,
        metadata={
            "name": "IsOperational",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_renting: None | bool = field(
        default=None,
        metadata={
            "name": "IsRenting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_accepting_returns: None | bool = field(
        default=None,
        metadata={
            "name": "IsAcceptingReturns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    available_vehicles: None | int = field(
        default=None,
        metadata={
            "name": "AvailableVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_vehicles: None | int = field(
        default=None,
        metadata={
            "name": "DisabledVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    available_docks: None | int = field(
        default=None,
        metadata={
            "name": "AvailableDocks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_docks: None | int = field(
        default=None,
        metadata={
            "name": "DisabledDocks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
