from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityRuleParameter
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.entities_in_version_rel_structure import GeneralFrame
from netex.models.entities_in_version_rel_structure import GeneralFrameMembersRelStructure
from netex.models.general_frame_member import GeneralFrameMember
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.participant_ref import ParticipantRef
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.relative_operator_enumeration import RelativeOperatorEnumeration
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure
from netex.models.version_ref_structure import VersionRefStructure
from xsdata.formats.dataclass.models.generics import AnyElement
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
        )
    ),
    publication_refresh_interval=XmlDuration("P1Y2M3DT10H30M0S"),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mybus:CompositeFrame:CF1',
                version='any',
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
                            id='mybus:ServiceFrame:ntwkf002',
                            version='001',
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='mybus:ServiceLink:SL_AtoB01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Version one of Link from A to B'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0001A'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0002B'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybus:ServiceLink:SL_BtoC01',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Version one of Link from B to C'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0002B'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0003C'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybus:ServiceLink:SL_AtoC01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Version one of Link from A to C'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0001A'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0003C'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='mybus:ServicePattern:SP001',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='From A to B to  C, Normal condiation '
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='mybus:StopPointInJourneyPattern:SP001_01',
                                                    version='001',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        value='EXTERNAL',
                                                        ref='mybus:ScheduledStopPoint:SSP0001A'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:StopPointInJourneyPattern:SP001_02',
                                                    version='001',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        value='EXTERNAL',
                                                        ref='mybus:ScheduledStopPoint:SSP0002B'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:StopPointInJourneyPattern:SP001_03',
                                                    version='001',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        value='EXTERNAL',
                                                        ref='mybus:ScheduledStopPoint:SSP0003C'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServicePattern(
                                        id='mybus:ServicePattern:SP003',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='From A to C, direct - Icy conditions, omit B '
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='mybus:StopPointInJourneyPattern:SP003_01',
                                                    version='001',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        ref='mybus:ScheduledStopPoint:SSP0001A'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:StopPointInJourneyPattern:SP003_02',
                                                    version='001',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        ref='mybus:ScheduledStopPoint:SSP0003C'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        GeneralFrame(
                            id='mybus:GeneralFrame:ntwkf002',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='mybus:AvailabilityCondition:VC_ntwkf002_002_mf',
                                            created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                            version='any',
                                            description=MultilingualString(
                                                value='Use when no ice'
                                            ),
                                            from_date=XmlDateTime(2010, 5, 17, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 5, 17, 0, 0, 0, 0, 0),
                                            day_types=DayTypesRelStructure(
                                                day_type_ref_or_day_type=[
                                                    DayTypeRef(
                                                        value='EXTERNAL',
                                                        ref='mybus:DayType:DT001_MF'
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
                            version='002',
                            responsibility_set_ref_attribute='mybus:ResponsibilitySet:RS_10',
                            name=MultilingualString(
                                value='ntwkf002  - Frame with SERVICE PATTERN for Normal conditions'
                            ),
                            baseline_version_frame_ref=VersionRefStructure(
                                version='001',
                                ref='mybus:GeneralFrame'
                            ),
                            members=GeneralFrameMembersRelStructure(
                                choice=[
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_01',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ScheduledStopPointRef(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0001A'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_02',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ScheduledStopPointRef(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0001B'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_05',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ScheduledStopPointRef(
                                            value='EXTERNAL',
                                            ref='mybus:ScheduledStopPoint:SSP0001C'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:ntwkf002_03',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=DayTypeRef(
                                            value='EXTERNAL',
                                            ref='mybus:DayType:DT001_MF'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_04',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ServiceLinkRef(
                                            version='001',
                                            ref='mybus:ServiceLink:SL_AtoB01'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_06',
                                        choice=ServiceLinkRef(
                                            version='001',
                                            ref='mybus:ServiceLink:SL_BtoC01'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf002_07',
                                        choice=ServicePatternRef(
                                            version='001',
                                            ref='mybus:ServicePattern:SP001'
                                        )
                                    ),
                                ]
                            )
                        ),
                        GeneralFrame(
                            id='mybus:GeneralFrame:ntwkf003',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        ValidityRuleParameter(
                                            id='mybus:ValidityRuleParameter:VC_ntwkf003_002_icy',
                                            created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                            version='any',
                                            responsibility_set_ref_attribute='mybus:ResponsibilitySet:RS_10',
                                            description=MultilingualString(
                                                value='Use when Icy'
                                            ),
                                            rule_object_ref=VersionOfObjectRefStructure(
                                                value='EXTERNAL',
                                                name_of_ref_class='Weather',
                                                ref='Myobj:Cur001'
                                            ),
                                            choice=[
                                                'roadCondition',
                                                RelativeOperatorEnumeration.EQ,
                                                AnyElement(
                                                    qname='{http://www.netex.org.uk/netex}AttributeValue',
                                                    text='icy'
                                                ),
                                            ]
                                        ),
                                        AvailabilityCondition(
                                            id='mybus:AvailabilityCondition:VC_ntwkf003_002_mf',
                                            created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                            version='any',
                                            responsibility_set_ref_attribute='mybus:ResponsibilitySet:RS_10',
                                            description=MultilingualString(
                                                value='Use when winter MF'
                                            ),
                                            from_date=XmlDateTime(2010, 5, 17, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 5, 17, 0, 0, 0, 0, 0),
                                            day_types=DayTypesRelStructure(
                                                day_type_ref_or_day_type=[
                                                    DayTypeRef(
                                                        ref='mybus:DayType:DT001_MF'
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
                            version='002',
                            responsibility_set_ref_attribute='mybus:ResponsibilitySet:RS_10',
                            name=MultilingualString(
                                value='ntwkf003 Different Frame  with a different condition - a different frame'
                            ),
                            baseline_version_frame_ref=VersionRefStructure(
                                version='001',
                                ref='mybus:GeneralFrame:ntwkf001'
                            ),
                            members=GeneralFrameMembersRelStructure(
                                choice=[
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf003_01',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ScheduledStopPointRef(
                                            ref='mybus:ScheduledStopPoint:SSP0001A'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf003_05',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ScheduledStopPointRef(
                                            ref='mybus:ScheduledStopPoint:SSP0001C'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf003_03',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=DayTypeRef(
                                            ref='mybus:DayType:DT001_MF'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf003_04',
                                        modification=ModificationEnumeration.REVISE,
                                        choice=ServiceLinkRef(
                                            version='001',
                                            ref='mybus:ServiceLink:SL_AtoC01'
                                        )
                                    ),
                                    GeneralFrameMember(
                                        id='mybus:GeneralFrameMember:ntwkf003_07',
                                        choice=ServicePatternRef(
                                            ref='mybus:ServicePattern:SP002'
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
