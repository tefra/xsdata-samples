from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.maintenance_vehicle_actions_enum import (
    MaintenanceVehicleActionsEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MaintenanceVehicles:
    """
    Details of the maintenance vehicles involved in the roadworks activity.

    :ivar number_of_maintenance_vehicles: The number of maintenance
        vehicles associated with the roadworks activities at the
        specified location.
    :ivar maintenance_vehicle_actions: The actions of the maintenance
        vehicles associated with the roadworks activities.
    :ivar maintenance_vehicles_extension:
    """

    number_of_maintenance_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfMaintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maintenance_vehicle_actions: list[MaintenanceVehicleActionsEnum] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceVehicleActions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maintenance_vehicles_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceVehiclesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
