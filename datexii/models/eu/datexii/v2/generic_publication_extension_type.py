from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_status_publication import (
    ParkingStatusPublication,
)
from datexii.models.eu.datexii.v2.parking_table_publication import (
    ParkingTablePublication,
)
from datexii.models.eu.datexii.v2.parking_vehicles_publication import (
    ParkingVehiclesPublication,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GenericPublicationExtensionType:
    class Meta:
        name = "_GenericPublicationExtensionType"

    parking_table_publication: ParkingTablePublication | None = field(
        default=None,
        metadata={
            "name": "parkingTablePublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_status_publication: ParkingStatusPublication | None = field(
        default=None,
        metadata={
            "name": "parkingStatusPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_vehicles_publication: ParkingVehiclesPublication | None = field(
        default=None,
        metadata={
            "name": "parkingVehiclesPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
