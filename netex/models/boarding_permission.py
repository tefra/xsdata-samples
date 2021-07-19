from dataclasses import dataclass, field
from typing import Optional
from .boarding_permission_enumeration import BoardingPermissionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BoardingPermission:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[BoardingPermissionEnumeration] = field(
        default=None
    )
