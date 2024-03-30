from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.arrival_structure import ArrivalStructure
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.models.assistance_facility_list import AssistanceFacilityList
from netex.models.authority_ref_structure import AuthorityRefStructure
from netex.models.block_ref import BlockRef
from netex.models.call import Call
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
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
from netex.models.direction_type import DirectionType
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import OperatingDay
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.fare_classes import FareClasses
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.group_of_links import GroupOfLinks
from netex.models.group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from netex.models.group_of_timing_links_ref import GroupOfTimingLinksRef
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_accounting import JourneyAccounting
from netex.models.journey_accounting_enumeration import JourneyAccountingEnumeration
from netex.models.journey_accountings_rel_structure import JourneyAccountingsRelStructure
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
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.link_refs_rel_structure import LinkRefsRelStructure
from netex.models.links_in_journey_pattern_rel_structure import LinksInJourneyPatternRelStructure
from netex.models.locale import Locale
from netex.models.location_structure_2 import LocationStructure2
from netex.models.luggage_carriage_enumeration import LuggageCarriageEnumeration
from netex.models.luggage_carriage_facility_list import LuggageCarriageFacilityList
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration
from netex.models.mobility_facility_list import MobilityFacilityList
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.notice import Notice
from netex.models.notice_assignment import NoticeAssignment
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.notice_ref import NoticeRef
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.nuisance_facility_list import NuisanceFacilityList
from netex.models.onward_timing_link_view import OnwardTimingLinkView
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operating_day_ref_structure import OperatingDayRefStructure
from netex.models.operating_days_in_frame_rel_structure import OperatingDaysInFrameRelStructure
from netex.models.operating_period import OperatingPeriod
from netex.models.operating_periods_in_frame_rel_structure import OperatingPeriodsInFrameRelStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.passenger_information_facility_list import PassengerInformationFacilityList
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.presentation_structure import PresentationStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.property_of_day_structure import PropertyOfDayStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.route import Route
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
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.service_facility_set import ServiceFacilitySet
from netex.models.service_facility_set_ref import ServiceFacilitySetRef
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
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
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
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
from netex.models.vehicle_journey_run_time import VehicleJourneyRunTime
from netex.models.vehicle_journey_run_times_rel_structure import VehicleJourneyRunTimesRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
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
                                id='request',
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
        value='Example  of simple timetable frame with two journeys and service calendar, with detailed timings\n\t\n1. OVERVIEW\n============\n\n   The route has just  three stops         A - B  - C   \n   \n     with three intremediate timing points\n \n   The route has just  three stops         A - t1 - t2 - B  - t3 - C    \n \n\tThere are just two  SERVICE JOURNEYs   in a single DIRECTION \n\n    hde:sj_24o_01   at 14:20   outbound\n    hde:sj_24o_02   at 15:20   outbound\n \nAnd the timetable is thus\n\n\t\t\tsj_24o_01  \t\t\t\t sj_24o_02\n\n\tA\td\t\t14:00\t\t\t\t15:00\n\tB\ta\t\t14:30\t\t\t\t15:30         \n\tB\td\t\t14:32\t    \t\t15:32 \n\tC\ta\t\t15:10\t\t\t\t16:10\n\t\t\t\t\t\t\t\t\t\t\nIn this example we include both  detailed TIMING and JOURNEY PATTERN data as well as the\nSERVICE JOURNEY with  CALLs.\n\nThe CALLs are in effect derived from the other  data and could be omitted\n \nJourney  sj_24o_01   runs every day that is not a holiday and on Christmas day, New years day, Goodfriday and Easter monday\nJourney  sj_24o_01   runs every monday to fridays that are not a holiday\n\n==================================\n2. DETAILS\n\nThere are just two SERVICE JOURNEYs in the timetable  for LINE 24\n\n     (i)  SERVICE JOURNEY hde:sj_24o_01         \n             Departs 14:00   on         \n             DAY TYPEs  \n\t\t\t\t\t\thde:DT_02-Everyday-NotHoliday  \n\t\t\t\t\t\thde:DT_ChristmasEve \n\t\t\t\t\t\thde:DT_ChristmasDay \n\t\t\t\t\t\thde:DT_ChristmasDayDisplacement \n\t\t\t\t\t\thde:DT_NewYearsEve \n\t\t\t\t\t\thde:DT_NewYearsDay \n\t\t\t\t\t\thde:DT_2ndJanuary \n\t\t\t\t\t\thde:DT_NewYearsDayDisplacement \n\t\t\t\t\t\thde:DT_GoodFriday \n\t\t\t\t\t\thde:DT_EasterSunday \n\t\t\t\t\t\thde:DT_EasterMonday                     \n             \n\n     (ii)  SERVICE JOURNEY hde:sj_24o_02     \n             Departs 15:00   on        \n                DAY TYPEs   \n\t\t\t\t\t\thde:DT_01-MF-NotHoliday \n             Connects with LINE 4 at stop B \n\n\nSCHEDULED STOP POINTs\n\t    A)  mybus:ssp_001  Alpha\t\t\t\t\t\t \n\t\tB)  mybus:ssp_002   Bravo\t\t\t\t\t\t\t \n\t\tC)  mybus:ssp_077\t Charley\n\nSERVICE LINKS\n\t\t\tSERVICE LINK :\tA\t\t - B     \tmybus:SSP_001_to_SSP_002  \n\t\t\tSERVICE LINK :\tB\t\t - C\t\tmybus:SSP_002_to_SSP_077\n\n\nThere is a single SERVICE  PATTERN  has  three STOP POINTs IN JOURNEY PATTERN referencing the  three SCHEDULED STOP POINTs  \n which are connected by two      SERVICE LINKs   .\n \n SERVICE PATTERN:  ServicePattern:svp_24o  follows  SERVICE JOURNEY PATTERN:  ServiceJourneyPattern:sjp_24o\n\t1 A STOP POINT IN JOURNEY PATTERN\t hde:spip_24o_01\n\t\tSCHEDULED STOP POINT:  A  mybus:SSP_001  \n\t\tSERVICE LINK :\tA\t\t - B     \tmybus:SSP_001_to_SSP_002 \n\t2 B  STOP POINT IN JOURNEY PATTERN \t hde:spip_24o_02\n\t\tSCHEDULED STOP POINT: B     mybus:SSP_002\n\t\tSERVICE LINK :\tB\t\t - C\t\tmybus:SSP_002_to_SSP_077\n\t3 C  STOP POINT IN JOURNEY PATTERN \t hde:spip_24o_03\n\t\tSCHEDULED STOP POINT:   C   mybus:SSP_077\n\n\n    The TIMING PATTERN has   three intermediate TIMING POINTs which are not SCHEDULED STOP POINTs, as well as the three     SCHEDULED STOP POINTs\n\t\t\t  A - a_t1 - a_t2 - B  - b_t3 - C   \n\ntiming points\n     TIMING POINT: mybus:SSP_001_t1\n\t TIMING POINT: mybus:SSP_001_t2\n     TIMING POINT: mybus:SSP_002_t3\n\ntiming links\n\t\tTIMING LINK :\tA\t\t - \ta_t1     \tmybus:SSP_001_to_SSP_001_t1\n\t\tTIMING LINK :\t a_t1\t-\ta_t2\t\tmybus:SSP_001_t1_to_SSP_001_t2\n\t\tTIMING LINK :\ta_t2\t-\tB\t\t \tmybus:SSP_001_t2_to_SSP_002\n\t\tTIMING LINK :\tA\t\t - b_t3\t\t\tmybus:SSP_002_to_SSP_002_t3\n\t\tTIMING LINK :\tb_t3\t\t- \tC\t\t\tmybus:SSP_002_t3_to_SSP_077\n\n   There is a single TIME DEMAND TYPE and one set of RUN TIMES \n \t01\t\t\t02\t\t \t \n\tA\td\t\t14:00\t \t15:00\t\t    \n\t  t1\t\t\t\t\t\t\t\t\t\t+10m\tRUN TIME \n\t  t2\t\t\t\t\t\t\t\t\t\t+10m\tRUN TIME \n\tB\ta\t\t14:30\t\t15:30 \t\t+10m\tRUN TIME  \n\tB\td\t\t14:32\t...\t15:32 \t\t+2m\t \tWAIT TIME\n\t  t1\t\t\t\t\t\t\t\t\t\t+180m\t RUN TIME .\n\tC\td\t\t15:10\t\t16:10\t\t.+20m\tRUN TIME  \n\t\t\t\t\t\t\t\t\t\t\t\t+70m\t JOURNEY PATTERN RUN TIME  \t\n\n\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_001_to_SSP_077\t   70M\n\n    The TIMING PATTERN  has  thus six POINTs IN TIMING PATTERN, referencing the  TIMING POINTs \n\tconnected by five   TIMING LINKs    \n\n TIMING PATTERN:  TimingPattern:tp_24o\n\t1.TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_01\n\t\t\tTIMING POINT:  A   mybus:SSP_001\n\t\t\tTIMING LINK :\tA\t\t - \ta_t1     \tmybus:SSP_001_to_SSP_001_t1\n\t\t\t\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_001_to_SSP_001_t1  \t 4M \n\t\t Depart: 14:20, 15 20\n\n    2. TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_02\n\t\t\tTIMING POINT: mybus:SSP_001_t1\n\t\t\tTIMING LINK :\t a_t1\t-\ta_t2\t\tmybus:SSP_001_t1_to_SSP_001_t2\n\t\t\t\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_001_t1_to_SSP_001_t2   10M\n\n\t3. TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_03\n\t\t\tTIMING POINT: mybus:SSP_001_t2\n\t\t\tTIMING LINK :\ta_t2\t-\tB\t\t\t\tmybus:SSP_001_t2_to_SSP_002\n\t\t\t\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_001_t1_to_SSP_002\t   10M\n\n\t4. TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_04\n\t\t\tTIMING POINT:  B   mybus:SSP_002\n \t\t\t\tJOURNEY WAIT TIME  mybus:tdtr_TD01_SSP_002\t   2M\n\t\t\tTIMING LINK :\tA\t\t - b_t3\t\t\tmybus:SSP_002_to_SSP_002_t3    \n\t\t\t\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_002_to_SSP_002_t3  \t 18M\n\t\t\t  Arrive14:30, 15 30 \n\t\t\t  Depart14:32, 15 32\n\n    5. TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_05\n\t\t\tTIMING POINT: mybus:SSP_002_t3\n\t\t\tTIMING LINK :\tb_t3\t\t- \tC\t\t\tmybus:SSP_002_t3_to_SSP_077\n\t\t\t\tJOURNEY RUN TIME  mybus:tdtr_TD01_SSP_002_t3_to_SSP_077\t   20M\n\n\t6. TIMING POINT IN JOURNEY PATTERN\t: hde:tpip_24o_06\n\t\t\tTIMING POINT:  C   mybus:SSP_077\n\t\t\t Arrive: 15:10, 16 10\n\nThere is alink for the whole route as well\n  TIMING LINK :\tA\t\t - \tC    \tmybus:SSP_001_to_SSP_077\n \t  \n\t\n\nThe SERVICE JOURNEY  PATTERN  has  six  POINT IN JOURNEY PATTERN referencing the  three SCHEDULED STOP POINTs  and three additional timing points\n which are connected by two      SERVICE LINKs   .and five TIMING LINKs\n \n SERVICE JOURNEY PATTERN:  ServiceJourneyPattern:sjp_24o\n\t1  POINT IN JOURNEY PATTERN\t\t hde:tpip_24o_01\n\t\t\tSCHEDULED STOP POINT:  A   mybus:SSP_001\n\t\t\tSERVICE LINK :\tA\t\t - B     \tmybus:SSP_001_to_SSP_002 \n\t\t\tTIMING LINK :\tA\t\t - \ta_t1     \tmybus:SSP_001_to_SSP_001_t1\n\n    2.   POINT IN JOURNEY PATTERN:\t\thde:tpip_24o_02\n\t\t\tTIMING POINT: mybus:SSP_001_t1\n\t\t\tTIMING LINK :\t a_t1\t-\ta_t2\t\tmybus:SSP_001_t1_to_SSP_001_t2\n\n\t3.   POINT IN JOURNEY PATTERN:\t\thde:tpip_24o_03\n\t\t\tTIMING POINT: mybus:SSP_001_t2\n\t\t\tTIMING LINK :\ta_t2\t-\tB\t\t\t\tmybus:SSP_001_t2_to_SSP_002\n\n\t4 POINT IN JOURNEY PATTERN:   hde:tpip_24o_04\n\t\t\tSCHEDULED STOP POINT:  B   mybus:SSP_002\n\t\t\tSERVICE LINK :\tB\t\t - C\t\tmybus:SSP_002_to_SSP_077\n\t\t\tTIMING LINK :\tA\t\t - b_t3\t\t\tmybus:SSP_002_to_SSP_002_t3  JOURNEY RUN TIME  18M\n\n\t5. POINT IN JOURNEY PATTERN: \t\thde:tpip_24o_05\n\t\t\tTIMING POINT: mybus:SSP_002_t3\n\t\t\tTIMING LINK :\tb_t3\t\t- \tC\t\t\tmybus:SSP_002_t3_to_SSP_077  JOURNEY RUN TIME  20M\n\n\t6 POINT IN JOURNEY PATTERN: \t\thde:tpip_24o_06\n\t\t\tSCHEDULED STOP POINT:  C   mybus:SSP_077\n\nThe   JOURNEY  PATTERN  has  six  POINT IN JOURNEY PATTERN referencing the  three SCHEDULED STOP POINTs  and three additional timing points\n which are connected by two      SERVICE LINKs   .and five TIMING LINKs\n \n SERVICE JOURNEY PATTERN:  ServiceJourneyPattern:sjp_24o\n\t1  POINT IN JOURNEY PATTERN\t\t hde:tpip_24o_01\n\t\t\tSCHEDULED STOP POINT:  A   mybus:SSP_001\n\t\t\tSERVICE LINK :\tA\t\t - B     \tmybus:SSP_001_to_SSP_002 \n\t\t\tTIMING LINK :\tA\t\t - \ta_t1     \tmybus:SSP_001_to_SSP_001_t1\n\n    2.   POINT IN JOURNEY PATTERN:\t\thde:tpip_24o_02\n\t\t\tTIMING POINT: mybus:SSP_001_t1\n\t\t\tTIMING LINK :\t a_t1\t-\ta_t2\t\tmybus:SSP_001_t1_to_SSP_001_t2\n\n\t3.   POINT IN JOURNEY PATTERN:\t\thde:tpip_24o_03\n\t\t\tTIMING POINT: mybus:SSP_001_t2\n\t\t\tTIMING LINK :\ta_t2\t-\tB\t\t\t\tmybus:SSP_001_t2_to_SSP_002\n\n\t4 POINT IN JOURNEY PATTERN:   hde:tpip_24o_04\n\t\t\tSCHEDULED STOP POINT:  B   mybus:SSP_002\n\t\t\tSERVICE LINK :\tB\t\t - C\t\tmybus:SSP_002_to_SSP_077\n\t\t\tTIMING LINK :\tA\t\t - b_t3\t\t\tmybus:SSP_002_to_SSP_002_t3  JOURNEY RUN TIME  18M\n\n\t5. POINT IN JOURNEY PATTERN: \t\thde:tpip_24o_05\n\t\t\tTIMING POINT: mybus:SSP_002_t3\n\t\t\tTIMING LINK :\tb_t3\t\t- \tC\t\t\tmybus:SSP_002_t3_to_SSP_077  JOURNEY RUN TIME  20M\n\n\t6 POINT IN JOURNEY PATTERN: \t\thde:tpip_24o_06\n\t\t\tSCHEDULED STOP POINT:  C   mybus:SSP_077\n\n\nThere are Three NOTICes defining Stop Announcements\nThese are associated with a POINT IN JOURNEY PATTERN  using a NOTICE ASSIGNMENT\n\t mybus:Na_Nxa_SSP_001   = = > mybus:Nxa_SSP_001 \n\t\t\t Next stop is \n\t mybus:Na_Nxa_SSP_002   = = > mybus:Nxa_SSP_002 \n\t mybus:Na_Nxa_SSP_077   = = > mybus:Nxa_SSP_077 \n   \nA COMPOSITE FRAME is used to group the component FRAMEs\n \n   - It has a VALIDITY CONDITION  that specifies it is valid from Sept to Matrch\n\n\t\tA SERVICE  FRAME is used to contain the STOP POINT  elements   LINE, etc\n\t\tA TIMETABLE FRAME is used to contain  the SERVICE JOURNEY   elements \n \n\t\t\t a SERVICE CALENDAR FRAMEb\tA SERVICE CALENDAR FRAME is used to contain the DAY TYPEs etc \n\nThe Calendar is shown coded as\n      Compact : OPERATING DAYs are assumed for each calendar date within the period of the calendar \n\t\n\t'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='hde:ACS@Line_24',
                version='1.0',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
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
                            id='mybus:ACS@Line_24@network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24 '
                            ),
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='hde',
                                        xmlns='hde',
                                        xmlns_url='http://www.halt.de/',
                                        description='Stop data  data'
                                    ),
                                ]
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='acs:ACS@Common_resources'
                                    ),
                                ]
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
                                            value='Line 24 Alpha to Charley  (Details not GIVEN)'
                                        ),
                                        direction_type=DirectionType(

                                        ),
                                        direction_ref=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Westbound'
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
                                        public_code='24',
                                        operator_ref=OperatorRef(
                                            version='1.0',
                                            ref='acs:ACS'
                                        ),
                                        routes=RouteRefsRelStructure(
                                            route_ref=[
                                                RouteRef(
                                                    ref='mybus:RT_24o'
                                                ),
                                            ]
                                        ),
                                        presentation=PresentationStructure(
                                            colour_name='Red'
                                        )
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='mybus:DST_Bravo',
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
                                        id='mybus:DST_Charley',
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
                                            value='ALPH'
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
                                            value='Bravo Street'
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
                                            value='BRAV'
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
                                            value='Charley Crescent'
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
                                        id='mybus:SSP_002_to_SSP_077',
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
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern=[
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
                                            journey_pattern_ref=[
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
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        value='Redundant Information!',
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
                                                    ),
                                                    for_alighting=False,
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:spijp_24o_01',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_001'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_001'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        value='Redundant Information!',
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_077'
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:spijp_24o_02',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_002'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_002'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:spijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    for_boarding=False,
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:spijp_24o_03',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_077'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_077'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
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
                            timing_points=TimingPointsInFrameRelStructure(
                                timing_point=[
                                    TimingPoint(
                                        id='mybus:SSP_001_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Between  Alpha   and Bravo Point 1'
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
                                            value='Between  Alpha   and Bravo  Point 2'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT
                                    ),
                                    TimingPoint(
                                        id='mybus:SSP_002_t3',
                                        version='any',
                                        name=MultilingualString(
                                            value='Between  Bravo   and Charley  Point 1'
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
                                        id='mybus:SSP_001_to_SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Overall timing Alpha  to  Charley reen'
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
                                        id='mybus:SSP_001_to_SSP_001_t1',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha   t1'
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
                                        id='mybus:SSP_001_t1_to_SSP_001_t2',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha   t1 to After Alpha  t2'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_001_t1'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002_t3'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:SSP_001_t2_to_SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Alpha  t2 to Bravo'
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
                                        id='mybus:SSP_002_to_SSP_002_t3',
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
                                            ref='mybus:SSP_002_t3'
                                        )
                                    ),
                                    TimingLink(
                                        id='mybus:SSP_002_t3_to_SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='After Bravo t1 to Charley'
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_002_t3'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='any',
                                            ref='mybus:SSP_077'
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
                                        direction_type=DirectionType(

                                        ),
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_01',
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
                                                        ref='mybus:SSP_001_to_SSP_001_t1'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001_t1_to_SSP_001_t2'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t2'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001_t2_to_SSP_002'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_04',
                                                    version='any',
                                                    order=4,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_002_t3'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_t3'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002_t3_to_SSP_077'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpijp_24o_06',
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
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                journey_pattern=[
                                    ServiceJourneyPattern(
                                        id='hde:sjp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley - All POINTs'
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
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_077'
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
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:pijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t1'
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:pijp_24o_02',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_001'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_001'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:pijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t2'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_04',
                                                    version='any',
                                                    order=4,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:pijp_24o_04',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_002'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_002'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='hde:tpip_24o_05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_t3'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:tpip_24o_06',
                                                    version='any',
                                                    order=6,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    notice_assignments=NoticeAssignmentsRelStructure(
                                                        sales_notice_assignment_or_notice_assignment_or_notice_assignment_view=[
                                                            NoticeAssignment(
                                                                id='mybus:tpip_24o_06',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Next Stop Announcement for SSP_077'
                                                                ),
                                                                order=1,
                                                                notice_ref_or_group_of_notices_ref_or_notice=NoticeRef(
                                                                    version='any',
                                                                    ref='mybus:Nxa_SSP_077'
                                                                ),
                                                                advertised=True
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        links_in_sequence=LinksInJourneyPatternRelStructure(
                                            service_link_in_journey_pattern_or_timing_link_in_journey_pattern=[
                                                ServiceLinkInJourneyPattern(
                                                    id='hde:lijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    service_link_ref=ServiceLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
                                                    )
                                                ),
                                                ServiceLinkInJourneyPattern(
                                                    id='hde:lijp_24o_02',
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
                                                    id='mybus:tdtr_TD01_SSP_001_to_SSP_001_t1',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_001_t1'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01_SSP_001_t1_to_SSP_001_t2',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t1_to_SSP_001_t2'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01_SSP_001_t2_to_SSP_002',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_t2_to_SSP_002'
                                                    ),
                                                    run_time=XmlDuration("PT10M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01_SSP_002_to_SSP_002_t3',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_002_t3'
                                                    ),
                                                    run_time=XmlDuration("PT18M")
                                                ),
                                                JourneyRunTime(
                                                    id='mybus:tdtr_TD01_SSP_002_t3_to_SSP_077',
                                                    version='any',
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_002_t3_to_SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT20M")
                                                ),
                                            ]
                                        ),
                                        wait_times=JourneyWaitTimesRelStructure(
                                            journey_wait_time=[
                                                JourneyWaitTime(
                                                    id='mybus:tdwt_24o1_SSP_002',
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
                            ),
                            time_demand_type_assignments=TimeDemandTypeAssignmentsInFrameRelStructure(
                                time_demand_type_assignment=[
                                    TimeDemandTypeAssignment(
                                        id='mybus:TA_001',
                                        version='any',
                                        order=1,
                                        time_demand_type_ref=TimeDemandTypeRef(
                                            version='any',
                                            ref='mybus:tdt_01'
                                        ),
                                        timeband_ref=TimebandRef(
                                            ref='mybus:tdt_01'
                                        ),
                                        group_of_timing_links_ref=GroupOfTimingLinksRef(
                                            version='any',
                                            ref='mybus:Bogus'
                                        )
                                    ),
                                ]
                            ),
                            timing_link_groups=GroupOfLinksInFrameRelStructure(
                                group_of_links=[
                                    GroupOfLinks(
                                        id='mybus:Bogus',
                                        version='any',
                                        name=MultilingualString(
                                            value='bogus group'
                                        ),
                                        members=LinkRefsRelStructure(
                                            link_ref_or_infrastructure_link_ref_or_link_ref_by_value=[
                                                TimingLinkRef(
                                                    version='any',
                                                    ref='mybus:SSP_001_t2_to_SSP_002'
                                                ),
                                                TimingLinkRef(
                                                    version='any',
                                                    ref='mybus:SSP_002_to_SSP_002_t3'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            notices=NoticesInFrameRelStructure(
                                notice=[
                                    Notice(
                                        id='mybus:Nxa_SSP_001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Next Stop Announcement for SSP_002'
                                        ),
                                        text=MultilingualString(
                                            value='Welcome This service goes to Charley Crescent. Stopping everywhere',
                                            lang='en'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_001_en',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Welcome This service goes to Charley Crescent.',
                                                        lang='de'
                                                    )
                                                ),
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_001_de',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Willkommen  Dieser Dienst   fahrt nach Charley Crescent.',
                                                        lang='de'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Notice(
                                        id='mybus:Nxa_SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Next Stop Announcement for SSP_002'
                                        ),
                                        text=MultilingualString(
                                            value='Next Stop is Bravo Road. Alight here for Chocolate Museum',
                                            lang='en'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_002_en',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Next Stop is Bravo Road',
                                                        lang='de'
                                                    )
                                                ),
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_002_de',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Nachste Haltstelle Bravo Road.  ',
                                                        lang='de'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Notice(
                                        id='mybus:Nxa_SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Next Stop Announcement for SSP_077'
                                        ),
                                        text=MultilingualString(
                                            value='Next Stop is Charley Road. Service Terminates here',
                                            lang='en'
                                        ),
                                        variants=DeliveryVariantsRelStructure(
                                            delivery_variant=[
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_002_en',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Next Stop is Charley Crescent. All alight here.',
                                                        lang='de'
                                                    )
                                                ),
                                                DeliveryVariant(
                                                    id='mybus:Nxa_SSP_002_de',
                                                    version='any',
                                                    delivery_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    variant_text=MultilingualString(
                                                        value='Nachste Haltstelle Charley Crescent. Aussteigen',
                                                        lang='de'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='hde:LN_24',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='hde:Cnd001',
                                            version='any',
                                            description=MultilingualString(
                                                value='Sept  to April'
                                            ),
                                            from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 4, 30, 0, 0, 0, 0, 0)
                                        ),
                                    ]
                                ),
                            ],
                            version='1.0',
                            name=MultilingualString(
                                value='Winter timetable for route 23 outbound'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:ACS@Line_24@network'
                                    ),
                                    ServiceCalendarFrameRef(
                                        version='1.0',
                                        ref='hde:Calendar@2010'
                                    ),
                                ]
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id='hde:sj_24o_01',
                                        version='any',
                                        journey_accountings=JourneyAccountingsRelStructure(
                                            journey_accounting_ref_or_journey_accounting=[
                                                JourneyAccounting(
                                                    id='mytim:ac02',
                                                    version='any',
                                                    order=1,
                                                    organisation_ref=AuthorityRefStructure(
                                                        value='EXTERNAL',
                                                        ref='txc:xshire'
                                                    ),
                                                    accounting_type=JourneyAccountingEnumeration.SUBSIDY,
                                                    partial=[
                                                        False,
                                                    ],
                                                    distance=Decimal('20')
                                                ),
                                                JourneyAccounting(
                                                    id='mytim:ac03',
                                                    version='any',
                                                    order=2,
                                                    organisation_ref=AuthorityRefStructure(
                                                        value='EXTERNAL',
                                                        ref='txc:xshire'
                                                    ),
                                                    accounting_type=JourneyAccountingEnumeration.CONTRACT,
                                                    partial=[
                                                        False,
                                                    ],
                                                    distance=Decimal('20')
                                                ),
                                            ]
                                        ),
                                        departure_time=XmlTime(14, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_02-Everyday-NotHoliday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_ChristmasEve'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_ChristmasDay'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_ChristmasDayDisplacement'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_NewYearsEve'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_NewYearsDay'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_2ndJanuary'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_GoodFriday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_EasterSunday'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_EasterMonday'
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
                                        block_ref=BlockRef(
                                            value='EXTERNAL',
                                            ref='mybus:BLK_24o5'
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
                                                ref='mybus:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_24o_01',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_01_SSP_001',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_01'
                                                    ),
                                                    departure_time=XmlTime(14, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_01_SSP_001_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_02'
                                                    ),
                                                    departure_time=XmlTime(14, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_01_SSP_001_t2',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_03'
                                                    ),
                                                    departure_time=XmlTime(14, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_01_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_02'
                                                    ),
                                                    departure_time=XmlTime(14, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_01_SSP_002_t3',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_05'
                                                    ),
                                                    departure_time=XmlTime(14, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_01_SSP_077',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_03'
                                                    ),
                                                    arrival_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_24o_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='mybus:SSP_001_to_SSP_001_t1'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_001_t1'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
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
                                                    id='hde:sj_24o_01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='mybus:SSP_002_to_SSP_002_t3'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_002_t3'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_077'
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
                                                    ref='hde:sfs_24o_01'
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney(
                                        id='hde:sj_24o_02',
                                        version='any',
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NotHoliday'
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
                                        block_ref=BlockRef(
                                            value='EXTERNAL',
                                            ref='mybus:BLK_24o8'
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
                                                ref='mybus:DST_Charley'
                                            )
                                        ),
                                        run_times=VehicleJourneyRunTimesRelStructure(
                                            vehicle_journey_run_time=[
                                                VehicleJourneyRunTime(
                                                    id='hde:vjrt_sj_24o_02',
                                                    name=MultilingualString(
                                                        value='Overall run time'
                                                    ),
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='mybus:tdt_01'
                                                    ),
                                                    timing_link_ref=TimingLinkRef(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_077'
                                                    ),
                                                    run_time=XmlDuration("PT70M")
                                                ),
                                            ]
                                        ),
                                        passing_times=TimetabledPassingTimesRelStructure(
                                            timetabled_passing_time=[
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_02_SSP_001',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_01'
                                                    ),
                                                    departure_time=XmlTime(15, 0, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_02_SSP_001_t1',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_02'
                                                    ),
                                                    departure_time=XmlTime(15, 10, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_02_SSP_001_t2',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_03'
                                                    ),
                                                    departure_time=XmlTime(15, 20, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_02_SSP_002',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_02'
                                                    ),
                                                    departure_time=XmlTime(15, 30, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='hde:tpt_24o_02_SSP_002_t3',
                                                    version='any',
                                                    point_in_journey_pattern_ref=TimingPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:tpijp_24o_05'
                                                    ),
                                                    departure_time=XmlTime(15, 50, 0, 0, 0)
                                                ),
                                                TimetabledPassingTime(
                                                    id='mybus:tpt_24o_02_SSP_077',
                                                    version='any',
                                                    point_in_journey_pattern_ref=StopPointInJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:spijp_24o_03'
                                                    ),
                                                    arrival_time=XmlTime(16, 10, 0, 0, 0)
                                                ),
                                            ]
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:sj_24o_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='mybus:SSP_001_to_SSP_001_t1'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_001_t1'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
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
                                                                    ref='mybus:DST_Bravo'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    change_of_destination_display=False,
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:sj_24o_02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            version='any',
                                                            ref='mybus:SSP_002_to_SSP_002_t3'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_002_t3'
                                                        )
                                                    ),
                                                    onward_service_link_ref_or_onward_service_link_view=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_077'
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
                                                    id='hde:sj_24o_02_003',
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
                                        ),
                                        facilities=ServiceFacilitySetsRelStructure(
                                            service_facility_set_ref_or_service_facility_set=[
                                                ServiceFacilitySetRef(
                                                    version='any',
                                                    ref='hde:sfs_24o_01'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='hde:sfs_24o_01',
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
                            id='hde:Calendar@2010',
                            version='1.0',
                            name=MultilingualString(
                                value='Service Calendar Nov to April 2010  (Compact Coding) '
                            ),
                            service_calendar=ServiceCalendar(
                                id='hde:Calendar@2010',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
                                        id='hde:DT_01-MF-NotHoliday',
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
                                        id='hde:DT_02-Everyday-NotHoliday',
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
                                        id='hde:DT_03-WE-NotHoliday',
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
                                        id='hde:DT_04-AA-NotHoliday',
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
                                    DayType(
                                        id='hde:DT_ChristmasEve',
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
                                    DayType(
                                        id='hde:DT_ChristmasDay',
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
                                    DayType(
                                        id='hde:DT_ChristmasDayDisplacement',
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
                                    DayType(
                                        id='hde:DT_NewYearsEve',
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
                                    DayType(
                                        id='hde:DT_NewYearsDay',
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
                                    DayType(
                                        id='hde:DT_2ndJanuary',
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
                                    DayType(
                                        id='hde:DT_NewYearsDayDisplacement',
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
                                    DayType(
                                        id='hde:DT_GoodFriday',
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
                                    DayType(
                                        id='hde:DT_EasterSunday',
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
                                    DayType(
                                        id='hde:DT_EasterMonday',
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
                                        id='hde:OD_2010-11-01',
                                        version='any',
                                        calendar_date=XmlDate(2010, 11, 1),
                                        name=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        earliest_time=XmlTime(2, 0, 0, 0),
                                        day_length=XmlDuration("PT24H")
                                    ),
                                    OperatingDay(
                                        id='hde:OD_2011-04-30',
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
                                    OperatingPeriod(
                                        id='hde:op_010',
                                        version='any',
                                        name=MultilingualString(
                                            value='WInter 2011'
                                        ),
                                        from_operating_day_ref_or_from_date=OperatingDayRefStructure(
                                            version='any',
                                            ref='hde:OD_2010-11-01'
                                        ),
                                        to_operating_day_ref_or_to_date=OperatingDayRefStructure(
                                            version='any',
                                            ref='hde:OD_2011-04-30'
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
                                        id='hde:DayAsgn_2010-11-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        order=1,
                                        choice=OperatingDayRef(
                                            version='any',
                                            ref='hde:OD_2010-11-01'
                                        ),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_03-WE-NotHoliday'
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
                                            ref='hde:DT_03-WE-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
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
                                            ref='hde:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-11-13',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-13'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 13),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NotHoliday'
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
                                            ref='hde:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-12-24',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-12-24'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 31),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_ChristmasEve'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-12-25',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-12-25 Christams Day'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 25),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_ChristmasDay'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-12-27',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-12-27 (Christjmas Day displacement holiday)'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 27),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_ChristmasDayDisplacement'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2010-12-31',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday 2010-12-31  New Years eve'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 12, 31),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_NewYearsEve'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2011-01-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday  2011-01-01 New Years day'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 1, 1),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_NewYearsDay'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2011-01-03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Satuurday  2011-01-03 New Years day displacement'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 1, 3),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_NewYearsDayDisplacement'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_>2011-04-22',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday 2011-04-22 Good Friday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 22),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_GoodFriday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_>2011-04-24',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2011-04-24 Easter Sunday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 24),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_EasterSunday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_>2011-04-25',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2011-04-25 Easter Monday'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 25),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_EasterMonday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2011-04-29',
                                        version='any',
                                        description=MultilingualString(
                                            value='Friday2011-04-29'
                                        ),
                                        order=1,
                                        choice=XmlDate(2011, 4, 29),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_01-MF-NotHoliday'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='hde:DayAsgn_2011-04-30',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2011-04-30'
                                        ),
                                        order=1,
                                        choice=OperatingDayRef(
                                            version='any',
                                            ref='hde:OD_2011-04-30'
                                        ),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='hde:DT_03-WE-NotHoliday'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='acs:ACS@Common_resources',
                            version='1.0',
                            codespaces=CodespacesRelStructure(
                                codespace_ref_or_codespace=[
                                    Codespace(
                                        id='acs',
                                        xmlns='acs',
                                        xmlns_url='http://autocarssuperbe.fr',
                                        description='Service data '
                                    ),
                                ]
                            ),
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_codespace_ref=CodespaceRefStructure(
                                    ref='acs'
                                )
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='acs:ACS',
                                        version='1.0',
                                        name=MultilingualString(
                                            value='Autocars superbe'
                                        ),
                                        locale=Locale(
                                            default_language='fr'
                                        ),
                                        contact_details=ContactStructure(
                                            phone='+33-1-675-9876',
                                            url='http://autocarssuperbe.fr'
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
