from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonRoadEventInformation(SituationRecord):
    """
    Information about an event which is not on the road, but which may influence
    the behaviour of drivers and hence the characteristics of the traffic flow.
    """
    non_road_event_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonRoadEventInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
