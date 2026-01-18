from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.access_type import AccessType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Access:
    class Meta:
        name = "access"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: AccessType = field(
        metadata={
            "required": True,
        }
    )
