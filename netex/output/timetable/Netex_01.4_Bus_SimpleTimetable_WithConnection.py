from decimal import Decimal
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import OrganisationDayType
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.call import Call
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing16_enumeration import CompassBearing16Enumeration
from netex.models.connection import Connection
from netex.models.connection_end_structure import ConnectionEndStructure
from netex.models.connection_ref_structure import ConnectionRefStructure
from netex.models.contact_structure import ContactStructure
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
from netex.models.flexible_line import FlexibleLine
from netex.models.flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from netex.models.flexible_stop_assignment import FlexibleStopAssignment
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.models.flexible_stop_place_version_structure import FlexibleStopPlaceVersionStructure
from netex.models.flexible_stop_places_in_frame_rel_structure import FlexibleStopPlacesInFrameRelStructure
from netex.models.hail_and_ride_area import HailAndRideArea
from netex.models.hail_and_ride_area_ref import HailAndRideAreaRef
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_interchanges_in_frame_rel_structure import JourneyInterchangesInFrameRelStructure
from netex.models.journey_meeting import JourneyMeeting
from netex.models.journey_meeting_ref import JourneyMeetingRef
from netex.models.journey_meeting_views_rel_structure import JourneyMeetingViewsRelStructure
from netex.models.journey_meetings_in_frame_rel_structure import JourneyMeetingsInFrameRelStructure
from netex.models.journey_pattern_ref import JourneyPatternRef
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journey_run_time import JourneyRunTime
from netex.models.journey_run_times_rel_structure import JourneyRunTimesRelStructure
from netex.models.journey_wait_time import JourneyWaitTime
from netex.models.journey_wait_times_rel_structure import JourneyWaitTimesRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line import Line
from netex.models.line_derived_view_structure import LineDerivedViewStructure
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.notice import Notice
from netex.models.notice_assignment import NoticeAssignment
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.notice_ref import NoticeRef
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.operating_period import OperatingPeriod
from netex.models.operating_periods_in_frame_rel_structure import OperatingPeriodsInFrameRelStructure
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.passenger_capacity import PassengerCapacity
from netex.models.passenger_carrying_requirements_view import PassengerCarryingRequirementsView
from netex.models.point_in_sequence_ref_structure import PointInSequenceRefStructure
from netex.models.point_ref_structure import PointRefStructure
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.pos import Pos
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.publicity_channel_enumeration import PublicityChannelEnumeration
from netex.models.resource_frame import ResourceFrame
from netex.models.route import Route
from netex.models.route_ref import RouteRef
from netex.models.route_ref_structure import RouteRefStructure
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.season_enumeration import SeasonEnumeration
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_calendar_ref import ServiceCalendarRef
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey import ServiceJourney
from netex.models.service_journey_interchange import ServiceJourneyInterchange
from netex.models.service_journey_interchange_ref import ServiceJourneyInterchangeRef
from netex.models.service_journey_interchange_view import ServiceJourneyInterchangeView
from netex.models.service_journey_interchanges_rel_structure import ServiceJourneyInterchangesRelStructure
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.serviced_organisation import ServicedOrganisation
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.serviced_organisation_type_enumeration import ServicedOrganisationTypeEnumeration
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.time_demand_type import TimeDemandType
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timetabled_passing_time import TimetabledPassingTime
from netex.models.timetabled_passing_times_rel_structure import TimetabledPassingTimesRelStructure
from netex.models.timing_link import TimingLink
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_link_ref_structure import TimingLinkRefStructure
from netex.models.timing_links_in_frame_rel_structure import TimingLinksInFrameRelStructure
from netex.models.timing_pattern import TimingPattern
from netex.models.timing_patterns_in_frame_rel_structure import TimingPatternsInFrameRelStructure
from netex.models.timing_point import TimingPoint
from netex.models.timing_point_in_journey_pattern import TimingPointInJourneyPattern
from netex.models.timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from netex.models.timing_point_ref import TimingPointRef
from netex.models.timing_point_ref_structure import TimingPointRefStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.timing_points_in_frame_rel_structure import TimingPointsInFrameRelStructure
from netex.models.timing_points_in_journey_pattern_rel_structure import TimingPointsInJourneyPatternRelStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.vehicle_journey_ref_structure import VehicleJourneyRefStructure
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
                        validity_condition=[
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
                    common_frame=[
                        SiteFrame(
                            id='mybus:svf_12',
                            version='1',
                            name=MultilingualString(
                                value='Geometry of HAIL AND RIDE stop for   24 '
                            ),
                            flexible_stop_places=FlexibleStopPlacesInFrameRelStructure(
                                flexible_stop_place=[
                                    FlexibleStopPlace(
                                        id='mybus:fsp_Quebec',
                                        version='any',
                                        name=MultilingualString(
                                            value='Hail and Ride area Zone Quebec'
                                        ),
                                        short_name=MultilingualString(
                                            value='Quebec H and R'
                                        ),
                                        description=[
                                            MultilingualString(
                                                value='Qbece road'
                                            ),
                                        ],
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        12354.78,
                                                        2342.2,
                                                    ]
                                                )
                                            )
                                        ),
                                        areas=FlexibleStopPlaceVersionStructure.Areas(
                                            choice=[
                                                HailAndRideArea(
                                                    id='mybus:HailAndRideArea:hara_Quebec_EW',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Quebec hail and ride area - East bound'
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Quebec HR Eastbound'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    12345.76,
                                                                ]
                                                            ),
                                                            precision=Decimal('12')
                                                        )
                                                    ),
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    bearing_compass=CompassBearing16Enumeration.E,
                                                    start_point_ref=PointRefStructure(
                                                        value='EXTERNAL',
                                                        ref='gis:Point:hara_Quebec_01'
                                                    ),
                                                    end_point_ref=PointRefStructure(
                                                        value='EXTERNAL',
                                                        ref='gis:Point:hara_Quebec_02'
                                                    )
                                                ),
                                                HailAndRideArea(
                                                    id='mybus:HailAndRideArea:hara_Quebec_WE',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Quebec hail and ride area - West bound'
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Quebec HR Westbound'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    12345.76,
                                                                ]
                                                            ),
                                                            precision=Decimal('12')
                                                        )
                                                    ),
                                                    transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    bearing_compass=CompassBearing16Enumeration.W,
                                                    start_point_ref=PointRefStructure(
                                                        value='EXTERNAL',
                                                        ref='gis:Point:hara_Quebec_02'
                                                    ),
                                                    end_point_ref=PointRefStructure(
                                                        value='EXTERNAL',
                                                        ref='gis:Point:hara_Quebec_01'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
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
                                route=[
                                    Route(
                                        id='mybus:RT_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Westbound'
                                        )
                                    ),
                                    Route(
                                        id='mybus:RT_46o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 46 Bravo to Romeo'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Southbound'
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='mybus:LN_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='24'
                                    ),
                                    FlexibleLine(
                                        id='mybus:LN_46',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 46 Park Lane to Quebec'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 46'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='46',
                                        flexible_line_type=FlexibleLineTypeEnumeration.HAIL_AND_RIDE_SECTIONS
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='hde:DST_Bravo',
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
                                        id='hde:DST_Charley',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley'
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley G'
                                        ),
                                        public_code='Charley'
                                    ),
                                    DestinationDisplay(
                                        id='hde:DST_Quebec',
                                        version='any',
                                        name=MultilingualString(
                                            value='Quebec'
                                        ),
                                        short_name=MultilingualString(
                                            value='Quebec'
                                        ),
                                        public_code='Quebec'
                                    ),
                                    DestinationDisplay(
                                        id='hde:DST_Romeo',
                                        version='any',
                                        name=MultilingualString(
                                            value='RomeoRail Station'
                                        ),
                                        short_name=MultilingualString(
                                            value='Romeo'
                                        ),
                                        public_code='Romeo'
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
                                            value='Bravo'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='MARCH'
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
                                            value='Charley'
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
                                            value='KENG'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_021',
                                        version='any',
                                        name=MultilingualString(
                                            value='Romeo'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Romeo'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='ROM'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Quebec Street'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Quebec'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='QBC'
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
                                        id='mybus:SL@SSP_001+SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha & Castle to Bravo'
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
                                        id='mybus:SL@SSP_002+SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo to Charley'
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
                                    ServiceLink(
                                        id='mybus:SL@SSP_002+SSP_021',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravoe  to Quebec'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_021'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybus:SL@SSP_021+SSP_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Quebec to Romeo'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_021'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_022'
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
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o@01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_001+SSP_002'
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o@02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_002+SSP_077'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o@03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    for_boarding=False
                                                ),
                                            ]
                                        )
                                    ),
                                    ServicePattern(
                                        id='hde:svp_46o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo  to Romeo'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='mybus:RT_46o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_46o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_002+SSP_021'
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_46o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_021'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_021+SSP_022'
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='hde:svp_46o',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Can connect to LINE 4'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='hde:sj_24o@02'
                                                                ),
                                                                mark='++3',
                                                                publicity_channel=PublicityChannelEnumeration.ALL,
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_46o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_022'
                                                    ),
                                                    for_boarding=False
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                transfer=[
                                    Connection(
                                        id='mybus:cx_SSP_002+SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Connection to line 46'
                                        ),
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.BUS,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_002'
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.BUS,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_002'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    FlexibleStopAssignment(
                                        id='hde:fsa_SSP_021+fsp_Quebec',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns   Quebec  to flexibleHail and ride section',
                                            lang='en'
                                        ),
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_021'
                                        ),
                                        flexible_stop_place_ref=FlexibleStopPlaceRef(
                                            version='any',
                                            ref='mybus:fsp_Quebec'
                                        ),
                                        flexible_quay_ref=HailAndRideAreaRef(
                                            version='any',
                                            ref='mybus:HailAndRideArea:hara_Quebec_EW'
                                        )
                                    ),
                                ]
                            ),
                            timing_points=TimingPointsInFrameRelStructure(
                                timing_point=[
                                    TimingPoint(
                                        id='mybus:SSP_001_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha & Castle  Point 1'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint(
                                        id='mybus:SSP_001_t2',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha & Castle  Point 2'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint(
                                        id='mybus:SSP_002_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Bravo  Point 1'
                                        ),
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
                                        id='mybus:TL@SSP_001+SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Overall timing Alpha  to  Charley  '
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_077'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_002+SSP_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Overall timing Bravo  to  Quebec  '
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_022'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_001+SSP_001_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha  to  After Alpha  t1'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001_t1'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_001_t1+SSP_001_t2',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha   t1 to After Alpha   t2'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001_t1'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002_t1'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_001_t2+SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha t2 to Bravo'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001_t2'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_002+SSP_002_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo to After Bravo t1'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002_t1'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_002_t1+SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Bravo t1 to Charley'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002_t1'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_077'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_002+SSP_021',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo  to Quebec'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_021'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:TL@SSP_021+SSP_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Quebec to Romeo'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_021'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_022'
                                        )
                                    ),
                                ]
                            ),
                            timing_patterns=TimingPatternsInFrameRelStructure(
                                timing_pattern=[
                                    TimingPattern(
                                        id='hde:tp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Route 24'
                                        ),
                                        route_ref=RouteRefStructure(
                                            version='any',
                                            ref='mybus:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@01',
                                                    version='any',
                                                    order=1,
                                                    choice_1=DerivedElement(
                                                        qname='{http://www.netex.org.uk/netex}TimingPointRef',
                                                        value=ScheduledStopPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_001'
                                                        ),
                                                        type='{http://www.netex.org.uk/netex}ScheduledStopPointRefStructure'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001+SSP_001_t1'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001_t1+SSP_001_t2'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t2'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001_t2+SSP_002'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@04',
                                                    version='any',
                                                    order=4,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_002_t1'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_t1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002_t1+SSP_077'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o@06',
                                                    version='any',
                                                    order=6,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPattern(
                                        id='hde:tp_46o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Route 24'
                                        ),
                                        route_ref=RouteRefStructure(
                                            version='any',
                                            ref='mybus:RT_46o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpip_46o_01',
                                                    version='any',
                                                    order=1,
                                                    choice_1=DerivedElement(
                                                        qname='{http://www.netex.org.uk/netex}TimingPointRef',
                                                        value=ScheduledStopPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_002'
                                                        ),
                                                        type='{http://www.netex.org.uk/netex}ScheduledStopPointRefStructure'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_021'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpip_46o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=DerivedElement(
                                                        qname='{http://www.netex.org.uk/netex}TimingPointRef',
                                                        value=ScheduledStopPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_021'
                                                        ),
                                                        type='{http://www.netex.org.uk/netex}ScheduledStopPointRefStructure'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:TL@SSP_021+SSP_022'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:ScheduledStopPointRefStructure:tpip_46o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_022'
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
                                        id='hde:sjp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='mybus:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        run_times=JourneyPatternRunTimesRelStructure(
                                            journey_pattern_run_time_ref_or_journey_pattern_run_time=[
                                                JourneyPatternRunTime(
                                                    id='mybus:jp_24o1_SSP_001+SSP_077',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001+SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o@01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_001+SSP_002'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o@02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_002+SSP_077'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o@03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:sjp_46o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo to Romeo'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='any',
                                            ref='mybus:RT_46o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        run_times=JourneyPatternRunTimesRelStructure(
                                            journey_pattern_run_time_ref_or_journey_pattern_run_time=[
                                                JourneyPatternRunTime(
                                                    id='mybus:jp_46o1_SSP_002+SSP_021',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_021'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_002+SSP_021'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_021'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SL@SSP_021+SSP_022'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_022'
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
                                        id='mybus:tdt_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Normal Day'
                                        ),
                                        run_times=JourneyRunTimesRelStructure(
                                            journey_run_time=[
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01@SSP_001+SSP_001_t1',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001+SSP_001_t1'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01@SSP_001_t1+SSP_001_t2',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001_t1+SSP_001_t2'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01@SSP_001_t2+SSP_002',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001_t2+SSP_002'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01@SSP_002+SSP_002_t1',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_002_t1'
                                                    ),
                                                    run_time=XmlDuration("PT18M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01@SSP_002_t1+SSP_077',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002_t1+SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT20M")
                                                ),
                                            ]
                                        ),
                                        wait_times=JourneyWaitTimesRelStructure(
                                            journey_wait_time=[
                                                JourneyWaitTime(
                                                    id='mybus:jp_24o1_SSP_002',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wait at Stop B'
                                                    ),
                                                    choice=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    wait_time=XmlDuration("PT2M")
                                                ),
                                            ]
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
                                                day_type_ref_or_day_type=[
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
                            content_validity_conditions=ValidityConditionsRelStructure(
                                choice=[
                                    AvailabilityCondition(
                                        id='mybus:Dth_termtime_Only',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sept  to March'
                                        ),
                                        day_types=DayTypesRelStructure(
                                            day_type_ref_or_day_type=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DotheboysTerm'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id='hde:sj_24o@01',
                                        version='any',
                                        departure_time=XmlTime(14, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:tdt_01'
                                        ),
                                        choice=LineRef(
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
                                                ref='hde:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_24o@01',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001+SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@01_SSP_001',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@01',
                                                        order=1
                                                    ),
                                                    departure_time=XmlTime(14, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@01_SSP_001_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@02',
                                                        order=2
                                                    ),
                                                    departure_time=XmlTime(14, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@01_SSP_001_t2',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@03',
                                                        order=3
                                                    ),
                                                    departure_time=XmlTime(14, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@01_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@02',
                                                        order=2
                                                    ),
                                                    departure_time=XmlTime(14, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@01_SSP_002_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@05',
                                                        order=5
                                                    ),
                                                    departure_time=XmlTime(14, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@01_SSP_077',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@03',
                                                        order=3
                                                    ),
                                                    arrival_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_24o@01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_24o@01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(14, 30, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M"),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingRef(
                                                                    version='any',
                                                                    ref='hde:jm_24o@46o_01'
                                                                ),
                                                            ]
                                                        ),
                                                        interchanges=ServiceJourneyInterchangesRelStructure(
                                                            service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view=[
                                                                ServiceJourneyInterchangeView(
                                                                    service_journey_interchange_ref=ServiceJourneyInterchangeRef(
                                                                        version='any',
                                                                        ref='hde:sji_24o@01+46o_01'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection with 46'
                                                                    ),
                                                                    stay_seated=False,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    connecting_journey_ref_or_connecting_journey_view=VehicleJourneyRefStructure(
                                                                        version='any',
                                                                        ref='hde:sj_46o_01'
                                                                    ),
                                                                    connecting_line_view=LineDerivedViewStructure(
                                                                        id='',
                                                                        line_ref=LineRef(
                                                                            version='any',
                                                                            ref='mybus:LN_46'
                                                                        )
                                                                    ),
                                                                    standard_transfer_time=XmlDuration("PT0M")
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    note=MultilingualString(
                                                        value='Arrival at Terminus'
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_24o@01_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
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
                                    ServiceJourney(
                                        id='hde:sj_24o@02',
                                        version='any',
                                        departure_time=XmlTime(15, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:tdt_01'
                                        ),
                                        choice=LineRef(
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
                                                ref='hde:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_24o@02',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_001+SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@02_SSP_001',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@02',
                                                        order=2
                                                    ),
                                                    departure_time=XmlTime(15, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@02_SSP_001_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@02',
                                                        order=2
                                                    ),
                                                    departure_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@02_SSP_001_t2',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@03',
                                                        order=3
                                                    ),
                                                    departure_time=XmlTime(15, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@02_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@02',
                                                        order=2
                                                    ),
                                                    departure_time=XmlTime(15, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o@02_SSP_002_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o@05',
                                                        order=5
                                                    ),
                                                    departure_time=XmlTime(15, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o@02_SSP_077',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o@03',
                                                        order=3
                                                    ),
                                                    arrival_time=XmlTime(16, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_24o@02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
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
                                                                    ref='hde:DST_Bravo'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_24o@02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 30, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M"),
                                                        journey_meetings=JourneyMeetingViewsRelStructure(
                                                            journey_meeting_ref_or_journey_meeting_view=[
                                                                JourneyMeetingRef(
                                                                    version='any',
                                                                    ref='hde:jm_24o@46o_02'
                                                                ),
                                                            ]
                                                        ),
                                                        interchanges=ServiceJourneyInterchangesRelStructure(
                                                            service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view=[
                                                                ServiceJourneyInterchangeView(
                                                                    service_journey_interchange_ref=ServiceJourneyInterchangeRef(
                                                                        version='any',
                                                                        ref='hde:sji_24o@02+46o_02'
                                                                    ),
                                                                    description=MultilingualString(
                                                                        value='Connection with 46'
                                                                    ),
                                                                    stay_seated=False,
                                                                    planned=True,
                                                                    guaranteed=True,
                                                                    advertised=True,
                                                                    connecting_journey_ref_or_connecting_journey_view=VehicleJourneyRefStructure(
                                                                        version='any',
                                                                        ref='hde:sj_46o_02'
                                                                    ),
                                                                    connecting_line_view=LineDerivedViewStructure(
                                                                        id='',
                                                                        line_ref=LineRef(
                                                                            version='any',
                                                                            ref='mybus:LN_46'
                                                                        )
                                                                    ),
                                                                    standard_transfer_time=XmlDuration("PT0M")
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            '',
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='hde:sj_24o@02_002',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Can connect to LINE 4'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='hde:sj_24o@02'
                                                                ),
                                                                mark='++3',
                                                                publicity_channel=PublicityChannelEnumeration.ALL,
                                                                advertised=True
                                                            ),
                                                        ]
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_24o@02_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
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
                                        )
                                    ),
                                    ServiceJourney(
                                        id='hde:sj_46o_01',
                                        validity_conditions_or_valid_between=[
                                            ValidityConditionsRelStructure(
                                                choice=[
                                                    AvailabilityConditionRef(
                                                        version='any',
                                                        ref='mybus:Dth_termtime_Only'
                                                    ),
                                                ]
                                            ),
                                        ],
                                        version='any',
                                        notice_assignments=NoticeAssignmentsRelStructure(
                                            sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                NoticeAssignment(
                                                    id='hde:vjrt_sj_46o_01',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityConditionRef(
                                                                    version='any',
                                                                    ref='mybus:Dth_termtime_Only'
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Only runs during term times of Dothebys Hall'
                                                    ),
                                                    order=1,
                                                    notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                        version='any',
                                                        ref='hde:sj_46o_01'
                                                    ),
                                                    choice=JourneyPatternRef(
                                                        version='any',
                                                        ref='hde:sjp_46o'
                                                    ),
                                                    mark='++1',
                                                    publicity_channel=PublicityChannelEnumeration.ALL,
                                                    advertised=True
                                                ),
                                            ]
                                        ),
                                        departure_time=XmlTime(15, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_46o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:tdt_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_46'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='mybus:RT_46o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='hde:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_46o_01',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_022'
                                                    ),
                                                    run_time=XmlDuration("PT40M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_01_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_01'
                                                    ),
                                                    departure_time=XmlTime(15, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_01_SSP_021',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_02'
                                                    ),
                                                    departure_time=XmlTime(15, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_01_SSP_022',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_03'
                                                    ),
                                                    arrival_time=XmlTime(15, 40, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_46o_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False,
                                                        interchanges=ServiceJourneyInterchangesRelStructure(
                                                            service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view=[
                                                                ServiceJourneyInterchangeRef(
                                                                    version='any',
                                                                    ref='hde:sji_24o@01+46o_01'
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(16, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_46o_01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_021'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 20, 0, 0, 0)
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='hde:sj_46o_01_002',
                                                                validity_conditions_or_valid_between=[
                                                                    ValidityConditionsRelStructure(
                                                                        choice=[
                                                                            AvailabilityConditionRef(
                                                                                version='any',
                                                                                ref='mybus:Dth_termtime_Only'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ],
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Stops at Q only during term times of Dothebys Hall'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='hde:sj_46_021'
                                                                ),
                                                                choice=JourneyPatternRef(
                                                                    version='any',
                                                                    ref='hde:sjp_46o'
                                                                ),
                                                                start_point_in_pattern_ref=PointInSequenceRefStructure(
                                                                    version='any',
                                                                    ref='hde:pijp_46o_02'
                                                                ),
                                                                end_point_in_pattern_ref=PointInSequenceRefStructure(
                                                                    version='any',
                                                                    ref='hde:pijp_46o_03'
                                                                ),
                                                                mark='++2',
                                                                publicity_channel=PublicityChannelEnumeration.ALL,
                                                                advertised=True
                                                            ),
                                                        ]
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_46o_01_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_022'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(15, 40, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney(
                                        id='hde:sj_46o_02',
                                        version='any',
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_46o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            version='any',
                                            ref='mybus:tdt_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_46'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version='any',
                                                ref='mybus:RT_46o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='hde:DST_Romeo'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_46o_02',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:TL@SSP_002+SSP_022'
                                                    ),
                                                    run_time=XmlDuration("PT40M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_02_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_02'
                                                    ),
                                                    departure_time=XmlTime(16, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_02_SSP_021',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_02'
                                                    ),
                                                    departure_time=XmlTime(16, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_46o_02_SSP_022',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_46o_03'
                                                    ),
                                                    arrival_time=XmlTime(16, 40, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_46o_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False,
                                                        interchanges=ServiceJourneyInterchangesRelStructure(
                                                            service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view=[
                                                                ServiceJourneyInterchangeRef(
                                                                    version='any',
                                                                    ref='hde:sji_24o@02+46o_02'
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 20, 0, 0, 0)
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            ViaVersionedChildStructure(
                                                                destination_display_ref_or_destination_display_view_or_name=DestinationDisplayRef(
                                                                    version='any',
                                                                    ref='hde:DST_Bravo'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_46o_02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_021'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(16, 20, 0, 0, 0)
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            '',
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='hde:vjrt_sj_46o_02',
                                                                validity_conditions_or_valid_between=[
                                                                    ValidityConditionsRelStructure(
                                                                        choice=[
                                                                            AvailabilityConditionRef(
                                                                                version='any',
                                                                                ref='mybus:Dth_termtime_Only'
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ],
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Stops at Q only during term times of Dothebys Hall'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='hde:sj_46_021'
                                                                ),
                                                                choice=JourneyPatternRef(
                                                                    version='any',
                                                                    ref='hde:sjp_46o'
                                                                ),
                                                                start_point_in_pattern_ref=PointInSequenceRefStructure(
                                                                    version='any',
                                                                    ref='hde:pijp_46o_02'
                                                                ),
                                                                end_point_in_pattern_ref=PointInSequenceRefStructure(
                                                                    version='any',
                                                                    ref='hde:pijp_46o_03'
                                                                ),
                                                                mark='++2',
                                                                publicity_channel=PublicityChannelEnumeration.ALL,
                                                                advertised=True
                                                            ),
                                                        ]
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:sj_46o_02_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_022'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(16, 40, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view=PassengerCarryingRequirementsView(
                                            passenger_capacity=PassengerCapacity(
                                                id='PC1',
                                                version='any',
                                                seating_capacity=22,
                                                standing_capacity=44,
                                                special_place_capacity=2,
                                                pushchair_capacity=6,
                                                wheelchair_place_capacity=1
                                            ),
                                            low_floor=True,
                                            has_lift_or_ramp=True
                                        )
                                    ),
                                ]
                            ),
                            notices=NoticesInFrameRelStructure(
                                notice=[
                                    Notice(
                                        id='hde:sj_46o_01',
                                        version='any',
                                        text=MultilingualString(
                                            value='Only runs during termtimes of Dothebys Hall'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='hde:sj_46_01',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.MOBILE,
                                                    variant_text=MultilingualString(
                                                        value='Termtimes Only'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Notice(
                                        id='hde:sj_46_021',
                                        version='any',
                                        text=MultilingualString(
                                            value='Stops at Q only during term times of Dothebys Hall'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='hde:sj_46_01',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.MOBILE,
                                                    variant_text=MultilingualString(
                                                        value='Termtimes Only'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Notice(
                                        id='hde:sj_24o@02',
                                        version='any',
                                        text=MultilingualString(
                                            value='Can connect to LINE 4'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='hde:sj_24o@02_01',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='At this stop it is possible to change to line 4 for Dotheboys academy and Stop R'
                                                    )
                                                ),
                                                DeliveryVariant(
                                                    id='hde:sj_24o@02_02',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.MOBILE,
                                                    variant_text=MultilingualString(
                                                        value='X Line 4'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            journey_meetings=JourneyMeetingsInFrameRelStructure(
                                journey_meeting=[
                                    JourneyMeeting(
                                        id='hde:jm_24o@46o_01',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_24o@01'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_46o_01'
                                        ),
                                        description=MultilingualString(
                                            value='Transfer to route 46'
                                        ),
                                        earliest_time=XmlTime(14, 30, 0, 0, 0),
                                        latest_time=XmlTime(14, 35, 0, 0, 0)
                                    ),
                                    JourneyMeeting(
                                        id='hde:jm_24o@46o_02',
                                        version='any',
                                        at_stop_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_24o@01'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_46o_01'
                                        ),
                                        description=MultilingualString(
                                            value='Transfer to route 46'
                                        ),
                                        earliest_time=XmlTime(15, 30, 0, 0, 0),
                                        latest_time=XmlTime(15, 35, 0, 0, 0)
                                    ),
                                ]
                            ),
                            journey_interchanges=JourneyInterchangesInFrameRelStructure(
                                service_journey_pattern_interchange_or_service_journey_interchange=[
                                    ServiceJourneyInterchange(
                                        id='hde:sji_24o@01+46o_01',
                                        version='any',
                                        description=MultilingualString(
                                            value='15:00  Change for Romeo\t '
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version='any',
                                            ref='mybus:cx_SSP_002+SSP_002'
                                        ),
                                        stay_seated=False,
                                        planned=True,
                                        guaranteed=False,
                                        advertised=True,
                                        controlled=False,
                                        standard_wait_time=XmlDuration("PT30M"),
                                        maximum_wait_time=XmlDuration("PT35M"),
                                        standard_transfer_time=XmlDuration("PT1M"),
                                        minimum_transfer_time=XmlDuration("PT1M"),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_24o@01'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_46o_01'
                                        )
                                    ),
                                    ServiceJourneyInterchange(
                                        id='hde:sji_24o@02+46o_02',
                                        version='any',
                                        description=MultilingualString(
                                            value='16:00  Change for Romeo\t '
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version='any',
                                            ref='mybus:cx_SSP_002+SSP_002'
                                        ),
                                        stay_seated=False,
                                        planned=True,
                                        guaranteed=False,
                                        advertised=True,
                                        controlled=False,
                                        standard_wait_time=XmlDuration("PT30M"),
                                        maximum_wait_time=XmlDuration("PT35M"),
                                        standard_transfer_time=XmlDuration("PT1M"),
                                        minimum_transfer_time=XmlDuration("PT1M"),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        from_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_24o@02'
                                        ),
                                        to_journey_ref=VehicleJourneyRefStructure(
                                            version='any',
                                            ref='hde:sj_46o_02'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='hde:CAL_02',
                            version='1',
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
                                day_type=[
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
                                    OrganisationDayType(
                                        id='hde:DotheboysTerm',
                                        version='any',
                                        is_service_day=True,
                                        serviced_organisation_ref=ServicedOrganisationRef(
                                            version='1',
                                            ref='dth:Dotheboys'
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
                                        choice=XmlDate(2010, 11, 1),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 2),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 3),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 4),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 5),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 6),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 7),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 8),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 9),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 10),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 11),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 12),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 13),
                                        day_type_ref=DayTypeRef(
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
                                        choice=XmlDate(2010, 11, 14),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NH'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='hde:RS_01',
                            version='any',
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    ServicedOrganisation(
                                        id='dth:Dotheboys',
                                        version='1',
                                        name=MultilingualString(
                                            value='Dotheboys Hall,'
                                        ),
                                        short_name=MultilingualString(
                                            value='Dotheboys'
                                        ),
                                        contact_details=ContactStructure(
                                            contact_person=MultilingualString(
                                                value='Wackford Squeers  '
                                            ),
                                            email='enquiries@Dotheboys.ac.uk'
                                        ),
                                        service_calendar_ref=ServiceCalendarRef(
                                            version='any',
                                            ref='dth:DTH_01'
                                        ),
                                        serviced_organisation_type=ServicedOrganisationTypeEnumeration.SCHOOL
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='dth:DTH_01',
                            version='1',
                            name=MultilingualString(
                                value='Dotheboys Hall School Terms   '
                            ),
                            service_calendar=ServiceCalendar(
                                id='dth:DTH_01',
                                version='any',
                                from_date=XmlDate(2010, 9, 1),
                                to_date=XmlDate(2011, 8, 1)
                            ),
                            operating_periods=OperatingPeriodsInFrameRelStructure(
                                operating_period_or_uic_operating_period=[
                                    OperatingPeriod(
                                        id='dth:OP_01',
                                        version='1',
                                        name=MultilingualString(
                                            value='Autumn term '
                                        ),
                                        from_operating_day_ref_or_from_date=XmlDateTime(2010, 9, 1, 0, 0, 0),
                                        to_operating_day_ref_or_to_date=XmlDateTime(2010, 9, 24, 0, 0, 0),
                                        holiday_type=[
                                            HolidayTypeEnumeration.SCHOOL_DAY,
                                        ],
                                        season=[
                                            SeasonEnumeration.AUTUMN,
                                        ]
                                    ),
                                    OperatingPeriod(
                                        id='dth:OP_02',
                                        version='1',
                                        name=MultilingualString(
                                            value='Spring term '
                                        ),
                                        from_operating_day_ref_or_from_date=XmlDateTime(2011, 1, 1, 0, 0, 0),
                                        to_operating_day_ref_or_to_date=XmlDateTime(2010, 4, 1, 0, 0, 0),
                                        holiday_type=[
                                            HolidayTypeEnumeration.SCHOOL_DAY,
                                        ],
                                        season=[
                                            SeasonEnumeration.SPRING,
                                        ]
                                    ),
                                    OperatingPeriod(
                                        id='dth:OP_03',
                                        version='1',
                                        name=MultilingualString(
                                            value='Summer term '
                                        ),
                                        from_operating_day_ref_or_from_date=XmlDateTime(2011, 4, 11, 0, 0, 0),
                                        to_operating_day_ref_or_to_date=XmlDateTime(2010, 8, 1, 0, 0, 0),
                                        holiday_type=[
                                            HolidayTypeEnumeration.SCHOOL_DAY,
                                        ],
                                        season=[
                                            SeasonEnumeration.SUMMER,
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
)
