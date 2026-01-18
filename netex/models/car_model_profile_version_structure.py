from __future__ import annotations

from dataclasses import dataclass, field

from .transmission_enumeration import TransmissionEnumeration
from .vehicle_model_profile_version_structure import (
    VehicleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    class Meta:
        name = "CarModelProfile_VersionStructure"

    seats: None | int = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    doors: None | int = field(
        default=None,
        metadata={
            "name": "Doors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transmission: None | TransmissionEnumeration = field(
        default=None,
        metadata={
            "name": "Transmission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cruise_control: None | bool = field(
        default=None,
        metadata={
            "name": "CruiseControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sat_nav: None | bool = field(
        default=None,
        metadata={
            "name": "SatNav",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioning: None | bool = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    convertible: None | bool = field(
        default=None,
        metadata={
            "name": "Convertible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usb_power_sockets: None | bool = field(
        default=None,
        metadata={
            "name": "UsbPowerSockets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    winter_tyres: None | bool = field(
        default=None,
        metadata={
            "name": "WinterTyres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    chains: None | bool = field(
        default=None,
        metadata={
            "name": "Chains",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trailer_hitch: None | bool = field(
        default=None,
        metadata={
            "name": "TrailerHitch",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roof_rack: None | bool = field(
        default=None,
        metadata={
            "name": "RoofRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cycle_rack: None | bool = field(
        default=None,
        metadata={
            "name": "CycleRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ski_rack: None | bool = field(
        default=None,
        metadata={
            "name": "SkiRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
