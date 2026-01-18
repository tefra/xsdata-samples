from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BaseAddress(UnsignedLongintExpression):
    """
    Base of an address block, bank or address space.

    Expressed as the number of addressable units from the containing
    memoryMap or localMemoryMap.
    """

    class Meta:
        name = "baseAddress"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
