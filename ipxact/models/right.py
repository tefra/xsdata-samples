from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Right(UnsignedIntExpression):
    """
    The optional element right specifies the right boundary.
    """

    class Meta:
        name = "right"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
