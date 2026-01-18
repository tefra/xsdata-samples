from __future__ import annotations

from dataclasses import dataclass

from .medium_access_device_version_structure import (
    MediumAccessDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmvCardVersionStructure(MediumAccessDeviceVersionStructure):
    class Meta:
        name = "EmvCard_VersionStructure"
