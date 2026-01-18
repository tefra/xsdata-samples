from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)
from datexii.models.eu.datexii.v2.vehicle_status_enum import VehicleStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfVehiclesInvolved:
    """
    Group of the vehicles involved having common characteristics and/or
    status.

    :ivar number_of_vehicles: The number of vehicles of this group that
        are involved.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar group_of_vehicles_involved_extension:
    """

    number_of_vehicles: int | None = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_status: VehicleStatusEnum | None = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_characteristics: VehicleCharacteristics | None = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_vehicles_involved_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "groupOfVehiclesInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
