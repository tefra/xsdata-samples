from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.data_source import DataSource
from netex.models.data_source_ref import DataSourceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataSourcesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dataSources_RelStructure"

    data_source_ref: List[DataSourceRef] = field(
        default_factory=list,
        metadata={
            "name": "DataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
