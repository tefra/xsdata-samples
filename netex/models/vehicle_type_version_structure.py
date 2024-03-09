from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .facility_requirements_rel_structure import (
    FacilityRequirementsRelStructure,
)
from .passenger_capacities_rel_structure import PassengerCapacitiesRelStructure
from .passenger_carrying_requirements_rel_structure import (
    PassengerCarryingRequirementsRelStructure,
)
from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .transport_type_version_structure import TransportTypeVersionStructure
from .vehicle_manoeuvring_requirements_rel_structure import (
    VehicleManoeuvringRequirementsRelStructure,
)
from .vehicle_model_ref_structure import VehicleModelRefStructure
from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeVersionStructure(TransportTypeVersionStructure):
    class Meta:
        name = "VehicleType_VersionStructure"

    capacities: Optional[PassengerCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    included_in: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "IncludedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classified_as_ref: Optional[VehicleModelRefStructure] = field(
        default=None,
        metadata={
            "name": "ClassifiedAsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_carry: Optional[PassengerCarryingRequirementsRelStructure] = field(
        default=None,
        metadata={
            "name": "canCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_manoeuvre: Optional[VehicleManoeuvringRequirementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "canManoeuvre",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    satisfies_facility_requirements: Optional[
        FacilityRequirementsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "satisfiesFacilityRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
