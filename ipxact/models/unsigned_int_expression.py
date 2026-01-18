from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class UnsignedIntExpression(ComplexBaseExpression):
    """
    An unsigned int which supports an expression value.

    :ivar minimum: For elements which can be specified using expression
        which are supposed to be resolved to an unsiged int value, this
        indicates the minimum value allowed.
    :ivar maximum: For elements which can be specified using expression
        which are supposed to be resolved to a unsigned int value, this
        indicates the maximum value allowed.
    """

    class Meta:
        name = "unsignedIntExpression"

    minimum: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
