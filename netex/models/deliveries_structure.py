from dataclasses import dataclass, field
from typing import List

from .data_object_delivery import DataObjectDelivery

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeliveriesStructure:
    data_object_delivery: List[DataObjectDelivery] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectDelivery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
