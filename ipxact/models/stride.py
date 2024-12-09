from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Stride(UnsignedPositiveLongintExpression):
    class Meta:
        name = "stride"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
