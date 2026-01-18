from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AlternateRegisterRef:
    class Meta:
        name = "alternateRegisterRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    alternate_register_ref: str | None = field(
        default=None,
        metadata={
            "name": "alternateRegisterRef",
            "type": "Attribute",
            "required": True,
        },
    )
