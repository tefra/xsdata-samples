from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .data_object_service_permission_structure import (
    DataObjectServicePermissionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectPermissions:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: Iterable[DataObjectServicePermissionStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "DataObjectPermission",
                "type": "Element",
            },
        )
    )
