from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.maintenance_vehicles import (
    MaintenanceVehicles,
)
from datexii.models.eu.datexii.v2.mobility import Mobility
from datexii.models.eu.datexii.v2.operator_action import OperatorAction
from datexii.models.eu.datexii.v2.roadworks_duration_enum import (
    RoadworksDurationEnum,
)
from datexii.models.eu.datexii.v2.roadworks_scale_enum import (
    RoadworksScaleEnum,
)
from datexii.models.eu.datexii.v2.subjects import Subjects

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Roadworks(OperatorAction):
    """
    Highway maintenance, installation and construction activities that may
    potentially affect traffic operations.

    :ivar roadworks_duration: Indicates in general terms the expected
        duration of the roadworks.
    :ivar roadworks_scale: Indication of the scale of the roadworks in
        terms of the traffic disruption they are likely to cause.
    :ivar under_traffic: Indicates that the road section where the
        roadworks are located is under traffic or not under traffic.
        'True' indicates the road is under traffic.
    :ivar urgent_roadworks: Indication of whether the roadworks are
        considered to be urgent whereby emergency work is being, or
        needs to be, undertaken to mitigate safety concerns. 'True'
        indicates they are urgent.
    :ivar mobility:
    :ivar subjects:
    :ivar maintenance_vehicles:
    :ivar roadworks_extension:
    """

    roadworks_duration: None | RoadworksDurationEnum = field(
        default=None,
        metadata={
            "name": "roadworksDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    roadworks_scale: None | RoadworksScaleEnum = field(
        default=None,
        metadata={
            "name": "roadworksScale",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    under_traffic: None | bool = field(
        default=None,
        metadata={
            "name": "underTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    urgent_roadworks: None | bool = field(
        default=None,
        metadata={
            "name": "urgentRoadworks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    mobility: None | Mobility = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    subjects: None | Subjects = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maintenance_vehicles: None | MaintenanceVehicles = field(
        default=None,
        metadata={
            "name": "maintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    roadworks_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
