from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.arrival_structure import ArrivalStructure
from netex.models.call_1 import Call1
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType1
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.explicit_journey_refs_rel_structure import ExplicitJourneyRefsRelStructure
from netex.models.frequency_groups_in_frame_rel_structure import FrequencyGroupsInFrameRelStructure
from netex.models.frequency_structure import FrequencyStructure
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.headway_journey_group import HeadwayJourneyGroup
from netex.models.headway_journey_group_ref import HeadwayJourneyGroupRef
from netex.models.headway_use_enumeration import HeadwayUseEnumeration
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line_1 import Line1
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.onward_timing_link_view import OnwardTimingLinkView
from netex.models.participant_ref import ParticipantRef
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey_1 import ServiceJourney1
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_link_ref import TimingLinkRef
from netex.models.timing_point_ref_structure import TimingPointRefStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
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
                                id='hde:TIM_23_O',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value='REQUEST',
                            ref='hde:TIM_23HFT_O'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple timetable frame with a group of headway journeys '
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='hde:CF_1',
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
                        TimetableFrame(
                            id='hde:hde:TIM_23HFT_O',
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
                                            to_date=XmlDateTime(2011, 3, 31, 0, 0, 0, 0, 0)
                                        ),
                                    ]
                                ),
                            ],
                            version='any',
                            name=MultilingualString(
                                value='Winter timetable for route 23 outbound'
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney1(
                                        id='hde:sj_fg_24o_01',
                                        version='any',
                                        departure_time=XmlTime(10, 0, 0, 0, 0),
                                        frequency=FrequencyStructure(
                                            scheduled_headway_interval=XmlDuration("PT10M"),
                                            headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                        ),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        journey_frequency_group_ref=HeadwayJourneyGroupRef(
                                            version='any',
                                            ref='hde:hjg_24o_02_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_01_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            value='EXCLUDED',
                                                            ref='mybus:TL_001_to_002'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_002'
                                                        )
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_01_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_timing_link_view=OnwardTimingLinkView(
                                                        timing_link_ref=TimingLinkRef(
                                                            value='EXCLUDED',
                                                            ref='mybus:TL_002_to_077'
                                                        ),
                                                        to_point_ref=TimingPointRefStructure(
                                                            version='any',
                                                            ref='mybus:SSP_077'
                                                        )
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 22, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_01_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(10, 40, 0, 0, 0)
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
                                        id='hde:sj_fg_24o_02',
                                        version='any',
                                        departure_time=XmlTime(10, 15, 0, 0, 0),
                                        frequency=FrequencyStructure(
                                            scheduled_headway_interval=XmlDuration("PT10M"),
                                            headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                        ),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        journey_frequency_group_ref=HeadwayJourneyGroupRef(
                                            version='any',
                                            ref='hde:hjg_24o_02_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_02_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 15, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_02_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 35, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_02_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(10, 50, 0, 0, 0)
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
                                        id='hde:sj_fg_24o_03',
                                        version='any',
                                        departure_time=XmlTime(10, 30, 0, 0, 0),
                                        frequency=FrequencyStructure(
                                            scheduled_headway_interval=XmlDuration("PT10M"),
                                            headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                        ),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        journey_frequency_group_ref=HeadwayJourneyGroupRef(
                                            version='any',
                                            ref='hde:hjg_24o_02_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_03_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 30, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_03_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 50, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_03_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(11, 10, 0, 0, 0)
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
                                        id='hde:sj_fg_24o_04',
                                        version='any',
                                        departure_time=XmlTime(10, 45, 0, 0, 0),
                                        frequency=FrequencyStructure(
                                            scheduled_headway_interval=XmlDuration("PT10M"),
                                            headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                        ),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        journey_frequency_group_ref=HeadwayJourneyGroupRef(
                                            version='any',
                                            ref='hde:hjg_24o_02_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_04_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 45, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_04_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(11, 5, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_04_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(11, 25, 0, 0, 0)
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
                                        id='hde:sj_fg_24o_05',
                                        version='any',
                                        departure_time=XmlTime(11, 0, 0, 0, 0),
                                        frequency=FrequencyStructure(
                                            scheduled_headway_interval=XmlDuration("PT10M"),
                                            headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                        ),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        journey_frequency_group_ref=HeadwayJourneyGroupRef(
                                            version='any',
                                            ref='hde:hjg_24o_02_01'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_05_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(11, 20, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_05_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(11, 40, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_05_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 0, 0, 0, 0)
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
                                        id='hde:sj_fg_24o_06',
                                        version='any',
                                        departure_time=XmlTime(12, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            version='any',
                                            ref='hde:svp_24o'
                                        ),
                                        choice=LineRef(
                                            version='any',
                                            ref='mybus:LN_24o'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call1(
                                                    id='hde:sj_fg_24o_06_001',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(12, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_06_002',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(12, 20, 0, 0, 0)
                                                    ),
                                                    order=2
                                                ),
                                                Call1(
                                                    id='hde:sj_fg_24o_06_003',
                                                    version='any',
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 40, 0, 0, 0)
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
                            frequency_groups=FrequencyGroupsInFrameRelStructure(
                                headway_journey_group_or_rhythmical_journey_group=[
                                    HeadwayJourneyGroup(
                                        id='hde:hjg_24o_02_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='every 10 minutes between 10am and 10:50pm'
                                        ),
                                        description=[
                                            MultilingualString(
                                                value='About every 10 minutes'
                                            ),
                                        ],
                                        first_departure_time=XmlTime(10, 0, 0, 0),
                                        last_departure_time=XmlTime(11, 0, 0, 0),
                                        journeys=ExplicitJourneyRefsRelStructure(
                                            service_journey_ref_or_vehicle_journey_ref=[
                                                ServiceJourneyRef(
                                                    version='any',
                                                    ref='hde:sj_fg_24o_01'
                                                ),
                                                ServiceJourneyRef(
                                                    version='any',
                                                    ref='hde:sj_fg_24o_02'
                                                ),
                                                ServiceJourneyRef(
                                                    version='any',
                                                    ref='hde:sj_fg_24o_03'
                                                ),
                                                ServiceJourneyRef(
                                                    version='any',
                                                    ref='hde:sj_fg_24o_04'
                                                ),
                                                ServiceJourneyRef(
                                                    version='any',
                                                    ref='hde:sj_fg_24o_05'
                                                ),
                                            ]
                                        ),
                                        scheduled_headway_interval=XmlDuration("PT15M"),
                                        minimum_headway_interval=XmlDuration("PT2M"),
                                        maximum_headway_interval=XmlDuration("PT17M"),
                                        headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='mybus:svf_24o',
                            version='any',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 24o '
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line1(
                                        id='mybus:LN_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24o Alpha to Charley Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24o'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='24o'
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
                                            value='Alpha to Charley Green'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_001_to_SSP_002'
                                                    ),
                                                    for_alighting=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='any',
                                                        ref='mybus:SSP_002_to_SSP_077'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_03',
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
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='hde:CAL_01',
                            version='any',
                            name=MultilingualString(
                                value='Service Calendar Nov 2010 '
                            ),
                            service_calendar=ServiceCalendar(
                                id='hde:SC_01',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2010, 11, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType1(
                                        id='hde:DT_01MTWTFSS',
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
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
