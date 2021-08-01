from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.parking_status_publication import ParkingStatusPublication
from datexii.models.eu.datexii.v2.parking_table_publication import ParkingTablePublication
from datexii.models.eu.datexii.v2.parking_vehicles_publication import ParkingVehiclesPublication

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GenericPublicationExtensionType:
    class Meta:
        name = "_GenericPublicationExtensionType"

    parking_table_publication: Optional[ParkingTablePublication] = field(
        default=None,
        metadata={
            "name": "parkingTablePublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_publication: Optional[ParkingStatusPublication] = field(
        default=None,
        metadata={
            "name": "parkingStatusPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vehicles_publication: Optional[ParkingVehiclesPublication] = field(
        default=None,
        metadata={
            "name": "parkingVehiclesPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
