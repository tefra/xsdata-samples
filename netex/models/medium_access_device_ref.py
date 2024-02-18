from dataclasses import dataclass
from .medium_access_device_ref_structure import MediumAccessDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDeviceRef(MediumAccessDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
