from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.road_maintenance_type_enum import (
    RoadMaintenanceTypeEnum,
)
from datexii.models.eu.datexii.v2.roadworks import Roadworks

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MaintenanceWorks(Roadworks):
    """
    Roadworks involving the maintenance or installation of infrastructure.

    :ivar road_maintenance_type: The type of road maintenance or
        installation work at the specified location.
    :ivar maintenance_works_extension:
    """

    road_maintenance_type: list[RoadMaintenanceTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    maintenance_works_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
