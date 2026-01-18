from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OccupancyChangeValue(DataValue):
    """
    A measured or calculated value of change of occupied parking spaces
    expressed as integer.

    :ivar occupancy_change: A measured or calculated absolut change of
        occupied parking spaces within a specified time expressed as
        integer.
    :ivar occupancy_change_value_extension:
    """

    occupancy_change: int | None = field(
        default=None,
        metadata={
            "name": "occupancyChange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    occupancy_change_value_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "occupancyChangeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
