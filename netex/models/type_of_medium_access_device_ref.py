from __future__ import annotations

from dataclasses import dataclass

from .type_of_medium_access_device_ref_structure import (
    TypeOfMediumAccessDeviceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMediumAccessDeviceRef(TypeOfMediumAccessDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
