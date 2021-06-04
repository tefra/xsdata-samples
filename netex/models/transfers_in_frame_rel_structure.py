from dataclasses import dataclass, field
from typing import List
from netex.models.access import Access
from netex.models.connection import Connection
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.default_connection import DefaultConnection
from netex.models.site_connection import SiteConnection
from netex.models.transfer import Transfer

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransfersInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transfersInFrame_RelStructure"

    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    default_connection: List[DefaultConnection] = field(
        default_factory=list,
        metadata={
            "name": "DefaultConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_connection: List[SiteConnection] = field(
        default_factory=list,
        metadata={
            "name": "SiteConnection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transfer: List[Transfer] = field(
        default_factory=list,
        metadata={
            "name": "Transfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
