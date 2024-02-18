from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType1
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.private_code import PrivateCode
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.version import Version
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_ref_structure import VersionRefStructure
from netex.models.version_status_enumeration import VersionStatusEnumeration
from netex.models.version_type_enumeration import VersionTypeEnumeration
from netex.models.versions_rel_structure import VersionsRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        ServiceFrameRef(
                            value='REQUEST',
                            ref='mybus:ntwkf001'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Versioning Example Step 02'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mybus:ntwkf001',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            AvailabilityCondition(
                                id='mybus:ntwkf001',
                                version='any',
                                from_date=XmlDateTime(2010, 5, 17, 0, 0, 0, 0, 0),
                                to_date=XmlDateTime(2011, 5, 17, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                ],
                version='002',
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
                    ),
                    default_responsibility_set_ref=ResponsibilitySetRefStructure(
                        value='EXTERNAL',
                        ref='mybus:RS_10'
                    )
                ),
                versions=VersionsRelStructure(
                    version_ref_or_version=[
                        Version(
                            id='mybus:ntwkf001',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            version='002',
                            status=VersionStatusEnumeration.VERSIONED,
                            description=MultilingualString(
                                value='Version 2 of Composite Frame '
                            ),
                            version_type=VersionTypeEnumeration.BASELINE,
                            derived_from_version_ref=VersionRefStructure(
                                version='001',
                                ref='mybus:ntwkf001'
                            )
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceCalendarFrame(
                            id='mybus:ntwkf001@calendar',
                            version='001',
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='mybus:ntwkf001@calendar',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of Service Calendar Frame: ntwkf001'
                                        )
                                    ),
                                    Version(
                                        id='mybus:DT001_MF',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of Day Type '
                                        )
                                    ),
                                ]
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType1(
                                        id='mybus:DT001_MF',
                                        created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Monday to Friday'
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
                                                        HolidayTypeEnumeration.WORKING_DAY,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='mybus:ntwkf001@service',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='mybus:VC002_mf',
                                            created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                            version='001',
                                            description=MultilingualString(
                                                value='Use when no ice'
                                            ),
                                            from_date=XmlDateTime(2010, 5, 17, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 5, 17, 0, 0, 0, 0, 0),
                                            day_types=DayTypesRelStructure(
                                                day_type_ref_or_day_type=[
                                                    DayTypeRef(
                                                        version='001',
                                                        ref='mybus:DT001_MF'
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            changed=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='002',
                            derived_from_version_ref_attribute='001',
                            name=MultilingualString(
                                value='My Network  Version 2 with two stops in it and a VALIDITY conditiona added  in it'
                            ),
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='mybus:ntwkf001@service',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='002',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 2 of Service Frame ntwkf001 '
                                        ),
                                        version_type=VersionTypeEnumeration.BASELINE,
                                        derived_from_version_ref=VersionRefStructure(
                                            version='001',
                                            ref='mybus:ntwkf001'
                                        )
                                    ),
                                    Version(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        version='002',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 2 of StopPoint SSP001A '
                                        ),
                                        derived_from_version_ref=VersionRefStructure(
                                            version='001',
                                            ref='mybus:SSP0001A'
                                        )
                                    ),
                                    Version(
                                        id='mybus:SSP0002B',
                                        created=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of StopPoint SSP001B '
                                        )
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        derived_from_version_ref_attribute='001',
                                        name=MultilingualString(
                                            value='Haltstelle A - Museum'
                                        ),
                                        description=MultilingualString(
                                            value='Version two of stop A. Name is Changed'
                                        ),
                                        private_code=PrivateCode(
                                            value='mycodeA'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0002B',
                                        created=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Haltstelle B'
                                        ),
                                        description=MultilingualString(
                                            value='Version one of stop B'
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
