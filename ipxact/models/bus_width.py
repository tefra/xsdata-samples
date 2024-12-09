from dataclasses import dataclass

from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BusWidth(UnsignedIntExpression):
    """Defines the bus size in bits.

    This can be the result of an expression.
    """

    class Meta:
        name = "busWidth"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
