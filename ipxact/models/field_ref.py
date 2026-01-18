from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class FieldRef:
    class Meta:
        name = "fieldRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: None | Indices = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    field_ref: str = field(
        metadata={
            "name": "fieldRef",
            "type": "Attribute",
            "required": True,
        }
    )
