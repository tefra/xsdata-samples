from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_table_versioned_reference import (
    ParkingTableVersionedReference,
)
from datexii.models.eu.datexii.v2.parking_vehicle import ParkingVehicle

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingVehiclesPublication:
    """
    Information about individual parking vehicles.

    :ivar parking_table_reference: It is possible to limit the
        publication to one or more ParkingTable and to set a reference
        to these tables here.
    :ivar parking_vehicle:
    """

    parking_table_reference: list[ParkingTableVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "parkingTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_vehicle: list[ParkingVehicle] = field(
        default_factory=list,
        metadata={
            "name": "parkingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
