from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class RegisterFileRef:
    class Meta:
        name = "registerFileRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: Optional[Indices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    register_file_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "registerFileRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
