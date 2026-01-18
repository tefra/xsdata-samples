from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DirectionBearingValue(DataValue):
    """
    A measured or calculated value of direction as a bearing.

    :ivar direction_bearing: A value of direction expressed in terms of
        a bearing measured in whole degrees. Unless otherwise specified
        the reference direction corresponding to 0 degrees is North.
    :ivar direction_bearing_value_extension:
    """

    direction_bearing: int | None = field(
        default=None,
        metadata={
            "name": "directionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    direction_bearing_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "directionBearingValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
