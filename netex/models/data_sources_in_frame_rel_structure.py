from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .data_source import DataSource

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataSourcesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dataSourcesInFrame_RelStructure"

    data_source: Iterable[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
