from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from netex.models.data_object_request import DataObjectRequest
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectDeliveryStructure(AbstractServiceDeliveryStructure):
    data_object_request: Optional[DataObjectRequest] = field(
        default=None,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_objects: Optional[DataObjectsRelStructure] = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
