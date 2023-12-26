from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.obstruction import Obstruction
from datexii.models.eu.datexii.v2.vehicle import Vehicle
from datexii.models.eu.datexii.v2.vehicle_obstruction_type_enum import (
    VehicleObstructionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleObstruction(Obstruction):
    """
    An obstruction on the road caused by one or more vehicles.

    :ivar vehicle_obstruction_type: Characterization of an obstruction
        on the road caused by one or more vehicles.
    :ivar obstructing_vehicle: The obstructing vehicle.
    :ivar vehicle_obstruction_extension:
    """

    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
