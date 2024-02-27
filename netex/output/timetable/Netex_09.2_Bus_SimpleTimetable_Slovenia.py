from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType1
from netex.models.alternative_texts_rel_structure import OperatingDay
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.models.assistance_facility_list import AssistanceFacilityList
from netex.models.block_ref import BlockRef
from netex.models.call_1 import Call1
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.day_type_assignments_in_frame_rel_structure import DayTypeAssignmentsInFrameRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.direction import Direction
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type import DirectionType
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.fare_classes import FareClasses
from netex.models.group_of_links import GroupOfLinks
from netex.models.group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from netex.models.group_of_timing_links_ref import GroupOfTimingLinksRef
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journey_run_time import JourneyRunTime
from netex.models.journey_run_times_rel_structure import JourneyRunTimesRelStructure
from netex.models.journey_wait_time import JourneyWaitTime
from netex.models.journey_wait_times_rel_structure import JourneyWaitTimesRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line_1 import Line1
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.link_refs_rel_structure import LinkRefsRelStructure
from netex.models.links_in_journey_pattern_rel_structure import LinksInJourneyPatternRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.luggage_carriage_enumeration import LuggageCarriageEnumeration
from netex.models.luggage_carriage_facility_list import LuggageCarriageFacilityList
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration
from netex.models.mobility_facility_list import MobilityFacilityList
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.nuisance_facility_list import NuisanceFacilityList
from netex.models.onward_timing_link_view import OnwardTimingLinkView
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operating_day_ref_structure import OperatingDayRefStructure
from netex.models.operating_days_in_frame_rel_structure import OperatingDaysInFrameRelStructure
from netex.models.operating_period_1 import OperatingPeriod1
from netex.models.operating_periods_in_frame_rel_structure import OperatingPeriodsInFrameRelStructure
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.passenger_information_facility_list import PassengerInformationFacilityList
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.property_of_day_structure import PropertyOfDayStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.route_1 import Route1
from netex.models.route_ref import RouteRef
from netex.models.route_ref_structure import RouteRefStructure
from netex.models.route_refs_rel_structure import RouteRefsRelStructure
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.season_enumeration import SeasonEnumeration
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
from netex.models.service_link import ServiceLink
from netex.models.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.time_demand_type import TimeDemandType
from netex.models.time_demand_type_assignment import TimeDemandTypeAssignment
from netex.models.time_demand_type_assignments_in_frame_rel_structure import TimeDemandTypeAssignmentsInFrameRelStructure
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.timeband_ref import TimebandRef
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_link import TimingLink
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_link_ref_structure import TimingLinkRefStructure
from netex.models.timing_links_in_frame_rel_structure import TimingLinksInFrameRelStructure
from netex.models.timing_pattern import TimingPattern
from netex.models.timing_patterns_in_frame_rel_structure import TimingPatternsInFrameRelStructure
from netex.models.timing_point_1 import TimingPoint1
from netex.models.timing_point_in_journey_pattern import TimingPointInJourneyPattern
from netex.models.timing_point_ref import TimingPointRef
from netex.models.timing_point_ref_structure import TimingPointRefStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.timing_points_in_frame_rel_structure import TimingPointsInFrameRelStructure
from netex.models.timing_points_in_journey_pattern_rel_structure import TimingPointsInJourneyPatternRelStructure
from netex.models.vehicle_journey_run_time import VehicleJourneyRunTime
from netex.models.vehicle_journey_run_times_rel_structure import VehicleJourneyRunTimesRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.via_versioned_child_structure import ViaVersionedChildStructure
from netex.models.vias_rel_structure import ViasRelStructure
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
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
                                id='ao:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value='REQUEST',
                            ref='ao:TimetableFrameTIM_23_O'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple timetable frame with two journeys and service calendar, with detailed timings'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='ao:CAL_02',
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
                        ),
                        Codespace(
                            id='hde',
                            xmlns='hde',
                            xmlns_url='http://www.halt.de/',
                            description='Stop data  data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='ao:svf_12',
                            version='1',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24 '
                            ),
                            directions=DirectionsInFrameRelStructure(
                                direction=[
                                    Direction(
                                        id='ao:DR_Westbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Westbound'
                                        )
                                    ),
                                    Direction(
                                        id='ao:DR_Southbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Eastbound'
                                        )
                                    ),
                                ]
                            ),
                            routes=RoutesInFrameRelStructure(
                                route=[
                                    Route1(
                                        id='ao:RT_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley  (Details not GIVEN)'
                                        ),
                                        direction_type=DirectionType(

                                        ),
                                        direction_ref=DirectionRef(
                                            version='any',
                                            ref='ao:DR_Westbound'
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line1(
                                        id='ao:K66',
                                        version='any',
                                        name=MultilingualString(
                                            value='Kocevje - Petrina'
                                        ),
                                        short_name=MultilingualString(
                                            value='K66'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='K66',
                                        routes=RouteRefsRelStructure(
                                            route_ref=[
                                                RouteRef(
                                                    ref='ao:RT_24o'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='ao:DST_Bravo',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        public_code='Bravo'
                                    ),
                                    DestinationDisplay(
                                        id='ao:DST_Charley',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley'
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley G'
                                        ),
                                        public_code='Charley'
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='ao:Briga-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='Briga smer Petrina'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.0000'),
                                            latitude=Decimal('0.1000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='ao:Briga-k',
                                        version='any',
                                        name=MultilingualString(
                                            value='Briga smer  Kocevje'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.0000'),
                                            latitude=Decimal('0.1000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='ao:Banjaloka-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='BANJALOKA smer Petrina'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='ao:Banjaloka-k',
                                        version='any',
                                        name=MultilingualString(
                                            value='BANJALOKA smer Kocevje'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='ao:NovaSela-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='NOVA SELA  smer Kocevje'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='ao:NovaSela-k',
                                        version='any',
                                        name=MultilingualString(
                                            value='NOVA SELA smer Petrina'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='ao:Briga-p_to_Banjaloka-p',
                                        version='any',
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ao:Banjaloka-p_to_NovaSela-p',
                                        version='any',
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:NovaSela-p'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ao:NovaSela-p_to_Banjaloka-p',
                                        version='any',
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:NovaSela-p'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ao:Banjaloka-p_to_Briga-p',
                                        version='any',
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='ao:K66_outbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Kocevje - Petrina'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        journey_patterns=JourneyPatternRefsRelStructure(
                                            journey_pattern_ref=[
                                                ServiceJourneyPatternRef(
                                                    version='any',
                                                    ref='ao:sjp_24o'
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='ao:K66_outbound_24o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p'
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ao:K66_outbound_24o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ao:K66_outbound_24o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:NovaSela-p'
                                                    ),
                                                    for_boarding=False
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            timing_points=TimingPointsInFrameRelStructure(
                                timing_point=[
                                    TimingPoint1(
                                        id='ao:Briga-p_t1',
                                        version='any',
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint1(
                                        id='ao:Briga-p_t2',
                                        version='any',
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint1(
                                        id='ao:Banjaloka-p_t3',
                                        version='any',
                                        location=LocationStructure2(
                                            longitude=Decimal('53.4000'),
                                            latitude=Decimal('0.4000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                ]
                            ),
                            timing_links=TimingLinksInFrameRelStructure(
                                timing_link=[
                                    TimingLink(
                                        id='ao:Briga-p_to_NovaSela-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='Overall timing Alpha  to  Charley reen'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:NovaSela-p'
                                        )
                                    ),
                                    TimingLink(
                                        id='ao:Briga-p_to_Briga-p_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha   t1'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p_t1'
                                        )
                                    ),
                                    TimingLink(
                                        id='ao:Briga-p_t1_to_Briga-p_t2',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha   t1 to After Alpha  t2'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p_t1'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p_t3'
                                        )
                                    ),
                                    TimingLink(
                                        id='ao:Briga-p_t2_to_Banjaloka-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha  t2 to Bravo'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Briga-p_t2'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        )
                                    ),
                                    TimingLink(
                                        id='ao:Banjaloka-p_to_Banjaloka-p_t3',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo to After Bravo t1'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p_t3'
                                        )
                                    ),
                                    TimingLink(
                                        id='ao:Banjaloka-p_t3_to_NovaSela-p',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Bravo t1 to Charley'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='ao:Banjaloka-p_t3'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='ao:NovaSela-p'
                                        )
                                    ),
                                ]
                            ),
                            timing_patterns=TimingPatternsInFrameRelStructure(
                                timing_pattern=[
                                    TimingPattern(
                                        id='ao:tp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Route 24'
                                        ),
                                        route_ref=RouteRefStructure(
                                            version='any',
                                            ref='ao:RT_24o'
                                        ),
                                        direction_type=DirectionType(

                                        ),
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    choice_1=DerivedElement(
                                                        qname='{http://www.netex.org.uk/netex}TimingPointRef',
                                                        value=ScheduledStopPointRefStructure(
                                                            version='any',
                                                            ref='ao:Briga-p'
                                                        ),
                                                        type='{http://www.netex.org.uk/netex}ScheduledStopPointRefStructure'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Briga-p_to_Briga-p_t1'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Briga-p_t1_to_Briga-p_t2'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t2'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Briga-p_t2_to_Banjaloka-p'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_04',
                                                    version='any',
                                                    order=4,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_to_Banjaloka-p_t3'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_t3'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_t3_to_NovaSela-p'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpijp_24o_06',
                                                    version='any',
                                                    order=6,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:NovaSela-p'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                choice=[
                                    ServiceJourneyPattern(
                                        id='ao:sjp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley - All POINTs'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='ao:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        run_times=JourneyPatternRunTimesRelStructure(
                                            journey_pattern_run_time_ref_or_journey_pattern_run_time=[
                                                JourneyPatternRunTime(
                                                    id='ao:jprt_24o1_Briga-p_to_NovaSela-p',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='ao:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_to_NovaSela-p'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='ao:pijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:pijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t1'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:pijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t2'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ao:pijp_24o_04',
                                                    version='any',
                                                    order=4,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ao:tpip_24o_05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_t3'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ao:tpip_24o_06',
                                                    version='any',
                                                    order=6,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:NovaSela-p'
                                                    )
                                                ),
                                            ]
                                        ),
                                        links_in_sequence=LinksInJourneyPatternRelStructure(
                                            service_link_in_journey_pattern_or_timing_link_in_journey_pattern=[
                                                ServiceLinkInJourneyPattern(
                                                    id='ao:lijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    service_link_ref=ServiceLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_to_Banjaloka-p'
                                                    )
                                                ),
                                                ServiceLinkInJourneyPattern(
                                                    id='ao:lijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    service_link_ref=ServiceLinkRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_to_NovaSela-p'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            time_demand_types=TimeDemandTypesInFrameRelStructure(
                                time_demand_type=[
                                    TimeDemandType(
                                        id='ao:tdt_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Normal Day'
                                        ),
                                        run_times=JourneyRunTimesRelStructure(
                                            journey_run_time=[
                                                JourneyRunTime(
                                                    id='ao:tdtr_TD01_Briga-p_to_Briga-p_t1',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_to_Briga-p_t1'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='ao:tdtr_TD01_Briga-p_t1_to_Briga-p_t2',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t1_to_Briga-p_t2'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='ao:tdtr_TD01_Briga-p_t2_to_Banjaloka-p',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_t2_to_Banjaloka-p'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='ao:tdtr_TD01_Banjaloka-p_to_Banjaloka-p_t3',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_to_Banjaloka-p_t3'
                                                    ),
                                                    run_time=XmlDuration("PT18M")
                                                ),
                                                JourneyRunTime(
                                                    id='ao:tdtr_TD01_Banjaloka-p_t3_to_NovaSela-p',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_t3_to_NovaSela-p'
                                                    ),
                                                    run_time=XmlDuration("PT20M")
                                                ),
                                            ]
                                        ),
                                        wait_times=JourneyWaitTimesRelStructure(
                                            journey_wait_time=[
                                                JourneyWaitTime(
                                                    id='ao:tdwt_24o1_Banjaloka-p',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wait at Stop B'
                                                    ),
                                                    choice=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    ),
                                                    wait_time=XmlDuration("PT2M")
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            time_demand_type_assignments=TimeDemandTypeAssignmentsInFrameRelStructure(
                                time_demand_type_assignment=[
                                    TimeDemandTypeAssignment(
                                        id='ao:TA_001',
                                        version='any',
                                        order=1,
                                        time_demand_type_ref=TimeDemandTypeRef(
                                            version='any',
                                            ref='ao:tdt_01'
                                        ),
                                        timeband_ref=TimebandRef(
                                            ref='ao:tdt_01'
                                        ),
                                        group_of_timing_links_ref=GroupOfTimingLinksRef(
                                            version='any',
                                            ref='ao:Bogus'
                                        )
                                    ),
                                ]
                            ),
                            timing_link_groups=GroupOfLinksInFrameRelStructure(
                                group_of_links=[
                                    GroupOfLinks(
                                        id='ao:Bogus',
                                        version='any',
                                        name=MultilingualString(
                                            value='bogus group'
                                        ),
                                        members=LinkRefsRelStructure(
                                            link_ref_or_infrastructure_link_ref_or_link_ref_by_value=[
                                                TimingLinkRef(
                                                    version='any',
                                                    ref='ao:Briga-p_t2_to_Banjaloka-p'
                                                ),
                                                TimingLinkRef(
                                                    version='any',
                                                    ref='ao:Banjaloka-p_to_Banjaloka-p_t3'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='ao:TIM_23_O',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='ao:Cnd001',
                                            version='any',
                                            description=MultilingualString(
                                                value='Sept  to April'
                                            ),
                                            from_date=XmlDateTime(2009, 1, 1, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2009, 12, 31, 0, 0, 0, 0, 0)
                                        ),
                                    ]
                                ),
                            ],
                            version='1',
                            name=MultilingualString(
                                value='Winter timetable for route 66 outbound'
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney1(
                                        id='ao:K66_outbound_01',
                                        version='any',
                                        departure_time=XmlTime(14, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_02-Everyday-NotHoliday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_ChristmasEve'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_ChristmasDay'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_ChristmasDayDisplacement'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_NewYearsEve'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_NewYearsDay'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_2ndJanuary'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_GoodFriday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_EasterSunday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_EasterMonday'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='ao:K66_outbound'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='ao:tdt_01'
                                        ),
                                        block_ref=BlockRef(
                                            value='EXTERNAL',
                                            ref='ao:BLK_24o5'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='ao:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='ao:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='ao:vjrt_sj_24o_01',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='ao:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_to_NovaSela-p'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='ao:K66_outbound_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='ao:Briga-p_to_Briga-p_t1'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='ao:Briga-p_t1'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Briga-p_to_Banjaloka-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='ao:K66_outbound_01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='ao:Banjaloka-p_to_Banjaloka-p_t3'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='ao:Banjaloka-p_t3'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_to_NovaSela-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(14, 30, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    note=MultilingualString(
                                                        value='Arrival at Terminus'
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='ao:K66_outbound_01_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:NovaSela-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 10, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney1(
                                        id='ao:K66_inbound_02',
                                        version='any',
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='ao:DT_01-MF-NotHoliday'
                                                ),
                                            ]
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='ao:tdt_01'
                                        ),
                                        block_ref=BlockRef(
                                            value='EXTERNAL',
                                            ref='ao:BLK_24o8'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='ao:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.INBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='ao:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='ao:vjrt_sj_24o_02',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='ao:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='ao:Briga-p_to_NovaSela-p'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='ao:K66_inbound_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Briga-p'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='ao:Briga-p_to_Briga-p_t1'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='ao:Briga-p_t1'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Briga-p_to_Banjaloka-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 0, 0, 0, 0)
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            ViaVersionedChildStructure(
                                                                destination_display_ref_or_destination_display_view_or_name=DestinationDisplayRef(
                                                                    version='any',
                                                                    ref='ao:DST_Bravo'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    change_of_destination_display=False,
                                                    order=1
                                                ),
                                                Call1(
                                                    id='ao:K66_inbound_02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:Banjaloka-p'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='ao:Banjaloka-p_to_Banjaloka-p_t3'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='ao:Banjaloka-p_t3'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='ao:Banjaloka-p_to_NovaSela-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 30, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='ao:K66_inbound_02_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='ao:NovaSela-p'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(16, 10, 0, 0, 0)
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
                                                    ref='ao:sfs_24o_01'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='ao:sfs_24o_01',
                                        version='any',
                                        provided_by_ref=OrganisationRefStructure(
                                            value='EXTERNAL',
                                            ref='xyz:4567'
                                        ),
                                        assistance_facility_list=AssistanceFacilityList(
                                            value=[
                                                AssistanceFacilityEnumeration.BOARDING_ASSISTANCE,
                                                AssistanceFacilityEnumeration.CONDUCTOR,
                                                AssistanceFacilityEnumeration.WHEELCHAIR_ASSISTANCE,
                                            ]
                                        ),
                                        fare_classes=FareClasses(
                                            value=[
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
                                                NuisanceFacilityEnumeration.NO_SMOKING,
                                            ]
                                        ),
                                        passenger_information_facility_list=PassengerInformationFacilityList(
                                            value=[
                                                PassengerInformationFacilityEnumeration.NEXT_STOP_INDICATOR,
                                                PassengerInformationFacilityEnumeration.REAL_TIME_CONNECTIONS,
                                                PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS,
                                            ]
                                        ),
                                        ticketing_service_facility_list=TicketingServiceFacilityList(
                                            value=[
                                                TicketingServiceFacilityEnumeration.PURCHASE,
                                            ]
                                        ),
                                        luggage_carriage_facility_list=LuggageCarriageFacilityList(
                                            value=[
                                                LuggageCarriageEnumeration.NO_BAGGAGE_STORAGE,
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='ao:CAL_02',
                            version='1',
                            name=MultilingualString(
                                value='Service Calendar Nov to April 2010  (Compact Coding) '
                            ),
                            service_calendar=ServiceCalendar(
                                id='ao:CAL_02',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType1(
                                        id='ao:DT_01-MF-NotHoliday',
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
                                        id='ao:DT_02-Everyday-NotHoliday',
                                        version='any',
                                        name=MultilingualString(
                                            value='Everyday unless a holiday'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.EVERYDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NOT_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_03-WE-NotHoliday',
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
                                    DayType1(
                                        id='ao:DT_04-AA-NotHoliday',
                                        version='any',
                                        name=MultilingualString(
                                            value='Holidays'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.EVERYDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.ANY_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_ChristmasEve',
                                        version='any',
                                        name=MultilingualString(
                                            value='Christmas Ev e  '
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    month_of_year_or_day_of_month_or_day_of_year=PropertyOfDayStructure.DayOfYear(
                                                        value=XmlPeriod("--12-24")
                                                    ),
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.EVE_OF_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_ChristmasDay',
                                        version='any',
                                        name=MultilingualString(
                                            value='Christmas Day  '
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    month_of_year_or_day_of_month_or_day_of_year=PropertyOfDayStructure.DayOfYear(
                                                        value=XmlPeriod("--12-25")
                                                    ),
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NATIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_ChristmasDayDisplacement',
                                        version='any',
                                        name=MultilingualString(
                                            value='Christmas Day Displacement holidday '
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
                                                        HolidayTypeEnumeration.HOLIDAY_DISPLACEMENT_DAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_NewYearsEve',
                                        version='any',
                                        name=MultilingualString(
                                            value="NewYear's Eve  "
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    month_of_year_or_day_of_month_or_day_of_year=PropertyOfDayStructure.DayOfYear(
                                                        value=XmlPeriod("--12-31")
                                                    ),
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.EVE_OF_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_NewYearsDay',
                                        version='any',
                                        name=MultilingualString(
                                            value="NewYear's  Day  "
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    month_of_year_or_day_of_month_or_day_of_year=PropertyOfDayStructure.DayOfYear(
                                                        value=XmlPeriod("--01-01")
                                                    ),
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NATIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_2ndJanuary',
                                        version='any',
                                        name=MultilingualString(
                                            value='2nd January Holiday (Scotland)  '
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    month_of_year_or_day_of_month_or_day_of_year=PropertyOfDayStructure.DayOfYear(
                                                        value=XmlPeriod("--02-01")
                                                    ),
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.REGIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_NewYearsDayDisplacement',
                                        version='any',
                                        name=MultilingualString(
                                            value="NewYear's  Day Displacement holiday "
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
                                                        HolidayTypeEnumeration.HOLIDAY_DISPLACEMENT_DAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_GoodFriday',
                                        version='any',
                                        name=MultilingualString(
                                            value='Good Friday '
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.FRIDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NATIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_EasterSunday',
                                        version='any',
                                        name=MultilingualString(
                                            value='Easter Sunday  '
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.SUNDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NATIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType1(
                                        id='ao:DT_EasterMonday',
                                        version='any',
                                        name=MultilingualString(
                                            value='Easter Monday'
                                        ),
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.MONDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.NATIONAL_HOLIDAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            operating_days=OperatingDaysInFrameRelStructure(
                                operating_day=[
                                    OperatingDay(
                                        id='ao:OD_2010-11-01',
                                        version='any',
                                        calendar_date=XmlDate(2010, 11, 1),
                                        name=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        earliest_time=XmlTime(2, 0, 0, 0),
                                        day_length=XmlDuration("PT24H")
                                    ),
                                    OperatingDay(
                                        id='ao:OD_2011-04-30',
                                        version='any',
                                        calendar_date=XmlDate(2011, 4, 30),
                                        name=MultilingualString(
                                            value='Saturday 2011-04-30'
                                        ),
                                        earliest_time=XmlTime(2, 0, 0, 0),
                                        day_length=XmlDuration("PT24H")
                                    ),
                                ]
                            ),
                            operating_periods=OperatingPeriodsInFrameRelStructure(
                                operating_period_or_uic_operating_period=[
                                    OperatingPeriod1(
                                        id='ao:op_010',
                                        version='any',
                                        name=MultilingualString(
                                            value='WInter 2011'
                                        ),
                                        from_operating_day_ref_or_from_date=OperatingDayRefStructure(
                                            version='any',
                                            ref='ao:OD_2010-11-01'
                                        ),
                                        to_operating_day_ref_or_to_date=OperatingDayRefStructure(
                                            version='any',
                                            ref='ao:OD_2011-04-30'
                                        ),
                                        holiday_type=[
                                            HolidayTypeEnumeration.NOT_HOLIDAY,
                                        ],
                                        season=[
                                            SeasonEnumeration.WINTER,
                                        ]
                                    ),
                                ]
                            ),
                            day_type_assignments=DayTypeAssignmentsInFrameRelStructure(
                                day_type_assignment=[
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        order=1,
                                        choice=OperatingDayRef(
                                            version='any',
                                            ref='ao:OD_2010-11-01'
                                        ),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-02',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-02'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 2),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-03'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 3),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-04',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-04'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 4),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-05',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-05'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 5),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-06',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-06'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 6),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-07',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-07'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 7),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-08',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-08'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 8),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-09',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-09'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 9),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-10',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-10'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 10),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-11',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-11'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 11),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-12',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-12'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 12),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-13',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-13'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 13),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-11-14',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-14'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 14),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-12-24',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-12-24'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 31),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_ChristmasEve'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-12-25',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-12-25 Christams Day'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 25),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_ChristmasDay'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-12-27',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-12-27 (Christjmas Day displacement holiday)'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 27),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_ChristmasDayDisplacement'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2010-12-31',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday 2010-12-31  New Years eve'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 31),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_NewYearsEve'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2011-01-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday  2011-01-01 New Years day'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 1, 1),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_NewYearsDay'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2011-01-03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Satuurday  2011-01-03 New Years day displacement'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 1, 3),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_NewYearsDayDisplacement'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_>2011-04-22',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday 2011-04-22 Good Friday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 22),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_GoodFriday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_>2011-04-24',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2011-04-24 Easter Sunday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 24),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_EasterSunday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_>2011-04-25',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2011-04-25 Easter Monday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 25),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_EasterMonday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2011-04-29',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday2011-04-29'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 29),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='ao:DayAsgn_2011-04-30',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2011-04-30'
                                        ),
                                        order=1,
                                        choice=OperatingDayRef(
                                            version='any',
                                            ref='ao:OD_2011-04-30'
                                        ),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='ao:DT_03-WE-NotHoliday'
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
