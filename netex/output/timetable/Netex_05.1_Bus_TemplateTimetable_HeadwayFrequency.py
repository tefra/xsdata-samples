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
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.models.departure_structure import DepartureStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.frequency_groups_rel_structure import FrequencyGroupsRelStructure
from netex.models.headway_journey_group import HeadwayJourneyGroup
from netex.models.headway_use_enumeration import HeadwayUseEnumeration
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.template_service_journey import TemplateServiceJourney
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
                                id='hde:01',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    version_frame_ref=[
                        TimetableFrameRef(
                            value='REQUEST',
                            ref='hde:TIM_24o_FS_Outbound'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple Headwayal  template timetable   with three    journeys  '
    ),
    data_objects=DataObjectsRelStructure(
        common_frame=[
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
                        ServiceCalendarFrame(
                            id='hde:TIM_24o_FS_Outbound',
                            version='any',
                            name=MultilingualString(

                            ),
                            service_calendar=ServiceCalendar(
                                id='hde:TIM_24o_FS_Outbound',
                                version='any',
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayType(
                                            id='hde:DT_01MTWTFSS',
                                            version='any',
                                            name=MultilingualString(
                                                value='Everyday'
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
                                            id='hde:DT_01MTWTF',
                                            version='any',
                                            name=MultilingualString(
                                                value='Weekdays'
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
                                )
                            )
                        ),
                        TimetableFrame(
                            id='hde:TIM_24o_FS_Outbound',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    validity_condition_ref_or_validity_condition=[
                                        AvailabilityCondition(
                                            id='hde:TIM_24o_FS_Outbound',
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
                            version='001',
                            name=MultilingualString(
                                value='Winter timetable for route 234 outbound'
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    TemplateServiceJourney(
                                        id='hde:tvjh_24o_01',
                                        version='any',
                                        departure_time=XmlTime(10, 0, 0, 0, 0),
                                        day_types=DayTypeRefsRelStructure(
                                            day_type_ref=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01MTWTFSS'
                                                ),
                                            ]
                                        ),
                                        journey_pattern_ref=ServicePatternRef(
                                            value='EXTERNAL',
                                            ref='hde:svp_24o'
                                        ),
                                        line_ref=LineRef(
                                            version='any',
                                            ref='mybus:LN_234'
                                        ),
                                        calls=CallsRelStructure(
                                            call=[
                                                Call(
                                                    id='hde:tvjh_24o_02_001',
                                                    version='any',
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        for_alighting=False
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(10, 20, 0, 0, 0)
                                                    ),
                                                    order=1
                                                ),
                                                Call(
                                                    id='hde:tvjh_24o_02_002',
                                                    version='any',
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(11, 20, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        time=XmlTime(11, 22, 0, 0, 0),
                                                        wait_time=XmlDuration("PT2M")
                                                    ),
                                                    order=2
                                                ),
                                                Call(
                                                    id='hde:tvjh_24o_02_003',
                                                    version='any',
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    ),
                                                    arrival=ArrivalStructure(
                                                        time=XmlTime(12, 20, 0, 0, 0)
                                                    ),
                                                    departure=DepartureStructure(
                                                        for_boarding=False
                                                    ),
                                                    order=3
                                                ),
                                            ]
                                        ),
                                        frequency_groups=FrequencyGroupsRelStructure(
                                            choice=[
                                                HeadwayJourneyGroup(
                                                    id='hde:hjg_24o_01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Regular  Interval service between 10am and 12:00 pm'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='About every 12 minutes'
                                                        ),
                                                    ],
                                                    first_departure_time=XmlTime(10, 0, 0, 0),
                                                    last_departure_time=XmlTime(12, 0, 0, 0),
                                                    scheduled_headway_interval=XmlDuration("PT12M"),
                                                    headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                                ),
                                                HeadwayJourneyGroup(
                                                    id='hde:hjg_24o_02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Regular  Interval service between 12am and 18:00 pm'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='About every 20 minutes'
                                                        ),
                                                    ],
                                                    first_departure_time=XmlTime(12, 0, 0, 0),
                                                    last_departure_time=XmlTime(18, 0, 0, 0),
                                                    scheduled_headway_interval=XmlDuration("PT20M"),
                                                    headway_display=HeadwayUseEnumeration.DISPLAY_INSTEAD_OF_PASSING_TIMES
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='mybus:svf_12',
                            version='any',
                            name=MultilingualString(
                                value='Stops for Winter timetable for route 234 '
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='mybus:LN_234',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 234 Alpha to Charley Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 234'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='234'
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
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
