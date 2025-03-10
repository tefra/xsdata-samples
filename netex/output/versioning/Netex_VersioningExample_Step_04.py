from decimal import Decimal
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import DayTypesRelStructure
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.general_frame_member import GeneralFrameMember
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.general_version_frame_structure import GeneralFrame
from netex.models.general_version_frame_structure import GeneralFrameMembersRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.modification_set_enumeration import ModificationSetEnumeration
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
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.version import Version
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_ref_structure import VersionRefStructure
from netex.models.version_status_enumeration import VersionStatusEnumeration
from netex.models.version_type_enumeration import VersionTypeEnumeration
from netex.models.versions_rel_structure import VersionsRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        ServiceFrameRef(
                            ref='mybus:ntwkf001'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Versioning Example Step 04'
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
                version='004',
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
                        ref='mybus:RS_10'
                    )
                ),
                versions=VersionsRelStructure(
                    version_ref_or_version=[
                        Version(
                            id='mybus:ntwkf001',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            version='004',
                            status=VersionStatusEnumeration.VERSIONED,
                            description=MultilingualString(
                                value='Version 4 of Composite Frame '
                            ),
                            version_type=VersionTypeEnumeration.BASELINE,
                            derived_from_version_ref=VersionRefStructure(
                                version='003',
                                ref='mybus:ntwkf001'
                            )
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceCalendarFrame(
                            id='mybus:ntwkf001@calendar',
                            version='003',
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='mybus:ntwkf001@calendar',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='003',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 3 of Service Calendar Frame: ntwkf001'
                                        ),
                                        derived_from_version_ref=VersionRefStructure(
                                            version='002',
                                            ref='mybus:ntwkf001'
                                        )
                                    ),
                                    Version(
                                        id='mybus:DT001_MF',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of Day Type  DT001_MF'
                                        )
                                    ),
                                    Version(
                                        id='mybus:DT002_MFHols',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of Day Type DT002_MFHols'
                                        )
                                    ),
                                ]
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
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
                                    DayType(
                                        id='mybus:DT002_MFHols',
                                        created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Monday to Friday, Holidays'
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
                                                        HolidayTypeEnumeration.ANY_HOLIDAY,
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
                                            modification=ModificationEnumeration.REVISE,
                                            version='002',
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
                                                    DayTypeRef(
                                                        version='001',
                                                        ref='mybus:DT002_MFHols'
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            changed=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='004',
                            derived_from_version_ref_attribute='003',
                            name=MultilingualString(
                                value='My Network  Version 4 with three stops in it '
                            ),
                            baseline_version_frame_ref=VersionRefStructure(
                                value='EXTERNAL',
                                ref='mybus:003'
                            ),
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='mybus:ntwkf001@service',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='004',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 4 of Service Frame ntwkf001 '
                                        ),
                                        version_type=VersionTypeEnumeration.BASELINE,
                                        derived_from_version_ref=VersionRefStructure(
                                            version='003',
                                            ref='mybus:ntwkf001'
                                        )
                                    ),
                                    Version(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
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
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        version='002',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 2 of StopPoint SSP001B '
                                        ),
                                        derived_from_version_ref=VersionRefStructure(
                                            version='001',
                                            ref='mybus:SSP0002B'
                                        )
                                    ),
                                    Version(
                                        id='mybus:SSP0003C',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of StopPoint SSP003C '
                                        )
                                    ),
                                    Version(
                                        id='mybu:SL_AtoB01',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='002',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 2 of ServiceLink SL_AtoB01 '
                                        ),
                                        derived_from_version_ref=VersionRefStructure(
                                            version='001',
                                            ref='mybu:SL_AtoB01'
                                        )
                                    ),
                                    Version(
                                        id='mybu:SL_BtoA01',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of ServiceLink  SL_BtoA01 '
                                        )
                                    ),
                                    Version(
                                        id='mybus:SP_001',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of ServicePattern  SP_001 '
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
                                        changed=XmlDateTime(2010, 6, 18, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        name=MultilingualString(
                                            value='Haltstelle B'
                                        ),
                                        description=MultilingualString(
                                            value='Version two of stop B'
                                        ),
                                        private_code=PrivateCode(
                                            value='mycodeB'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0003C',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Haltstelle C'
                                        ),
                                        description=MultilingualString(
                                            value='Version one of stop C'
                                        )
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='mybu:SL_AtoB01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        name=MultilingualString(
                                            value='Version one of Link from A to B'
                                        ),
                                        distance=Decimal('1.12'),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0001A'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybu:SL_BtoC01',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Version one of Link from B to C'
                                        ),
                                        distance=Decimal('1.25'),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='mybus:SSP0003C'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybu:SL_BtoA01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 51, 0, 0),
                                        changed=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        modification=ModificationEnumeration.DELETE,
                                        version='002',
                                        name=MultilingualString(
                                            value='Version two - deleting  Link from B to A'
                                        ),
                                        distance=Decimal('1.01'),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0001A'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern=[
                                    ServicePattern(
                                        id='mybus:SP_001',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='From A to C, version 1'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='002',
                                                        ref='mybus:SSP0001A'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='002',
                                                        ref='mybus:SSP0002B'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='mybus:SSP0003C'
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
            ),
            GeneralFrame(
                id='mybus:GeneralFrame:ntwkf001_Delta',
                created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                changed=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                modification=ModificationEnumeration.REVISE,
                version='004',
                responsibility_set_ref_attribute='mybus:RS_10',
                name=MultilingualString(
                    value='ntwkf001 experssed as a delta - only the removed stop is described - Baseline is version 3'
                ),
                baseline_version_frame_ref=VersionRefStructure(
                    version='003',
                    ref='mybus:GeneralFrame:ntwkf001'
                ),
                members=GeneralFrameMembersRelStructure(
                    modification_set=ModificationSetEnumeration.CHANGES_ONLY,
                    choice=[
                        GeneralFrameMember(
                            id='mybus:EntityInVersionInFrame:ntwkf001_05',
                            modification=ModificationEnumeration.DELETE,
                            choice=ServiceLinkRef(
                                version='002',
                                ref='mybu:SL_BtoA01'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:EntityInVersionInFrame:ntwkf001_02',
                            modification=ModificationEnumeration.REVISE,
                            choice=ScheduledStopPointRef(
                                version='001',
                                ref='mybus:SSP0003C'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:EntityInVersionInFrame:ntwkf001_06',
                            choice=ServiceLinkRef(
                                version='001',
                                ref='mybu:SL_BtoC01'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:EntityInVersionInFrame:ntwkf001_07',
                            choice=ServicePatternRef(
                                version='001',
                                ref='mybus:SP_001'
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
