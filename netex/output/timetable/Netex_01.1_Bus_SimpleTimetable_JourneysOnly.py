from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.arrival_structure import ArrivalStructure
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.models.assistance_facility_list import AssistanceFacilityList
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
from netex.models.delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from netex.models.departure_structure import DepartureStructure
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_display_variant import DestinationDisplayVariant
from netex.models.destination_display_variants_rel_structure import DestinationDisplayVariantsRelStructure
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import DayTypesRelStructure
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.fare_classes import FareClasses
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journey_pattern_view import JourneyPatternView
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.locale import Locale
from netex.models.location_structure_2 import LocationStructure2
from netex.models.luggage_carriage_enumeration import LuggageCarriageEnumeration
from netex.models.luggage_carriage_facility_list import LuggageCarriageFacilityList
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration
from netex.models.mobility_facility_list import MobilityFacilityList
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.nuisance_facility_list import NuisanceFacilityList
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.passenger_information_facility_list import PassengerInformationFacilityList
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.route_ref import RouteRef
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
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
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.models.via_versioned_child_structure import ViaVersionedChildStructure
from netex.models.vias_rel_structure import ViasRelStructure
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
                                id='acs:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value='REQUEST',
                            ref='acs:TimetableFrameTIM_23_O'
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
                id='acs:ACS@Line_24',
                version='1.0',
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:ACS@Line_24@Network',
                            version='1.0',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24 '
                            ),
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
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ResourceFrameRef(
                                        version='1.0',
                                        ref='acs:ACS@Common_Resources'
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
                                        )
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='mybus:Bravo',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Road'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo Rd'
                                        ),
                                        public_code='BRAV',
                                        variants=DestinationDisplayVariantsRelStructure(
                                            destination_display_variant=[
                                                DestinationDisplayVariant(
                                                    destination_display_variant_media_type=DeliveryVariantTypeEnumeration.TEXT_TO_SPEECH,
                                                    name=MultilingualString(
                                                        value='Bravo'
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            ViaVersionedChildStructure(
                                                                destination_display_ref_or_destination_display_view_or_name=MultilingualString(
                                                                    value='Eye Hospital'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:Charley',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Crescent'
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley C'
                                        ),
                                        public_code='CHAS'
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
                                    ScheduledStopPoint(
                                        id='mybus:SSP_015',
                                        version='any',
                                        name=MultilingualString(
                                            value='Park Lane'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Park Lane'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='PARK'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='acs:ACS@Line_24@Timetable',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='acs:Cnd001',
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
                                                        ref='acs:DT_01-MF-NH'
                                                    ),
                                                    DayTypeRef(
                                                        version='any',
                                                        ref='acs:DT_03-WE-NH'
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            version='1.0',
                            name=MultilingualString(
                                value='Winter timetable for route 24 outbound'
                            ),
                            prerequisites=VersionFrameRefsRelStructure(
                                version_frame_ref=[
                                    ServiceFrameRef(
                                        version='1.0',
                                        ref='mybus:ACS@Line_24@Network'
                                    ),
                                    ServiceFrameRef(
                                        ref='mybus:ACS@Line_24@Routes_and_JourneyPatterns',
                                        version_ref='EXTERNAL'
                                    ),
                                    ServiceCalendarFrameRef(
                                        version='1.0',
                                        ref='acs:ACS@Winter_2010'
                                    ),
                                    VehicleScheduleFrameRef(
                                        ref='mybus:ACS@Line_24@Schedule',
                                        version_ref='EXTERNAL'
                                    ),
                                ]
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id='acs:sj_24o_01',
                                        version='any',
                                        departure_time=XmlTime(14, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='acs:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            value='EXTERNAL',
                                            ref='acs:jp_24o',
                                            version_ref='EXTERNAL'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:td_01',
                                            version_ref='EXTERNAL'
                                        ),
                                        block_ref=BlockRef(
                                            value='EXTERNAL',
                                            ref='mybus:BLK_24o5',
                                            version_ref='EXTERNAL'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24'
                                        ),
                                        journey_pattern_view=JourneyPatternView(
                                            route_ref_or_route_view=RouteRef(
                                                value='EXTERNAL',
                                                ref='mybus:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='mybus:Charley'
                                            )
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='acs:sj_24o_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(14, 20, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='acs:sj_24o_01_002',
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
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    note=MultilingualString(
                                                        value='Arrival at Terminus'
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='acs:sj_24o_01_003',
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
                                                    ref='acs:sfs_24o_01'
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney(
                                        id='acs:sj_24o_02',
                                        version='any',
                                        departure_time=XmlTime(15, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='acs:DT_01-MF-NH'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServiceJourneyPatternRef(
                                            value='EXTERNAL',
                                            ref='acs:jp_24o'
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:td_01'
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
                                                value='EXTERNAL',
                                                ref='mybus:RT_24o'
                                            ),
                                            direction_type=DirectionTypeEnumeration.OUTBOUND,
                                            destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                                version='any',
                                                ref='mybus:Charley'
                                            )
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='acs:sj_24o_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(15, 20, 0, 0, 0)
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            ViaVersionedChildStructure(
                                                                destination_display_ref_or_destination_display_view_or_name=DestinationDisplayRef(
                                                                    version='any',
                                                                    ref='mybus:Bravo'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    order=1
                                                ),
                                                Call(
                                                    id='acs:sj_24o_02_002',
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
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    vias=ViasRelStructure(
                                                        none_or_via=[
                                                            '',
                                                        ]
                                                    ),
                                                    change_of_destination_display=True,
                                                    order=2
                                                ),
                                                Call(
                                                    id='acs:sj_24o_02_003',
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
                                                    ref='acs:sfs_24o_01'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='acs:sfs_24o_01',
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
                            id='acs:ACS@Winter_2010',
                            version='1.0',
                            name=MultilingualString(
                                value='Service Calendar Nov 2010 ALTERNATE MORE COMPACT Coding  '
                            ),
                            service_calendar=ServiceCalendar(
                                id='acs:ACS@Winter_2010',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
                                        id='acs:DT_01-MF-NH',
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
                                        id='acs:DT_02-AA-NH',
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
                                        id='acs:DT_03-WE-NH',
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
                                        id='acs:DT_04-AA-NH',
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
                                        id='acs:2010-11-01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-01'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 1),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-02',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-02'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 2),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-03'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 3),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-04',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-04'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 4),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-05',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-05'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 5),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-06',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-06'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 6),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-07',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-07'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 7),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-08',
                                        version='any',
                                        description=MultilingualString(
                                            value='Monday 2010-11-08'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 8),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-09',
                                        version='any',
                                        description=MultilingualString(
                                            value='Tuesday 2010-11-09'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 9),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-10',
                                        version='any',
                                        description=MultilingualString(
                                            value='Wednesday 2010-11-10'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 10),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-11',
                                        version='any',
                                        description=MultilingualString(
                                            value='Thusday 2010-11-11'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 11),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-12',
                                        version='any',
                                        description=MultilingualString(
                                            value='MFriday 2010-11-12'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 12),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_01-MF-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-113',
                                        version='any',
                                        description=MultilingualString(
                                            value='Saturday 2010-11-13'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 13),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_03-WE-NH'
                                        )
                                    ),
                                    DayTypeAssignment(
                                        id='acs:2010-11-14',
                                        version='any',
                                        description=MultilingualString(
                                            value='Sunday 2010-11-14'
                                        ),
                                        order=1,
                                        choice=XmlDate(2010, 11, 14),
                                        day_type_ref=DayTypeRef(
                                            version='any',
                                            ref='acs:DT_03-WE-NH'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='acs:ACS@Common_Resources',
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
