from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.mobility import Mobility
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Activity(TrafficElement):
    """
    Deliberate human action external to the traffic stream or roadway which
    could disrupt traffic.

    :ivar mobility_of_activity: Mobility of the activity.
    :ivar activity_extension:
    """

    mobility_of_activity: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfActivity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "activityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
