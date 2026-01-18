from dataclasses import dataclass, field

from .dated_calls_rel_structure import DatedCallsRelStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .driver_ref import DriverRef
from .external_object_ref_structure import ExternalObjectRefStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .operating_day_ref import OperatingDayRef
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .special_service_ref import SpecialServiceRef
from .target_passing_times_rel_structure import TargetPassingTimesRelStructure
from .template_service_journey_ref import TemplateServiceJourneyRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_version_structure import VehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedVehicleJourneyVersionStructure(VehicleJourneyVersionStructure):
    class Meta:
        name = "DatedVehicleJourney_VersionStructure"

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
    operating_day_ref: OperatingDayRef | None = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    external_dated_vehicle_journey_ref: ExternalObjectRefStructure | None = (
        field(
            default=None,
            metadata={
                "name": "ExternalDatedVehicleJourneyRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    dated_journey_pattern_ref: JourneyPatternRefStructure | None = field(
        default=None,
        metadata={
            "name": "DatedJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_ref: DriverRef | None = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_passing_times: TargetPassingTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "datedPassingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_calls: DatedCallsRelStructure | None = field(
        default=None,
        metadata={
            "name": "datedCalls",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
