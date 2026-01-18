from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_parking_sites_type_enum import (
    GroupOfParkingSitesTypeEnum,
)
from datexii.models.eu.datexii.v2.parking_record import ParkingRecord
from datexii.models.eu.datexii.v2.parking_record_versioned_reference import (
    ParkingRecordVersionedReference,
)
from datexii.models.eu.datexii.v2.parking_site import ParkingSite

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfParkingSites(ParkingRecord):
    """
    A logical composition of parking sites with aggregated properties (e.g.
    number of spaces).

    Examples: Urban parking area "West" or all truck parkings along a
    motorway. The included parking sites may -but must not- be specified as
    subcomponents.

    :ivar group_of_parking_sites_type: The type of this group of parking
        sites.
    :ivar parking_site_by_reference: Parking sites of this collection
        defined by reference.
    :ivar parking_site:
    :ivar group_of_parking_sites_extension:
    """

    group_of_parking_sites_type: GroupOfParkingSitesTypeEnum | None = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_by_reference: list[ParkingRecordVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteByReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site: list[ParkingSite] = field(
        default_factory=list,
        metadata={
            "name": "parkingSite",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_sites_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
