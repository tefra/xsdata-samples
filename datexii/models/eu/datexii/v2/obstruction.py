from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.mobility import Mobility
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Obstruction(TrafficElement):
    """
    Any stationary or moving obstacle of a physical nature (e.g. obstacles
    or vehicles from an earlier accident, shed loads on carriageway, rock
    fall, abnormal or dangerous loads, or animals etc.) which could disrupt
    or endanger traffic.

    :ivar number_of_obstructions: The number of obstructions that are
        partly or wholly blocking the road.
    :ivar mobility_of_obstruction: The mobility of the obstruction.
    :ivar obstruction_extension:
    """

    number_of_obstructions: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfObstructions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    mobility_of_obstruction: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfObstruction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
