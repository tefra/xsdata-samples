from dataclasses import dataclass, field
from typing import List
from .dated_calls_rel_structure import DatedCallsRelStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .driver_ref import DriverRef
from .external_object_ref_structure import ExternalObjectRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .journey_ref import JourneyRef
from .operating_day_ref import OperatingDayRef
from .service_journey_ref import ServiceJourneyRef
from .special_service_ref import SpecialServiceRef
from .special_service_version_structure import SpecialServiceVersionStructure
from .target_passing_times_rel_structure import TargetPassingTimesRelStructure
from .template_service_journey_ref import TemplateServiceJourneyRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedSpecialServiceVersionStructure(SpecialServiceVersionStructure):
    class Meta:
        name = "DatedSpecialService_VersionStructure"

    choice_1: List[object] = field(
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
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExternalDatedVehicleJourneyRef",
                    "type": ExternalObjectRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedJourneyPatternRef",
                    "type": JourneyPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverRef",
                    "type": DriverRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "datedPassingTimes",
                    "type": TargetPassingTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "datedCalls",
                    "type": DatedCallsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 1,
            "max_occurs": 37,
        }
    )
