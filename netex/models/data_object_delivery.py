from dataclasses import dataclass
from .data_object_delivery_structure import DataObjectDeliveryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectDelivery(DataObjectDeliveryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
