from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.comparison_operator_enum import (
    ComparisonOperatorEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LengthCharacteristic:
    """
    Length characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_length: The overall distance between the front and
        back of an individual vehicle, including the length of any
        trailers, couplings, etc.
    :ivar length_characteristic_extension:
    """

    comparison_operator: ComparisonOperatorEnum | None = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vehicle_length: float | None = field(
        default=None,
        metadata={
            "name": "vehicleLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    length_characteristic_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "lengthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
