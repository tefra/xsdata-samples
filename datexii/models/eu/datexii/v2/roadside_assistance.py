from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operator_action import OperatorAction
from datexii.models.eu.datexii.v2.roadside_assistance_type_enum import (
    RoadsideAssistanceTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadsideAssistance(OperatorAction):
    """
    Details of road side assistance required or being given.

    :ivar roadside_assistance_type: Indicates the nature of the road
        side assistance that will be, is or has been provided.
    :ivar roadside_assistance_extension:
    """

    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
