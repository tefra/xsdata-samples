from netex.models.accommodation import Accommodation
from netex.models.accommodation_access_enumeration import AccommodationAccessEnumeration
from netex.models.accommodation_access_list import AccommodationAccessList
from netex.models.accommodation_facility import AccommodationFacility
from netex.models.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from netex.models.accommodation_facility_list import AccommodationFacilityList
from netex.models.accommodations_rel_structure import AccommodationsRelStructure
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType1
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.models.assistance_facility_list import AssistanceFacilityList
from netex.models.berth_facility import BerthFacility
from netex.models.berth_facility_enumeration import BerthFacilityEnumeration
from netex.models.block_parts_rel_structure import BlockPartsRelStructure
from netex.models.block_ref import BlockRef
from netex.models.blocks_in_frame_rel_structure import BlocksInFrameRelStructure
from netex.models.boarding_permission import BoardingPermission
from netex.models.boarding_permission_enumeration import BoardingPermissionEnumeration
from netex.models.call_1 import Call1
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.catering_facility_enumeration import CateringFacilityEnumeration
from netex.models.catering_facility_list import CateringFacilityList
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compound_block import CompoundBlock
from netex.models.compound_train import CompoundTrain
from netex.models.compound_train_ref import CompoundTrainRef
from netex.models.connecting_journey_view import ConnectingJourneyView
from netex.models.connection import Connection
from netex.models.connection_ref_structure import ConnectionRefStructure
from netex.models.couchette_facility import CouchetteFacility
from netex.models.couchette_facility_enumeration import CouchetteFacilityEnumeration
from netex.models.couchette_facility_list import CouchetteFacilityList
from netex.models.coupled_journey import CoupledJourney
from netex.models.coupled_journeys_in_frame_rel_structure import CoupledJourneysInFrameRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_class import FareClass
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.fare_classes import FareClasses
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_meeting import JourneyMeeting
from netex.models.journey_meeting_ref import JourneyMeetingRef
from netex.models.journey_meeting_view import JourneyMeetingView
from netex.models.journey_meeting_views_rel_structure import JourneyMeetingViewsRelStructure
from netex.models.journey_meetings_in_frame_rel_structure import JourneyMeetingsInFrameRelStructure
from netex.models.journey_part import JourneyPart
from netex.models.journey_part_couple import JourneyPartCouple
from netex.models.journey_part_couple_ref import JourneyPartCoupleRef
from netex.models.journey_part_couples_in_frame_rel_structure import JourneyPartCouplesInFrameRelStructure
from netex.models.journey_part_ref import JourneyPartRef
from netex.models.journey_part_ref_structure import JourneyPartRefStructure
from netex.models.journey_part_refs_rel_structure import JourneyPartRefsRelStructure
from netex.models.journey_parts_rel_structure import JourneyPartsRelStructure
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line_1 import Line1
from netex.models.line_derived_view_structure import LineDerivedViewStructure
from netex.models.line_view import LineView
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.luggage_carriage_enumeration import LuggageCarriageEnumeration
from netex.models.luggage_carriage_facility_list import LuggageCarriageFacilityList
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration
from netex.models.mobility_facility_list import MobilityFacilityList
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.nuisance_facility_list import NuisanceFacilityList
from netex.models.onboard_stay import OnboardStay
from netex.models.onboard_stays_rel_structure import OnboardStaysRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from netex.models.passenger_comms_facility_list import PassengerCommsFacilityList
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.passenger_information_facility_list import PassengerInformationFacilityList
from netex.models.point_ref_structure import PointRefStructure
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from netex.models.quay_1 import Quay1
from netex.models.quay_assignment_view import QuayAssignmentView
from netex.models.quay_ref_structure import QuayRefStructure
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.reason_for_meeting_enumeration import ReasonForMeetingEnumeration
from netex.models.route_1 import Route1
from netex.models.route_ref import RouteRef
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.models.sanitary_facility_list import SanitaryFacilityList
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_facility_set import ServiceFacilitySet
from netex.models.service_facility_set_ref import ServiceFacilitySetRef
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey_1 import ServiceJourney1
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.service_journey_ref_structure import ServiceJourneyRefStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_place_1 import StopPlace1
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.train import Train
from netex.models.train_block import TrainBlock
from netex.models.train_block_part import TrainBlockPart
from netex.models.train_block_part_ref import TrainBlockPartRef
from netex.models.train_block_ref import TrainBlockRef
from netex.models.train_component import TrainComponent
from netex.models.train_components_rel_structure import TrainComponentsRelStructure
from netex.models.train_element import TrainElement
from netex.models.train_element_type_enumeration import TrainElementTypeEnumeration
from netex.models.train_in_compound_train_versioned_child_structure import TrainInCompoundTrainVersionedChildStructure
from netex.models.train_number import TrainNumber
from netex.models.train_number_ref import TrainNumberRef
from netex.models.train_numbers_in_frame_rel_structure import TrainNumbersInFrameRelStructure
from netex.models.train_ref import TrainRef
from netex.models.train_size import TrainSize
from netex.models.train_size_enumeration import TrainSizeEnumeration
from netex.models.trains_in_compound_train_rel_structure import TrainsInCompoundTrainRelStructure
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.vehicle_journey_ref import VehicleJourneyRef
from netex.models.vehicle_journey_ref_structure import VehicleJourneyRefStructure
from netex.models.vehicle_journey_refs_rel_structure import VehicleJourneyRefsRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.vehicle_schedule_frame import VehicleScheduleFrame
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='bbd:TIM_23_O',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            ref='bbd:TIM_23_O'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple timetable frame with two journeys and service calendar'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='bbd:TIM_23_O',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            AvailabilityCondition(
                                id='bbd:Cnd001',
                                version='any',
                                description=MultilingualString(
                                    value='Sept  to March'
                                ),
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0),
                                to_date=XmlDateTime(2011, 3, 31, 0, 0, 0, 0, 0),
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayTypeRef(
                                            version='any',
                                            ref='bbd:DT_01-MF-NH'
                                        ),
                                        DayTypeRef(
                                            version='any',
                                            ref='bbd:DT_03-WE-NH'
                                        ),
                                    ]
                                )
                            ),
                        ]
                    ),
                ],
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='ops',
                            xmlns='ops',
                            xmlns_url='http://www.erail.eu/ops',
                            description='Operations buses'
                        ),
                        Codespace(
                            id='bbd',
                            xmlns='bbd',
                            xmlns_url='http://www.borninabahn.de/',
                            description='Train  data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='bbd'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        TimetableFrame(
                            id='bbd:TIM_23_O',
                            version='any',
                            name=MultilingualString(
                                value='Winter timetable for route 23 Outbound'
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.RAIL,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney1(
                                        id='bbd:sj_447',
                                        version='any',
                                        description=MultilingualString(
                                            value='447 Amsterdam to Warsaw'
                                        ),
                                        departure_time=XmlTime(9, 0, 0, 0, 0),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            version='any',
                                            ref='bbd:JP_447_amsterdam_warsaw'
                                        ),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_447'
                                        ),
                                        block_ref=BlockRef(
                                            version='any',
                                            ref='ops:blk_447_amsterdam-warsaw'
                                        ),
                                        choice=LineView(
                                            public_code='447',
                                            name=MultilingualString(
                                                value='Amsterdam to Warsaw Express'
                                            ),
                                            transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='myrail:RT_447'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='bbd:DST_warsaw'
                                            )
                                        ),
                                        parts=JourneyPartsRelStructure(
                                            journey_part_ref_or_journey_part=[
                                                JourneyPart(
                                                    id='bbd:jpt_447_01',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Amsterdam to Hannover'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_447'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_01'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_01_amsterdam-hannover'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_01_amsterdam-hannover'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    start_time=XmlTime(9, 0, 0, 0, 0),
                                                    end_time=XmlTime(12, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    ),
                                                    order=1
                                                ),
                                                JourneyPart(
                                                    id='bbd:jpt_447_02',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Hannover to Berlin'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_447'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_02'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_02_hannover-berlin'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_02_hannover-berlin'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    start_time=XmlTime(12, 0, 0, 0, 0),
                                                    end_time=XmlTime(15, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    ),
                                                    order=2
                                                ),
                                                JourneyPart(
                                                    id='bbd:jpt_447_03',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Berlin to Warsaw'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_447'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_03'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_03_berlin-warsaw'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:pl_warsaw'
                                                    ),
                                                    start_time=XmlTime(15, 10, 0, 0, 0),
                                                    end_time=XmlTime(19, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='bbd:sj_447_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(9, 0, 0, 0, 0),
                                                        for_boarding=True,
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_457_joinTo_447_dep_amsterdam'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Join with 457  '
                                                                    ),
                                                                    earliest_time=XmlTime(9, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING
                                                                ),
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_40447_joinTo_477_dep_amsterdam'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Join with 40447'
                                                                    ),
                                                                    earliest_time=XmlTime(9, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='uic:nl_amsterdam'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:nl_amsterdam_1'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 1'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_hannover'
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='bbd:sj_447_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_40447_splitFrom_447_arr_hannover'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection to Copenhagen '
                                                                    ),
                                                                    earliest_time=XmlTime(15, 30, 0, 0, 0),
                                                                    latest_time=XmlTime(15, 40, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT5M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_hannover_01'
                                                                    ),
                                                                    connecting_stop_point_ref=[
                                                                        ScheduledStopPointRefStructure(
                                                                            version='any',
                                                                            ref='uic:de_hannover'
                                                                        ),
                                                                    ],
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_40447'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(12, 15, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_40447_amsterdam-copenhagen'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='40447'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(12, 5, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT5M"),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_hannover_5'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 5'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_warsaw'
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='bbd:sj_447_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_457_splitFrom_447_arr_berlin'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection at Berlin to Prague '
                                                                    ),
                                                                    earliest_time=XmlTime(14, 40, 0, 0, 0),
                                                                    latest_time=XmlTime(14, 50, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_berlin_01'
                                                                    ),
                                                                    connecting_stop_point_ref=[
                                                                        ScheduledStopPointRefStructure(
                                                                            version='any',
                                                                            ref='uic:de_berlin'
                                                                        ),
                                                                    ],
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_457'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(14, 50, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_457_amsterdam-prague'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='457'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 10, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT10M"),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_berlin_3'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 3'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_warsaw'
                                                    ),
                                                    order=3
                                                ),
                                                Call1(
                                                    id='bbd:sj_447_004',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:pl_warsaw'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(19, 10, 0, 0, 0),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:pl_warsaw_8'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 8'
                                                            )
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=4
                                                ),
                                            ]
                                        ),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_first'
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney1(
                                        id='bbd:sj_40447',
                                        version='any',
                                        description=MultilingualString(
                                            value='40447 Amsterdam to Copenhagen'
                                        ),
                                        departure_time=XmlTime(9, 0, 0, 0, 0),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            version='any',
                                            ref='bbd:JP_40447_amsterdam-copenhagen'
                                        ),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_40447'
                                        ),
                                        block_ref=BlockRef(
                                            version='any',
                                            ref='ops:blk_40447_amsterdam-copenhagen'
                                        ),
                                        choice=LineView(
                                            public_code='40447',
                                            transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='myrail:RT_40447'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='bbd:DST_copenhagen'
                                            )
                                        ),
                                        parts=JourneyPartsRelStructure(
                                            journey_part_ref_or_journey_part=[
                                                JourneyPart(
                                                    id='bbd:jpt_40447_01',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Amsterdam to Hannover'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_40447'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_01'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_01_amsterdam-hannover'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_01_amsterdam-hannover'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    start_time=XmlTime(9, 0, 0, 0, 0),
                                                    end_time=XmlTime(12, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    )
                                                ),
                                                JourneyPart(
                                                    id='bbd:jpt_40447_02',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Hannover to Copenhagen'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_40447'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_40447_01'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_40447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_40447_02_hannover-copenhagen'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:dk_copenhagen'
                                                    ),
                                                    start_time=XmlTime(12, 10, 0, 0, 0),
                                                    end_time=XmlTime(16, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='standalone',
                                                        ref='bbd:standalone'
                                                    )
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='bbd:sj_40447_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(9, 0, 0, 0, 0),
                                                        for_boarding=True,
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_40447_joinTo_477_dep_amsterdam'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Start at Amsterdam (train couples)'
                                                                    ),
                                                                    earliest_time=XmlTime(9, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='uic:nl_amsterdam'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:nl_amsterdam_1'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 1'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_hannover'
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='bbd:sj_40447_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_40447_splitFrom_447_arr_hannover'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Split connection at Hannover to Copenhagen '
                                                                    ),
                                                                    earliest_time=XmlTime(15, 20, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT5M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_hannover_02'
                                                                    ),
                                                                    connecting_stop_point_ref=[
                                                                        ScheduledStopPointRefStructure(
                                                                            version='any',
                                                                            ref='uic:de_hannover'
                                                                        ),
                                                                    ],
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_40447'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(12, 15, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_40447_amsterdam-copenhagen'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='40447'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(12, 4, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT5M"),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_hannover_5'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 5'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_copenhagen'
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='bbd:sj_40447_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:dk_copenhagen'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(16, 0, 0, 0, 0),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:dk_copenhagen_1'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 1'
                                                            )
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_first'
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney1(
                                        id='bbd:sj_457',
                                        version='any',
                                        description=MultilingualString(
                                            value='457 Amsterdam to Prague'
                                        ),
                                        departure_time=XmlTime(9, 0, 0, 0, 0),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            version='any',
                                            ref='bbd:JP_457_amsterdam-prague'
                                        ),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_457'
                                        ),
                                        block_ref=BlockRef(
                                            version='any',
                                            ref='ops:blk_40447_amsterdam-copenhagen'
                                        ),
                                        choice=LineView(
                                            public_code='457',
                                            transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='myrail:RT_457'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='bbd:DST_prague'
                                            )
                                        ),
                                        parts=JourneyPartsRelStructure(
                                            journey_part_ref_or_journey_part=[
                                                JourneyPart(
                                                    id='bbd:jpt_457_01',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Amsterdam to Hannover'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_457'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_01'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_01_amsterdam-hannover'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_01_amsterdam-hannover'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    start_time=XmlTime(9, 0, 0, 0, 0),
                                                    end_time=XmlTime(12, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    )
                                                ),
                                                JourneyPart(
                                                    id='bbd:jpt_457_02',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Hannover to Berlin'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_457'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_447_02'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_02_hannover-berlin'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_447'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_447_02_hannover-berlin'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    start_time=XmlTime(12, 0, 0, 0, 0),
                                                    end_time=XmlTime(15, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='coupling',
                                                        ref='bbd:coupling'
                                                    )
                                                ),
                                                JourneyPart(
                                                    id='bbd:jpt_457_03',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Berlin to Prague'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_457'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_457_03'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_03_berlin-prague'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_457'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_457_03_berlin-prague'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    ),
                                                    start_time=XmlTime(15, 20, 0, 0, 0),
                                                    end_time=XmlTime(20, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='standalone',
                                                        ref='bbd:standalone'
                                                    )
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='bbd:sj_457_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(9, 0, 0, 0, 0),
                                                        for_boarding=True,
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_457_joinTo_447_dep_amsterdam'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Start at Amsterdam (train couples)'
                                                                    ),
                                                                    earliest_time=XmlTime(9, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='uic:nl_amsterdam'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:nl_amsterdam_1'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 1'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_hannover'
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='bbd:sj_457_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_40447_splitFrom_447_arr_hannover'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection at Hannover to Copenhagen '
                                                                    ),
                                                                    earliest_time=XmlTime(15, 20, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT5M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_hannover_01'
                                                                    ),
                                                                    connecting_stop_point_ref=[
                                                                        ScheduledStopPointRefStructure(
                                                                            version='any',
                                                                            ref='uic:de_hannover'
                                                                        ),
                                                                    ],
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_40447'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(12, 15, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_40447_amsterdam-copenhagen'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='40447'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(12, 5, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT5M"),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_hannover_5'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 5'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_berlin'
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='bbd:sj_457_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_457_splitFrom_447_arr_berlin'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection at Berlin to Warsaw on 447 (train splits)'
                                                                    ),
                                                                    earliest_time=XmlTime(14, 40, 0, 0, 0),
                                                                    latest_time=XmlTime(14, 50, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_berlin_01'
                                                                    ),
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_447'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(14, 50, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_447_amsterdam_warsaw'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='447'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    controlled=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 5, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT5M"),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_60457_joinTo_457_dep_berlin'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Joining at Berlin with    60457 to Prague '
                                                                    ),
                                                                    earliest_time=XmlTime(15, 20, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_berlin_02'
                                                                    ),
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_60457'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(15, 20, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_60457_berlin-prague'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='60457'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    advertised=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_berlin_3'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 3'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_prague'
                                                    ),
                                                    order=3
                                                ),
                                                Call1(
                                                    id='bbd:sj_457_004',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(20, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_60457_splitFrom_457_arr_prague'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Splitting at Prague of    60457 from 457   '
                                                                    ),
                                                                    earliest_time=XmlTime(20, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_60457'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(15, 20, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_60457_berlin-prague'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='60457'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    advertised=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:cz_prague_2'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 2'
                                                            )
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=4
                                                ),
                                            ]
                                        ),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_first'
                                                ),
                                            ]
                                        ),
                                        train_size=TrainSize(
                                            number_of_cars=22,
                                            train_size_type=TrainSizeEnumeration.LONG
                                        )
                                    ),
                                    ServiceJourney1(
                                        id='bbd:sj_60457',
                                        version='any',
                                        description=MultilingualString(
                                            value='60457 Berlin to Prague'
                                        ),
                                        departure_time=XmlTime(15, 0, 0, 0, 0),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            version='any',
                                            ref='bbd:JP_457_amsterdam-prague'
                                        ),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_457'
                                        ),
                                        block_ref=BlockRef(
                                            version='any',
                                            ref='ops:blk_457_amsterdam-prague'
                                        ),
                                        choice=LineView(
                                            public_code='457',
                                            transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='myrail:RT_60457'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='bbd:DST_prague'
                                            )
                                        ),
                                        parts=JourneyPartsRelStructure(
                                            journey_part_ref_or_journey_part=[
                                                JourneyPart(
                                                    id='bbd:jpt_60457_01',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Berlin to Prague'
                                                    ),
                                                    parent_journey_ref=VehicleJourneyRefStructure(
                                                        version='any',
                                                        ref='bbd:sj_60457'
                                                    ),
                                                    main_part_ref=JourneyPartRefStructure(
                                                        version='any',
                                                        ref='bbd:jpt_457_03'
                                                    ),
                                                    journey_part_couple_ref=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_03_berlin-prague'
                                                    ),
                                                    train_number_ref=TrainNumberRef(
                                                        version='any',
                                                        ref='bbd:tn_457'
                                                    ),
                                                    block_part_ref=TrainBlockPartRef(
                                                        version='any',
                                                        ref='ops:blkpt_457_03_berlin-prague'
                                                    ),
                                                    from_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    to_stop_point_ref=ScheduledStopPointRefStructure(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    ),
                                                    start_time=XmlTime(15, 20, 0, 0, 0),
                                                    end_time=XmlTime(20, 0, 0, 0, 0),
                                                    purpose_of_journey_partition_ref=PurposeOfJourneyPartitionRef(
                                                        value='standalone',
                                                        ref='bbd:standalone'
                                                    )
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='bbd:sj_60457_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 5, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT5M"),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_60457_joinTo_457_dep_berlin'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Joining at Berlin with    60457 to Prague '
                                                                    ),
                                                                    earliest_time=XmlTime(15, 20, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.JOINING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    connection_ref=ConnectionRefStructure(
                                                                        version='any',
                                                                        ref='uic:cx_de_berlin_02'
                                                                    ),
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_60457'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(15, 20, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_60457_berlin-prague'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='60457'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    advertised=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:de_berlin_3'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 3'
                                                            )
                                                        )
                                                    ),
                                                    destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                        version='any',
                                                        ref='bbd:DST_prague'
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='bbd:sj_60457_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(20, 0, 0, 0, 0),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingView(
                                                                    journey_meeting_ref=JourneyMeetingRef(
                                                                        version='any',
                                                                        ref='bbd:jm_60457_splitFrom_457_arr_prague'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Splitting at Prague of    60457 from 457   '
                                                                    ),
                                                                    earliest_time=XmlTime(20, 0, 0, 0, 0),
                                                                    reason=ReasonForMeetingEnumeration.SPLITTING,
                                                                    maximum_wait_time=XmlDuration("PT10M"),
                                                                    choice=ConnectingJourneyView(
                                                                        service_journey_ref=ServiceJourneyRefStructure(
                                                                            version='any',
                                                                            ref='bbd:sj_60457'
                                                                        ),
                                                                        departure_time_or_frequency=XmlTime(15, 20, 0, 0, 0),
                                                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                                                            version='any',
                                                                            ref='bbd:JP_60457_berlin-prague'
                                                                        )
                                                                    ),
                                                                    flexible_line_ref_or_line_ref_or_connecting_line_view=LineDerivedViewStructure(
                                                                        name=MultilingualString(
                                                                            value='60457'
                                                                        ),
                                                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                                                    ),
                                                                    stay_seated=True,
                                                                    planned=True,
                                                                    advertised=True,
                                                                    transfer_duration=TransferDurationStructure(
                                                                        default_duration=XmlDuration("PT0M")
                                                                    )
                                                                ),
                                                            ]
                                                        ),
                                                        choice=QuayAssignmentView(
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='uic:cz_prague_2'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Platform 2'
                                                            )
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=2
                                                ),
                                            ]
                                        ),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySet(
                                                    id='bbd:svcfc_60457',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Second  class facilities only'
                                                    ),
                                                    catering_facility_list=CateringFacilityList(
                                                        value=[
                                                            CateringFacilityEnumeration.BUFFET,
                                                        ]
                                                    ),
                                                    fare_classes=FareClasses(
                                                        value=[
                                                            FareClassEnumeration.SECOND_CLASS,
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            train_numbers=TrainNumbersInFrameRelStructure(
                                train_number_or_train_number_ref=[
                                    TrainNumber(
                                        id='bbd:tn_447',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdam - Warsaw'
                                        ),
                                        for_advertisement='447',
                                        for_production='447'
                                    ),
                                    TrainNumber(
                                        id='bbd:tn_40447',
                                        version='any',
                                        description=MultilingualString(
                                            value='Hannover - Copenhagen'
                                        ),
                                        for_advertisement='40447',
                                        for_production='40447'
                                    ),
                                    TrainNumber(
                                        id='bbd:tn_457',
                                        version='any',
                                        description=MultilingualString(
                                            value='Berlin - Prague'
                                        ),
                                        for_advertisement='457',
                                        for_production='457'
                                    ),
                                ]
                            ),
                            journey_part_couples=JourneyPartCouplesInFrameRelStructure(
                                journey_part_couple=[
                                    JourneyPartCouple(
                                        id='bbd:jpc_01_amsterdam-hannover',
                                        version='any',
                                        start_time=XmlTime(9, 0, 0, 0, 0),
                                        end_time=XmlTime(12, 0, 0, 0, 0),
                                        from_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:nl_amsterdam'
                                        ),
                                        to_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_hannover'
                                        ),
                                        main_part_ref=JourneyPartRefStructure(
                                            version='any',
                                            ref='bbd:jpt_447_01'
                                        ),
                                        journey_parts=JourneyPartRefsRelStructure(
                                            journey_part_ref=[
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_447_01'
                                                ),
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_457_01'
                                                ),
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_40447_01'
                                                ),
                                            ]
                                        ),
                                        train_number_ref=TrainNumberRef(
                                            version='any',
                                            ref='bbd:tn_447'
                                        ),
                                        order=1
                                    ),
                                    JourneyPartCouple(
                                        id='bbd:jpc_02_hannover-berlin',
                                        version='any',
                                        description=MultilingualString(
                                            value='Hannover to Berlin'
                                        ),
                                        start_time=XmlTime(12, 5, 0, 0, 0),
                                        end_time=XmlTime(15, 0, 0, 0, 0),
                                        from_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_hannover'
                                        ),
                                        to_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_berlin'
                                        ),
                                        main_part_ref=JourneyPartRefStructure(
                                            version='any',
                                            ref='bbd:jpt_447_02'
                                        ),
                                        journey_parts=JourneyPartRefsRelStructure(
                                            journey_part_ref=[
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_447_02'
                                                ),
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_457_02'
                                                ),
                                            ]
                                        ),
                                        train_number_ref=TrainNumberRef(
                                            version='any',
                                            ref='bbd:tn_447'
                                        ),
                                        order=2
                                    ),
                                    JourneyPartCouple(
                                        id='bbd:jpc_03_berlin-prague',
                                        version='any',
                                        description=MultilingualString(
                                            value='Berlin to Prague'
                                        ),
                                        start_time=XmlTime(15, 10, 0, 0, 0),
                                        end_time=XmlTime(19, 0, 0, 0, 0),
                                        from_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_berlin'
                                        ),
                                        to_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:cz_prague'
                                        ),
                                        main_part_ref=JourneyPartRefStructure(
                                            version='any',
                                            ref='bbd:jpt_457_03'
                                        ),
                                        journey_parts=JourneyPartRefsRelStructure(
                                            journey_part_ref=[
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_60457_01'
                                                ),
                                                JourneyPartRef(
                                                    version='any',
                                                    ref='bbd:jpt_457_03'
                                                ),
                                            ]
                                        ),
                                        train_number_ref=TrainNumberRef(
                                            version='any',
                                            ref='bbd:tn_457'
                                        ),
                                        order=3
                                    ),
                                ]
                            ),
                            coupled_journeys=CoupledJourneysInFrameRelStructure(
                                coupled_journey=[
                                    CoupledJourney(
                                        id='bbd:CoupledJourney:cj_447_01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdamn to hannover'
                                        ),
                                        train_block_ref=TrainBlockRef(
                                            version='any',
                                            ref='bbd:XX-447_amsterdam-hannover'
                                        ),
                                        journeys=VehicleJourneyRefsRelStructure(
                                            vehicle_journey_ref=[
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_447'
                                                ),
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_40447'
                                                ),
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_457'
                                                ),
                                            ]
                                        )
                                    ),
                                    CoupledJourney(
                                        id='bbd:CoupledJourney:cj_447_02',
                                        version='any',
                                        description=MultilingualString(
                                            value='Hannover - Berlin'
                                        ),
                                        train_block_ref=TrainBlockRef(
                                            version='any',
                                            ref='bbd:YY-447_hannover-berlin'
                                        ),
                                        journeys=VehicleJourneyRefsRelStructure(
                                            vehicle_journey_ref=[
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_447'
                                                ),
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_457'
                                                ),
                                            ]
                                        )
                                    ),
                                    CoupledJourney(
                                        id='bbd:CoupledJourney:sj_457_03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Berlin  - Prague'
                                        ),
                                        train_block_ref=TrainBlockRef(
                                            version='any',
                                            ref='bbd:cmpblk_ZZ-457_berlin-prague'
                                        ),
                                        journeys=VehicleJourneyRefsRelStructure(
                                            vehicle_journey_ref=[
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_60457'
                                                ),
                                                VehicleJourneyRef(
                                                    version='any',
                                                    ref='bbd:sj_457'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='bbd:svcfc_general',
                                        version='any',
                                        description=MultilingualString(
                                            value='General facilities'
                                        ),
                                        assistance_facility_list=AssistanceFacilityList(
                                            value=[
                                                AssistanceFacilityEnumeration.BOARDING_ASSISTANCE,
                                                AssistanceFacilityEnumeration.CONDUCTOR,
                                                AssistanceFacilityEnumeration.WHEELCHAIR_ASSISTANCE,
                                            ]
                                        ),
                                        catering_facility_list=CateringFacilityList(
                                            value=[
                                                CateringFacilityEnumeration.BUFFET,
                                            ]
                                        ),
                                        fare_classes=FareClasses(
                                            value=[
                                                FareClassEnumeration.FIRST_CLASS,
                                                FareClassEnumeration.STANDARD_CLASS,
                                            ]
                                        ),
                                        mobility_facility_list=MobilityFacilityList(
                                            value=[
                                                MobilityFacilityEnumeration.STEP_FREE_ACCESS,
                                                MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS,
                                            ]
                                        ),
                                        nuisance_facility_list=NuisanceFacilityList(
                                            value=[
                                                NuisanceFacilityEnumeration.MOBILE_PHONE_FREE_ZONE,
                                                NuisanceFacilityEnumeration.NO_SMOKING,
                                            ]
                                        ),
                                        passenger_comms_facility_list=PassengerCommsFacilityList(
                                            value=[
                                                PassengerCommsFacilityEnumeration.PUBLIC_WIFI,
                                            ]
                                        ),
                                        passenger_information_facility_list=PassengerInformationFacilityList(
                                            value=[
                                                PassengerInformationFacilityEnumeration.NEXT_STOP_INDICATOR,
                                                PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY,
                                                PassengerInformationFacilityEnumeration.REAL_TIME_CONNECTIONS,
                                                PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS,
                                            ]
                                        ),
                                        sanitary_facility_list=SanitaryFacilityList(
                                            value=[
                                                SanitaryFacilityEnumeration.TOILET,
                                                SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET,
                                            ]
                                        ),
                                        ticketing_service_facility_list=TicketingServiceFacilityList(
                                            value=[
                                                TicketingServiceFacilityEnumeration.PURCHASE,
                                            ]
                                        ),
                                        accommodation_access_list=AccommodationAccessList(
                                            value=[
                                                AccommodationAccessEnumeration.RESERVATION,
                                            ]
                                        ),
                                        accommodation_facility_list=AccommodationFacilityList(
                                            value=[
                                                AccommodationFacilityEnumeration.COUCHETTE,
                                                AccommodationFacilityEnumeration.SEATING,
                                                AccommodationFacilityEnumeration.SLEEPER,
                                            ]
                                        ),
                                        couchette_facility_list=CouchetteFacilityList(
                                            value=[
                                                CouchetteFacilityEnumeration.C2,
                                                CouchetteFacilityEnumeration.C4,
                                                CouchetteFacilityEnumeration.C6,
                                                CouchetteFacilityEnumeration.T2,
                                            ]
                                        ),
                                        luggage_carriage_facility_list=LuggageCarriageFacilityList(
                                            value=[
                                                LuggageCarriageEnumeration.BAGGAGE_STORAGE,
                                                LuggageCarriageEnumeration.BAGGAGE_VAN,
                                                LuggageCarriageEnumeration.CYCLES_ALLOWED_WITH_RESERVATION,
                                                LuggageCarriageEnumeration.LUGGAGE_RACKS,
                                            ]
                                        )
                                    ),
                                    ServiceFacilitySet(
                                        id='bbd:svcfc_first',
                                        version='any',
                                        description=MultilingualString(
                                            value='First class facilities'
                                        ),
                                        catering_facility_list=CateringFacilityList(
                                            value=[
                                                CateringFacilityEnumeration.BREAKFAST_IN_CAR,
                                            ]
                                        ),
                                        fare_classes=FareClasses(
                                            value=[
                                                FareClassEnumeration.FIRST_CLASS,
                                            ]
                                        ),
                                        passenger_comms_facility_list=PassengerCommsFacilityList(
                                            value=[
                                                PassengerCommsFacilityEnumeration.POWER_SUPPLY_SOCKETS,
                                                PassengerCommsFacilityEnumeration.PUBLIC_WIFI,
                                            ]
                                        ),
                                        accommodation_access_list=AccommodationAccessList(
                                            value=[
                                                AccommodationAccessEnumeration.RESERVATION,
                                            ]
                                        ),
                                        accommodation_facility_list=AccommodationFacilityList(
                                            value=[
                                                AccommodationFacilityEnumeration.SLEEPER,
                                            ]
                                        ),
                                        accommodations=AccommodationsRelStructure(
                                            accommodation_ref_or_accommodation=[
                                                Accommodation(
                                                    id='bbd:svcfc_firs@singleSleeper',
                                                    version='any',
                                                    fare_class=FareClass(
                                                        value=FareClassEnumeration.FIRST_CLASS
                                                    ),
                                                    accommodation_facility=AccommodationFacility(
                                                        value=AccommodationFacilityEnumeration.SINGLE_COUCHETTE
                                                    ),
                                                    berth_facility=BerthFacility(
                                                        value=BerthFacilityEnumeration.LOWER
                                                    ),
                                                    shower_facility=SanitaryFacilityEnumeration.SHOWER,
                                                    toilet_facility=SanitaryFacilityEnumeration.TOILET,
                                                    nuisance_facility_list=NuisanceFacilityList(
                                                        value=[
                                                            NuisanceFacilityEnumeration.NO_SMOKING,
                                                            NuisanceFacilityEnumeration.MOBILE_PHONE_FREE_ZONE,
                                                        ]
                                                    ),
                                                    passenger_comms_facility_list=PassengerCommsFacilityList(
                                                        value=[
                                                            PassengerCommsFacilityEnumeration.FREE_WIFI,
                                                        ]
                                                    )
                                                ),
                                                Accommodation(
                                                    id='bbd:svcfc_firs@doubleSleeper',
                                                    version='any',
                                                    fare_class=FareClass(
                                                        value=FareClassEnumeration.FIRST_CLASS
                                                    ),
                                                    accommodation_facility=AccommodationFacility(
                                                        value=AccommodationFacilityEnumeration.DOUBLE_SLEEPER
                                                    ),
                                                    couchette_facility=CouchetteFacility(
                                                        value=CouchetteFacilityEnumeration.C2
                                                    ),
                                                    shower_facility=SanitaryFacilityEnumeration.SHOWER,
                                                    toilet_facility=SanitaryFacilityEnumeration.TOILET,
                                                    passenger_comms_facility_list=PassengerCommsFacilityList(
                                                        value=[
                                                            PassengerCommsFacilityEnumeration.FREE_WIFI,
                                                        ]
                                                    )
                                                ),
                                                Accommodation(
                                                    id='bbd:svcfc_firs@sleeper',
                                                    version='any',
                                                    fare_class=FareClass(
                                                        value=FareClassEnumeration.SECOND_CLASS
                                                    ),
                                                    accommodation_facility=AccommodationFacility(
                                                        value=AccommodationFacilityEnumeration.COUCHETTE
                                                    ),
                                                    couchette_facility=CouchetteFacility(
                                                        value=CouchetteFacilityEnumeration.C4
                                                    ),
                                                    passenger_comms_facility_list=PassengerCommsFacilityList(
                                                        value=[
                                                            PassengerCommsFacilityEnumeration.FREE_WIFI,
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        onboard_stays=OnboardStaysRelStructure(
                                            onboard_stay=[
                                                OnboardStay(
                                                    id='bbd:svcfc_firs@earlyBoardingPossibleBeforeDeparture',
                                                    version='any',
                                                    fare_class=FareClass(
                                                        value=FareClassEnumeration.FIRST_CLASS
                                                    ),
                                                    boarding_permission=BoardingPermission(
                                                        value=BoardingPermissionEnumeration.EARLY_BOARDING_POSSIBLE_BEFORE_DEPARTURE
                                                    ),
                                                    period=XmlDuration("PT1H")
                                                ),
                                                OnboardStay(
                                                    id='bbd:svcfc_firs@overnightStayOnboardAllowed',
                                                    version='any',
                                                    fare_class=FareClass(
                                                        value=FareClassEnumeration.FIRST_CLASS
                                                    ),
                                                    boarding_permission=BoardingPermission(
                                                        value=BoardingPermissionEnumeration.OVERNIGHT_STAY_ONBOARD_ALLOWED
                                                    ),
                                                    period=XmlDuration("PT9H")
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            journey_meetings=JourneyMeetingsInFrameRelStructure(
                                journey_meeting=[
                                    JourneyMeeting(
                                        id='bbd:jm_457_joinTo_447_dep_amsterdam',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:nl_amsterdam'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_457'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_447'
                                        ),
                                        description=MultilingualString(
                                            value='Join 457 to 447 at Amsterdam'
                                        ),
                                        earliest_time=XmlTime(9, 0, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.JOINING
                                    ),
                                    JourneyMeeting(
                                        id='bbd:jm_40447_joinTo_477_dep_amsterdam',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:nl_amsterdam'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_40447'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_447'
                                        ),
                                        description=MultilingualString(
                                            value='Join 40447 to 447 at Amsterdam'
                                        ),
                                        earliest_time=XmlTime(9, 0, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.JOINING
                                    ),
                                    JourneyMeeting(
                                        id='bbd:jm_40447_splitFrom_447_arr_hannover',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_hannover'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_40447'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_447'
                                        ),
                                        description=MultilingualString(
                                            value='Split  40447 from 447 at Hannover'
                                        ),
                                        earliest_time=XmlTime(12, 0, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.JOINING
                                    ),
                                    JourneyMeeting(
                                        id='bbd:jm_457_splitFrom_447_arr_berlin',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_berlin'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_457'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_447'
                                        ),
                                        description=MultilingualString(
                                            value='Split  457 from 447 at Hannover'
                                        ),
                                        earliest_time=XmlTime(15, 0, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.JOINING
                                    ),
                                    JourneyMeeting(
                                        id='bbd:jm_60457_joinTo_457_dep_berlin',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:de_berlin'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_60457'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_457'
                                        ),
                                        description=MultilingualString(
                                            value='Join 60457 to 457 at Berlin'
                                        ),
                                        earliest_time=XmlTime(15, 10, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.JOINING
                                    ),
                                    JourneyMeeting(
                                        id='bbd:jm_60457_splitFrom_457_arr_prague',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='uic:cz_prague'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_60457'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='bbd:sj_457'
                                        ),
                                        earliest_time=XmlTime(20, 10, 0, 0, 0),
                                        reason=ReasonForMeetingEnumeration.SPLITTING
                                    ),
                                ]
                            ),
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                choice=[
                                    CompoundTrain(
                                        id='bbd:ctrn_XX-447',
                                        version='any',
                                        name=MultilingualString(
                                            value='447 + 457 + 40447 Amsterdam - Hannover'
                                        ),
                                        description=MultilingualString(
                                            value='E - 2 2 2 2 2 2 R 1 1 -    2  2  2  2  2  -   2  2  2  1 1 - E'
                                        ),
                                        self_propelled=True,
                                        components=TrainsInCompoundTrainRelStructure(
                                            train_in_compound_train=[
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_XX-447_40447',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_40447'
                                                    ),
                                                    label=MultilingualString(
                                                        value='40447'
                                                    ),
                                                    order=1
                                                ),
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_XX-447_457',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_457'
                                                    ),
                                                    label=MultilingualString(
                                                        value='457'
                                                    ),
                                                    order=2
                                                ),
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_XX-447_447',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_447'
                                                    ),
                                                    label=MultilingualString(
                                                        value='447'
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundTrain(
                                        id='bbd:ctrn_YY-447',
                                        version='any',
                                        name=MultilingualString(
                                            value='447 + 457  Hannover - Berlin'
                                        ),
                                        description=MultilingualString(
                                            value='E- 2 2 2 2 2 2 R 1 1 -    2  2  2  2 2 -  E'
                                        ),
                                        self_propelled=True,
                                        components=TrainsInCompoundTrainRelStructure(
                                            train_in_compound_train=[
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_YY-447_457',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_457'
                                                    ),
                                                    label=MultilingualString(
                                                        value='457'
                                                    ),
                                                    order=1
                                                ),
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_YY-447_447',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_447'
                                                    ),
                                                    label=MultilingualString(
                                                        value='447'
                                                    ),
                                                    order=2
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundTrain(
                                        id='bbd:ctrn_ZZ-457',
                                        version='any',
                                        name=MultilingualString(
                                            value='457 + 60457  Berlin - Prague'
                                        ),
                                        description=MultilingualString(
                                            value='2  2  2  2 2  -   R  2   2   2   2  - E'
                                        ),
                                        self_propelled=True,
                                        components=TrainsInCompoundTrainRelStructure(
                                            train_in_compound_train=[
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_ZZ-457_60457',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_60457'
                                                    ),
                                                    label=MultilingualString(
                                                        value='60457'
                                                    ),
                                                    order=1
                                                ),
                                                TrainInCompoundTrainVersionedChildStructure(
                                                    id='bbd:trninctrn_ZZ-457_457',
                                                    version='any',
                                                    train_ref_or_train=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_457'
                                                    ),
                                                    label=MultilingualString(
                                                        value='447'
                                                    ),
                                                    order=2
                                                ),
                                            ]
                                        )
                                    ),
                                    Train(
                                        id='bbd:trn_40447',
                                        version='any',
                                        name=MultilingualString(
                                            value='40447 Hanover - Copenhagen'
                                        ),
                                        description=MultilingualString(
                                            value='2  2  2 1 1 E'
                                        ),
                                        self_propelled=True,
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_first'
                                                ),
                                            ]
                                        ),
                                        components=TrainComponentsRelStructure(
                                            train_component_ref_or_train_component=[
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_01',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Engine '
                                                    ),
                                                    description=MultilingualString(
                                                        value='Engine'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_01',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.ENGINE
                                                    ),
                                                    order=1
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_02',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage A'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Front Carriage 1st Class'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_02',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=2
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_03',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage B'
                                                    ),
                                                    description=MultilingualString(
                                                        value='2nd Carriage 1st CLass'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_03',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_04',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage B'
                                                    ),
                                                    description=MultilingualString(
                                                        value='3rd Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_04',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_05',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage D'
                                                    ),
                                                    description=MultilingualString(
                                                        value='4th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_05',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=4
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_40447_06',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage E'
                                                    ),
                                                    description=MultilingualString(
                                                        value='5th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_40447_06',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=5
                                                ),
                                            ]
                                        )
                                    ),
                                    Train(
                                        id='bbd:trn_447',
                                        version='any',
                                        name=MultilingualString(
                                            value='447 Amsterdam - Warsaw '
                                        ),
                                        description=MultilingualString(
                                            value='E 2 2 2 2 2 2 R 1 1   X'
                                        ),
                                        self_propelled=True,
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_first'
                                                ),
                                            ]
                                        ),
                                        components=TrainComponentsRelStructure(
                                            train_component_ref_or_train_component=[
                                                TrainComponent(
                                                    id='bbd:trncmp_447_01',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage K'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Front Carriage 1st Class'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_01',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=1
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_02',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage L'
                                                    ),
                                                    description=MultilingualString(
                                                        value='2nd Carriage 1st CLass'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_02',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=2
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_03',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage M'
                                                    ),
                                                    description=MultilingualString(
                                                        value='3rd Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_03',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.RESTAURANT_CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_04',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage N'
                                                    ),
                                                    description=MultilingualString(
                                                        value='4th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_04',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=4
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_05',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage O'
                                                    ),
                                                    description=MultilingualString(
                                                        value='5th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_05',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=5
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_06',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage P'
                                                    ),
                                                    description=MultilingualString(
                                                        value='6th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_06',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=6
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_07',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage Q'
                                                    ),
                                                    description=MultilingualString(
                                                        value='7th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_07',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=7
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_08',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage R'
                                                    ),
                                                    description=MultilingualString(
                                                        value='8th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_08',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=8
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_447_09',
                                                    version='any',
                                                    label=MultilingualString(

                                                    ),
                                                    description=MultilingualString(
                                                        value='Engine'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_447_09',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.ENGINE
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    Train(
                                        id='bbd:trn_457',
                                        version='any',
                                        name=MultilingualString(
                                            value='457  Amsterdam - Prague '
                                        ),
                                        description=MultilingualString(
                                            value='-   2  2  2  2 2  -    '
                                        ),
                                        self_propelled=False,
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                            ]
                                        ),
                                        components=TrainComponentsRelStructure(
                                            train_component_ref_or_train_component=[
                                                TrainComponent(
                                                    id='bbd:trncmp_457_01',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage F'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Front Carriage '
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_457_01',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=1
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_457_02',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage G'
                                                    ),
                                                    description=MultilingualString(
                                                        value='2nd Carriage  '
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_457_02',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=2
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_457_03',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage H'
                                                    ),
                                                    description=MultilingualString(
                                                        value='3rd Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_457_03',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.FIRST_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_457_04',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage I'
                                                    ),
                                                    description=MultilingualString(
                                                        value='4th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_457_04',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.RESTAURANT_CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=4
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_457_05',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage J'
                                                    ),
                                                    description=MultilingualString(
                                                        value='5th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_457_05',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.RESTAURANT_CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.STANDARD_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=5
                                                ),
                                            ]
                                        )
                                    ),
                                    Train(
                                        id='bbd:trn_60457',
                                        version='any',
                                        name=MultilingualString(
                                            value='60457  Berlin - Prague '
                                        ),
                                        description=MultilingualString(
                                            value='-  R  2   2   2   2  - E'
                                        ),
                                        self_propelled=False,
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='bbd:svcfc_general'
                                                ),
                                            ]
                                        ),
                                        components=TrainComponentsRelStructure(
                                            train_component_ref_or_train_component=[
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_01',
                                                    version='any',
                                                    label=MultilingualString(

                                                    ),
                                                    description=MultilingualString(
                                                        value='Engine'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_01',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.ENGINE
                                                    ),
                                                    order=1
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_02',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage AA'
                                                    ),
                                                    description=MultilingualString(
                                                        value='Front Carriage '
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_02',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=2
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_03',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage BB'
                                                    ),
                                                    description=MultilingualString(
                                                        value='2nd Carriage  '
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_03',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_04',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage CC'
                                                    ),
                                                    description=MultilingualString(
                                                        value='3rd Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_04',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=4
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_05',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage DD'
                                                    ),
                                                    description=MultilingualString(
                                                        value='4th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_05',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=5
                                                ),
                                                TrainComponent(
                                                    id='bbd:trncmp_60457_06',
                                                    version='any',
                                                    label=MultilingualString(
                                                        value='Carriage EE'
                                                    ),
                                                    description=MultilingualString(
                                                        value='5th Carriage'
                                                    ),
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bbd:trne_60457_06',
                                                        version='any',
                                                        name=MultilingualString(

                                                        ),
                                                        train_element_type=TrainElementTypeEnumeration.CARRIAGE,
                                                        fare_classes=FareClasses(
                                                            value=[
                                                                FareClassEnumeration.SECOND_CLASS,
                                                            ]
                                                        )
                                                    ),
                                                    order=6
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        VehicleScheduleFrame(
                            id='ops:VSF_23_O',
                            version='any',
                            name=MultilingualString(
                                value='BLOCKS Winter timetable for Asmterdam Example'
                            ),
                            blocks=BlocksInFrameRelStructure(
                                block_or_compound_block_or_train_block=[
                                    TrainBlock(
                                        id='ops:blk_447_amsterdam-warsaw',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdam - Hannover - Berrlin  Warsaw'
                                        ),
                                        preparation_duration=XmlDuration("PT10M"),
                                        finishing_duration=XmlDuration("PT10H"),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_447'
                                        ),
                                        start_point_ref=PointRefStructure(
                                            ref='uic:nl_amsterdam'
                                        ),
                                        end_point_ref=PointRefStructure(
                                            ref='uic:pl_warsaw'
                                        ),
                                        block_parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPart(
                                                    id='ops:blkpt_447_01_amsterdam-hannover',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Amsterdam to Hannover (447+ 457 +40447)'
                                                    ),
                                                    vehicle_type_ref=CompoundTrainRef(
                                                        version='any',
                                                        ref='bbd:ctrn_XX-447'
                                                    ),
                                                    journey_part_couple_ref_or_journey_parts=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_01_amsterdam-hannover'
                                                    ),
                                                    order=1
                                                ),
                                                TrainBlockPart(
                                                    id='ops:blkpt_447_02_hannover-berlin',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Hannover to Berlin (447+ 457)'
                                                    ),
                                                    vehicle_type_ref=CompoundTrainRef(
                                                        version='any',
                                                        ref='bbd:ctrn_YY-447'
                                                    ),
                                                    journey_part_couple_ref_or_journey_parts=JourneyPartCoupleRef(
                                                        version='any',
                                                        ref='bbd:jpc_02_hannover-berlin'
                                                    ),
                                                    order=2
                                                ),
                                                TrainBlockPart(
                                                    id='ops:blkpt_447_03_berlin-warsaw',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Berlin to Warsaw (447)'
                                                    ),
                                                    vehicle_type_ref=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_447'
                                                    ),
                                                    journey_part_couple_ref_or_journey_parts=JourneyPartRefsRelStructure(
                                                        journey_part_ref=[
                                                            JourneyPartRef(
                                                                version='any',
                                                                ref='bbd:jpt_447_03'
                                                            ),
                                                        ]
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    TrainBlock(
                                        id='ops:blk_40447_amsterdam-copenhagen',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdam to  Copenhagen (40447)'
                                        ),
                                        preparation_duration=XmlDuration("PT10M"),
                                        finishing_duration=XmlDuration("PT7H"),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_40447'
                                        ),
                                        start_point_ref=PointRefStructure(
                                            ref='uic:de_hannover'
                                        ),
                                        end_point_ref=PointRefStructure(
                                            ref='uic:dk_copenhagen'
                                        ),
                                        block_parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_447_01_amsterdam-hannover'
                                                ),
                                                TrainBlockPart(
                                                    id='ops:blkpt_40447_02_hannover-copenhagen',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Hannover to  Copenhagen'
                                                    ),
                                                    vehicle_type_ref=TrainRef(
                                                        version='any',
                                                        ref='bbd:trn_40447'
                                                    ),
                                                    journey_part_couple_ref_or_journey_parts=JourneyPartRefsRelStructure(
                                                        journey_part_ref=[
                                                            JourneyPartRef(
                                                                version='any',
                                                                ref='bbd:jpt_40447_02'
                                                            ),
                                                        ]
                                                    ),
                                                    order=2
                                                ),
                                            ]
                                        )
                                    ),
                                    TrainBlock(
                                        id='ops:blk_457_amsterdam-prague',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdam to Prague'
                                        ),
                                        preparation_duration=XmlDuration("PT10M"),
                                        finishing_duration=XmlDuration("PT10H"),
                                        vehicle_type_ref=TrainRef(
                                            version='any',
                                            ref='bbd:trn_457'
                                        ),
                                        start_point_ref=PointRefStructure(
                                            ref='uic:de_berlin'
                                        ),
                                        end_point_ref=PointRefStructure(
                                            ref='uic:cz_prague'
                                        ),
                                        block_parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_447_01_amsterdam-hannover'
                                                ),
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_447_02_hannover-berlin'
                                                ),
                                                TrainBlockPart(
                                                    id='ops:blkpt_457_03_berlin-prague',
                                                    version='any',
                                                    description=MultilingualString(
                                                        value='Berlin to Prague'
                                                    ),
                                                    vehicle_type_ref=CompoundTrainRef(
                                                        version='any',
                                                        ref='bbd:ctrn_ZZ-457'
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundBlock(
                                        id='bbd:XX-447_amsterdam-hannover',
                                        version='any',
                                        description=MultilingualString(
                                            value='Amsterdam to Hannover'
                                        ),
                                        vehicle_type_ref=CompoundTrainRef(
                                            version='any',
                                            ref='bbd:ctrn_XX-447'
                                        ),
                                        parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_447_01_amsterdam-hannover'
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundBlock(
                                        id='bbd:YY-447_hannover-berlin',
                                        version='any',
                                        description=MultilingualString(
                                            value='Hannover to Berlin'
                                        ),
                                        vehicle_type_ref=CompoundTrainRef(
                                            version='any',
                                            ref='bbd:ctrn_YY-447'
                                        ),
                                        parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_447_02_hannover-berlin'
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundBlock(
                                        id='bbd:cmpblk_ZZ-457_berlin-prague',
                                        version='any',
                                        description=MultilingualString(
                                            value='Berlin to Prague'
                                        ),
                                        vehicle_type_ref=CompoundTrainRef(
                                            version='any',
                                            ref='bbd:ctrn_ZZ-457'
                                        ),
                                        parts=BlockPartsRelStructure(
                                            choice=[
                                                TrainBlockPartRef(
                                                    version='any',
                                                    ref='ops:blkpt_457_03_berlin-prague'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='myrail:svf_12',
                            version='any',
                            name=MultilingualString(
                                value='Stops for Winter timetable for Splitting timnetable  Amsterdamn to Warsaw  '
                            ),
                            routes=RoutesInFrameRelStructure(
                                route=[
                                    Route1(
                                        id='myrail:RT_447',
                                        version='any',
                                        name=MultilingualString(
                                            value='amsterdam-warsaw'
                                        ),
                                        short_name=MultilingualString(
                                            value='Route 447'
                                        )
                                    ),
                                    Route1(
                                        id='myrail:RT_40447',
                                        version='any',
                                        name=MultilingualString(
                                            value='amsterdam-copenhagen'
                                        ),
                                        short_name=MultilingualString(
                                            value='Route 40447'
                                        )
                                    ),
                                    Route1(
                                        id='myrail:RT_457',
                                        version='any',
                                        name=MultilingualString(
                                            value='amsterdam-prague'
                                        ),
                                        short_name=MultilingualString(
                                            value='Route 457'
                                        )
                                    ),
                                    Route1(
                                        id='myrail:RT_60457',
                                        version='any',
                                        name=MultilingualString(
                                            value='berlin-prague'
                                        ),
                                        short_name=MultilingualString(
                                            value='Route 60457'
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line1(
                                        id='myrail:LN_nl_amsterdam-cz_prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='LN_amsterdam-cz_prague'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                    ),
                                    Line1(
                                        id='myrail:LN_nl_amsterdam-pl_warsaw',
                                        version='any',
                                        name=MultilingualString(
                                            value='LN_amsterdam-pl_warsaw'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 25'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                    ),
                                    Line1(
                                        id='myrail:LN_nl_amsterdam-dk_copenhagen',
                                        version='any',
                                        name=MultilingualString(
                                            value='LN_amsterdam-pl_warsaw'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 31'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='bbd:DST_berlin',
                                        version='any',
                                        name=MultilingualString(
                                            value='Berlin  Hochbahnhof',
                                            lang='de'
                                        ),
                                        short_name=MultilingualString(
                                            value='Berlin HBF'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='bbd:DST_copenhagen',
                                        version='any',
                                        name=MultilingualString(
                                            value='Copenhagen Main Station'
                                        ),
                                        short_name=MultilingualString(
                                            value='Hannover HBF'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='bbd:DST_hannover',
                                        version='any',
                                        name=MultilingualString(
                                            value='Hannover  Hochbahnhof',
                                            lang='de'
                                        ),
                                        short_name=MultilingualString(
                                            value='Hannover HBF'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='bbd:DST_prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='Prague'
                                        ),
                                        short_name=MultilingualString(
                                            value='Prague'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='bbd:DST_warsaw',
                                        version='any',
                                        name=MultilingualString(
                                            value='Warsaw'
                                        ),
                                        short_name=MultilingualString(
                                            value='Warsaw'
                                        )
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='uic:nl_amsterdam',
                                        version='any',
                                        name=MultilingualString(
                                            value='Amsterdamn'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='uic:de_hannover',
                                        version='any',
                                        name=MultilingualString(
                                            value='Hannover'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='uic:de_berlin',
                                        version='any',
                                        name=MultilingualString(
                                            value='Berlin'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='uic:cz_prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='Prague HBF'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='uic:dk_copenhagen',
                                        version='any',
                                        name=MultilingualString(
                                            value='Copenhagen HBF'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='uic:pl_warsaw',
                                        version='any',
                                        name=MultilingualString(
                                            value='Berlin'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                transfer=[
                                    Connection(
                                        id='uic:cx_de_hannover_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Connection at Hannover for berlin'
                                        )
                                    ),
                                    Connection(
                                        id='uic:cx_de_hannover_02',
                                        version='any',
                                        name=MultilingualString(
                                            value='Connection at Hannover for Copenhagen'
                                        )
                                    ),
                                    Connection(
                                        id='uic:cx_de_berlin_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Connection at Berlin for Warsaw'
                                        )
                                    ),
                                    Connection(
                                        id='uic:cx_de_berlin_02',
                                        version='any',
                                        name=MultilingualString(
                                            value='Connection at Berlin for Prague'
                                        )
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                choice=[
                                    ServiceJourneyPattern(
                                        id='bbd:JP_447_amsterdam_warsaw',
                                        version='any',
                                        name=MultilingualString(
                                            value='Amsterdam  to Warsaw'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_447_amsterdam_warsaw_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_447_amsterdam_warsaw_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_447_amsterdam_warsaw_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_447_amsterdam_warsaw_04',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:pl_warsaw'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='bbd:JP_40447_amsterdam-copenhagen',
                                        version='any',
                                        name=MultilingualString(
                                            value='Amsterdamn to Copenhagen'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_40447_amsterdam_copenhagen_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_40447_amsterdam_copenhagen_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_40447_amsterdam_copenhagen_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:dk_copenhagen'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='bbd:JP_457_amsterdam-prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='Amsterdam to prague'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_457_amsterdam_prague_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:nl_amsterdam'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_457_amsterdam_prague_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_hannover'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_457_amsterdam_prague_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_457_amsterdam_prague_04',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='bbd:JP_60457_berlin-prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='Berlin to Prague'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_60457_berlin_prague_01',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:de_berlin'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bbd:JP_60457_berlin_prague_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='uic:cz_prague'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='mybus:svf_12',
                            version='any',
                            name=MultilingualString(
                                value='Stop Places for Winter timetable for route 24 '
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace1(
                                        id='uic:nl_amsterdam',
                                        version='any',
                                        name=MultilingualString(
                                            value='Amsterdam'
                                        ),
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:nl_amsterdam_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace1(
                                        id='uic:de_berlin',
                                        version='any',
                                        name=MultilingualString(
                                            value='Berlin HBF'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:de_berlin_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                                Quay1(
                                                    id='uic:de_berlin_2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 2'
                                                    )
                                                ),
                                                Quay1(
                                                    id='uic:de_berlin_3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 3'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace1(
                                        id='uic:dk_copenhagen',
                                        version='any',
                                        name=MultilingualString(
                                            value='Copenhagen HBF'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:dk_copenhagen_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace1(
                                        id='uic:de_hannover',
                                        version='any',
                                        name=MultilingualString(
                                            value='Hannover HBF'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:de_hannover_5',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 5'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace1(
                                        id='uic:cz_prague',
                                        version='any',
                                        name=MultilingualString(
                                            value='Warsaw HBF'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:cz_prague_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                                Quay1(
                                                    id='uic:cz_prague_2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 2'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace1(
                                        id='uic:pl_warsaw',
                                        version='any',
                                        name=MultilingualString(
                                            value='Warsaw HBF'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='uic:pl_warsaw_7',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                                Quay1(
                                                    id='uic:pl_warsaw_8',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Platform 1'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='bbd:CAL_01',
                            version='any',
                            name=MultilingualString(
                                value='Service Calendar Nov 2010 '
                            ),
                            service_calendar=ServiceCalendar(
                                id='bbd:SC_01',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType1(
                                        id='bbd:DT_01-MF-NH',
                                        version='any',
                                        name=MultilingualString(
                                            value='Weekdays unless a holiday'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.MONDAY,
                                                        DayOfWeekEnumeration.TUESDAY,
                                                        DayOfWeekEnumeration.WEDNESDAY,
                                                        DayOfWeekEnumeration.THURSDAY,
                                                        DayOfWeekEnumeration.FRIDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NOT_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='bbd:DT_03-WE-NH',
                                        version='any',
                                        name=MultilingualString(
                                            value='Weekends unless a holiday'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.SATURDAY,
                                                        DayOfWeekEnumeration.SUNDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NOT_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
