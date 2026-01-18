from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class QualifiedExpression(ComplexBaseExpression):
    """
    Represents an expression qualified by an accompanying type.

    It supports an expression value.
    """

    class Meta:
        name = "qualifiedExpression"
