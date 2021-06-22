from dataclasses import dataclass, field
from typing import List
from .alternative_texts_rel_structure import VersionedChildStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .fare_point_in_pattern_ref import FarePointInPatternRef
from .journey_ref import JourneyRef
from .point_in_journey_pattern_ref import PointInJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
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

    choice: List[object] = field(
        default_factory=list,
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
                    "name": "JourneyRef",
                    "type": JourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlightAndReboard",
                    "type": bool,
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
            "max_occurs": 26,
        }
    )
