from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.parking_table import ParkingTable

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingTablePublication:
    """
    A publication defining one or more tables that have entries of parking sites or
    groups of them, located in an urban or interurban context.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_table: List[ParkingTable] = field(
        default_factory=list,
        metadata={
            "name": "parkingTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
