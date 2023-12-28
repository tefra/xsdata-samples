from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.entities_in_version_rel_structure import GeneralFrame
from netex.models.entities_in_version_rel_structure import GeneralFrameMembersRelStructure
from netex.models.general_frame_member import GeneralFrameMember
from netex.models.multilingual_string import MultilingualString
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_ref_structure import VersionRefStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 8, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 8, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002'
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Versioning Example Step 05 Variant using GENERAL FRAME references.'
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
                                version='003',
                                description=MultilingualString(
                                    value='Use when no ice'
                                ),
                                from_date=XmlDateTime(2010, 5, 17, 0, 0, 0, 0, 0),
                                to_date=XmlDateTime(2011, 5, 17, 0, 0, 0, 0, 0),
                                day_types=DayTypesRelStructure(
                                    day_type_ref_or_day_type=[
                                        DayTypeRef(
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
                        ref='mybus:RS_10'
                    )
                ),
                members=GeneralFrameMembersRelStructure(
                    choice=[
                        GeneralFrameMember(
                            id='mybus:ntwkf001_01',
                            choice=ScheduledStopPointRef(
                                ref='mybus:SSP0001A'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_02',
                            choice=ScheduledStopPointRef(
                                ref='mybus:SSP0001B'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_05',
                            choice=ScheduledStopPointRef(
                                ref='mybus:SSP0001C'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_03',
                            choice=DayTypeRef(
                                ref='mybus:DT001_MF'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_04',
                            choice=ServiceLinkRef(
                                ref='mybu:SL_AtoB01'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_06',
                            choice=ServiceLinkRef(
                                ref='mybu:SL_BtoC01'
                            )
                        ),
                        GeneralFrameMember(
                            id='mybus:ntwkf001_07',
                            choice=ServicePatternRef(
                                ref='mybus:SP001'
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
