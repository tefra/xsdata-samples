from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import OperatingDay
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.day_type_assignments_in_frame_rel_structure import DayTypeAssignmentsInFrameRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operating_day_ref import OperatingDayRef
from netex.models.operating_days_in_frame_rel_structure import OperatingDaysInFrameRelStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


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
                                id='hde:AvailabilityCondition:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            ref='hde:TimetableFrameTIM_23_O'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of compact and verobose service calendar'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            ServiceCalendarFrame(
                id='hde:ServiceCalendarFrame:CAL_02',
                version='any',
                name=MultilingualString(
                    value='Service Calendar Nov 2010 ALTERNATE MORE COMPACT Coding  '
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='hde_data',
                            xmlns='hde',
                            xmlns_url='http://www.halt.de/',
                            description='Day typess'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='hde_data'
                    )
                ),
                service_calendar=ServiceCalendar(
                    id='hde:ServiceCalendar:CAL_02',
                    version='any',
                    from_date=XmlDate(2010, 11, 1),
                    to_date=XmlDate(2010, 11, 14)
                ),
                day_type_assignments=DayTypeAssignmentsInFrameRelStructure(
                    day_type_assignment=[
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-01',
                            version='any',
                            description=MultilingualString(
                                value='Monday 2010-11-01'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 1),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-02',
                            version='any',
                            description=MultilingualString(
                                value='Tuesday 2010-11-02'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 2),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-03',
                            version='any',
                            description=MultilingualString(
                                value='Wednesday 2010-11-03'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 3),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-04',
                            version='any',
                            description=MultilingualString(
                                value='Thusday 2010-11-04'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 4),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-05',
                            version='any',
                            description=MultilingualString(
                                value='MFriday 2010-11-05'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 5),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-06',
                            version='any',
                            description=MultilingualString(
                                value='Saturday 2010-11-06'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 6),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-07',
                            version='any',
                            description=MultilingualString(
                                value='Sunday 2010-11-07'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 7),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-08',
                            version='any',
                            description=MultilingualString(
                                value='Monday 2010-11-08'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 8),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-09',
                            version='any',
                            description=MultilingualString(
                                value='Tuesday 2010-11-09'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 9),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-10',
                            version='any',
                            description=MultilingualString(
                                value='Wednesday 2010-11-10'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 10),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-11',
                            version='any',
                            description=MultilingualString(
                                value='Thusday 2010-11-11'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 11),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-12',
                            version='any',
                            description=MultilingualString(
                                value='MFriday 2010-11-12'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 12),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-113',
                            version='any',
                            description=MultilingualString(
                                value='Saturday 2010-11-13'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 13),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-14',
                            version='any',
                            description=MultilingualString(
                                value='Sunday 2010-11-14'
                            ),
                            order=1,
                            choice=XmlDate(2010, 11, 14),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                    ]
                )
            ),
            ServiceCalendarFrame(
                id='hde:ServiceCalendarFrame:CAL_01',
                version='any',
                name=MultilingualString(
                    value='Service Calendar Nov 2010 '
                ),
                service_calendar=ServiceCalendar(
                    id='hde:ServiceCalendar:SC_01',
                    version='any',
                    from_date=XmlDate(2010, 11, 1),
                    to_date=XmlDate(2010, 11, 14)
                ),
                day_types=DayTypesInFrameRelStructure(
                    day_type=[
                        DayType(
                            id='hde:DayType:DT_01-MF-NH',
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
                            id='hde:DayType:DT_02-AA-NH',
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
                            id='hde:DayType:DT_03-WE-NH',
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
                            id='hde:DayType:DT_04-AA-NH',
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
                operating_days=OperatingDaysInFrameRelStructure(
                    operating_day=[
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-01',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 1)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-02',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 2)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-03',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 3)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-04',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 4)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-05',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 5)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-06',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 6)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-07',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 7)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-08',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 8)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-09',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 9)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-10',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 10)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-11',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 11)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-12',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 12)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-13',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 13)
                        ),
                        OperatingDay(
                            id='hde:OperatingDay:OPDAY_2010-11-14',
                            version='any',
                            calendar_date=XmlDate(2010, 11, 14)
                        ),
                    ]
                ),
                day_type_assignments=DayTypeAssignmentsInFrameRelStructure(
                    day_type_assignment=[
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-01b',
                            version='any',
                            description=MultilingualString(
                                value='Monday 2010-11-01'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-01'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-02b',
                            version='any',
                            description=MultilingualString(
                                value='Tuesday 2010-11-02'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-02'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-03b',
                            version='any',
                            description=MultilingualString(
                                value='Wednesday 2010-11-03'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-03'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-04b',
                            version='any',
                            description=MultilingualString(
                                value='Thusday 2010-11-04'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-04'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-05b',
                            version='any',
                            description=MultilingualString(
                                value='MFriday 2010-11-05'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-05'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-06b',
                            version='any',
                            description=MultilingualString(
                                value='Saturday 2010-11-06'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-06'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-07b',
                            version='any',
                            description=MultilingualString(
                                value='Sunday 2010-11-07'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-07'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-08b',
                            version='any',
                            description=MultilingualString(
                                value='Monday 2010-11-08'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-08'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-09b',
                            version='any',
                            description=MultilingualString(
                                value='Tuesday 2010-11-09'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-09'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-10b',
                            version='any',
                            description=MultilingualString(
                                value='Wednesday 2010-11-10'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-10'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-11b',
                            version='any',
                            description=MultilingualString(
                                value='Thusday 2010-11-11'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-11'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-12b',
                            version='any',
                            description=MultilingualString(
                                value='MFriday 2010-11-12'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-12'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_01-MF-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-113b',
                            version='any',
                            description=MultilingualString(
                                value='Saturday 2010-11-13'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-13'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                        DayTypeAssignment(
                            id='hde:DayTypeAssignment:DayAsgn_2010-11-14b',
                            version='any',
                            description=MultilingualString(
                                value='Sunday 2010-11-14'
                            ),
                            order=1,
                            choice=OperatingDayRef(
                                version='any',
                                ref='hde:OperatingDay:OPDAY_2010-11-14'
                            ),
                            day_type_ref=DayTypeRef(
                                version='any',
                                ref='hde:DayType:DT_03-WE-NH'
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
