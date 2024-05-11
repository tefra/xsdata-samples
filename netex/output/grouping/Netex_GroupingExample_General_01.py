from netex.models.class_ref import ClassRef
from netex.models.class_refs_rel_structure import ClassRefsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.general_group_of_entities import GeneralGroupOfEntities
from netex.models.group_of_entities_in_frame_rel_structure import GroupOfEntitiesInFrameRelStructure
from netex.models.group_of_tariff_zones import GroupOfTariffZones
from netex.models.groups_of_tariff_zones_in_frame_rel_structure import GroupsOfTariffZonesInFrameRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.object_refs_rel_structure import ObjectRefsRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.purpose_of_grouping import PurposeOfGrouping
from netex.models.purpose_of_grouping_ref import PurposeOfGroupingRef
from netex.models.resource_frame import ResourceFrame
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.site_frame import SiteFrame
from netex.models.tariff_zone_ref import TariffZoneRef
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.value_set import ValueSet
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime


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
    description=MultilingualString(
        value='Example of simpleGrouping  '
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            ResourceFrame(
                id='mybus:Example_Groups_of_Entities',
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
                types_of_value=TypesOfValueInFrameRelStructure(
                    choice=[
                        ValueSet(
                            id='mybus:Purposes_of_Grouping',
                            version='001',
                            name=MultilingualString(

                            ),
                            values=TypesOfValueStructure(
                                type_of_value_or_type_of_entity=[
                                    PurposeOfGrouping(
                                        id='mybus:My_Purpose',
                                        version='any',
                                        name=MultilingualString(
                                            value='Group of Scheduled StopPoints and Links'
                                        ),
                                        classes=ClassRefsRelStructure(
                                            class_ref=[
                                                ClassRef(
                                                    name_of_class='ScheduledStopPoint'
                                                ),
                                                ClassRef(
                                                    name_of_class='ServiceLink'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            class_of_values='PurposeOfGrouping'
                        ),
                    ]
                ),
                groups_of_entities=GroupOfEntitiesInFrameRelStructure(
                    choice=[
                        GeneralGroupOfEntities(
                            id='mybus:GGE001',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            version='001',
                            name=MultilingualString(
                                value='My Group'
                            ),
                            purpose_of_grouping_ref=PurposeOfGroupingRef(
                                version='any',
                                ref='mybus:My_Purpose'
                            ),
                            members=ObjectRefsRelStructure(
                                choice=[
                                    ScheduledStopPointRef(
                                        ref='mybus:SSP0001A',
                                        version_ref='EXTERNAL'
                                    ),
                                    ScheduledStopPointRef(
                                        ref='mybus:SSP0002B',
                                        version_ref='EXTERNAL'
                                    ),
                                    ScheduledStopPointRef(
                                        ref='mybus:SSP0003CA',
                                        version_ref='EXTERNAL'
                                    ),
                                    ServiceLinkRef(
                                        ref='mybus:SL_AtoB01'
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
            SiteFrame(
                id='mybus:ExampleGroupOfTariffZones',
                version='any',
                groups_of_tariff_zones=GroupsOfTariffZonesInFrameRelStructure(
                    group_of_tariff_zones=[
                        GroupOfTariffZones(
                            id='mybus:InnerOslo',
                            version='any',
                            members=TariffZoneRefsRelStructure(
                                tariff_zone_ref=[
                                    TariffZoneRef(
                                        ref='mybus:ZoneA',
                                        version_ref='EXTERNAL'
                                    ),
                                    TariffZoneRef(
                                        ref='mybus:ZoneB',
                                        version_ref='EXTERNAL'
                                    ),
                                ]
                            )
                        ),
                        GroupOfTariffZones(
                            id='mybus:GreaterOslo',
                            version='any',
                            members=TariffZoneRefsRelStructure(
                                tariff_zone_ref=[
                                    TariffZoneRef(
                                        ref='mybus:ZoneC',
                                        version_ref='EXTERNAL'
                                    ),
                                    TariffZoneRef(
                                        ref='mybus:ZoneD',
                                        version_ref='EXTERNAL'
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
