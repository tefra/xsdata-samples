from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.kind_type import KindType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Kind:
    """Defines the protocol type.

    Defaults to tlm_base_protocol_type for TLM sockets
    """

    class Meta:
        name = "kind"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[KindType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    custom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
