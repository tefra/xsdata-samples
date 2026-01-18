from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.delay_value_unit_type import DelayValueUnitType
from ipxact.models.real_expression import RealExpression
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
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

    single_shot_offset: SingleShotDriver.SingleShotOffset = field(
        metadata={
            "name": "singleShotOffset",
            "type": "Element",
            "required": True,
        }
    )
    single_shot_value: UnsignedBitVectorExpression = field(
        metadata={
            "name": "singleShotValue",
            "type": "Element",
            "required": True,
        }
    )
    single_shot_duration: SingleShotDriver.SingleShotDuration = field(
        metadata={
            "name": "singleShotDuration",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class SingleShotOffset(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class SingleShotDuration(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )
