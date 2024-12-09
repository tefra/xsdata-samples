from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddressBlockRef:
    class Meta:
        name = "addressBlockRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: Optional[Indices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address_block_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressBlockRef",
            "type": "Attribute",
            "required": True,
        },
    )
