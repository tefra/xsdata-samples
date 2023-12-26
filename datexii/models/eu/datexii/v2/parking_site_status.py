from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.opening_status_enum import OpeningStatusEnum
from datexii.models.eu.datexii.v2.parking_record_status import (
    ParkingRecordStatus,
)
from datexii.models.eu.datexii.v2.parking_site_overcrowding_status_enum import (
    ParkingSiteOvercrowdingStatusEnum,
)
from datexii.models.eu.datexii.v2.parking_site_status_enum import (
    ParkingSiteStatusEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSiteStatus(ParkingRecordStatus):
    """
    Dynamic status information for the static object 'ParkingSite'.

    :ivar parking_site_status: The status of the parking site (spaces
        available or not).
    :ivar parking_site_opening_status: The opening status of the parking
        site (open or not).
    :ivar parking_site_overcrowding_status: The overcrowding status of
        the parking site. Choose between using a two-stage approach or
        the more general statement ‘(not) overcrowding’. You can sharpen
        this information by using the ‘Thresholds’ component.
    :ivar parking_site_full_at_floor: The parking site is full at the
        specified floor(s).
    :ivar parking_site_status_extension:
    """

    parking_site_status: Optional[ParkingSiteStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_opening_status: Optional[OpeningStatusEnum] = field(
        default=None,
        metadata={
            "name": "parkingSiteOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_overcrowding_status: Optional[
        ParkingSiteOvercrowdingStatusEnum
    ] = field(
        default=None,
        metadata={
            "name": "parkingSiteOvercrowdingStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_full_at_floor: List[int] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteFullAtFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSiteStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
