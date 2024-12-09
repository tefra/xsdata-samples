from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.delay_value_unit_type import DelayValueUnitType
from ipxact.models.real_expression import RealExpression
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SingleShotDriver:
    """
    Describes a driven one-shot port.

    :ivar single_shot_offset: Time in nanoseconds until start of one-
        shot.
    :ivar single_shot_value: Value of port after first  edge of one-
        shot.
    :ivar single_shot_duration: Duration in nanoseconds of the one shot.
    """

    class Meta:
        name = "singleShotDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    single_shot_offset: Optional["SingleShotDriver.SingleShotOffset"] = field(
        default=None,
        metadata={
            "name": "singleShotOffset",
            "type": "Element",
            "required": True,
        },
    )
    single_shot_value: Optional[UnsignedBitVectorExpression] = field(
        default=None,
        metadata={
            "name": "singleShotValue",
            "type": "Element",
            "required": True,
        },
    )
    single_shot_duration: Optional["SingleShotDriver.SingleShotDuration"] = (
        field(
            default=None,
            metadata={
                "name": "singleShotDuration",
                "type": "Element",
                "required": True,
            },
        )
    )

    @dataclass
    class SingleShotOffset(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class SingleShotDuration(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )
