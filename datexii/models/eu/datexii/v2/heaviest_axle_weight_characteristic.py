from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.comparison_operator_enum import (
    ComparisonOperatorEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class HeaviestAxleWeightCharacteristic:
    """
    Weight characteristic of the heaviest axle on the vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar heaviest_axle_weight: The weight of the heaviest axle on the
        vehicle.
    :ivar heaviest_axle_weight_characteristic_extension:
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
    heaviest_axle_weight: None | float = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    heaviest_axle_weight_characteristic_extension: None | ExtensionType = (
        field(
            default=None,
            metadata={
                "name": "heaviestAxleWeightCharacteristicExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
