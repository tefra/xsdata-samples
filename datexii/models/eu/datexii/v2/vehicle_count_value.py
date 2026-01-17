from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCountValue(DataValue):
    """
    A measured or calculated value of absolute count of vehicles within a
    specified period of time expressed as non negative integer.

    :ivar vehicle_count: A measured or calculated absolute count of
        vehicles within a specified period of time expressed as non
        negative integer.
    :ivar vehicle_count_value_extension:
    """

    vehicle_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleCount",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vehicle_count_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCountValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
