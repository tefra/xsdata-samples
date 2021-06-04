from dataclasses import dataclass
from netex.models.data_object_request_structure import DataObjectRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectRequest(DataObjectRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
