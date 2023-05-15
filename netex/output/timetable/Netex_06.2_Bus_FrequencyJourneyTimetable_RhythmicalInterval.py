from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import TimebandVersionedChildStructure
from netex.models.alternative_texts_rel_structure import TimebandsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.arrival_structure import ArrivalStructure
from netex.models.call import Call
from netex.models.calls_rel_structure import CallsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.frequency_groups_rel_structure import FrequencyGroupsRelStructure
from netex.models.frequency_structure import FrequencyStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.line_view import LineView
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.rhythmical_journey_group import RhythmicalJourneyGroup
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey import ServiceJourney
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.template_service_journey import TemplateServiceJourney
from netex.models.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from netex.models.timeband_ref import TimebandRef
from netex.models.timeband_refs_rel_structure import TimebandRefsRelStructure
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
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
                                id="hde:01",
                                version="any",
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value="REQUEST",
                            ref="hde:TIM_23_O"
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value="Example  of simple rhythmical  template timetable   with three    journeys  "
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id="hde:CF_1",
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
                        TimetableFrame(
                            id="hde:TIM_23_O",
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id="hde:Cnd001",
                                            version="any",
                                            description=MultilingualString(
                                                value="Sept  to March"
                                            ),
                                            from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 3, 31, 0, 0, 0, 0, 0),
                                            day_types=DayTypesRelStructure(
                                                choice=[
                                                    DayTypeRef(
                                                        version="any",
                                                        ref="hde:DT_01MTWTFSS"
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            version="001",
                            name=MultilingualString(
                                value="Winter timetable for route 23 outbound"
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    ServiceJourney(
                                        id="hde:sj_24o_01",
                                        version="any",
                                        departure_time=XmlTime(8, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version="any",
                                                    ref="hde:DT_01MTWTFSS"
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            value="EXTERNAL",
                                            ref="hde:svp_24a"
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            value="EXTERNAL",
                                            ref="hde:TDT_45_morning"
                                        ),
                                        choice_1=LineView(
                                            flexible_line_ref_or_line_ref=LineRef(
                                                version="any",
                                                ref="mybus:LN_234"
                                            ),
                                            public_code="24",
                                            name=MultilingualString(
                                                value="Line 24 Alpha to Charley Green"
                                            ),
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id="hde:sj_24o_01_001",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(8, 0, 0, 0, 0),
                                                        for_boarding=True
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id="hde:sj_24o_01_002",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(9, 0, 0, 0, 0),
                                                        for_alighting=True
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(9, 2, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id="hde:sj_24o_01_003",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(10, 0, 0, 0, 0),
                                                        for_alighting=True
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        )
                                    ),
                                    TemplateServiceJourney(
                                        id="hde:tvj_24o_02",
                                        version="any",
                                        departure_time=XmlTime(10, 20, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version="any",
                                                    ref="hde:DT_01MTWTFSS"
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            value="EXTERNAL",
                                            ref="hde:svp_24a"
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            value="EXTERNAL",
                                            ref="hde:TDT_45"
                                        ),
                                        choice_1=LineView(
                                            flexible_line_ref_or_line_ref=LineRef(
                                                version="any",
                                                ref="mybus:LN_234"
                                            ),
                                            public_code="24",
                                            name=MultilingualString(
                                                value="Line 24 Alpha to Charley Green"
                                            ),
                                            short_name=MultilingualString(
                                                value="Line 24"
                                            ),
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id="hde:tvj_24o_02_001",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 20, 0, 0, 0)
                                                    ),
                                                    frequency=FrequencyStructure(
                                                        scheduled_headway_interval=XmlDuration("PT8M")
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id="hde:tvj_24o_02_002",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(11, 20, 0, 0, 0),
                                                        for_alighting=True
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(11, 22, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    frequency=FrequencyStructure(
                                                        scheduled_headway_interval=XmlDuration("PT8M")
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id="hde:tvj_24o_02_003",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 20, 0, 0, 0),
                                                        for_alighting=True
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    frequency=FrequencyStructure(
                                                        scheduled_headway_interval=XmlDuration("PT8M")
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        frequency_groups=FrequencyGroupsRelStructure(
                                            choice=[
                                                RhythmicalJourneyGroup(
                                                    id="hde:rjg_24o_01",
                                                    version="any",
                                                    name=MultilingualString(
                                                        value="Regular  Interval service between 10am and 17:00 pm"
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value="At 20 &amp; 45 Minutes past the hour "
                                                        ),
                                                    ],
                                                    first_departure_time=XmlTime(10, 0, 0, 0),
                                                    last_departure_time=XmlTime(17, 0, 0, 0),
                                                    timebands=TimebandRefsRelStructure(
                                                        timeband_ref=[
                                                            TimebandRef(
                                                                version="any",
                                                                ref="hde:TM_20"
                                                            ),
                                                            TimebandRef(
                                                                version="any",
                                                                ref="hde:TM_45"
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourney(
                                        id="hde:sj_24o_04",
                                        version="any",
                                        departure_time=XmlTime(18, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            fare_day_type_ref_or_day_type_ref=[
                                                DayTypeRef(
                                                    version="any",
                                                    ref="hde:DT_02MTWTF"
                                                ),
                                            ]
                                        ),
                                        choice=ServicePatternRef(
                                            value="EXTERNAL",
                                            ref="hde:svp_24a"
                                        ),
                                        time_demand_type_ref=TimeDemandTypeRefStructure(
                                            value="EXTERNAL",
                                            ref="hde:TDT_45"
                                        ),
                                        choice_1=LineView(
                                            flexible_line_ref_or_line_ref=LineRef(
                                                version="any",
                                                ref="mybus:LN_234"
                                            ),
                                            public_code="24",
                                            name=MultilingualString(
                                                value="Line 24 Alpha to Charley Green"
                                            ),
                                            short_name=MultilingualString(
                                                value="Line 24"
                                            ),
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS
                                        ),
                                        calls=CallsRelStructure(
                                            choice=[
                                                Call(
                                                    id="hde:sj_24o_04_001",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_001"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(18, 0, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id="hde:sj_24o_04_002",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_002"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(19, 0, 0, 0, 0),
                                                        for_alighting=True
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(19, 2, 0, 0, 0),
                                                        for_boarding=True,
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id="hde:sj_24o_04_003",
                                                    version="any",
                                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(
                                                        version="any",
                                                        ref="mybus:SSP_077"
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(20, 0, 0, 0, 0),
                                                        for_alighting=True
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
                            )
                        ),
                        ServiceFrame(
                            id="mybus:svf_12",
                            version="any",
                            name=MultilingualString(
                                value="Stops for Winter timetable for route 234 "
                            ),
                            lines=LinesInFrameRelStructure(
                                flexible_line_or_line=[
                                    Line(
                                        id="mybus:LN_234",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 234 Alpha  to Charley"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 234"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="234"
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id="mybus:SSP_001",
                                        version="any",
                                        name=MultilingualString(
                                            value="Alpha &amp; Castle"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.0000"),
                                            latitude=Decimal("0.1000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
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
                                            value="Bravo Arch"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.2000"),
                                            latitude=Decimal("0.2000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Bravo Arch"
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
                                            value="Charley Green"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.3000"),
                                            latitude=Decimal("0.3000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Charley"
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value="CHAS"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id="hde:SCF01",
                            version="any",
                            name=MultilingualString(

                            ),
                            service_calendar=ServiceCalendar(
                                id="hde:cal01",
                                version="any",
                                day_types=DayTypesRelStructure(
                                    choice=[
                                        DayType(
                                            id="hde:DT_01MTWTFSS",
                                            version="any",
                                            name=MultilingualString(
                                                value="Everyday"
                                            ),
                                            properties=PropertiesOfDayRelStructure(
                                                property_of_day=[
                                                    PropertyOfDay(
                                                        days_of_week=[
                                                            DayOfWeekEnumeration.EVERYDAY,
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                        DayType(
                                            id="hde:DT_02MTWTF",
                                            version="any",
                                            name=MultilingualString(
                                                value="Weekdays"
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
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                timebands=TimebandsRelStructure(
                                    timeband_ref_or_timeband=[
                                        TimebandVersionedChildStructure(
                                            id="hde:TM_20",
                                            version="any",
                                            name=MultilingualString(
                                                value="20 minutes past the hourt"
                                            ),
                                            start_time=XmlTime(10, 20, 0, 0),
                                            end_time_or_day_offset_or_duration=[
                                                XmlTime(10, 20, 0, 0),
                                            ]
                                        ),
                                        TimebandVersionedChildStructure(
                                            id="hde:TM_45",
                                            version="any",
                                            name=MultilingualString(
                                                value="45 minutes past the hourt"
                                            ),
                                            start_time=XmlTime(10, 45, 0, 0),
                                            end_time_or_day_offset_or_duration=[
                                                XmlTime(10, 45, 0, 0),
                                            ]
                                        ),
                                    ]
                                )
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
