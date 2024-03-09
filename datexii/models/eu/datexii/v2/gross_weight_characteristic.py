from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.comparison_operator_enum import (
    ComparisonOperatorEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GrossWeightCharacteristic:
    """
    Gross weight characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar gross_vehicle_weight: The gross weight of the vehicle and its
        load, including any trailers.
    :ivar gross_weight_characteristic_extension:
    """

    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
