from dataclasses import dataclass, field
from typing import Optional
from netex.models.activation_link_ref import ActivationLinkRef
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.infrastructure_link_ref import InfrastructureLinkRef
from netex.models.line_link_ref import LineLinkRef
from netex.models.link_ref import LinkRef
from netex.models.multilingual_string import MultilingualString
from netex.models.path_link_ref import PathLinkRef
from netex.models.railway_link_ref import RailwayLinkRef
from netex.models.road_link_ref import RoadLinkRef
from netex.models.route_link_ref import RouteLinkRef
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.wire_link_ref import WireLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineShapeStructure2(DataManagedObjectStructure):
    class Meta:
        name = "LineShapeStructure"

    formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formula",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
