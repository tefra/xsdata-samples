from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.retail_device import RetailDevice
from netex.models.retail_device_ref import RetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDevicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "RetailDevices_RelStructure"

    retail_device_ref: List[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device: List[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
