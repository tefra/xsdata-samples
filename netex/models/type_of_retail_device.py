from dataclasses import dataclass

from .type_of_retail_device_version_structure import (
    TypeOfRetailDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfRetailDevice(TypeOfRetailDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
