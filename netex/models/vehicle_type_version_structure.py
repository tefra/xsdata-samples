from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

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


@dataclass(kw_only=True)
class VehicleTypeVersionStructure(TransportTypeVersionStructure):
    class Meta:
        name = "VehicleType_VersionStructure"

    capacities: None | PassengerCapacitiesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: None | bool = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: None | bool = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: None | bool = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: None | Decimal = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    included_in: None | VehicleTypeRefStructure = field(
        default=None,
        metadata={
            "name": "IncludedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classified_as_ref: None | VehicleModelRefStructure = field(
        default=None,
        metadata={
            "name": "ClassifiedAsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: None | ServiceFacilitySetsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_carry: None | PassengerCarryingRequirementsRelStructure = field(
        default=None,
        metadata={
            "name": "canCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_manoeuvre: None | VehicleManoeuvringRequirementsRelStructure = field(
        default=None,
        metadata={
            "name": "canManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    satisfies_facility_requirements: (
        None | FacilityRequirementsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "satisfiesFacilityRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
