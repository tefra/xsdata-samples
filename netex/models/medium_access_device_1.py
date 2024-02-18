from dataclasses import dataclass
from .medium_access_device_version_structure import (
    MediumAccessDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDevice1(MediumAccessDeviceVersionStructure):
    class Meta:
        name = "MediumAccessDevice"
        namespace = "http://www.netex.org.uk/netex"
