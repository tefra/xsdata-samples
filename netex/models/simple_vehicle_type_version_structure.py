from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

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

    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_axle_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstAxleHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    licence_requirements: Optional[LicenceRequirementsEnumeration] = field(
        default=None,
        metadata={
            "name": "LicenceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_category: Optional[SimpleVehicleCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    portable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Portable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accepted_driver_permits: Optional[AcceptedDriverPermitsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "acceptedDriverPermits",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
