from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class UnsignedPositiveLongintExpression(ComplexBaseExpression):
    """
    A positive unsigned longint which supports an expression value.

    :ivar minimum: For elements which can be specified using expression
        which are supposed to be resolved to a positive unsigned longint
        value, this indicates the minimum value allowed.
    :ivar maximum: For elements which can be specified using expression
        which are supposed to be resolved to a positive unsigned longint
        value, this indicates the maximum value allowed.
    """

    class Meta:
        name = "unsignedPositiveLongintExpression"

    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
