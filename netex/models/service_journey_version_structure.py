from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDuration, XmlTime
from .block_ref import BlockRef
from .calls_rel_structure import CallsRelStructure
from .check_constraints_rel_structure import CheckConstraintsRelStructure
from .compound_train_ref import CompoundTrainRef
from .course_of_journeys_ref import CourseOfJourneysRef
from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .flexible_line_ref import FlexibleLineRef
from .flexible_line_view import FlexibleLineView
from .flexible_service_properties import FlexibleServiceProperties
from .flexible_service_properties_ref import FlexibleServicePropertiesRef
from .frequency_structure import FrequencyStructure
from .group_of_services_refs_rel_structure import (
    GroupOfServicesRefsRelStructure,
)
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .journey_endpoint_structure import JourneyEndpointStructure
from .journey_frequency_group_ref import JourneyFrequencyGroupRef
from .journey_parts_rel_structure import JourneyPartsRelStructure
from .journey_pattern_ref import JourneyPatternRef
from .journey_pattern_view import JourneyPatternView
from .journey_version_structure import JourneyVersionStructure
from .line_ref import LineRef
from .line_view import LineView
from .operational_context_ref import OperationalContextRef
from .operator_ref import OperatorRef
from .operator_view import OperatorView
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from .passenger_carrying_requirements_view import (
    PassengerCarryingRequirementsView,
)
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from .route_ref import RouteRef
from .service_alteration_enumeration import ServiceAlterationEnumeration
from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .time_demand_type_ref_structure import TimeDemandTypeRefStructure
from .time_demand_type_refs_rel_structure import TimeDemandTypeRefsRelStructure
from .timetabled_passing_times_rel_structure import (
    TimetabledPassingTimesRelStructure,
)
from .timing_algorithm_type_ref import TimingAlgorithmTypeRef
from .train_block_ref import TrainBlockRef
from .train_number_refs_rel_structure import TrainNumberRefsRelStructure
from .train_ref import TrainRef
from .train_size import TrainSize
from .vehicle_equipments_rel_structure import VehicleEquipmentsRelStructure
from .vehicle_journey_layovers_rel_structure import (
    VehicleJourneyLayoversRelStructure,
)
from .vehicle_journey_run_times_rel_structure import (
    VehicleJourneyRunTimesRelStructure,
)
from .vehicle_journey_wait_times_rel_structure import (
    VehicleJourneyWaitTimesRelStructure,
)
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "ServiceJourney_VersionStructure"

    service_alteration: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlteration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
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
    time_demand_type_ref: Optional[TimeDemandTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_algorithm_type_ref: Optional[TimingAlgorithmTypeRef] = field(
        default=None,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rhythmical_journey_group_ref_or_headway_journey_group_ref_or_journey_frequency_group_ref: Optional[
        Union[
            RhythmicalJourneyGroupRef,
            HeadwayJourneyGroupRef,
            JourneyFrequencyGroupRef,
        ]
    ] = field(
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
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
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
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_block_ref_or_block_ref: Optional[
        Union[TrainBlockRef, BlockRef]
    ] = field(
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
    course_of_journeys_ref: Optional[CourseOfJourneysRef] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref_or_operator_view: Optional[
        Union[OperatorRef, OperatorView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorView",
                    "type": OperatorView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[FlexibleLineRef, LineRef, LineView, FlexibleLineView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineView",
                    "type": LineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLineView",
                    "type": FlexibleLineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_view: Optional[JourneyPatternView] = field(
        default=None,
        metadata={
            "name": "JourneyPatternView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_services: Optional[GroupOfServicesRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: Optional[TimeDemandTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_numbers: Optional[TrainNumberRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: Optional[VehicleJourneyWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: Optional[VehicleJourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: Optional[VehicleJourneyLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_times: Optional[TimetabledPassingTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "passingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: Optional[JourneyPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    calls: Optional[CallsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: Optional[CheckConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view: Optional[
        Union[
            PassengerCarryingRequirementRef, PassengerCarryingRequirementsView
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: Optional[VehicleEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_service_properties_ref_or_flexible_service_properties: Optional[
        Union[FlexibleServicePropertiesRef, FlexibleServiceProperties]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
