from dataclasses import dataclass
from netex.models.data_object_delivery_structure import DataObjectDeliveryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectDelivery(DataObjectDeliveryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
