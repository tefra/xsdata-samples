from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .data_object_service_permission_structure import (
    DataObjectServicePermissionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectPermissions:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: Sequence[DataObjectServicePermissionStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "DataObjectPermission",
                "type": "Element",
            },
        )
    )
