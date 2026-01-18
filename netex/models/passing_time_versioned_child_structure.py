from __future__ import annotations

from dataclasses import dataclass, field

from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_point_in_pattern_ref import FarePointInPatternRef
from .point_in_journey_pattern_ref import PointInJourneyPatternRef
from .point_in_single_journey_path_ref import PointInSingleJourneyPathRef
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PassingTime_VersionedChildStructure"

    choice: (
        SingleJourneyRef
        | DatedVehicleJourneyRef
        | DatedSpecialServiceRef
        | SpecialServiceRef
        | TemplateServiceJourneyRef
        | ServiceJourneyRef
        | DeadRunRef
        | VehicleJourneyRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
            ),
        },
    )
    alight_and_reboard: bool | None = field(
        default=None,
        metadata={
            "name": "AlightAndReboard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_in_journey_pattern_ref: (
        PointInSingleJourneyPathRef
        | FarePointInPatternRef
        | StopPointInJourneyPatternRef
        | TimingPointInJourneyPatternRef
        | PointInJourneyPatternRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInSingleJourneyPathRef",
                    "type": PointInSingleJourneyPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPatternRef",
                    "type": StopPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
