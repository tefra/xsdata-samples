from dataclasses import dataclass

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class UnsignedBitExpression(ComplexBaseExpression):
    """
    Represents a single-bit/bool.

    It supports an expression value.
    """

    class Meta:
        name = "unsignedBitExpression"
