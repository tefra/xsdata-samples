from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .block_ref import BlockRef
from .compound_train_ref import CompoundTrainRef
from .course_of_journeys_ref import CourseOfJourneysRef
from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .frequency_structure import FrequencyStructure
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .journey_frequency_group_ref import JourneyFrequencyGroupRef
from .journey_parts_rel_structure import JourneyPartsRelStructure
from .journey_pattern_ref import JourneyPatternRef
from .journey_version_structure import JourneyVersionStructure
from .operational_context_ref import OperationalContextRef
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from .route_ref import RouteRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .time_demand_type_ref_structure import TimeDemandTypeRefStructure
from .time_demand_type_refs_rel_structure import TimeDemandTypeRefsRelStructure
from .timetabled_passing_times_rel_structure import (
    TimetabledPassingTimesRelStructure,
)
from .timing_algorithm_type_ref import TimingAlgorithmTypeRef
from .train_block_ref import TrainBlockRef
from .train_component_label_assignments_rel_structure import (
    TrainComponentLabelAssignmentsRelStructure,
)
from .train_ref import TrainRef
from .vehicle_journey_layovers_rel_structure import (
    VehicleJourneyLayoversRelStructure,
)
from .vehicle_journey_run_times_rel_structure import (
    VehicleJourneyRunTimesRelStructure,
)
from .vehicle_journey_stop_assignments_rel_structure import (
    VehicleJourneyStopAssignmentsRelStructure,
)
from .vehicle_journey_wait_times_rel_structure import (
    VehicleJourneyWaitTimesRelStructure,
)
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "VehicleJourney_VersionStructure"

    departure_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: FrequencyStructure | None = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: DayTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_ref: RouteRef | None = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_ref: ServiceJourneyPatternRef | ServicePatternRef | DeadRunJourneyPatternRef | JourneyPatternRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    time_demand_type_ref: TimeDemandTypeRefStructure | None = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_algorithm_type_ref: TimingAlgorithmTypeRef | None = field(
        default=None,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_frequency_group_ref: RhythmicalJourneyGroupRef | HeadwayJourneyGroupRef | JourneyFrequencyGroupRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RhythmicalJourneyGroupRef",
                    "type": RhythmicalJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroupRef",
                    "type": HeadwayJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyFrequencyGroupRef",
                    "type": JourneyFrequencyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_type_ref: CompoundTrainRef | TrainRef | VehicleTypeRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    operational_context_ref: OperationalContextRef | None = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_ref: TrainBlockRef | BlockRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    course_of_journeys_ref: CourseOfJourneysRef | None = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: TimeDemandTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: JourneyPartsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_component_label_assignments: TrainComponentLabelAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "trainComponentLabelAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_stop_assignments: VehicleJourneyStopAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: VehicleJourneyWaitTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: VehicleJourneyRunTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: VehicleJourneyLayoversRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_times: TimetabledPassingTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "passingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
