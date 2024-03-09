from dataclasses import dataclass

from .medium_access_device_version_structure import (
    MediumAccessDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobileDeviceVersionStructure(MediumAccessDeviceVersionStructure):
    class Meta:
        name = "MobileDevice_VersionStructure"
