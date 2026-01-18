from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class IntegerMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in whole metres.

    :ivar integer_metre_distance: A value of distance expressed in
        metres in a non negative integer format.
    :ivar integer_metre_distance_value_extension:
    """

    integer_metre_distance: int | None = field(
        default=None,
        metadata={
            "name": "integerMetreDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    integer_metre_distance_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "integerMetreDistanceValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
