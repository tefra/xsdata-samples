from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.call import Call
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.day_type_assignments_in_frame_rel_structure import DayTypeAssignmentsInFrameRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.delivery_variant import DeliveryVariant
from netex.models.delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from netex.models.delivery_variants_rel_structure import DeliveryVariantsRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.direction import Direction
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.notice import Notice
from netex.models.notice_assignment_view import NoticeAssignmentView
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.notice_ref import NoticeRef
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.pos import Pos
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay import Quay
from netex.models.quay_assignment_view import QuayAssignmentView
from netex.models.quay_ref import QuayRef
from netex.models.quay_ref_structure import QuayRefStructure
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.road_address import RoadAddress
from netex.models.route import Route
from netex.models.route_ref import RouteRef
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey import ServiceJourney
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.service_link import ServiceLink
from netex.models.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_links_in_journey_pattern_rel_structure import ServiceLinksInJourneyPatternRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.time_demand_type import TimeDemandType
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        choice=[
                            AvailabilityCondition(
                                id='hde:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value='REQUEST',
                            ref='hde:TimetableFrameTIM_23_O'
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
                id='hde:CAL_02',
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
                        Codespace(
                            id='dth',
                            xmlns='dth',
                            xmlns_url='http://www.dothebyshall.edu/timetable',
                            description='Timetable     data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                frames=FramesRelStructure(
                    choice=[
                        ServiceFrame(
                            id='mybus:svf_12',
                            version='1',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24 '
                            ),
                            directions=DirectionsInFrameRelStructure(
                                direction=[
                                    Direction(
                                        id='mybus:DR_Westbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Westbound'
                                        )
                                    ),
                                    Direction(
                                        id='mybus:DR_Southbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Eastbound'
                                        )
                                    ),
                                ]
                            ),
                            routes=RoutesInFrameRelStructure(
                                flexible_route_or_route=[
                                    Route(
                                        id='mybus:RT_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley Green'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Westbound'
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                flexible_line_or_line=[
                                    Line(
                                        id='mybus:LN_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='24'
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='mybus:DST_Charley',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Green'
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
                                        id='mybus:SSP_001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha & Castle'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.0000'),
                                            latitude=Decimal('0.1000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Alpha'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='EANDC'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAVO'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Green'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Charley'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='CHAS'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='mybus:SSP_001_to_SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha & Castle to Bravo Arch'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybus:SSP_002_to_SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch to Charley Green'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_077'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='hde:svp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='mybus:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        journey_patterns=JourneyPatternRefsRelStructure(
                                            choice=[
                                                ServiceJourneyPatternRef(
                                                    version='any',
                                                    ref='hde:sjp_24o'
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    for_boarding=False
                                                ),
                                            ]
                                        ),
                                        links_in_sequence=ServiceLinksInJourneyPatternRelStructure(
                                            service_link_in_journey_pattern=[
                                                ServiceLinkInJourneyPattern(
                                                    id='hde:slijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    service_link_ref=ServiceLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
                                                    )
                                                ),
                                                ServiceLinkInJourneyPattern(
                                                    id='hde:slijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    service_link_ref=ServiceLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_077'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                choice=[
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_001_to_SP57001A_Q4',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns   Alpha to physical stop -   quay  4',
                                            lang='en'
                                        ),
                                        order=1,
                                        boarding_use=True,
                                        alighting_use=True,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_001'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP57001A'
                                        ),
                                        quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP57001A_4'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_002_to_SP57002B_Q1a',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Arrivals  at Bravo to Eastbound Quay',
                                            lang='en'
                                        ),
                                        order=1,
                                        boarding_use=False,
                                        alighting_use=True,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP57002B'
                                        ),
                                        quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP57002B_1a'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_002_to_SP57002B_Q1b',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Departures at Bravo to Eastbound Quay',
                                            lang='en'
                                        ),
                                        order=2,
                                        boarding_use=True,
                                        alighting_use=False,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP57002B'
                                        ),
                                        quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP57002B_1b'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_077_to_SP57003C',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns   to  Charley - no quay specified ',
                                            lang='en'
                                        ),
                                        order=1,
                                        boarding_use=True,
                                        alighting_use=True,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_077'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP57003C'
                                        )
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                choice=[
                                    ServiceJourneyPattern(
                                        id='hde:sjp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley  '
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='mybus:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        run_times=JourneyPatternRunTimesRelStructure(
                                            journey_pattern_run_time_ref_or_journey_pattern_run_time=[
                                                JourneyPatternRunTime(
                                                    id='mybus:jprt_24o1_SSP_001_to_SSP_077',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:td_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        ref='none'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_02',
                                                    version='any',
                                                    order=5,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_03',
                                                    version='any',
                                                    order=10,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
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
                                        id='mybus:td_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Normal Day'
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='hde:TIM_23_O',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='hde:Cnd001',
                                            version='any',
                                            description=MultilingualString(
                                                value='Sept  to March'
                                            ),
                                            from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 3, 31, 0, 0, 0, 0, 0),
                                            day_types=DayTypesRelStructure(
                                                choice=[
                                                    DayTypeRef(
                                                        version='any',
                                                        ref='hde:DT_01-MF-NH'
                                                    ),
                                                    DayTypeRef(
                                                        version='any',
                                                        ref='hde:DT_03-WE-NH'
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            version='1',
                            name=MultilingualString(
                                value='Winter timetable for route 23 outbound'
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id='hde:sj_24o_01',
                                        version='any',
                                        departure_time=XmlTime(14, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:td_01'
                                        ),
                                        choice_1=LineRef(
                                            version='any',
                                            ref='mybus:LN_24'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='mybus:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='mybus:DST_Charley'
                                            )
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id='hde:sj_24o_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False,
                                                        choice=QuayAssignmentView(
                                                            vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref=PassengerStopAssignmentRef(
                                                                version='any',
                                                                ref='hde:psa_SSP_001_to_SP57001A_Q4',
                                                                order=1
                                                            ),
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='mybus:SP57001A'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='mybus:Q_SP57001A_4'
                                                            ),
                                                            quay_name=MultilingualString(
                                                                value='Alpha Platform 4'
                                                            ),
                                                            label='Quay 4'
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 20, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_24o_01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(14, 30, 0, 0, 0),
                                                        choice=QuayAssignmentView(
                                                            vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref=PassengerStopAssignmentRef(
                                                                version='any',
                                                                ref='hde:psa_SSP_002_to_SP57002B_Q1a',
                                                                order=1
                                                            ),
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='mybus:SP57002B'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='mybus:Q_SP57002B_1a'
                                                            ),
                                                            label='Bravo 1A'
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M"),
                                                        choice=QuayAssignmentView(
                                                            vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref=PassengerStopAssignmentRef(
                                                                version='any',
                                                                ref='hde:psa_SSP_002_to_SP57002B_Q1b',
                                                                order=2
                                                            ),
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='mybus:SP57002B'
                                                            ),
                                                            quay_ref=QuayRefStructure(
                                                                version='any',
                                                                ref='mybus:Q_SP57002B_1b'
                                                            ),
                                                            label='Bravo 1B'
                                                        )
                                                    ),
                                                    note=MultilingualString(
                                                        value='Arrival at Terminus'
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_24o_01_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 10, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False,
                                                        choice=QuayAssignmentView(
                                                            vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref=PassengerStopAssignmentRef(
                                                                version='any',
                                                                ref='hde:psa_SSP_077_to_SP57003C',
                                                                order=1
                                                            ),
                                                            stop_place_ref=StopPlaceRef(
                                                                version='any',
                                                                ref='mybus:SP57003C'
                                                            ),
                                                            label='C1'
                                                        )
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney(
                                        id='hde:sj_24o_02',
                                        version='any',
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:td_01'
                                        ),
                                        choice_1=LineRef(
                                            version='any',
                                            ref='mybus:LN_24'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='mybus:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='mybus:DST_Charley'
                                            )
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id='hde:sj_24o_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 20, 0, 0, 0),
                                                        choice=PassengerStopAssignmentRef(
                                                            version='any',
                                                            ref='hde:psa_SSP_001_to_SP57001A_Q4',
                                                            order=1
                                                        )
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_24o_02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 30, 0, 0, 0),
                                                        choice=PassengerStopAssignmentRef(
                                                            version='any',
                                                            ref='hde:psa_SSP_002_to_SP57002B_Q1a',
                                                            order=1
                                                        ),
                                                        notice_assignments=NoticeAssignmentsRelStructure(
                                                            sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                                NoticeAssignmentView(
                                                                    id='hde:sj_24o_02_002_01',
                                                                    notice_ref=NoticeRef(
                                                                        version='any',
                                                                        ref='hde:sj_24o_02'
                                                                    ),
                                                                    text=MultilingualString(
                                                                        value='Can connect to LINE 4'
                                                                    ),
                                                                    order=1
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M"),
                                                        choice=PassengerStopAssignmentRef(
                                                            version='any',
                                                            ref='hde:psa_SSP_002_to_SP57002B_Q1b',
                                                            order=2
                                                        )
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_24o_02_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(16, 10, 0, 0, 0),
                                                        choice=PassengerStopAssignmentRef(
                                                            version='any',
                                                            ref='hde:psa_SSP_077_to_SP57003C',
                                                            order=1
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            notices=NoticesInFrameRelStructure(
                                notice=[
                                    Notice(
                                        id='hde:sj_24o_02',
                                        version='any',
                                        text=MultilingualString(
                                            value='foot note text'
                                        ),
                                        can_be_advertised=True,
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='hde:sj_24o_02_01',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='mobile foot note text'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='mybus:infraf002',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            changed=XmlDateTime(2010, 5, 22, 10, 30, 51, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='024',
                            derived_from_version_ref_attribute='0023',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    value='EXTERNAL',
                                    ref='mybus:RS_10'
                                )
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='mybus:SP57001A',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha and Castle'
                                        ),
                                        short_name=MultilingualString(
                                            value='Alpha '
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        transport_mode=VehicleModeEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP57001A_4',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Alpha Quay 4  '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop A is terminus serves both directions'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    label=MultilingualString(
                                                        value='Quay 4'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='mybus:SP57002B',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Road (SW19)'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='mybus:RAd_SP57002B_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Bravo Road'
                                            )
                                        ),
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP57002B_1a',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo  Eastbound  Arrivals(Quay 1)'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Ba  is paired with Stop Bb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Bravo 1A'
                                                    ),
                                                    public_code='1-3456a ',
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP57002B_1b',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo  Eastbound Departures (Quay 1b)'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Ba  is paired with Stop Bb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4317482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Bravo 1B'
                                                    ),
                                                    public_code='1-3456b ',
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP57002B_2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo  Westbound (Quay 2)'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Ba  is paired with Stop Bb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop Bb'
                                                    ),
                                                    public_code='1-3457 ',
                                                    compass_octant=CompassBearing8Enumeration.N,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='mybus:SP57003C',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Crescent'
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley C'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='mybus:RAd_SP57003C_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Foo Road'
                                            )
                                        ),
                                        transport_mode=VehicleModeEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP57003C_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Charley  Eaestbound (Quay 1)'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='StopCa  is paired with Stop Cb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value=' Ca'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.NE,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP57003C_2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Charley  Westbound (Quay 2)'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Cb  is paired with Stop Ca '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='  C1'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.SE,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='mybus:SP57004D',
                                        version='any',
                                        name=MultilingualString(
                                            value='Delta Avenue'
                                        ),
                                        short_name=MultilingualString(
                                            value='Delta'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='mybus:RAd_SP57004D_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Bar Road'
                                            )
                                        ),
                                        transport_mode=VehicleModeEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP57004D_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Delta  Eastbound (Quay 1)'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop D'
                                                    ),
                                                    public_code='1-3455 ',
                                                    compass_octant=CompassBearing8Enumeration.W,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='hde:CAL_02',
                            version='any',
                            name=MultilingualString(
                                value='Service Calendar Nov 2010 ALTERNATE MORE COMPACT Coding  '
                            ),
                            service_calendar=ServiceCalendar(
                                id='hde:CAL_02',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                fare_day_type_or_organisation_day_type_or_day_type=[
                                    DayType(
                                        id='hde:DT_01-MF-NH',
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
                                    DayType(
                                        id='hde:DT_02-AA-NH',
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
                                    DayType(
                                        id='hde:DT_03-WE-NH',
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
                                    DayType(
                                        id='hde:DT_04-AA-NH',
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
                                ]
                            ),
                            day_type_assignments=DayTypeAssignmentsInFrameRelStructure(
                                day_type_assignment=[
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 1),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-02',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-02'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 2),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-03'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 3),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-04',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-04'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 4),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-05',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-05'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 5),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-06',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-06'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 6),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-07',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-07'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 7),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-08',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-08'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 8),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-09',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-09'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 9),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-10',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-10'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 10),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-11',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-11'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 11),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-12',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-12'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 12),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-113',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-13'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 13),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-14',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-14'
                                        ),
                                        order=1,
                                        operating_period_ref_or_operating_day_ref_or_date=XmlDate(2010, 11, 14),
                                        fare_day_type_ref_or_day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NH'
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
