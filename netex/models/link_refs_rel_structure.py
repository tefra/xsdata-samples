from dataclasses import dataclass, field
from typing import List
from netex.models.activation_link_ref import ActivationLinkRef
from netex.models.activation_link_ref_by_value import ActivationLinkRefByValue
from netex.models.infrastructure_link_ref import InfrastructureLinkRef
from netex.models.line_link_ref import LineLinkRef
from netex.models.line_link_ref_by_value import LineLinkRefByValue
from netex.models.link_ref import LinkRef
from netex.models.link_ref_by_value import LinkRefByValue
from netex.models.modal_link_ref_by_value import ModalLinkRefByValue
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.path_link_ref import PathLinkRef
from netex.models.path_link_ref_by_value import PathLinkRefByValue
from netex.models.railway_link_ref import RailwayLinkRef
from netex.models.railway_link_ref_by_value import RailwayLinkRefByValue
from netex.models.road_link_ref import RoadLinkRef
from netex.models.road_link_ref_by_value import RoadLinkRefByValue
from netex.models.route_link_ref import RouteLinkRef
from netex.models.route_link_ref_by_value import RouteLinkRefByValue
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_link_ref_by_value import ServiceLinkRefByValue
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_link_ref_by_value import TimingLinkRefByValue
from netex.models.wire_link_ref import WireLinkRef
from netex.models.wire_link_ref_by_value import WireLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "linkRefs_RelStructure"

    service_link_ref: List[ServiceLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_link_ref: List[LineLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref: List[PathLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref: List[TimingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link_ref: List[RouteLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_link_ref: List[WireLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref: List[RoadLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref: List[RailwayLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_link_ref: List[InfrastructureLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link_ref: List[ActivationLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref: List[LinkRef] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref_by_value: List[ServiceLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_link_ref_by_value: List[LineLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "LineLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref_by_value: List[PathLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref_by_value: List[TimingLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "TimingLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link_ref_by_value: List[RouteLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "RouteLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_link_ref_by_value: List[WireLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "WireLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref_by_value: List[RoadLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "RoadLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref_by_value: List[RailwayLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "RailwayLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link_ref_by_value: List[ActivationLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modal_link_ref_by_value: List[ModalLinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "ModalLinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref_by_value: List[LinkRefByValue] = field(
        default_factory=list,
        metadata={
            "name": "LinkRefByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
