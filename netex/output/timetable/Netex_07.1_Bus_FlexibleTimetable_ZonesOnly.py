from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import TimebandVersionedChildStructure
from netex.models.alternative_texts_rel_structure import TimebandsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.booking_access_enumeration import BookingAccessEnumeration
from netex.models.bus_submode_enumeration import BusSubmodeEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.contained_availability_conditions_rel_structure import ContainedAvailabilityConditionsRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.exterior import Exterior
from netex.models.flexible_area import FlexibleArea
from netex.models.flexible_line import FlexibleLine
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.flexible_stop_place_version_structure import FlexibleStopPlaceVersionStructure
from netex.models.flexible_stop_places_in_frame_rel_structure import FlexibleStopPlacesInFrameRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.line_refs_rel_structure import LineRefsRelStructure
from netex.models.line_view import LineView
from netex.models.linear_ring import LinearRing
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.polygon import Polygon
from netex.models.pos import Pos
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.transport_submode import TransportSubmode
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
        value='Example  of simple flexible timetable  , zones only  \n\t\n1. OVERVIEW\n============\n\n   The servIce has two zones     Sigma   and  Tau\n \n\t SIgma has a single area,  Tau is made up of  two areas \n\t \n\tThere are on demand services between specified start and end time\n\t\n\t   9 to 5 Monday to Friday.\n\t   Booking starts 8 to 12: 1 to 4:30\n \t\t\t\t\t\t\t\t\t\t\n day\n\n==================================\n2. DETAILS\n\n  FLEXIBLE LINE  mybus:FL_24\n\t\thas booking  and references two  two flexible stop places \n\nFLEXIBLE STOP PLACES defines the geometry of the XOnes\n\t    A)    FLEXIBLE STOP PLAcE:  mybus:fsp_Sigma   \n\t\t\t\t\t with a single FLEXIBLE STOP AREA:fsp_Sigma:  \t\t\t\t\t\t \n\t\tB)   FLEXIBLE STOP PLAcE: mybus:fsp_Tau\t\t\t\t\t \n\t\t\t\t with a two FLEXIBLE STOP AREAs     \t\n\t\t\t\t\t :mybus:fa_Tau_01\n\t\t\t \t :mybus:fa_Tau_02\n \n A SERVICE CALENDAR FRAME is used to contain the DAY TYPEs etc \n\n This has FLEXIBLE BOOKING TIMES with avalabiliuty conbditiosn for the booking and service \n   \nA COMPOSITE FRAME is used to group the component FRAMEs\n  \n\t\tA SITE   FRAME is used to contain the FLEXIBLE STOP PLACEs , etc\n\t\tA SERVICE  FRAME is used to contain the     LINEs, etc\n\t\tA TIMETABLE FRAME is used to define the Servce AVAILABILITY and the  the Booking times     \n\t\t\t\nThe Calendar is shown coded as\n      Compact : OPERATING DAYs are assumed for each calendar date within the period of the calendar \n\t\n\t'
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
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                frames=FramesRelStructure(
                    choice=[
                        SiteFrame(
                            id='mybus:svf_24',
                            version='1',
                            name=MultilingualString(
                                value='Geometry of Zones  for Winter timetable for Flexible Route 24 '
                            ),
                            flexible_stop_places=FlexibleStopPlacesInFrameRelStructure(
                                flexible_stop_place=[
                                    FlexibleStopPlace(
                                        id='mybus:fsp_Sigma',
                                        version='any',
                                        name=MultilingualString(
                                            value='Flexible Zone Sigma'
                                        ),
                                        short_name=MultilingualString(
                                            value='Sigma'
                                        ),
                                        description=[
                                            MultilingualString(
                                                value='Area around Alphavilee'
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
                                                FlexibleArea(
                                                    id='mybus:fa_Sigma',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ZONE Sigma  Area - corresponds to whole of Zone S'
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Sigma'
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
                                                    polygon=Polygon(
                                                        id='a1234',
                                                        srs_name='wgs84',
                                                        exterior=Exterior(
                                                            linear_ring=LinearRing(
                                                                pos_or_point_property_or_pos_list=[
                                                                    Pos(
                                                                        value=[
                                                                            12345.78,
                                                                            2345.2,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12345.76,
                                                                            2346.2,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12345.88,
                                                                            2345.3,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12346.18,
                                                                            2344.2,
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
                                        ),
                                        lines=LineRefsRelStructure(
                                            flexible_line_ref_or_line_ref=[
                                                FlexibleLineRef(
                                                    version='any',
                                                    ref='mybus:FL_24'
                                                ),
                                            ]
                                        )
                                    ),
                                    FlexibleStopPlace(
                                        id='mybus:fsp_Tau',
                                        version='any',
                                        name=MultilingualString(
                                            value='Flexible Zone Tau'
                                        ),
                                        short_name=MultilingualString(
                                            value='Tau'
                                        ),
                                        description=[
                                            MultilingualString(
                                                value='Area around Beta ville'
                                            ),
                                        ],
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('53.0000'),
                                                latitude=Decimal('0.1000')
                                            )
                                        ),
                                        areas=FlexibleStopPlaceVersionStructure.Areas(
                                            choice=[
                                                FlexibleArea(
                                                    id='mybus:fa_Tau_01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ZONE Tau    Area 1 -   '
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Sigma 1'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    12355.78,
                                                                    2344.2,
                                                                ]
                                                            ),
                                                            precision=Decimal('12')
                                                        )
                                                    ),
                                                    polygon=Polygon(
                                                        id='b1234',
                                                        srs_name='wgs84',
                                                        exterior=Exterior(
                                                            linear_ring=LinearRing(
                                                                pos_or_point_property_or_pos_list=[
                                                                    Pos(
                                                                        value=[
                                                                            12355.78,
                                                                            2345.2,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12355.76,
                                                                            2355.2,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.88,
                                                                            2365.2,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.18,
                                                                            2355.1,
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
                                                    id='mybus:fa_Tau_02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ZONE Tau    Area 2 -   '
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Sigma 2'
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
                                                    polygon=Polygon(
                                                        id='c1234',
                                                        srs_name='wgs84',
                                                        exterior=Exterior(
                                                            linear_ring=LinearRing(
                                                                pos_or_point_property_or_pos_list=[
                                                                    Pos(
                                                                        value=[
                                                                            12356.77,
                                                                            2355.1,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12357.75,
                                                                            2356.1,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12357.88,
                                                                            2375.1,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12356.18,
                                                                            2378.1,
                                                                        ]
                                                                    ),
                                                                    Pos(
                                                                        value=[
                                                                            12354.18,
                                                                            2378.1,
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
                                        ),
                                        lines=LineRefsRelStructure(
                                            flexible_line_ref_or_line_ref=[
                                                FlexibleLineRef(
                                                    version='any',
                                                    ref='mybus:FL_24'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='mybus:svf_24',
                            version='1',
                            name=MultilingualString(
                                value='Lines for Winter timetable for route 24 '
                            ),
                            lines=LinesInFrameRelStructure(
                                flexible_line_or_line=[
                                    FlexibleLine(
                                        id='mybus:FL_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Sigma  to Tau FLEXIBLE SERVICE '
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        transport_submode=TransportSubmode(
                                            choice=BusSubmodeEnumeration.DEMAND_AND_RESPONSE_BUS
                                        ),
                                        public_code='24',
                                        flexible_line_type=FlexibleLineTypeEnumeration.FLEXIBLE_AREAS_ONLY,
                                        booking_access=BookingAccessEnumeration.PUBLIC,
                                        latest_booking_time=XmlTime(16, 30, 0, 0),
                                        minimum_booking_period=XmlDuration("PT30M")
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='hde:TIM_02',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='hde:AC_runs_02',
                                            version='any',
                                            description=MultilingualString(
                                                value='Operating  times for DRT service 24'
                                            ),
                                            is_available=True,
                                            day_types=DayTypesRelStructure(
                                                choice=[
                                                    DayTypeRef(
                                                        version='any',
                                                        ref='hde:DT_01-MF-NotHoliday'
                                                    ),
                                                ]
                                            ),
                                            timebands=TimebandsRelStructure(
                                                timeband_ref_or_timeband=[
                                                    TimebandVersionedChildStructure(
                                                        id='hde:AC_runs_01',
                                                        version='any',
                                                        start_time=XmlTime(9, 0, 0, 0),
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
                            version='1',
                            name=MultilingualString(
                                value='TimetableNov to Jan 2011   '
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ],
                            line_view=LineView(
                                flexible_line_ref_or_line_ref=FlexibleLineRef(
                                    version='any',
                                    ref='mybus:FL_24'
                                )
                            ),
                            booking_times=ContainedAvailabilityConditionsRelStructure(
                                availability_condition=[
                                    AvailabilityCondition(
                                        id='hde:AC_booking_01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Booking times for service'
                                        ),
                                        is_available=True,
                                        day_types=DayTypesRelStructure(
                                            choice=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='hde:DT_01-MF-NotHoliday'
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='hde:AC_booking_01',
                                                    version='any',
                                                    start_time=XmlTime(8, 30, 0, 0),
                                                    end_time_or_day_offset_or_duration=[
                                                        XmlTime(12, 0, 0, 0),
                                                    ]
                                                ),
                                                TimebandVersionedChildStructure(
                                                    id='hde:AC_booking_02',
                                                    version='any',
                                                    start_time=XmlTime(13, 0, 0, 0),
                                                    end_time_or_day_offset_or_duration=[
                                                        XmlTime(16, 30, 0, 0),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='hde:CAL_02',
                            version='1',
                            name=MultilingualString(
                                value='Service Calendar Nov to Jan 2011   '
                            ),
                            service_calendar=ServiceCalendar(
                                id='hde:CAL_02',
                                version='any',
                                from_date=XmlDate(2010, 11, 1),
                                to_date=XmlDate(2011, 1, 14)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                fare_day_type_or_organisation_day_type_or_day_type=[
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
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
