from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.comparison_operator_enum import (
    ComparisonOperatorEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NumberOfAxlesCharacteristic:
    """
    Number of axles characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar number_of_axles: The total number of axles of an individual
        vehicle.
    :ivar number_of_axles_characteristic_extension:
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
    number_of_axles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfAxles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    number_of_axles_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "numberOfAxlesCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
