from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.environmental_obstruction_type_enum import (
    EnvironmentalObstructionTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class EnvironmentalObstruction(Obstruction):
    """
    An obstruction on the road resulting from an environmental cause.

    :ivar depth: The depth of flooding or of snow on the road.
    :ivar environmental_obstruction_type: Characterization of an
        obstruction on the road resulting from an environmental cause.
    :ivar environmental_obstruction_extension:
    """

    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    environmental_obstruction_type: Optional[
        EnvironmentalObstructionTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
