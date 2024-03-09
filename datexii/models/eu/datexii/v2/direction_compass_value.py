from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.direction_compass_enum import (
    DirectionCompassEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DirectionCompassValue(DataValue):
    """
    A measured or calculated value of direction as a point of the compass.

    :ivar direction_compass: A value of direction expressed in terms of
        points of the compass.
    :ivar direction_compass_value_extension:
    """

    direction_compass: Optional[DirectionCompassEnum] = field(
        default=None,
        metadata={
            "name": "directionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    direction_compass_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "directionCompassValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
