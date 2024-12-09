from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.indices import Indices

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldRef:
    class Meta:
        name = "fieldRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indices: Optional[Indices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    field_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldRef",
            "type": "Attribute",
            "required": True,
        },
    )
