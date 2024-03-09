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

    seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    doors: Optional[int] = field(
        default=None,
        metadata={
            "name": "Doors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transmission: Optional[TransmissionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transmission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cruise_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CruiseControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sat_nav: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SatNav",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    convertible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Convertible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usb_power_sockets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsbPowerSockets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    winter_tyres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WinterTyres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    chains: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Chains",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trailer_hitch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrailerHitch",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roof_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RoofRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cycle_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CycleRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ski_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SkiRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
