from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.accessibility_enum import AccessibilityEnum
from datexii.models.eu.datexii.v2.dedicated_access import DedicatedAccess
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.occupancy_detection_type_enum import (
    OccupancyDetectionTypeEnum,
)
from datexii.models.eu.datexii.v2.parking_assignment import ParkingAssignment
from datexii.models.eu.datexii.v2.parking_mode_enum import ParkingModeEnum
from datexii.models.eu.datexii.v2.parking_security_enum import (
    ParkingSecurityEnum,
)
from datexii.models.eu.datexii.v2.parking_space_accessibility_enum import (
    ParkingSpaceAccessibilityEnum,
)
from datexii.models.eu.datexii.v2.parking_space_basics_equipment_or_service_facility_index_parking_equipment_or_service_facility import (
    ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility,
)
from datexii.models.eu.datexii.v2.parking_space_basics_scenario_index_parking_usage_scenario import (
    ParkingSpaceBasicsScenarioIndexParkingUsageScenario,
)
from datexii.models.eu.datexii.v2.parking_space_physics_enum import (
    ParkingSpacePhysicsEnum,
)
from datexii.models.eu.datexii.v2.reservation_type_enum import (
    ReservationTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingSpaceBasics:
    """
    Common properties of parking spaces and groups of parking spaces.

    :ivar parking_space_or_group_identifier: A public identifier or
        short description for the parking space or group of parking
        spaces, for example "6D" or "Truck parking west".
    :ivar parking_floor_or_level: The floor or level of the parking site
        on which the assigned parking spaces are located.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar parking_space_accessibility: Further easements for handicapped
        people related to this parking space or this group of parking
        spaces.
    :ivar parking_space_physics: Specifies 'driveThrough' or 'openAir'
        for the parking space or the group of parking spaces.
    :ivar parking_mode: The arrangement of the parking space or the
        group of parking spaces in relation to the road.
    :ivar parking_reservation: Indication of whether a parking
        reservation service is available and/or mandatory.
    :ivar maximum_parking_duration: The maximum parking duration for a
        parking record, a parking space or a group of parking spaces
        (e.g. to avoid overnight parking).
    :ivar distance_from_primary_road: Specifies the distance from the
        primary road in metres. Especially useful, if parking is located
        on a smaller type of road.
    :ivar parking_occupany_detection_type: Type of parking occupancy
        detection for a parking record, a parking space or a group of
        parking spaces, if any (balancing, single slot, ...  ).
    :ivar parking_security: Specifies security measures related to the
        parking site or particular spaces.
    :ivar dedicated_access:
    :ivar only_assigned_parking: Parking is only allowed for the
        assignment given in this class, i.e. other assignments are not
        allowed. By using this role, it is not allowed to use
        'assignedParkingAmongOthers' and 'prohibitedParking' for the
        same type of attributes.
    :ivar assigned_parking_among_others: Assignments for parking. Other
        assignments are allowed as well, i.e. the parking spaces are
        convenient for this kind of assignment.
    :ivar prohibited_parking: Parking is not allowed for the given
        assignment.
    :ivar parking_equipment_or_service_facility: Equiment, services and
        szenarios, which are directly related to the assigned parking
        space or parking space group. Note that the infrastructure index
        must be unique with respect to the Parking class' infrastrucure
        indeces
    :ivar parking_usage_scenario:
    :ivar parking_space_basics_extension:
    """

    parking_space_or_group_identifier: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "parkingSpaceOrGroupIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_floor_or_level: None | int = field(
        default=None,
        metadata={
            "name": "parkingFloorOrLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accessibility: list[AccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_accessibility: list[ParkingSpaceAccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpaceAccessibility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_physics: list[ParkingSpacePhysicsEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpacePhysics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 2,
        },
    )
    parking_mode: None | ParkingModeEnum = field(
        default=None,
        metadata={
            "name": "parkingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_reservation: None | ReservationTypeEnum = field(
        default=None,
        metadata={
            "name": "parkingReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_parking_duration: None | float = field(
        default=None,
        metadata={
            "name": "maximumParkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    distance_from_primary_road: None | int = field(
        default=None,
        metadata={
            "name": "distanceFromPrimaryRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupany_detection_type: list[OccupancyDetectionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingOccupanyDetectionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_security: list[ParkingSecurityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dedicated_access: list[DedicatedAccess] = field(
        default_factory=list,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    only_assigned_parking: None | ParkingAssignment = field(
        default=None,
        metadata={
            "name": "onlyAssignedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    assigned_parking_among_others: None | ParkingAssignment = field(
        default=None,
        metadata={
            "name": "assignedParkingAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    prohibited_parking: None | ParkingAssignment = field(
        default=None,
        metadata={
            "name": "prohibitedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_equipment_or_service_facility: list[
        ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility
    ] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_usage_scenario: list[
        ParkingSpaceBasicsScenarioIndexParkingUsageScenario
    ] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_basics_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
