from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BankRef:
    class Meta:
        name = "bankRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    bank_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankRef",
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
