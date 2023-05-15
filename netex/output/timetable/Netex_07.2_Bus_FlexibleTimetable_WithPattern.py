from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import TimebandVersionedChildStructure
from netex.models.alternative_texts_rel_structure import TimebandsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.authority_ref_structure import AuthorityRefStructure
from netex.models.block_ref import BlockRef
from netex.models.booking_access_enumeration import BookingAccessEnumeration
from netex.models.booking_method_enumeration import BookingMethodEnumeration
from netex.models.bus_submode_enumeration import BusSubmodeEnumeration
from netex.models.call import Call
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.contained_availability_conditions_rel_structure import ContainedAvailabilityConditionsRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
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
from netex.models.exterior import Exterior
from netex.models.flexible_area import FlexibleArea
from netex.models.flexible_line import FlexibleLine
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from netex.models.flexible_link_properties import FlexibleLinkProperties
from netex.models.flexible_link_properties_rel_structure import FlexibleLinkPropertiesRelStructure
from netex.models.flexible_point_properties import FlexiblePointProperties
from netex.models.flexible_point_properties_rel_structure import FlexiblePointPropertiesRelStructure
from netex.models.flexible_service_properties import FlexibleServiceProperties
from netex.models.flexible_stop_assignment import FlexibleStopAssignment
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.models.flexible_stop_places_in_frame_rel_structure import FlexibleStopPlacesInFrameRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_accounting import JourneyAccounting
from netex.models.journey_accounting_enumeration import JourneyAccountingEnumeration
from netex.models.journey_accountings_rel_structure import JourneyAccountingsRelStructure
from netex.models.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line_ref import LineRef
from netex.models.line_view import LineView
from netex.models.linear_ring import LinearRing
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.links_in_journey_pattern_rel_structure import LinksInJourneyPatternRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.notice import Notice
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.onward_timing_link_view import OnwardTimingLinkView
from netex.models.point_on_route import PointOnRoute
from netex.models.point_on_route_ref import PointOnRouteRef
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.points_on_route_rel_structure import PointsOnRouteRelStructure
from netex.models.polygon import Polygon
from netex.models.pos import Pos
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.route import Route
from netex.models.route_link import RouteLink
from netex.models.route_link_ref import RouteLinkRef
from netex.models.route_links_in_frame_rel_structure import RouteLinksInFrameRelStructure
from netex.models.route_point import RoutePoint
from netex.models.route_point_ref import RoutePointRef
from netex.models.route_point_ref_structure import RoutePointRefStructure
from netex.models.route_points_in_frame_rel_structure import RoutePointsInFrameRelStructure
from netex.models.route_ref import RouteRef
from netex.models.route_ref_structure import RouteRefStructure
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
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_links_in_journey_pattern_rel_structure import ServiceLinksInJourneyPatternRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
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
from netex.models.transport_submode import TransportSubmode
from netex.models.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
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
    participant_ref="SYS001",
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref="SYS002",
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        choice=[
                            AvailabilityCondition(
                                id="hde:CAL_02",
                                version="any",
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value="REQUEST",
                            ref="hde:TimetableFrameTIM_23_O"
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value="Example  of simple flexible timetable  , zones and sequence   &#10;&#9;&#10;1. OVERVIEW&#10;============&#10;&#10;   The servIce has one zones  T.&#10; &#9;All journeys go via stop A and B.&#10; &#9;&#10;&#9;There are on demand services between specified start and end time.&#10;&#9;&#9;&#10;&#9;&#9;   9 to 5 Monday to Friday.&#10;&#9;   Booking starts 8 to 12: 1 to 4:30&#10; &#9;&#9;&#9;&#9;&#9;&#9;&#9;&#9;&#9;&#9;&#10;  There are two journesy scheduled for And B at specific times.&#10;&#10;==================================&#10;2. DETAILS&#10;&#10; FLEXIBLE LINE  mybus:FL_24&#10;&#9;&#9;has booking  and references one flexible stop places&#10;&#10;FLEXIBLE STOP PLACES defines  geometry of the FLEIXBLE zones  &#10;&#9;&#9;a)   FLEXIBLE STOP PLAcE: mybus:fsp_Tau&#9;&#9;&#9;&#9;&#9; &#10;&#9;&#9;&#9;&#9; with a two FLEXIBLE STOP AREAs     &#9;&#10;&#9;&#9;&#9;&#9;&#9; :mybus:fa_Tau_01&#10;&#9;&#9;&#9; &#9; :mybus:fa_Tau_02&#10;&#10;There are just two    SERVICE JOURNEYs in the timetable  for LINE 24&#10;&#10;     (i)  SERVICE JOURNEY hde:sj_24o@01         &#10;             Departs 14:00             &#10;             has FLEXIBLE SERVICE PROPERTIES&#10;&#10;     (ii)  SERVICE JOURNEY hde:sj_24o@02     &#10;             Departs 15:00            &#10;          has FLEXIBLE SERVICE PROPERTIES&#10;&#10;SCHEDULED STOP POINTs&#10;&#9;    A)   mybus:ssp_001  Alpha&#9;&#9;&#9;Fixed&#9;&#9;&#9; &#10;&#9;&#9;B)  mybus:ssp_002   Bravo&#9;&#9;&#9;Fixed &#9;&#9;&#9;&#9; &#10;&#9;&#9;C)  mybus:ssp_077&#9; Charley=Tau    Zone&#10;&#10;SERVICE LINKS&#10;&#9;&#9;&#9;SERVICE LINK :&#9;A&#9;&#9; - B     &#9;mybus:SSP_001+SSP_002  &#10;&#9;&#9;&#9;SERVICE LINK :&#9;B&#9;&#9; - C&#9;&#9;mybus:SSP_002+SSP_077&#10;&#10;&#10;There is a single SERVICE  PATTERN  has  three STOP POINTs IN JOURNEY PATTERN referencing the  three SCHEDULED STOP POINTs  &#10; which are connected by two      SERVICE LINKs   .&#10; &#10; SERVICE PATTERN:  ServicePattern:svp_24o  follows  SERVICE JOURNEY PATTERN:  ServiceJourneyPattern:sjp_24o&#10;&#9;1 A STOP POINT IN JOURNEY PATTERN&#9; hde:spip_24o@01&#10;&#9;&#9;SCHEDULED STOP POINT:  A  mybus:SSP_001  &#10;&#9;&#9;SERVICE LINK :&#9;A&#9;&#9; - B     &#9;mybus:SSP_001+SSP_002 &#10;&#9;2 B  STOP POINT IN JOURNEY PATTERN &#9; hde:spip_24o@02&#10;&#9;&#9;SCHEDULED STOP POINT: B     mybus:SSP_002&#10;&#9;&#9;SERVICE LINK :&#9;B&#9;&#9; - C&#9;&#9;mybus:SSP_002+SSP_077&#10;&#9;3 C  STOP POINT IN JOURNEY PATTERN &#9; hde:spip_24o@03&#10;&#9;&#9;SCHEDULED STOP POINT:   C   mybus:SSP_077&#10; &#10; &#10;   &#10;A COMPOSITE FRAME is used to group the component FRAMEs&#10; &#10;   - It has a VALIDITY CONDITION  that specifies it is valid from Sept to Matrch.&#10;&#10;&#9;&#9;A SERVICE  FRAME is used to contain the STOP POINT  elements   LINE, etc.&#10;&#9;&#9;A TIMETABLE FRAME is used to contain  the SERVICE JOURNEY   elements &#10; &#10;&#9;&#9;&#9; a SERVICE CALENDAR FRAMEb&#9;A SERVICE CALENDAR FRAME is used to contain the DAY TYPEs etc.&#10;&#10;The Calendar is shown coded as&#10;      Compact : OPERATING DAYs are assumed for each calendar date within the period of the calendar.&#10;&#9;&#10;&#9;"
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id="hde:CAL_02",
                version="1",
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id="mybus",
                            xmlns="mybus",
                            xmlns_url="http://www.mybuses.eu/stuff",
                            description="My buses"
                        ),
                        Codespace(
                            id="hde",
                            xmlns="hde",
                            xmlns_url="http://www.halt.de/",
                            description="Stop data  data"
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref="mybus"
                    )
                ),
                frames=FramesRelStructure(
                    choice=[
                        SiteFrame(
                            id="mybus:svf_24",
                            version="1",
                            name=MultilingualString(
                                value="Stops for Winter timetable for Flexible Route 12 "
                            ),
                            flexible_stop_places=FlexibleStopPlacesInFrameRelStructure(
                                flexible_stop_place=[
                                    FlexibleStopPlace(
                                        id="mybus:fsp_Tau",
                                        version="any",
                                        name=MultilingualString(
                                            value="Flexible Zone Tau"
                                        ),
                                        short_name=MultilingualString(
                                            value="Tau"
                                        ),
                                        description=[
                                            MultilingualString(
                                                value="Area around Beta ville"
                                            ),
                                        ],
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal("53.0000"),
                                                latitude=Decimal("0.1000")
                                            )
                                        ),
                                        areas=FlexibleStopPlaceVersionStructure.Areas(
                                            choice=[
                                                FlexibleArea(
                                                    id="mybus:fa_Tau_01",
                                                    version="any",
                                                    name=MultilingualString(
                                                        value="ZONE Tau    Area 1 -   "
                                                    ),
                                                    short_name=MultilingualString(
                                                        value="Sigma 1"
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    12345.76,
                                                                ]
                                                            ),
                                                            precision=Decimal("12")
                                                        )
                                                    ),
                                                    polygon=Polygon(
                                                        id="b1234",
                                                        srs_name="wgs84",
                                                        exterior=Exterior(
                                                            linear_ring=LinearRing(
                                                                pos_or_point_property_or_pos_list=[
                                                                    Pos(
                                                                        value=[
                                                                            12355.78,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12355.76,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.88,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.18,
                                                                        ]
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    transport_mode=VehicleModeEnumeration.BUS,
                                                    boarding_use=True,
                                                    alighting_use=True
                                                ),
                                                FlexibleArea(
                                                    id="mybus:fa_Tau_02",
                                                    version="any",
                                                    name=MultilingualString(
                                                        value="ZONE Tau    Area 2 -   "
                                                    ),
                                                    short_name=MultilingualString(
                                                        value="Sigma 2"
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    12345.76,
                                                                ]
                                                            ),
                                                            precision=Decimal("12")
                                                        )
                                                    ),
                                                    polygon=Polygon(
                                                        id="c1234",
                                                        srs_name="wgs84",
                                                        exterior=Exterior(
                                                            linear_ring=LinearRing(
                                                                pos_or_point_property_or_pos_list=[
                                                                    Pos(
                                                                        value=[
                                                                            12356.77,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12357.75,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12357.88,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.18,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12354.18,
                                                                        ]
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    transport_mode=VehicleModeEnumeration.BUS,
                                                    boarding_use=True,
                                                    alighting_use=True
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id="mybus:svf_24",
                            version="1",
                            name=MultilingualString(
                                value="Stops for Winter timetable for route 24 "
                            ),
                            directions=DirectionsInFrameRelStructure(
                                direction=[
                                    Direction(
                                        id="mybus:DR_Westbound",
                                        version="any",
                                        name=MultilingualString(
                                            value="To Alpha"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Southbound",
                                        version="any",
                                        name=MultilingualString(
                                            value="To Tau "
                                        )
                                    ),
                                ]
                            ),
                            route_points=RoutePointsInFrameRelStructure(
                                route_point=[
                                    RoutePoint(
                                        id="mybus:RP_001",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha  "
                                        )
                                    ),
                                    RoutePoint(
                                        id="mybus:RP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="Beta  "
                                        )
                                    ),
                                    RoutePoint(
                                        id="mybus:RP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="Charley  "
                                        )
                                    ),
                                ]
                            ),
                            route_links=RouteLinksInFrameRelStructure(
                                route_link=[
                                    RouteLink(
                                        id="mybus:RP_001+RP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha to Bravo"
                                        ),
                                        from_point_ref=RoutePointRefStructure(
                                            version="any",
                                            ref="mybus:RP_001"
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version="any",
                                            ref="mybus:RP_002"
                                        )
                                    ),
                                    RouteLink(
                                        id="mybus:RP_002+RP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="Bravo to "
                                        ),
                                        from_point_ref=RoutePointRefStructure(
                                            version="any",
                                            ref="mybus:RP_002"
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version="any",
                                            ref="mybus:RP_077"
                                        )
                                    ),
                                ]
                            ),
                            routes=RoutesInFrameRelStructure(
                                flexible_route_or_route=[
                                    Route(
                                        id="mybus:RT_24o",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 24 Alpha to Charley   "
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref=DirectionRef(
                                            version="any",
                                            ref="mybus:DR_Westbound"
                                        ),
                                        points_in_sequence=PointsOnRouteRelStructure(
                                            point_on_route=[
                                                PointOnRoute(
                                                    id="mybus:RT_24o@01",
                                                    version="any",
                                                    order=1,
                                                    choice_1=RoutePointRef(
                                                        version="any",
                                                        ref="mybus:RP_001"
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id="mybus:RT_24o@02",
                                                    version="any",
                                                    order=2,
                                                    choice_1=RoutePointRef(
                                                        version="any",
                                                        ref="mybus:RP_002"
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id="mybus:RT_24o@03",
                                                    version="any",
                                                    order=3,
                                                    choice_1=RoutePointRef(
                                                        version="any",
                                                        ref="mybus:RP_077"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            flexible_point_properties=FlexiblePointPropertiesRelStructure(
                                flexible_point_properties=[
                                    FlexiblePointProperties(
                                        id="mybus:RP_077",
                                        version="any",
                                        choice=PointOnRouteRef(
                                            version="any",
                                            ref="mybus:RT_24o@03",
                                            order=3
                                        ),
                                        point_standing_for_azone=True
                                    ),
                                ]
                            ),
                            flexible_link_properties=FlexibleLinkPropertiesRelStructure(
                                flexible_link_properties=[
                                    FlexibleLinkProperties(
                                        id="mybus:RP_002+RP_077",
                                        version="any",
                                        choice=RouteLinkRef(
                                            version="any",
                                            ref="mybus:RP_002+RP_077"
                                        ),
                                        may_be_skipped=True,
                                        on_main_route=False,
                                        unscheduled_path=True
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                flexible_line_or_line=[
                                    FlexibleLine(
                                        id="mybus:FL_24",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 24 Alpha  to Tau FLEXIBLE SERVICE "
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 24"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        transport_submode=TransportSubmode(
                                            choice=BusSubmodeEnumeration.DEMAND_AND_RESPONSE_BUS
                                        ),
                                        public_code="24",
                                        flexible_line_type=FlexibleLineTypeEnumeration.MIXED_FLEXIBLE_AND_FIXED,
                                        booking_access=BookingAccessEnumeration.PUBLIC,
                                        latest_booking_time=XmlTime(16, 30, 0, 0),
                                        minimum_booking_period=XmlDuration("PT30M")
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id="mybus:DST_Alpha",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha"
                                        ),
                                        short_name=MultilingualString(
                                            value="Alpha"
                                        ),
                                        public_code="Alpha"
                                    ),
                                    DestinationDisplay(
                                        id="mybus:DST_Charley",
                                        version="any",
                                        name=MultilingualString(
                                            value="Charley"
                                        ),
                                        short_name=MultilingualString(
                                            value="Charley G"
                                        ),
                                        public_code="Charley"
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id="mybus:SSP_001",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha  "
                                        ),
                                        short_name=MultilingualString(
                                            value="Alpha"
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value="ALPH"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="Bravo Street"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.2000"),
                                            latitude=Decimal("0.2000")
                                        ),
                                        short_name=MultilingualString(
                                            value="Bravo"
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value="BRAV"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="Tau"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.3000"),
                                            latitude=Decimal("0.3000")
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value="CHAS"
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
                                        id="mybus:SSP_001+SSP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha to Bravo"
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001"
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002"
                                        )
                                    ),
                                    ServiceLink(
                                        id="mybus:SSP_002+SSP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="Bravo to "
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002"
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_077"
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id="hde:svp_24o",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha to Charley"
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version="any",
                                            ref="mybus:RT_24o"
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        journey_patterns=JourneyPatternRefsRelStructure(
                                            choice=[
                                                ServiceJourneyPatternRef(
                                                    version="any",
                                                    ref="hde:sjp_24o"
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id="hde:spijp_24o@01",
                                                    version="any",
                                                    order=1,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        value="Redundant Information!",
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_002"
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id="hde:spijp_24o@02",
                                                    version="any",
                                                    order=2,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        value="Redundant Information!",
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_077"
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id="hde:spijp_24o@03",
                                                    version="any",
                                                    order=3,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    ),
                                                    for_boarding=False
                                                ),
                                            ]
                                        ),
                                        links_in_sequence=ServiceLinksInJourneyPatternRelStructure(
                                            service_link_in_journey_pattern=[
                                                ServiceLinkInJourneyPattern(
                                                    id="hde:slijp_24o@01",
                                                    version="any",
                                                    order=1,
                                                    service_link_ref=ServiceLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_002"
                                                    )
                                                ),
                                                ServiceLinkInJourneyPattern(
                                                    id="hde:slijp_24o@02",
                                                    version="any",
                                                    order=2,
                                                    service_link_ref=ServiceLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_077"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                choice=[
                                    FlexibleStopAssignment(
                                        id="hde:fsa_SSP_077+fsp_Sigma",
                                        version="any",
                                        description=MultilingualString(
                                            value="Assigns Charley to Tau Zone ",
                                            lang="en"
                                        ),
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version="any",
                                            ref="mybus:SSP_077"
                                        ),
                                        flexible_stop_place_ref=FlexibleStopPlaceRef(
                                            version="any",
                                            ref="mybus:fsp_Tau"
                                        )
                                    ),
                                ]
                            ),
                            timing_points=TimingPointsInFrameRelStructure(
                                timing_point=[
                                    TimingPoint(
                                        id="mybus:SSP_001_t1",
                                        version="any",
                                        name=MultilingualString(
                                            value="Between  Alpha   and Bravo Point 1"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.2000"),
                                            latitude=Decimal("0.2000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint(
                                        id="mybus:SSP_001_t2",
                                        version="any",
                                        name=MultilingualString(
                                            value="Between  Alpha   and Bravo  Point 2"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.3000"),
                                            latitude=Decimal("0.3000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint(
                                        id="mybus:SSP_002_t3",
                                        version="any",
                                        name=MultilingualString(
                                            value="Between  Bravo   and Charley  Point 1"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.4000"),
                                            latitude=Decimal("0.4000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                ]
                            ),
                            timing_links=TimingLinksInFrameRelStructure(
                                timing_link=[
                                    TimingLink(
                                        id="mybus:SSP_001+SSP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="Overall timing Alpha  to  Charley reen"
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001"
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_077"
                                        )
                                    ),
                                    TimingLink(
                                        id="mybus:SSP_001+SSP_001_t1",
                                        version="any",
                                        name=MultilingualString(
                                            value="After Alpha   t1"
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001"
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001_t1"
                                        )
                                    ),
                                    TimingLink(
                                        id="mybus:SSP_001_t1+SSP_001_t2",
                                        version="any",
                                        name=MultilingualString(
                                            value="After Alpha   t1 to After Alpha  t2"
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001_t1"
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002_t3"
                                        )
                                    ),
                                    TimingLink(
                                        id="mybus:SSP_001_t2+SSP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="After Alpha  t2 to Bravo"
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_001_t2"
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002"
                                        )
                                    ),
                                    TimingLink(
                                        id="mybus:SSP_002+SSP_002_t3",
                                        version="any",
                                        name=MultilingualString(
                                            value="Bravo to After Bravo t1"
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002"
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002_t3"
                                        )
                                    ),
                                    TimingLink(
                                        id="mybus:SSP_002_t3+SSP_077",
                                        version="any",
                                        name=MultilingualString(
                                            value="After Bravo t1 to Charley"
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_002_t3"
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version="any",
                                            ref="mybus:SSP_077"
                                        )
                                    ),
                                ]
                            ),
                            timing_patterns=TimingPatternsInFrameRelStructure(
                                timing_pattern=[
                                    TimingPattern(
                                        id="hde:tp_24o",
                                        version="any",
                                        name=MultilingualString(
                                            value="Route 24"
                                        ),
                                        route_ref=RouteRefStructure(
                                            version="any",
                                            ref="mybus:RT_24o"
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@01",
                                                    version="any",
                                                    order=1,
                                                    choice_1=DerivedElement(
                                                        qname="{http://www.netex.org.uk/netex}TimingPointRef",
                                                        value=ScheduledStopPointRefStructure(
                                                            version="any",
                                                            ref="mybus:SSP_001"
                                                        ),
                                                        type="{http://www.netex.org.uk/netex}ScheduledStopPointRefStructure"
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_001_t1"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@02",
                                                    version="any",
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001_t1"
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_001_t1+SSP_001_t2"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@03",
                                                    version="any",
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001_t2"
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_001_t2+SSP_002"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@04",
                                                    version="any",
                                                    order=4,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_002_t3"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@05",
                                                    version="any",
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002_t3"
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_002_t3+SSP_077"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpijp_24o@06",
                                                    version="any",
                                                    order=6,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
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
                                        id="hde:sjp_24o",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha to Charley"
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version="any",
                                            ref="mybus:RT_24o"
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        run_times=JourneyPatternRunTimesRelStructure(
                                            journey_pattern_run_time_ref_or_journey_pattern_run_time=[
                                                JourneyPatternRunTime(
                                                    id="mybus:jprt_24o1_SSP_001+SSP_077",
                                                    version="any",
                                                    timing_link_ref=TimingLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_077"
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id="hde:pijp_24o@01",
                                                    version="any",
                                                    order=1,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:pijp_24o@02",
                                                    version="any",
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001_t1"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:pijp_24o@03",
                                                    version="any",
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001_t2"
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id="hde:pijp_24o@04",
                                                    version="any",
                                                    order=4,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id="hde:tpip_24o@05",
                                                    version="any",
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002_t3"
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id="hde:tpip_24o@06",
                                                    version="any",
                                                    order=6,
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    )
                                                ),
                                            ]
                                        ),
                                        links_in_sequence=LinksInJourneyPatternRelStructure(
                                            service_link_in_journey_pattern_or_timing_link_in_journey_pattern=[
                                                ServiceLinkInJourneyPattern(
                                                    id="hde:lijp_24o@01",
                                                    version="any",
                                                    order=1,
                                                    service_link_ref=ServiceLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_002"
                                                    )
                                                ),
                                                ServiceLinkInJourneyPattern(
                                                    id="hde:lijp_24o@02",
                                                    version="any",
                                                    order=2,
                                                    service_link_ref=ServiceLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_077"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id="hde:TIM_02",
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id="hde:AC_runs_02",
                                            version="any",
                                            description=MultilingualString(
                                                value="Operating  times for service"
                                            ),
                                            is_available=True,
                                            day_types=DayTypesRelStructure(
                                                choice=[
                                                    DayTypeRef(
                                                        version="any",
                                                        ref="hde:DT_01-MF-NotHoliday"
                                                    ),
                                                ]
                                            ),
                                            timebands=TimebandsRelStructure(
                                                timeband_ref_or_timeband=[
                                                    TimebandVersionedChildStructure(
                                                        id="hde:AC_runs_01",
                                                        version="any",
                                                        start_time=XmlTime(19, 0, 0, 0),
                                                        end_time_or_day_offset_or_duration=[
                                                            XmlTime(17, 0, 0, 0),
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            version="1",
                            name=MultilingualString(
                                value="TimetableNov to Jan 2011   "
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            line_view=LineView(
                                flexible_line_ref_or_line_ref=FlexibleLineRef(
                                    version="any",
                                    ref="mybus:FL_24"
                                )
                            ),
                            booking_times=ContainedAvailabilityConditionsRelStructure(
                                availability_condition=[
                                    AvailabilityCondition(
                                        id="hde:AC_booking_01",
                                        version="any",
                                        description=MultilingualString(
                                            value="Booking times for service"
                                        ),
                                        is_available=True,
                                        day_types=DayTypesRelStructure(
                                            choice=[
                                                DayTypeRef(
                                                    version="any",
                                                    ref="hde:DT_01-MF-NotHoliday"
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id="hde:AC_booking_01",
                                                    version="any",
                                                    start_time=XmlTime(8, 30, 0, 0),
                                                    end_time_or_day_offset_or_duration=[
                                                        XmlTime(12, 0, 0, 0),
                                                    ]
                                                ),
                                                TimebandVersionedChildStructure(
                                                    id="hde:AC_booking_02",
                                                    version="any",
                                                    start_time=XmlTime(13, 0, 0, 0),
                                                    end_time_or_day_offset_or_duration=[
                                                        XmlTime(16, 30, 0, 0),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id="hde:sj_24o@01",
                                        version="any",
                                        journey_accountings=JourneyAccountingsRelStructure(
                                            journey_accounting_ref_or_journey_accounting=[
                                                JourneyAccounting(
                                                    id="mytim:sj_24o@01_01",
                                                    version="any",
                                                    order=1,
                                                    organisation_ref=AuthorityRefStructure(
                                                        value="EXTERNAL",
                                                        ref="txc:xshire"
                                                    ),
                                                    accounting_type=JourneyAccountingEnumeration.SUBSIDY,
                                                    partial=[
                                                        False,
                                                    ],
                                                    distance=Decimal("20")
                                                ),
                                                JourneyAccounting(
                                                    id="mytim:sj_24o@01_02",
                                                    version="any",
                                                    order=2,
                                                    organisation_ref=AuthorityRefStructure(
                                                        value="EXTERNAL",
                                                        ref="txc:xshire"
                                                    ),
                                                    accounting_type=JourneyAccountingEnumeration.CONTRACT,
                                                    partial=[
                                                        False,
                                                    ],
                                                    distance=Decimal("20")
                                                ),
                                            ]
                                        ),
                                        departure_time=XmlTime(14, 20, 0, 0, 0),
                                        choice=ServicePatternRef(
                                            version="any",
                                            ref="hde:svp_24o"
                                        ),
                                        train_block_ref_or_block_ref=BlockRef(
                                            value="EXTERNAL",
                                            ref="mybus:BLK_24o5"
                                        ),
                                        choice_1=LineRef(
                                            version="any",
                                            ref="mybus:FL_24"
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version="any",
                                                ref="mybus:RT_24o"
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version="any",
                                                ref="mybus:DST_Charley"
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id="hde:vjrt_sj_24o@01",
                                                    name=MultilingualString(
                                                        value="Overall run time"
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_077"
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@01_SSP_001",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@01"
                                                    ),
                                                    departure_time=XmlTime(14, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@01_SSP_001_t1",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@02"
                                                    ),
                                                    departure_time=XmlTime(14, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@01_SSP_001_t2",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@03"
                                                    ),
                                                    departure_time=XmlTime(14, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@01_SSP_002",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@02"
                                                    ),
                                                    departure_time=XmlTime(14, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@01_SSP_002_t3",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@05"
                                                    ),
                                                    departure_time=XmlTime(14, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@01_SSP_077",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@03"
                                                    ),
                                                    arrival_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id="hde:sj_24o@01_001",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version="any",
                                                            ref="mybus:SSP_001+SSP_001_t1"
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version="any",
                                                            ref="mybus:SSP_001_t1"
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_002"
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
                                                    id="hde:sj_24o@01_002",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version="any",
                                                            ref="mybus:SSP_002+SSP_002_t3"
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version="any",
                                                            ref="mybus:SSP_002_t3"
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_077"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(14, 30, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 32, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    note=MultilingualString(
                                                        value="Arrival at Terminus"
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id="hde:sj_24o@01_003",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
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
                                        ),
                                        flexible_service_properties_ref_or_flexible_service_properties=FlexibleServiceProperties(
                                            id="hde:FlexibleServiceProperties:sj_24o@02",
                                            version="1",
                                            type_of_flexible_service_ref=TypeOfFlexibleServiceRef(
                                                version="any",
                                                ref="myfs"
                                            ),
                                            booking_methods=[
                                                BookingMethodEnumeration.ONLINE,
                                                BookingMethodEnumeration.CALL_OFFICE,
                                            ],
                                            booking_access=BookingAccessEnumeration.PUBLIC,
                                            latest_booking_time=XmlTime(16, 0, 0, 0, 0),
                                            minimum_booking_period=XmlDuration("PT2H")
                                        )
                                    ),
                                    ServiceJourney(
                                        id="hde:sj_24o@02",
                                        version="any",
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version="any",
                                                    ref="hde:DT_01-MF-NotHoliday"
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            version="any",
                                            ref="hde:svp_24o"
                                        ),
                                        train_block_ref_or_block_ref=BlockRef(
                                            value="EXTERNAL",
                                            ref="mybus:BLK_24o8"
                                        ),
                                        choice_1=LineRef(
                                            version="any",
                                            ref="mybus:FL_24"
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                version="any",
                                                ref="mybus:RT_24o"
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version="any",
                                                ref="mybus:DST_Charley"
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id="hde:vjrt_sj_24o@02",
                                                    name=MultilingualString(
                                                        value="Overall run time"
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_077"
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@02_SSP_001",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@01"
                                                    ),
                                                    departure_time=XmlTime(15, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@02_SSP_001_t1",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@02"
                                                    ),
                                                    departure_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@02_SSP_001_t2",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@03"
                                                    ),
                                                    departure_time=XmlTime(15, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@02_SSP_002",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@02"
                                                    ),
                                                    departure_time=XmlTime(15, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="hde:tpt_24o@02_SSP_002_t3",
                                                    version="any",
                                                    choice_1=TimingPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:tpijp_24o@05"
                                                    ),
                                                    departure_time=XmlTime(15, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id="mybus:tpt_24o@02_SSP_077",
                                                    version="any",
                                                    choice_1=StopPointInJourneyPatternRef(
                                                        version="any",
                                                        ref="hde:spijp_24o@03"
                                                    ),
                                                    arrival_time=XmlTime(16, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id="hde:sj_24o@02_001",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version="any",
                                                            ref="mybus:SSP_001+SSP_001_t1"
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version="any",
                                                            ref="mybus:SSP_001_t1"
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_001+SSP_002"
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
                                                                    version="any",
                                                                    ref="mybus:DST_Alpha"
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    order=1
                                                ),
                                                Call(
                                                    id="hde:sj_24o@02_002",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version="any",
                                                            ref="mybus:SSP_002+SSP_002_t3"
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version="any",
                                                            ref="mybus:SSP_002_t3"
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version="any",
                                                        ref="mybus:SSP_002+SSP_077"
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
                                                Call(
                                                    id="hde:sj_24o@02_003",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        flexible_service_properties_ref_or_flexible_service_properties=FlexibleServiceProperties(
                                            id="hde:FlexibleServiceProperties:sj_24o@02",
                                            version="1",
                                            type_of_flexible_service_ref=TypeOfFlexibleServiceRef(
                                                version="any",
                                                ref="myfs"
                                            ),
                                            booking_methods=[
                                                BookingMethodEnumeration.ONLINE,
                                                BookingMethodEnumeration.CALL_OFFICE,
                                            ],
                                            booking_access=BookingAccessEnumeration.PUBLIC,
                                            latest_booking_time=XmlTime(16, 0, 0, 0, 0),
                                            minimum_booking_period=XmlDuration("PT2H"),
                                            booking_note=MultilingualString(
                                                value="Some text"
                                            )
                                        )
                                    ),
                                ]
                            ),
                            notices=NoticesInFrameRelStructure(
                                notice=[
                                    Notice(
                                        id="hde:sj_24o@02_BN",
                                        version="1",
                                        text=MultilingualString(
                                            value="&#10;&#9;&#9;&#9;&#9;&#9;&#9;&#9;&#9;&#9;Bookings must be made at elast two houyrs begfore"
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id="hde:CAL_02",
                            version="1",
                            name=MultilingualString(
                                value="Service Calendar Nov to Jan 2011   "
                            ),
                            service_calendar=ServiceCalendar(
                                id="hde:CAL_02",
                                version="any",
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2011, 1, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                fare_day_type_or_organisation_day_type_or_day_type=[
                                    DayType(
                                        id="hde:DT_01-MF-NotHoliday",
                                        version="any",
                                        name=MultilingualString(
                                            value="Weekdays unless a holiday"
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
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
