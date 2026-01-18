from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.access_category_enum import (
    AccessCategoryEnum,
)
from datexii.models.eu.datexii.v2.access_equipment_enum import (
    AccessEquipmentEnum,
)
from datexii.models.eu.datexii.v2.accessibility_enum import AccessibilityEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.opening_times import OpeningTimes
from datexii.models.eu.datexii.v2.parking_assignment import ParkingAssignment
from datexii.models.eu.datexii.v2.road import Road

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingAccess:
    """
    Describes one entrance or exit (or both) to a parking site.

    :ivar access_category: Specifies the category(s) of this access.
    :ivar access_name: A name of the entrance or exit. This might be an
        indication to the corresponding road, for example.
    :ivar access_equipment: Specifies additional equipment for this
        access.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar access_only_assigned_for: Only the assignment given in this
        class is allowed for this access, i.e. other assignments are not
        allowed. By using this role, do not use the same set of
        attributes within the other two roles.
    :ivar access_assigned_among_others: The assignment given in this
        class is convenient for this access, but not exclusionary. By
        using this role, do not use the same set of attributes within
        the other two roles.
    :ivar access_prohibited_for: The assignment given in this class is
        prohibited for this access. By using this role, do not use the
        same set of attributes within the other two roles.
    :ivar primary_road: Identification for up to two primary roads
        located nearby the access or which make the parking accessible.
    :ivar location:
    :ivar opening_times:
    :ivar parking_access_extension:
    :ivar id:
    """

    access_category: list[AccessCategoryEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessCategory",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    access_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "accessName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    access_equipment: list[AccessEquipmentEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessEquipment",
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
    photo_url: str | None = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    access_only_assigned_for: ParkingAssignment | None = field(
        default=None,
        metadata={
            "name": "accessOnlyAssignedFor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    access_assigned_among_others: ParkingAssignment | None = field(
        default=None,
        metadata={
            "name": "accessAssignedAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    access_prohibited_for: ParkingAssignment | None = field(
        default=None,
        metadata={
            "name": "accessProhibitedFor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    primary_road: list[Road] = field(
        default_factory=list,
        metadata={
            "name": "primaryRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location: Location | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    opening_times: OpeningTimes | None = field(
        default=None,
        metadata={
            "name": "openingTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_access_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingAccessExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
