from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.comparison_operator_enum import ComparisonOperatorEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class HeightCharacteristic:
    """
    Height characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_height: The height of the highest part, excluding
        antennae, of an individual vehicle above the road surface, in
        metres.
    :ivar height_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vehicle_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    height_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
