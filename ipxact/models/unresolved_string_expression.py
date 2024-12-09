from dataclasses import dataclass

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class UnresolvedStringExpression(ComplexBaseExpression):
    """
    Represents a string which cannot be fully resolved.
    """

    class Meta:
        name = "unresolvedStringExpression"
