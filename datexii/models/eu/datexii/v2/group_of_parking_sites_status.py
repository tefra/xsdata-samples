from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_parking_sites_status_enum import (
    GroupOfParkingSitesStatusEnum,
)
from datexii.models.eu.datexii.v2.parking_record_status import (
    ParkingRecordStatus,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfParkingSitesStatus(ParkingRecordStatus):
    """
    Dynamic status information for the static object 'GroupOfParkingSites'.

    :ivar group_of_parking_sites_status: The status of the group of
        parking sites (available spaces or not).
    :ivar group_of_parking_sites_status_extension:
    """

    group_of_parking_sites_status: Optional[
        GroupOfParkingSitesStatusEnum
    ] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_sites_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfParkingSitesStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
