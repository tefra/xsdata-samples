from dataclasses import dataclass
from netex.models.data_source_ref_structure import DataSourceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataSourceRef(DataSourceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
