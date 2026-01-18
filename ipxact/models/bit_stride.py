from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BitStride(UnsignedPositiveLongintExpression):
    class Meta:
        name = "bitStride"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
