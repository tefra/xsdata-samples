from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .activation_link_ref import ActivationLinkRef
from .activation_link_ref_by_value import ActivationLinkRefByValue
from .line_link_ref import LineLinkRef
from .line_link_ref_by_value import LineLinkRefByValue
from .link_ref_by_value import LinkRefByValue
from .modal_link_ref_by_value import ModalLinkRefByValue
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from .path_link_ref import PathLinkRef
from .path_link_ref_by_value import PathLinkRefByValue
from .railway_link_ref import RailwayLinkRef
from .railway_link_ref_by_value import RailwayLinkRefByValue
from .road_link_ref import RoadLinkRef
from .road_link_ref_by_value import RoadLinkRefByValue
from .route_link_ref import RouteLinkRef
from .route_link_ref_by_value import RouteLinkRefByValue
from .service_link_ref import ServiceLinkRef
from .service_link_ref_by_value import ServiceLinkRefByValue
from .timing_link_ref import TimingLinkRef
from .timing_link_ref_by_value import TimingLinkRefByValue
from .vehicle_meeting_link_ref import VehicleMeetingLinkRef
from .wire_link_ref import WireLinkRef
from .wire_link_ref_by_value import WireLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "linkRefs_RelStructure"

    link_ref_or_infrastructure_link_ref_or_link_ref_by_value: Sequence[
        OnwardVehicleMeetingLinkRef
        | VehicleMeetingLinkRef
        | ServiceLinkRef
        | LineLinkRef
        | TimingLinkRef
        | WireLinkRef
        | RoadLinkRef
        | RailwayLinkRef
        | ActivationLinkRef
        | PathLinkRef
        | RouteLinkRef
        | ServiceLinkRefByValue
        | LineLinkRefByValue
        | TimingLinkRefByValue
        | WireLinkRefByValue
        | RoadLinkRefByValue
        | RailwayLinkRefByValue
        | ActivationLinkRefByValue
        | ModalLinkRefByValue
        | PathLinkRefByValue
        | RouteLinkRefByValue
        | LinkRefByValue
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnwardVehicleMeetingLinkRef",
                    "type": OnwardVehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingLinkRef",
                    "type": VehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRef",
                    "type": LineLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRef",
                    "type": ActivationLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLinkRefByValue",
                    "type": ServiceLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRefByValue",
                    "type": LineLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRefByValue",
                    "type": TimingLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRefByValue",
                    "type": WireLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRefByValue",
                    "type": RoadLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRefByValue",
                    "type": RailwayLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRefByValue",
                    "type": ActivationLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModalLinkRefByValue",
                    "type": ModalLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRefByValue",
                    "type": RouteLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkRefByValue",
                    "type": LinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
