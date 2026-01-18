from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddressBlockRef:
    class Meta:
        name = "addressBlockRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: Indices | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address_block_ref: str | None = field(
        default=None,
        metadata={
            "name": "addressBlockRef",
            "type": "Attribute",
            "required": True,
        },
    )
