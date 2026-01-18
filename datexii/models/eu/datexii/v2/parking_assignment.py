from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.hazardous_materials import HazardousMaterials
from datexii.models.eu.datexii.v2.parking_duration_enum import (
    ParkingDurationEnum,
)
from datexii.models.eu.datexii.v2.parking_permit import ParkingPermit
from datexii.models.eu.datexii.v2.time_period_by_hour import TimePeriodByHour
from datexii.models.eu.datexii.v2.user_type_enum import UserTypeEnum
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingAssignment:
    """
    One set of prohibited/only allowed/convenient assignment for parking
    space(s), parking site(s) or an access.

    Same kind of data forms a union (e.g. lorries OR buses), different kind
    of data forms an intersection (e.g. residents AND long-term).

    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar parking_duration: Temporal parking classification for this
        assignment (long term, short term, ...). Depending on the used
        role, these classifications are either assigned or prohibited.
    :ivar vehicle_characteristics:
    :ivar hazardous_materials: Hazardous Material which is prohibited to
        park there.
    :ivar time_period_by_hour: Used for example for mixed parking areas.
        If at least one restrictedValidity is given, spaces are not
        available outside the union of all given time ranges. EndTime
        might be a lower value than start time, whem validity contains
        midnight.
    :ivar parking_permit:
    :ivar parking_assignment_extension:
    """

    applicable_for_user: list[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_duration: list[ParkingDurationEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_characteristics: list[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    hazardous_materials: list[HazardousMaterials] = field(
        default_factory=list,
        metadata={
            "name": "hazardousMaterials",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    time_period_by_hour: list[TimePeriodByHour] = field(
        default_factory=list,
        metadata={
            "name": "timePeriodByHour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_permit: list[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_assignment_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingAssignmentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
