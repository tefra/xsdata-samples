from dataclasses import dataclass, field
from typing import Optional, Union
from .alternative_texts_rel_structure import VersionedChildStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .journey_pattern_ref import JourneyPatternRef
from .link_sequence_ref import LinkSequenceRef
from .multilingual_string import MultilingualString
from .navigation_path_ref import NavigationPathRef
from .projections_rel_structure import ProjectionsRelStructure
from .route_ref import RouteRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_pattern_ref import ServicePatternRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_pattern_ref import TimingPatternRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointInLinkSequenceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PointInLinkSequence_VersionedChildStructure"

    choice: Optional[
        Union[
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            NavigationPathRef,
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            TimingPatternRef,
            RouteRef,
            LinkSequenceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPatternRef",
                    "type": TimingPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
