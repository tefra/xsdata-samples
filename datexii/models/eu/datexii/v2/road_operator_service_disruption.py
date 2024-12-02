from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.non_road_event_information import (
    NonRoadEventInformation,
)
from datexii.models.eu.datexii.v2.road_operator_service_disruption_type_enum import (
    RoadOperatorServiceDisruptionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadOperatorServiceDisruption(NonRoadEventInformation):
    """
    Details of disruption to normal road operator services.

    :ivar road_operator_service_disruption_type: The type of road
        operator service which is disrupted.
    :ivar road_operator_service_disruption_extension:
    """

    road_operator_service_disruption_type: list[
        RoadOperatorServiceDisruptionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "roadOperatorServiceDisruptionExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
