from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .data_source import DataSource
from .data_source_ref import DataSourceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataSourcesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dataSources_RelStructure"

    data_source_ref_or_data_source: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataSourceRef",
                    "type": DataSourceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSource",
                    "type": DataSource,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
