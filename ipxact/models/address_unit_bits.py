from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddressUnitBits(UnsignedPositiveLongintExpression):
    """
    The number of data bits in an addressable unit.

    The default is byte addressable (8 bits).
    """

    class Meta:
        name = "addressUnitBits"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
