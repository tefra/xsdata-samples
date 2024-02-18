from netex.models.alternative_texts_rel_structure import DayType1
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityRuleParameter
from netex.models.alternative_texts_rel_structure import ValidityTrigger
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.participant_ref import ParticipantRef
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.relative_operator_enumeration import RelativeOperatorEnumeration
from netex.models.season_enumeration import SeasonEnumeration
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.validity_condition_ref_structure import ValidityConditionRefStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure
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
            ServiceCalendarFrame(
                id='hde:SCF01',
                version='any',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='abc',
                            xmlns='abc',
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
                        ref='hde'
                    )
                ),
                content_validity_conditions=ValidityConditionsRelStructure(
                    choice=[
                        ValidityRuleParameter(
                            id='hde:VC_ntwkf003_002_icy',
                            version='any',
                            description=MultilingualString(
                                value='Use when Icy'
                            ),
                            conditioned_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='TimetableFrame',
                                ref='abc:Tf01'
                            ),
                            with_condition_ref=ValidityConditionRefStructure(
                                version='any',
                                ref='hde:VC_ntwkf003_002_winter'
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
                        ValidityRuleParameter(
                            id='hde:VC_ntwkf003_002_winter',
                            version='any',
                            description=MultilingualString(
                                value='Use when Winter'
                            ),
                            conditioned_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='TimetableFrame',
                                ref='abc:Tf01'
                            ),
                            with_condition_ref=ValidityConditionRefStructure(
                                version='any',
                                ref='hde:rp_02_long'
                            ),
                            rule_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='DayType',
                                version='1',
                                ref='Myobj:DT001'
                            ),
                            choice=[
                                True,
                            ]
                        ),
                        ValidityRuleParameter(
                            id='hde:rp_02_long',
                            version='any',
                            description=MultilingualString(
                                value='If run time is greater than five minuets'
                            ),
                            conditioned_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='TimetableFrame',
                                ref='abc:Tf01'
                            ),
                            with_condition_ref=ValidityConditionRefStructure(
                                version='any',
                                ref='hde:vt_01'
                            ),
                            rule_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='JourneyPatternRunTime',
                                ref='JourneyPatternRunTime:JPRT_1234234'
                            ),
                            choice=[
                                'RunTime',
                                RelativeOperatorEnumeration.GT,
                                AnyElement(
                                    qname='{http://www.netex.org.uk/netex}AttributeValue',
                                    text="'PT5M'"
                                ),
                            ]
                        ),
                        ValidityTrigger(
                            id='hde:vt_01',
                            version='any',
                            description=MultilingualString(
                                value='Special event day'
                            ),
                            conditioned_object_ref=VersionOfObjectRefStructure(
                                name_of_ref_class='TimetableFrame',
                                ref='abc:Tf01'
                            )
                        ),
                    ]
                ),
                day_types=DayTypesInFrameRelStructure(
                    day_type=[
                        DayType1(
                            id='Myobj:DT001',
                            version='any',
                            name=MultilingualString(
                                value='Winter '
                            ),
                            properties=PropertiesOfDayRelStructure(
                                property_of_day=[
                                    PropertyOfDay(
                                        name=MultilingualString(
                                            value='Winter '
                                        ),
                                        seasons=[
                                            SeasonEnumeration.WINTER,
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
