from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.network_management import NetworkManagement
from datexii.models.eu.datexii.v2.road_or_carriageway_or_lane_management_type_enum import (
    RoadOrCarriagewayOrLaneManagementTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadOrCarriagewayOrLaneManagement(NetworkManagement):
    """
    Road, carriageway or lane management action that is instigated by the
    network/road operator.

    :ivar road_or_carriageway_or_lane_management_type: Type of road,
        carriageway or lane management action instigated by operator.
    :ivar minimum_car_occupancy: The minimum number of persons required
        in a vehicle in order for it to be allowed to transit the
        specified road section.
    :ivar road_or_carriageway_or_lane_management_extension:
    """

    road_or_carriageway_or_lane_management_type: (
        RoadOrCarriagewayOrLaneManagementTypeEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    minimum_car_occupancy: int | None = field(
        default=None,
        metadata={
            "name": "minimumCarOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    road_or_carriageway_or_lane_management_extension: ExtensionType | None = (
        field(
            default=None,
            metadata={
                "name": "roadOrCarriagewayOrLaneManagementExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
