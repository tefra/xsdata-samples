from decimal import Decimal
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.entities_in_version_rel_structure import GeneralFrame
from netex.models.entities_in_version_rel_structure import GeneralFrameMembersRelStructure
from netex.models.general_frame_ref import GeneralFrameRef
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.private_code import PrivateCode
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.service_link import ServiceLink
from netex.models.service_pattern import ServicePattern
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_ref_structure import VersionRefStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 8, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 8, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    version_frame_ref=[
                        GeneralFrameRef(
                            value='REQUEST',
                            ref='mynet:123'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Versioning Example Step 05. Use a general frame rather than a newtork frame '
    ),
    data_objects=DataObjectsRelStructure(
        common_frame=[
            GeneralFrame(
                id='mybus:ntwkf001',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        validity_condition_ref_or_validity_condition=[
                            AvailabilityCondition(
                                id='mybus:VC002_mf',
                                created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                modification=ModificationEnumeration.REVISE,
                                version='003',
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
                changed=XmlDateTime(2010, 5, 22, 10, 30, 51, 0, 0),
                modification=ModificationEnumeration.REVISE,
                version='005',
                derived_from_version_ref_attribute='004',
                responsibility_set_ref_attribute='mybus:RS_10',
                name=MultilingualString(
                    value='My Network  Version 4 One link has been removed. Baseline is version 3 as Links  needs exist'
                ),
                baseline_version_frame_ref=VersionRefStructure(
                    value='EXTERNAL',
                    ref='mybus:GeneralFrame:003'
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
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    ),
                    default_responsibility_set_ref=ResponsibilitySetRefStructure(
                        value='EXTERNAL',
                        ref='mybus:RS_10'
                    )
                ),
                members=GeneralFrameMembersRelStructure(
                    choice=[
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
                        ServiceLink(
                            id='mybu:SL_AtoB01',
                            created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                            changed=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
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
                        ServicePattern(
                            id='mybus:SP001',
                            created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                            changed=XmlDateTime(2010, 5, 22, 10, 30, 51, 0, 0),
                            version='002',
                            name=MultilingualString(
                                value='From A to D, version 2'
                            ),
                            points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                stop_point_in_journey_pattern=[
                                    StopPointInJourneyPattern(
                                        id='mybus:P001_01',
                                        version='002',
                                        order=1,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='002',
                                            ref='mybus:SSP0001A'
                                        )
                                    ),
                                    StopPointInJourneyPattern(
                                        id='mybus:P001_02',
                                        version='002',
                                        order=2,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        ),
                                        for_alighting=True,
                                        for_boarding=False
                                    ),
                                    StopPointInJourneyPattern(
                                        id='mybus:P001_03',
                                        version='001',
                                        order=3,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='001',
                                            ref='mybus:SSP0003C'
                                        )
                                    ),
                                ]
                            )
                        ),
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
                    ]
                )
            ),
        ]
    )
)
