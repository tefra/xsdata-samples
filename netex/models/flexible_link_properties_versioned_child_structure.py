from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.activation_link_ref import ActivationLinkRef
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.flexible_link_type_enumeration import FlexibleLinkTypeEnumeration
from netex.models.infrastructure_link_ref import InfrastructureLinkRef
from netex.models.line_link_ref import LineLinkRef
from netex.models.link_ref import LinkRef
from netex.models.path_link_ref import PathLinkRef
from netex.models.railway_link_ref import RailwayLinkRef
from netex.models.road_link_ref import RoadLinkRef
from netex.models.route_link_ref import RouteLinkRef
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLinkPropertiesVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FlexibleLinkProperties_VersionedChildStructure"

    service_link_ref: List[ServiceLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    line_link_ref: List[LineLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    path_link_ref: List[PathLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    timing_link_ref: List[TimingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    route_link_ref: List[RouteLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    wire_link_ref: List[WireLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    road_link_ref: List[RoadLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    railway_link_ref: List[RailwayLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    infrastructure_link_ref: List[InfrastructureLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    activation_link_ref: List[ActivationLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
    may_be_skipped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MayBeSkipped",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    on_main_route: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnMainRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    unscheduled_path: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnscheduledPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_link_type: Optional[FlexibleLinkTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleLinkType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
