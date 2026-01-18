from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class RegisterFileRef:
    class Meta:
        name = "registerFileRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: Indices | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    register_file_ref: str | None = field(
        default=None,
        metadata={
            "name": "registerFileRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
