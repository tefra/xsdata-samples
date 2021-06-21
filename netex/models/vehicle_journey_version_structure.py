from dataclasses import dataclass, field
from typing import List, Optional
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
from .timetabled_passing_times_rel_structure import TimetabledPassingTimesRelStructure
from .timing_algorithm_type_ref import TimingAlgorithmTypeRef
from .train_block_ref import TrainBlockRef
from .train_component_label_assignments_rel_structure import TrainComponentLabelAssignmentsRelStructure
from .train_ref import TrainRef
from .vehicle_journey_layovers_rel_structure import VehicleJourneyLayoversRelStructure
from .vehicle_journey_run_times_rel_structure import VehicleJourneyRunTimesRelStructure
from .vehicle_journey_stop_assignments_rel_structure import VehicleJourneyStopAssignmentsRelStructure
from .vehicle_journey_wait_times_rel_structure import VehicleJourneyWaitTimesRelStructure
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "VehicleJourney_VersionStructure"

    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmTypeRef",
                    "type": TimingAlgorithmTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "OperationalContextRef",
                    "type": OperationalContextRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "CourseOfJourneysRef",
                    "type": CourseOfJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PublicCode",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeDemandTypes",
                    "type": TimeDemandTypeRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parts",
                    "type": JourneyPartsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "trainComponentLabelAssignments",
                    "type": TrainComponentLabelAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vehicleJourneyStopAssignments",
                    "type": VehicleJourneyStopAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": VehicleJourneyWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "runTimes",
                    "type": VehicleJourneyRunTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "layovers",
                    "type": VehicleJourneyLayoversRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "passingTimes",
                    "type": TimetabledPassingTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 32,
        }
    )
