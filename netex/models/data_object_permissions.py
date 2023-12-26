from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectPermissions:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: List[float] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectPermission",
            "type": "Element",
        },
    )
