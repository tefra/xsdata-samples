from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_link_ref import PathLinkRef
from .site_path_link import SitePathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SitePathLinksRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathLinks_RelStructure"

    path_link_ref_or_site_path_link: Iterable[
        Union[PathLinkRef, SitePathLink]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
