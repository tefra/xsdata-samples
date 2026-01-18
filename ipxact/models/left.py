from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Left(UnsignedIntExpression):
    """
    The optional element left specifies the left boundary.
    """

    class Meta:
        name = "left"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
