from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .retail_device import RetailDevice
from .retail_device_ref import RetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDevicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "RetailDevices_RelStructure"

    retail_device_ref_or_retail_device: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
