from dataclasses import dataclass, field

from .abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from .data_object_request import DataObjectRequest
from .data_objects_rel_structure import DataObjectsRelStructure
from .extensions_2 import Extensions2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectDeliveryStructure(AbstractServiceDeliveryStructure):
    data_object_request: DataObjectRequest | None = field(
        default=None,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_objects: DataObjectsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Extensions2 | None = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
