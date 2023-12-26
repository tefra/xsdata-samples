from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.abnormal_traffic_type_enum import (
    AbnormalTrafficTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.relative_traffic_flow_enum import (
    RelativeTrafficFlowEnum,
)
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement
from datexii.models.eu.datexii.v2.traffic_flow_characteristics_enum import (
    TrafficFlowCharacteristicsEnum,
)
from datexii.models.eu.datexii.v2.traffic_trend_type_enum import (
    TrafficTrendTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AbnormalTraffic(TrafficElement):
    """
    A traffic condition which is not normal.

    :ivar abnormal_traffic_type: A characterization of the nature of
        abnormal traffic flow, i.e. specifically relating to the nature
        of the traffic movement.
    :ivar number_of_vehicles_waiting: The number of vehicles waiting in
        a queue.
    :ivar queue_length: The length of a queue or the average length of
        queues in separate lanes due to a situation.
    :ivar relative_traffic_flow: Assessment of the traffic flow
        conditions relative to normally expected conditions at this
        date/time.
    :ivar traffic_flow_characteristics: A characterization of the
        traffic flow.
    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar abnormal_traffic_extension:
    """

    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_vehicles_waiting: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehiclesWaiting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    queue_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "queueLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    relative_traffic_flow: Optional[RelativeTrafficFlowEnum] = field(
        default=None,
        metadata={
            "name": "relativeTrafficFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_flow_characteristics: Optional[
        TrafficFlowCharacteristicsEnum
    ] = field(
        default=None,
        metadata={
            "name": "trafficFlowCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    abnormal_traffic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
