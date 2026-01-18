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


@dataclass
class VehicleTypeVersionStructure(TransportTypeVersionStructure):
    class Meta:
        name = "VehicleType_VersionStructure"

    capacities: PassengerCapacitiesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: bool | None = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: bool | None = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: bool | None = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: Decimal | None = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    included_in: VehicleTypeRefStructure | None = field(
        default=None,
        metadata={
            "name": "IncludedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classified_as_ref: VehicleModelRefStructure | None = field(
        default=None,
        metadata={
            "name": "ClassifiedAsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: ServiceFacilitySetsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_carry: PassengerCarryingRequirementsRelStructure | None = field(
        default=None,
        metadata={
            "name": "canCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_manoeuvre: VehicleManoeuvringRequirementsRelStructure | None = field(
        default=None,
        metadata={
            "name": "canManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    satisfies_facility_requirements: (
        FacilityRequirementsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "satisfiesFacilityRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
