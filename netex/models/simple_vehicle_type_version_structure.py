from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .accepted_driver_permits_rel_structure import (
    AcceptedDriverPermitsRelStructure,
)
from .licence_requirements_enumeration import LicenceRequirementsEnumeration
from .simple_vehicle_category_enumeration import (
    SimpleVehicleCategoryEnumeration,
)
from .transport_type_version_structure import TransportTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleVehicleTypeVersionStructure(TransportTypeVersionStructure):
    class Meta:
        name = "SimpleVehicleType_VersionStructure"

    length: None | Decimal = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: None | Decimal = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_axle_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "FirstAxleHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    licence_requirements: None | LicenceRequirementsEnumeration = field(
        default=None,
        metadata={
            "name": "LicenceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_category: None | SimpleVehicleCategoryEnumeration = field(
        default=None,
        metadata={
            "name": "VehicleCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_age: None | int = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    portable: None | bool = field(
        default=None,
        metadata={
            "name": "Portable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accepted_driver_permits: None | AcceptedDriverPermitsRelStructure = field(
        default=None,
        metadata={
            "name": "acceptedDriverPermits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
