from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.opening_status_enum import OpeningStatusEnum
from datexii.models.eu.datexii.v2.parking_access_reference import (
    ParkingAccessReference,
)
from datexii.models.eu.datexii.v2.parking_fault_enum import ParkingFaultEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingAccessStatus:
    """
    The opening and fault status of one access.

    :ivar access_reference: The reference to an access defined in the
        static part of the model.
    :ivar access_opening_status: The opening status of this access.
    :ivar access_fault: A fault indicator for this special access.
    :ivar parking_access_status_extension:
    """

    access_reference: Optional[ParkingAccessReference] = field(
        default=None,
        metadata={
            "name": "accessReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    access_opening_status: Optional[OpeningStatusEnum] = field(
        default=None,
        metadata={
            "name": "accessOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    access_fault: List[ParkingFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "accessFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_access_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingAccessStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
