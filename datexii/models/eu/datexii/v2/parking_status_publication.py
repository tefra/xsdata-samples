from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.parking_record_status import (
    ParkingRecordStatus,
)
from datexii.models.eu.datexii.v2.parking_table_versioned_reference import (
    ParkingTableVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingStatusPublication:
    """
    A publication containing the current status of one or more parking
    sites and/or group of parking sites.

    :ivar parking_table_reference: It is possible to limit the
        publication to one or more ParkingTable and to set a reference
        to these tables here.
    :ivar header_information:
    :ivar parking_record_status:
    """

    parking_table_reference: list[ParkingTableVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_record_status: list[ParkingRecordStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingRecordStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
