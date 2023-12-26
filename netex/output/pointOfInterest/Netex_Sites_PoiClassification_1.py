from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.point_of_interest_classification import PointOfInterestClassification
from netex.models.point_of_interest_classification_hierarchies_in_frame_rel_structure import PointOfInterestClassificationHierarchiesInFrameRelStructure
from netex.models.point_of_interest_classification_hierarchy import PointOfInterestClassificationHierarchy
from netex.models.point_of_interest_classification_hierarchy_member_structure import PointOfInterestClassificationHierarchyMemberStructure
from netex.models.point_of_interest_classification_hierarchy_members_rel_structure import PointOfInterestClassificationHierarchyMembersRelStructure
from netex.models.point_of_interest_classification_ref_structure import PointOfInterestClassificationRefStructure
from netex.models.point_of_interest_classifications_in_frame_rel_structure import PointOfInterestClassificationsInFrameRelStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.site_frame import SiteFrame
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002'
    ),
    publication_refresh_interval=XmlDuration("PT5M0S"),
    data_objects=DataObjectsRelStructure(
        choice=[
            SiteFrame(
                id='poix:POI_Classifications',
                version='any',
                name=MultilingualString(
                    value='Poi Classifications'
                ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='poix',
                            xmlns='poix',
                            xmlns_url='http://www.poininfo.eu/stuff',
                            description='Point of Inteset data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='poix'
                    ),
                    default_responsibility_set_ref=ResponsibilitySetRefStructure(
                        value='EXTERNAL',
                        ref='poix:001'
                    )
                ),
                point_of_interest_classifications=PointOfInterestClassificationsInFrameRelStructure(
                    point_of_interest_classification=[
                        PointOfInterestClassification(
                            id='poix:Cl000',
                            version='any',
                            name=MultilingualString(
                                value='All'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl001',
                            version='any',
                            name=MultilingualString(
                                value='Tourist Attraction'
                            ),
                            short_name=MultilingualString(
                                value='Attraction'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl002',
                            version='any',
                            name=MultilingualString(
                                value='Museum'
                            ),
                            short_name=MultilingualString(
                                value='Museum'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl003',
                            version='any',
                            name=MultilingualString(
                                value='Art Galleriy'
                            ),
                            short_name=MultilingualString(
                                value='Gallery'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl004',
                            version='any',
                            name=MultilingualString(
                                value='Sports Facility'
                            ),
                            short_name=MultilingualString(
                                value='Sports Facility'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl005',
                            version='any',
                            name=MultilingualString(
                                value='Football Stadium'
                            ),
                            short_name=MultilingualString(
                                value='Football'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl006',
                            version='any',
                            name=MultilingualString(
                                value='Rugby Stadium'
                            ),
                            short_name=MultilingualString(
                                value='Rugby'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl007',
                            version='any',
                            name=MultilingualString(
                                value='Ice Rink'
                            ),
                            short_name=MultilingualString(
                                value='Ice Rink'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl008',
                            version='any',
                            name=MultilingualString(
                                value='Stadium'
                            ),
                            short_name=MultilingualString(
                                value='Stadium'
                            )
                        ),
                        PointOfInterestClassification(
                            id='poix:Cl009',
                            version='any',
                            name=MultilingualString(
                                value='Icerink'
                            ),
                            short_name=MultilingualString(
                                value='Icerink'
                            )
                        ),
                    ]
                ),
                point_of_interest_classification_hierarchies=PointOfInterestClassificationHierarchiesInFrameRelStructure(
                    point_of_interest_classification_hierarchy=[
                        PointOfInterestClassificationHierarchy(
                            id='poix:hm_1',
                            version='any',
                            name=MultilingualString(
                                value='Main Hierarchy'
                            ),
                            members=PointOfInterestClassificationHierarchyMembersRelStructure(
                                classification_hierarchy_member=[
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_00',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl000'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl001'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_01',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl001'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl002'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_02',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl001'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl003'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_00',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl000'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_03',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl008'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_04',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl008'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl005'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_05',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl008'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl006'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_1_06',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl009'
                                        )
                                    ),
                                ]
                            )
                        ),
                        PointOfInterestClassificationHierarchy(
                            id='poix:hm_2',
                            version='any',
                            name=MultilingualString(
                                value='Sports Hierarchy'
                            ),
                            members=PointOfInterestClassificationHierarchyMembersRelStructure(
                                classification_hierarchy_member=[
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_2_01',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl005'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_2_02',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl006'
                                        )
                                    ),
                                    PointOfInterestClassificationHierarchyMemberStructure(
                                        id='poix:hm_2_03',
                                        parent_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl004'
                                        ),
                                        point_of_interest_classification_ref=PointOfInterestClassificationRefStructure(
                                            version='any',
                                            ref='poix:Cl009'
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
