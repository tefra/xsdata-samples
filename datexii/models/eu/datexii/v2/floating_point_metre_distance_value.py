from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class FloatingPointMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in metres in a floating point
    format.

    :ivar floating_point_metre_distance: A value of distance expressed
        in metres in a floating point format.
    :ivar floating_point_metre_distance_value_extension:
    """

    floating_point_metre_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "floatingPointMetreDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    floating_point_metre_distance_value_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "floatingPointMetreDistanceValueExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
