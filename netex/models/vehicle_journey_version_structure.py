from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class VehicleJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "VehicleJourney_VersionStructure"

    departure_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: None | int = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: None | FrequencyStructure = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: None | DayTypeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_ref: None | RouteRef = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_ref: (
        None
        | ServiceJourneyPatternRef
        | ServicePatternRef
        | DeadRunJourneyPatternRef
        | JourneyPatternRef
    ) = field(
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
    time_demand_type_ref: None | TimeDemandTypeRefStructure = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_algorithm_type_ref: None | TimingAlgorithmTypeRef = field(
        default=None,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_frequency_group_ref: (
        None
        | RhythmicalJourneyGroupRef
        | HeadwayJourneyGroupRef
        | JourneyFrequencyGroupRef
    ) = field(
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
    vehicle_type_ref: None | CompoundTrainRef | TrainRef | VehicleTypeRef = (
        field(
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
    )
    operational_context_ref: None | OperationalContextRef = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_ref: None | TrainBlockRef | BlockRef = field(
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
    course_of_journeys_ref: None | CourseOfJourneysRef = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: None | TimeDemandTypeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: None | JourneyPartsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_component_label_assignments: (
        None | TrainComponentLabelAssignmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "trainComponentLabelAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_stop_assignments: (
        None | VehicleJourneyStopAssignmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: None | VehicleJourneyWaitTimesRelStructure = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: None | VehicleJourneyRunTimesRelStructure = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: None | VehicleJourneyLayoversRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_times: None | TimetabledPassingTimesRelStructure = field(
        default=None,
        metadata={
            "name": "passingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
