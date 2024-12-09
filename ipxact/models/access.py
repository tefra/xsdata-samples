from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_type import AccessType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Access:
    class Meta:
        name = "access"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[AccessType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
