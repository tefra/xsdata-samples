from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AlternateRegisterRef:
    class Meta:
        name = "alternateRegisterRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    alternate_register_ref: str = field(
        metadata={
            "name": "alternateRegisterRef",
            "type": "Attribute",
            "required": True,
        }
    )
