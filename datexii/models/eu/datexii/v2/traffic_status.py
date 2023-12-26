from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.traffic_status_value import (
    TrafficStatusValue,
)
from datexii.models.eu.datexii.v2.traffic_trend_type_enum import (
    TrafficTrendTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficStatus(BasicData):
    """
    The status of traffic conditions on a specific section or at a specific point
    on the road network.

    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar traffic_status: Status of traffic conditions on the identified
        section of road in the specified direction.
    :ivar traffic_status_extension:
    """

    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_status: Optional[TrafficStatusValue] = field(
        default=None,
        metadata={
            "name": "trafficStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
