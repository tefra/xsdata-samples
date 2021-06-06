from dataclasses import dataclass
from .retail_device_ref_structure import RetailDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDeviceRef(RetailDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
