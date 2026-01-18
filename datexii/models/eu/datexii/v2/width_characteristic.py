from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.comparison_operator_enum import (
    ComparisonOperatorEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class WidthCharacteristic:
    """
    Width characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_width: The maximum width of an individual vehicle, in
        metres.
    :ivar width_characteristic_extension:
    """

    comparison_operator: None | ComparisonOperatorEnum = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vehicle_width: None | float = field(
        default=None,
        metadata={
            "name": "vehicleWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    width_characteristic_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "widthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
