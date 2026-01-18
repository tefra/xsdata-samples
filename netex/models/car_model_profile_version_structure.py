from dataclasses import dataclass, field
from typing import Optional

from .transmission_enumeration import TransmissionEnumeration
from .vehicle_model_profile_version_structure import (
    VehicleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    class Meta:
        name = "CarModelProfile_VersionStructure"

    seats: int | None = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    doors: int | None = field(
        default=None,
        metadata={
            "name": "Doors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transmission: TransmissionEnumeration | None = field(
        default=None,
        metadata={
            "name": "Transmission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cruise_control: bool | None = field(
        default=None,
        metadata={
            "name": "CruiseControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sat_nav: bool | None = field(
        default=None,
        metadata={
            "name": "SatNav",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioning: bool | None = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    convertible: bool | None = field(
        default=None,
        metadata={
            "name": "Convertible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usb_power_sockets: bool | None = field(
        default=None,
        metadata={
            "name": "UsbPowerSockets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    winter_tyres: bool | None = field(
        default=None,
        metadata={
            "name": "WinterTyres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    chains: bool | None = field(
        default=None,
        metadata={
            "name": "Chains",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trailer_hitch: bool | None = field(
        default=None,
        metadata={
            "name": "TrailerHitch",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roof_rack: bool | None = field(
        default=None,
        metadata={
            "name": "RoofRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cycle_rack: bool | None = field(
        default=None,
        metadata={
            "name": "CycleRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ski_rack: bool | None = field(
        default=None,
        metadata={
            "name": "SkiRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
