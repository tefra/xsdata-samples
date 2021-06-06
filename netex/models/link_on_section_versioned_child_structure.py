from dataclasses import dataclass, field
from typing import Optional
from .activation_link import ActivationLink
from .activation_link_ref import ActivationLinkRef
from .infrastructure_link_1 import InfrastructureLink1
from .infrastructure_link_2 import InfrastructureLink2
from .infrastructure_link_ref import InfrastructureLinkRef
from .line_link_ref import LineLinkRef
from .link import Link
from .link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from .link_ref import LinkRef
from .path_link import PathLink
from .path_link_ref import PathLinkRef
from .railway_element import RailwayElement
from .railway_link_ref import RailwayLinkRef
from .road_element import RoadElement
from .road_link_ref import RoadLinkRef
from .route_link import RouteLink
from .route_link_ref import RouteLinkRef
from .service_link import ServiceLink
from .service_link_ref import ServiceLinkRef
from .site_path_link import SitePathLink
from .timing_link import TimingLink
from .timing_link_ref import TimingLinkRef
from .wire_element import WireElement
from .wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkOnSectionVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "LinkOnSection_VersionedChildStructure"

    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_link_ref: Optional[LineLinkRef] = field(
        default=None,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref: Optional[PathLinkRef] = field(
        default=None,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link_ref: Optional[RouteLinkRef] = field(
        default=None,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_link_ref: Optional[WireLinkRef] = field(
        default=None,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref: Optional[RoadLinkRef] = field(
        default=None,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref: Optional[RailwayLinkRef] = field(
        default=None,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link_ref: Optional[InfrastructureLinkRef] = field(
        default=None,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link_ref: Optional[ActivationLinkRef] = field(
        default=None,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref: Optional[LinkRef] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link: Optional[ServiceLink] = field(
        default=None,
        metadata={
            "name": "ServiceLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_path_link: Optional[SitePathLink] = field(
        default=None,
        metadata={
            "name": "SitePathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link: Optional[PathLink] = field(
        default=None,
        metadata={
            "name": "PathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link: Optional[RouteLink] = field(
        default=None,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link: Optional[TimingLink] = field(
        default=None,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link: Optional[InfrastructureLink1] = field(
        default=None,
        metadata={
            "name": "InfrastructureLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_element: Optional[WireElement] = field(
        default=None,
        metadata={
            "name": "WireElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_element: Optional[RoadElement] = field(
        default=None,
        metadata={
            "name": "RoadElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_element: Optional[RailwayElement] = field(
        default=None,
        metadata={
            "name": "RailwayElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_infrastructure_link: Optional[InfrastructureLink2] = field(
        default=None,
        metadata={
            "name": "InfrastructureLink_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link: Optional[ActivationLink] = field(
        default=None,
        metadata={
            "name": "ActivationLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link: Optional[Link] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
