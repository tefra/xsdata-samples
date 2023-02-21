from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.non_road_event_information import NonRoadEventInformation
from datexii.models.eu.datexii.v2.roadside_service_disruption_type_enum import RoadsideServiceDisruptionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadsideServiceDisruption(NonRoadEventInformation):
    """
    Details of disruption to normal roadside services (e.g. specific services at a
    service area).

    :ivar roadside_service_disruption_type: The type of roadside service
        which is disrupted.
    :ivar roadside_service_disruption_extension:
    """
    roadside_service_disruption_type: List[RoadsideServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadsideServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    roadside_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
