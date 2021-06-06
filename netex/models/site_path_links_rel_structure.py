from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_link_ref import PathLinkRef
from .site_path_link import SitePathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SitePathLinksRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathLinks_RelStructure"

    path_link_ref: List[PathLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_path_link: List[SitePathLink] = field(
        default_factory=list,
        metadata={
            "name": "SitePathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
