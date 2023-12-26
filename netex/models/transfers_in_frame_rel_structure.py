from dataclasses import dataclass, field
from typing import List, Union
from .access import Access
from .connection import Connection
from .containment_aggregation_structure import ContainmentAggregationStructure
from .default_connection import DefaultConnection
from .site_connection import SiteConnection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransfersInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transfersInFrame_RelStructure"

    choice: List[
        Union[Connection, DefaultConnection, SiteConnection, Access]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
