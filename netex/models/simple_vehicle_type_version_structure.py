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

    length: Decimal | None = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Decimal | None = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Decimal | None = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weight: Decimal | None = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_axle_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "FirstAxleHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    licence_requirements: LicenceRequirementsEnumeration | None = field(
        default=None,
        metadata={
            "name": "LicenceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_category: SimpleVehicleCategoryEnumeration | None = field(
        default=None,
        metadata={
            "name": "VehicleCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_age: int | None = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    portable: bool | None = field(
        default=None,
        metadata={
            "name": "Portable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accepted_driver_permits: AcceptedDriverPermitsRelStructure | None = field(
        default=None,
        metadata={
            "name": "acceptedDriverPermits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
