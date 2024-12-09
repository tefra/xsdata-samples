from dataclasses import dataclass

from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ReadResponse(UnsignedBitVectorExpression):
    class Meta:
        name = "readResponse"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
