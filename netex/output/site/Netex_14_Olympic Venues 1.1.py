from decimal import Decimal
from netex.models.alternative_name import AlternativeName
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.check_constraint import CheckConstraint
from netex.models.check_constraint_delay import CheckConstraintDelay
from netex.models.check_constraint_delays_rel_structure import CheckConstraintDelaysRelStructure
from netex.models.check_constraints_rel_structure import CheckConstraintsRelStructure
from netex.models.check_direction_enumeration import CheckDirectionEnumeration
from netex.models.check_process_type_enumeration import CheckProcessTypeEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.congestion_enumeration import CongestionEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.entrance_enumeration import EntranceEnumeration
from netex.models.entrance_ref_structure import EntranceRefStructure
from netex.models.facility_ref import FacilityRef
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.name_type_enumeration import NameTypeEnumeration
from netex.models.navigation_path import NavigationPath
from netex.models.navigation_paths_in_frame_rel_structure import NavigationPathsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.path_link_end_structure import PathLinkEndStructure
from netex.models.place_ref_structure import PlaceRefStructure
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_entrance import PointOfInterestEntrance
from netex.models.points_of_interest_in_frame_rel_structure import PointsOfInterestInFrameRelStructure
from netex.models.pos import Pos
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.purpose_of_grouping_ref import PurposeOfGroupingRef
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_ref_structure import SiteRefStructure
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.type_of_place_ref import TypeOfPlaceRef
from netex.models.type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure
from netex.models.type_of_zone_ref import TypeOfZoneRef
from netex.models.type_of_zone_refs_rel_structure import TypeOfZoneRefsRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
    participant_ref=ParticipantRef(
        value='ODAtransport_TDM'
    ),
    description=MultilingualString(
        value='Olympic Venue Definitions'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='oda:OPK_all',
                version='1.1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='napt_metadata',
                            xmlns='napt',
                            xmlns_url='http://www.naptan.org.uk/naptan',
                            description='UK NaPTAN Stop Place codes'
                        ),
                        Codespace(
                            id='naptPoi_data',
                            xmlns='naptPoi',
                            xmlns_url='http://www.naptan.org.uk/pois',
                            description='UK NaPTAN POI codes'
                        ),
                        Codespace(
                            id='naptStop_data',
                            xmlns='naptStopi',
                            xmlns_url='http://www.naptan.org.uk/stops',
                            description='UK NaPTAN stop  codes'
                        ),
                        Codespace(
                            id='oda',
                            xmlns='iso3166-2',
                            xmlns_url='http://www.oda.org.uk/data/',
                            description='data from Olympica Developmnet Authority'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='oda'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        SiteFrame(
                            id='oda:OPK',
                            created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Olympic Park'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100OPK',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Park'
                                        ),
                                        description=MultilingualString(
                                            value='Olympic Park'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Park'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537910.0,
                                                        184993.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Park',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Parc Olympique',
                                                        lang='fr'
                                                    )
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100OPKgN',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Northern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    537202.0,
                                                                    185730.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    public_use=PublicUseEnumeration.AUTHORISED_PUBLIC_ONLY,
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100OPKgN@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Northern Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                facility_ref=FacilityRef(
                                                                    ref='12345'
                                                                ),
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgN@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100OPKgN@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Northern Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgN@ExitQ',
                                                                            created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100OPKgE',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eastern (Stratford) Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    538178.0,
                                                                    184429.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100OPKgE@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Eastern Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgE@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100OPKgE@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Eastern Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgE@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100OPKgS',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Southern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    538230.0,
                                                                    183684.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100OPKgS@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Southern Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgS@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100OPKgS@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Southern Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgS@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100OPKgW',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Western Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    537307.0,
                                                                    183839.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100OPKgW@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Western Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgW@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100OPKgW@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Olympic Park Western Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100OPKgW@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100AQC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Aquatics Centre'
                                        ),
                                        description=MultilingualString(
                                            value='Aquatics Centre'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        538066.0,
                                                        184238.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Centre aquatique'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100STA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Stadium'
                                        ),
                                        description=MultilingualString(
                                            value='Olympic Stadium'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537655.0,
                                                        184052.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Stade olympique'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100VEL',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 7, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Velodrome'
                                        ),
                                        description=MultilingualString(
                                            value='Velodrome'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537705.0,
                                                        185368.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Vélodrome'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100BBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Basketball Arena'
                                        ),
                                        description=MultilingualString(
                                            value='Basketball Arena'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537819.0,
                                                        185156.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Pavillon de basketball'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100HOC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 4, 28, 12, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hockey Centre'
                                        ),
                                        description=MultilingualString(
                                            value='Hockey Centre'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537369.0,
                                                        185222.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Centre de Hockey'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100AWP',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Water Polo Arena'
                                        ),
                                        description=MultilingualString(
                                            value='Water Polo Arena'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537940.0,
                                                        184339.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Pavillon de water-polo'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100HBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Handball Arena'
                                        ),
                                        description=MultilingualString(
                                            value='Handball Arena'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537397.0,
                                                        184688.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Pavillon de handball'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100BMX',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 19, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='BMX Track'
                                        ),
                                        description=MultilingualString(
                                            value='BMX Track'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537845.0,
                                                        185409.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    lang='fr',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    name=MultilingualString(
                                                        value='Piste de BMX'
                                                    )
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100ETM',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Manor'
                                        ),
                                        description=MultilingualString(
                                            value='Eton Manor (Paralympics only)'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537699.0,
                                                        185672.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100OPK'
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100OPKgE_HOC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Hockey Centre'
                                        ),
                                        distance=Decimal('1562'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HOC_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hockey Centre to OPK East Entrance'
                                        ),
                                        distance=Decimal('1562'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_HBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Handball Arena'
                                        ),
                                        distance=Decimal('1033'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT14M21S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HBA_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Handball Arena to OPK East Entrance'
                                        ),
                                        distance=Decimal('1033'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT14M21S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_STA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Olympic Stadium'
                                        ),
                                        distance=Decimal('442'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M8S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_STA_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Stadium to OPK East Entrance'
                                        ),
                                        distance=Decimal('442'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M8S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_BBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Basketball Arena'
                                        ),
                                        distance=Decimal('1707'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BBA_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Basketball Arena to OPK East Entrance'
                                        ),
                                        distance=Decimal('1707'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_AWP',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Water Polo Arena'
                                        ),
                                        distance=Decimal('566'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT7M52S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AWP_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Water Polo Arena to OPK East Entrance'
                                        ),
                                        distance=Decimal('566'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT7M52S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_AQC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Aquatics Centre'
                                        ),
                                        distance=Decimal('631'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT8M46S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AQC_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Aquatics Centre to OPK East Entrance'
                                        ),
                                        distance=Decimal('631'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT8M46S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_VEL',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Velodrome'
                                        ),
                                        distance=Decimal('1826'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_VEL_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Velodrome to OPK East Entrance'
                                        ),
                                        distance=Decimal('1826'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_ETM',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to Eton Manor'
                                        ),
                                        distance=Decimal('2086'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_ETM_OPKgE',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Manor to OPK East Entrance'
                                        ),
                                        distance=Decimal('2086'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_BMX',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to BMX Circuit'
                                        ),
                                        distance=Decimal('2076'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BMX_OPKgE',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='BMX Circuit to OPK East Entrance'
                                        ),
                                        distance=Decimal('2076'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgE_OPK',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK East Entrance to centre of Olympic Park'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_OPK_OPKgE',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='centre of Olympic Park to OPK East Entrance'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgE'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_HOC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Hockey Centre'
                                        ),
                                        distance=Decimal('1627'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HOC_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hockey Centre to OPK South Entrance'
                                        ),
                                        distance=Decimal('1627'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_HBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Handball Arena'
                                        ),
                                        distance=Decimal('1243'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HBA_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Handball Arena to OPK South Entrance'
                                        ),
                                        distance=Decimal('1243'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_STA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Olympic Stadium'
                                        ),
                                        distance=Decimal('387'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M23S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_STA_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Stadium to OPK South Entrance'
                                        ),
                                        distance=Decimal('387'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M23S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_BBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Basketball Arena'
                                        ),
                                        distance=Decimal('1852'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BBA_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Basketball Arena to OPK South Entrance'
                                        ),
                                        distance=Decimal('1852'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_AWP',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Water Polo Arena'
                                        ),
                                        distance=Decimal('774'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M45S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AWP_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Water Polo Arena to OPK South Entrance'
                                        ),
                                        distance=Decimal('774'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M45S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_AQC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Aquatics Centre'
                                        ),
                                        distance=Decimal('470'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M32S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AQC_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Aquatics Centre to OPK South Entrance'
                                        ),
                                        distance=Decimal('470'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M32S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_VEL',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Velodrome'
                                        ),
                                        distance=Decimal('2036'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_VEL_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Velodrome to OPK South Entrance'
                                        ),
                                        distance=Decimal('2036'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_ETM',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to Eton Manor'
                                        ),
                                        distance=Decimal('2296'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_ETM_OPKgS',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Manor to OPK South Entrance'
                                        ),
                                        distance=Decimal('2296'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_BMX',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to BMX Circuit'
                                        ),
                                        distance=Decimal('2286'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BMX_OPKgS',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='BMX Circuit to OPK South Entrance'
                                        ),
                                        distance=Decimal('2286'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgS_OPK',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK South Entrance to centre of Olympic Park'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_OPK_OPKgS',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='centre of Olympic Park to OPK South Entrance'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_ETM',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Eton Manor'
                                        ),
                                        distance=Decimal('148'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_ETM_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Manor to OPK North Entrance'
                                        ),
                                        distance=Decimal('148'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_VEL',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Velodrome'
                                        ),
                                        distance=Decimal('407'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT7M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_VEL_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Velodrome to OPK North Entrance'
                                        ),
                                        distance=Decimal('407'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT7M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_BBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Basketball Arena'
                                        ),
                                        distance=Decimal('620'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT8M37S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BBA_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Basketball Arena to OPK North Entrance'
                                        ),
                                        distance=Decimal('620'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT8M37S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_HOC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Hockey Centre'
                                        ),
                                        distance=Decimal('808'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M13S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HOC_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hockey Centre to OPK North Entrance'
                                        ),
                                        distance=Decimal('808'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M13S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_HBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Handball Arena'
                                        ),
                                        distance=Decimal('1211'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HBA_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Handball Arena to OPK North Entrance'
                                        ),
                                        distance=Decimal('1211'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_STA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Olympic Stadium'
                                        ),
                                        distance=Decimal('1528'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_STA_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Stadium to OPK North Entrance'
                                        ),
                                        distance=Decimal('1528'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_AWP',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Water Polo Arena'
                                        ),
                                        distance=Decimal('1664'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AWP_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Water Polo Arena to OPK North Entrance'
                                        ),
                                        distance=Decimal('1664'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_AQC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to Aquatics Centre'
                                        ),
                                        distance=Decimal('2054'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AQC_OPKgN',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Aquatics Centre to OPK North Entrance'
                                        ),
                                        distance=Decimal('2054'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_BMX',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 2, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to BMX Circuit'
                                        ),
                                        distance=Decimal('657'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT9M8S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BMX_OPKgN',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='BMX Circuit to OPK North Entrance'
                                        ),
                                        distance=Decimal('657'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT9M8S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgN_OPK',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK North Entrance to centre of Olympic Park'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_OPK_OPKgN',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='centre of Olympic Park to OPK North Entrance'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_HOC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Hockey Centre'
                                        ),
                                        distance=Decimal('1313'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HOC_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hockey Centre to OPK West Entrance'
                                        ),
                                        distance=Decimal('1313'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HOC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_BBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Basketball Arena'
                                        ),
                                        distance=Decimal('1380'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BBA_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Basketball Arena to OPK West Entrance'
                                        ),
                                        distance=Decimal('1380'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_HBA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Handball Arena'
                                        ),
                                        distance=Decimal('792'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_HBA_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Handball Arena to OPK West Entrance'
                                        ),
                                        distance=Decimal('792'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HBA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_AWP',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Water Polo Arena'
                                        ),
                                        distance=Decimal('733'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M11S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AWP_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Water Polo Arena to OPK West Entrance'
                                        ),
                                        distance=Decimal('733'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AWP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M11S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_AQC',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Aquatics Centre'
                                        ),
                                        distance=Decimal('1123'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_AQC_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Aquatics Centre to OPK West Entrance'
                                        ),
                                        distance=Decimal('1123'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100AQC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_STA',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Olympic Stadium'
                                        ),
                                        distance=Decimal('180'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_STA_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Olympic Stadium to OPK West Entrance'
                                        ),
                                        distance=Decimal('180'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100STA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_VEL',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Velodrome'
                                        ),
                                        distance=Decimal('1560'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_VEL_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Velodrome to OPK West Entrance'
                                        ),
                                        distance=Decimal('1560'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100VEL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_ETM',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to Eton Manor'
                                        ),
                                        distance=Decimal('1830'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_ETM_OPKgW',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Manor to OPK West Entrance'
                                        ),
                                        distance=Decimal('1830'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_BMX',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to BMX Circuit'
                                        ),
                                        distance=Decimal('1810'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_BMX_OPKgW',
                                        created=XmlDateTime(2011, 2, 11, 9, 35, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='BMX Circuit to OPK West Entrance'
                                        ),
                                        distance=Decimal('1810'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100BMX'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPKgW_OPK',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='OPK West Entrance to centre of Olympic Park'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100OPK_OPK_OPKgW',
                                        created=XmlDateTime(2011, 2, 11, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 20, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='centre of Olympic Park to OPK West Entrance'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPK'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100OPKgW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:EXL',
                            created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 6, 6, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='ExCeL'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100EXL',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL'
                                        ),
                                        description=MultilingualString(
                                            value='ExCeL'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Park'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        540790.0,
                                                        180766.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100EXL@gEntr',
                                                    created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ExCeL Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    540503.0,
                                                                    180729.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100EXL@gEntr@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='ExCeL Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100EXL@gEntr@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100EXL@gExit',
                                                    created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ExCeL Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    541280.0,
                                                                    180742.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100EXL@gExit@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='ExCeL Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100EXL@gExit@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100EXLN1',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Excel North Sports Hall 1'
                                        ),
                                        description=MultilingualString(
                                            value='Excel North Sports Hall 1'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        540764.0,
                                                        180806.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100EXL'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100EXLN2',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Excel North Sports Hall 2'
                                        ),
                                        description=MultilingualString(
                                            value='Excel North Sports Hall 2'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        541013.0,
                                                        180806.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100EXL'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100EXLS1',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Excel South Sports Hall 1'
                                        ),
                                        description=MultilingualString(
                                            value='Excel South Sports Hall 1'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        540756.0,
                                                        180700.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100EXL'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100EXLS2',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Excel South Sports Hall 2'
                                        ),
                                        description=MultilingualString(
                                            value='Excel South Sports Hall 2'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        540921.0,
                                                        180700.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100EXL'
                                        )
                                    ),
                                    PointOfInterest(
                                        id='naptPoi:8100EXLS3',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Excel South Sports Hall 3'
                                        ),
                                        description=MultilingualString(
                                            value='Excel South Sports Hall 3'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        541046.0,
                                                        180700.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        parent_site_ref=SiteRefStructure(
                                            version='any',
                                            ref='naptPoi:8100EXL'
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXLN1',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to North Sports Hall 1'
                                        ),
                                        distance=Decimal('150'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLN1'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M15S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXLN2',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to North Sports Hall 2'
                                        ),
                                        distance=Decimal('400'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLN2'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXLS1',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to South Sports Hall 1'
                                        ),
                                        distance=Decimal('150'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS1'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M15S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXLS2',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to South Sports Hall 2'
                                        ),
                                        distance=Decimal('400'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS2'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXLS3',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to South Sports Hall 3'
                                        ),
                                        distance=Decimal('600'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS3'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT17M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL_8100EXL@gEntr+8100EXL',
                                        created=XmlDateTime(2011, 6, 6, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL Entrance to Excel (nominal venue point)'
                                        ),
                                        distance=Decimal('400'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT11M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXLN1+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL North Sports Hall 1 to Exit'
                                        ),
                                        distance=Decimal('550'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLN1'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M45S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXLN2+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL North Sports Hall 2 to Exit'
                                        ),
                                        distance=Decimal('300'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLN2'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT9M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXLS1+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL South Sports Hall 1 to Exit'
                                        ),
                                        distance=Decimal('550'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS1'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT15M45S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXLS2+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL South Sports Hall 2 to Exit'
                                        ),
                                        distance=Decimal('300'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS2'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT9M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXLS3+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL South Sports Hall 3 to Exit'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXLS3'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M45S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EXL+8100EXL_8100EXL@gExit',
                                        created=XmlDateTime(2011, 6, 6, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='ExCeL (nominal venue point) to Exit'
                                        ),
                                        distance=Decimal('300'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EXL@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT9M00S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:GRP',
                            created=XmlDateTime(2011, 2, 22, 16, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Greenwich Park'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100GRP',
                                        created=XmlDateTime(2011, 2, 22, 16, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park'
                                        ),
                                        description=MultilingualString(
                                            value='Greenwich Park'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        539055.0,
                                                        177256.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100GRP@gGNW',
                                                    created=XmlDateTime(2011, 2, 22, 16, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Greenwich Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    538663.0,
                                                                    177784.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gGNW@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greenwich Park Greenwich Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gGNW@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gGNW@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 7, 15, 17, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greenwich Park Greenwich Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gGNW@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT20M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100GRP@gBKH1',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityCondition(
                                                                    id='naptPoi:8100GRP@gBKH1',
                                                                    version='any',
                                                                    from_date=XmlDateTime(2012, 7, 28, 0, 0, 0, 0, 0),
                                                                    to_date=XmlDateTime(2012, 7, 31, 23, 59, 0, 0, 0)
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    created=XmlDateTime(2011, 2, 22, 16, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Blackheath Spectator Gate (Days 1-4)'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    539336.0,
                                                                    176791.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gBKH1@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greemwich Park Blackheath Gate (Days 1-4) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gBKH1@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gBKH1@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 7, 15, 17, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greenwich Park Blackheath Gate (Days 1-4) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gBKH1@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT20M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100GRP@gBKH6',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityCondition(
                                                                    id='naptPoi:8100GRP@gBKH6',
                                                                    version='any',
                                                                    from_date=XmlDateTime(2012, 8, 2, 0, 0, 0, 0, 0),
                                                                    to_date=XmlDateTime(2012, 8, 12, 23, 59, 0, 0, 0)
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    created=XmlDateTime(2011, 2, 22, 16, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Blackheath Spectator Gate (Days 6-16)'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    538967.0,
                                                                    177427.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gBKH6@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greenwich Park Blackheath Gate (Days 6-16) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gBKH6@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100GRP@gBKH6@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 7, 15, 17, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Greenwich Park Blackheath Gate (Days 6-16) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100GRP@gBKH6@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT20M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100GRP_8100GRP@gGNW+8100GRP',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Greenwich Entrance to Venue'
                                        ),
                                        distance=Decimal('180'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gGNW'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100GRP+8100GRP_8100GRP@gGNW',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Venue to Greenwich Entrance'
                                        ),
                                        distance=Decimal('180'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gGNW'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100GRP_8100GRP@gBKH1+8100GRP',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Blackheath Entrance (Days 1-4) to Venue'
                                        ),
                                        distance=Decimal('940'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gBKH1'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT13M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100GRP+8100GRP_8100GRP@gBKH1',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Venue to Blackheath Entrance (Days 1-4)'
                                        ),
                                        distance=Decimal('940'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gBKH1'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT13M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100GRP_8100GRP@gBKH6+8100GRP',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Blackheath Entrance (Days 6-16) to Venue'
                                        ),
                                        distance=Decimal('490'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gBKH6'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M50S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100GRP+8100GRP_8100GRP@gBKH6',
                                        created=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        changed=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Greenwich Park Venue to Blackheath Entrance (Days 6-16)'
                                        ),
                                        distance=Decimal('490'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100GRP@gBKH6'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT6M50S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:NGA',
                            created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='North Greenwich Arena'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100NGA',
                                        created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='North Greenwich Arena'
                                        ),
                                        description=MultilingualString(
                                            value='North Greenwich Arena'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        539118.0,
                                                        180126.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100NGA@gEntr',
                                                    created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='North Greenwich Arena Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    539326.0,
                                                                    179763.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100NGA@gEntr@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='North Greenwich Arena Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100NGA@gEntr@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100NGA@gExit',
                                                    created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='North Greenwich Arena Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    539219.0,
                                                                    179869.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='naptPoi:8100NGA@gExit@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='North Greenwich Arena Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='naptPoi:8100NGA@gExit@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100NGA_8100NGA@gEntr@NGA+8100NGA',
                                        created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='NGA Entrance to Venue'
                                        ),
                                        distance=Decimal('500'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT7M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100NGA+8100NGA_8100NGA@gExit',
                                        created=XmlDateTime(2011, 2, 23, 10, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='NGA Venue to Exit'
                                        ),
                                        distance=Decimal('330'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100NGA@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M30S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:RAB',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='The Royal Artillery Barracks'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100RAB',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Royal Artillery Barracks'
                                        ),
                                        description=MultilingualString(
                                            value='The Royal Artillery Barracks'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        542945.0,
                                                        177825.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100RAB@g0',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='The Royal Artillery Barracks Northern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    543199.0,
                                                                    177888.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100RAB@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Royal Artillery Barracks Northern Spectator Gate Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100RAB@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100RAB@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Royal Artillery Barracks Northern Spectator Gate Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100RAB@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100RAB@g1',
                                                    created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='The Royal Artillery Barracks Southern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    543129.0,
                                                                    177692.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100RAB@g1@EntrQ',
                                                                created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Royal Artillery Barracks Southern Spectator Gate Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100RAB@g1@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100RAB@g1@ExitQ',
                                                                created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Royal Artillery Barracks Southern Spectator Gate Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100RAB@g1@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100RAB_8100RAB@g0+8100RAB',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Royal Artillery Barracks Northern Spectator Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('260'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100RAB+8100RAB_8100RAB@g0',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Royal Artillery Barracks Spectator Area to Northern Spectator Gate (Exit)'
                                        ),
                                        distance=Decimal('260'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100RAB_8100RAB@g1+8100RAB',
                                        created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Royal Artillery Barracks Southern Spectator Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('260'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB@g1'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100RAB+8100RAB_8100RAB@g1',
                                        created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Royal Artillery Barracks Spectator Area to Southern Spectator Gate (Exit)'
                                        ),
                                        distance=Decimal('260'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100RAB@g1'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:EAR',
                            created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Earls Court'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100EAR',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Earls Court'
                                        ),
                                        description=MultilingualString(
                                            value='Earls Court'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        525200.0,
                                                        177997.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100EAR@gEntr',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Earls Court Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    525352.0,
                                                                    178069.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100EAR@gEntr@SecQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Earls Court Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100EAR@gEntr@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100EAR@gExit',
                                                    created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Earls Court Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    525360.0,
                                                                    178327.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100EAR@gExit@ExitQ',
                                                                created=XmlDateTime(2011, 3, 1, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Earls Court Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100EAR@gExit@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100EAR@gEntr@EAR',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Earls Court Spectator Entrance to Venue'
                                        ),
                                        distance=Decimal('1380'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT19M10S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100EAR+8100EAR_8100EAR@gExit',
                                        created=XmlDateTime(2011, 2, 10, 22, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 2, 23, 9, 30, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Earls Court Venue to Spectator Exit'
                                        ),
                                        distance=Decimal('1380'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100EAR@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT19M10S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:LCG',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Lords Cricket Ground'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100LCG',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lords Cricket Ground'
                                        ),
                                        description=MultilingualString(
                                            value='Lords Cricket Ground'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        526886.0,
                                                        182783.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100LCG@g0',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Lords Cricket Ground Western Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    526828.0,
                                                                    182618.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100LCG@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lords Cricket Ground Western Spectator Gate Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LCG@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100LCG@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lords Cricket Ground Western Spectator Gate Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LCG@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100LCG@g1',
                                                    created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Lords Cricket Ground Eastern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    526945.0,
                                                                    182732.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100LCG@g1@EntrQ',
                                                                created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lords Cricket Ground Eastern Spectator Gate Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LCG@g1@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100LCG@g1@ExitQ',
                                                                created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lords Cricket Ground Eastern Spectator Gate Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LCG@g1@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100LCG_8100LCG@g0+8100LCG',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lords Cricket Ground Western Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('175'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M25S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100LCG+8100LCG_8100LCG@g0',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lords Cricket Ground Spectator Area to Western Gate (Exit)'
                                        ),
                                        distance=Decimal('175'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M25S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100LCG_8100LCG@g1+8100LCG',
                                        created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lords Cricket Ground Eastern Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('250'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG@g1'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100LCG+8100LCG_8100LCG@g1',
                                        created=XmlDateTime(2011, 6, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lords Cricket Ground Spectator Area to Eastern Gate (Exit)'
                                        ),
                                        distance=Decimal('250'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LCG@g1'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M00S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:WIM',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Wimbledon'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100WIM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon'
                                        ),
                                        description=MultilingualString(
                                            value='Wimbledon'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524192.0,
                                                        172098.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WIM@gN',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wimbledon Northern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    524225.0,
                                                                    172332.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WIM@gN@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Northern Spectator Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WIM@gN@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100WIM@gN@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Northern Spectator Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WIM@gN@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WIM@gC',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wimbledon Central Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    524331.0,
                                                                    172026.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100LCG@gC@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Central Spectator Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LCG@gC@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100WIM@gC@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Central Spectator Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WIM@gC@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WIM@gS',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wimbledon Southern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    524342.0,
                                                                    171801.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WIM@gS@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Southern Spectator Gate Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WIM@gS@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100WIM@gS@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wimbledon Southern Spectator Gate Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WIM@gS@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100WIM_8100WIM@gN+8100WIM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Northern Spectator Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('236'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M16S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WIM+8100WIM_100WIM@gN',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Spectator Area to Northern Gate (Exit)'
                                        ),
                                        distance=Decimal('236'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M16S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WIM_8100WIM@gC+8100WIM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Central Spectator Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('156'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M10S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WIM+8100WIM_8100WIM@gC',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Spectator Area to Central Gate (Exit)'
                                        ),
                                        distance=Decimal('156'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M10S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WIM_8100WIM@gS+8100WIM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Southern Spectator Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('333'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M37S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WIM+8100WIM_8100WIM@gS',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wimbledon Spectator Area to Southern Gate (Exit)'
                                        ),
                                        distance=Decimal('333'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WIM@gS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M37S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:HGP',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Horse Guards Parade'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100HGP',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Horse Guards Parade'
                                        ),
                                        description=MultilingualString(
                                            value='Horse Guards Parade'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        529792.0,
                                                        180070.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HGP@gInN',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Horse Guards Parade Northern Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529777.0,
                                                                    180129.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HGP@gInN@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Horse Guards Parade Northern Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HGP@gInN@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HGP@gOutN',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Horse Guards Parade Northern Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529807.0,
                                                                    180175.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HGP@gOutN@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Horse Guards Parade Northern Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HGP@gOutN@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HGP@gInS',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Horse Guards Parade Southern Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529558.0,
                                                                    179864.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HGP@gInS@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Horse Guards Parade Southern Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HGP@gInS@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HGP@gOutS',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Horse Guards Parade Southern Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529777.0,
                                                                    179709.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HGP@gOutS@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Horse Guards Parade Southern Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HGP@gOutS@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100HGP_8100HGP@gInN+800HGP',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Horse Guards Parade Northern Spectator Entrance to Venue'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP@gInN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100HGP+800HGP_800HGP@gOutN',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Horse Guards Parade Venue to Northern Spectator Exit'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP@gOutN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100HGP_8100HGP@gInS@gInS+800HGP',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Horse Guards Parade Southern Spectator Entrance to Venue'
                                        ),
                                        distance=Decimal('320'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP@gInS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT13M00S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100HGP_800HGP_800HGP@gOutS',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Horse Guards Parade Venue to Southern Spectator Exit'
                                        ),
                                        distance=Decimal('360'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HGP@gOutS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT8M00S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:MAL',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='The Mall'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100MAL',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='The Mall'
                                        ),
                                        description=MultilingualString(
                                            value='The Mall'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        529424.0,
                                                        179933.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100MAL@gN',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='The Mall Northern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529343.0,
                                                                    179889.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100MAL@gN@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Mall Northern Gate (Entry) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100MAL@gN@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100MAL@gN@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Mall Northern Gate (Exit) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100MAL@gN@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100MAL@gS',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='The Mall Southern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    529501.0,
                                                                    179881.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100MAL@gS@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Mall Southern Gate (Entry) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100MAL@gS@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100MAL@gS@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='The Mall Southern Gate (Exit) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100MAL@gS@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100MAL_8100MAL@gN+8100MAL',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='The Mall Northern Spectator Gate to Venue'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL@gN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100MAL+8100MAL_8100MAL@gN',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='The Mall Venue to Northern Spectator Gate'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL@gN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100MAL_8100MAL@gS+8100MAL',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='The Mall Southern Spectator Gate to Venue'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL@gS'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100MAL+8100MAL_8100MAL@gS',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='The Mall Venue to Southern Spectator Gate'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100MAL@gS'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:HYD',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Hyde Park'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100HYD',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hyde Park'
                                        ),
                                        description=MultilingualString(
                                            value='Hyde Park'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        527225.0,
                                                        180252.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HYD@g0',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Hyde Park Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    527411.0,
                                                                    180236.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HYD@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Hyde Park Entrance Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HYD@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100HYD@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Hyde Park Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HYD@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100HYD_8100HYD@g0+8100HYD',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Hyde Park Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('200'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100HYD+8100HYD_8100HYD@g0',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Hyde Park Spectator Area to Gate (Exit)'
                                        ),
                                        distance=Decimal('200'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HYD@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:WEA',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Wembley Arena'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100WEA',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Arena'
                                        ),
                                        description=MultilingualString(
                                            value='Wembley Arena'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        519091.0,
                                                        185802.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WEA@gEntr',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wembley Arena Spectator Entrance'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    519263.0,
                                                                    185796.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WEA@gEntr@SecQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wembley Arena Entrance Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WEA@gEntr@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WEA@gExit',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wembley Arena Spectator Exit'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    519148.0,
                                                                    185718.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WEA@gExit@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wembley Arena Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WEA@gExit@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100WEA_8100WEA@gEntr+8100WEA',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Arena Spectator Entrance to Venue'
                                        ),
                                        distance=Decimal('172'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA@gEntr'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M23S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WEA+8100WEAWEA_8100WEA@gExit',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Arena Venue to Spectator Exit'
                                        ),
                                        distance=Decimal('100'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEA@gExit'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT1M24S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:LVC',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Lee Valley Centre'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100LVC',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Lee Valley Centre'
                                        ),
                                        description=MultilingualString(
                                            value='Lee Valley White Water Centre'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        537250.0,
                                                        200647.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100LVC@g0',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Lee Valley Centre Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    537073.0,
                                                                    200893.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100LVC@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lee Valley Centre Entrance Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LVC@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100LVC@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Lee Valley Centre Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100LVC@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100LVC_8100LVC_LVC@g0+8100LVC',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Lee Valley Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('303'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M12S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100LVC+8100LVC_8100LVC@g0',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Lee Valley Spectator Area to Gate (Exit)'
                                        ),
                                        distance=Decimal('303'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100LVC@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT4M12S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:HAD',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Hadleigh Farm'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100HAD',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Hadleigh Farm'
                                        ),
                                        description=MultilingualString(
                                            value='Hadleigh Farm'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        580171.0,
                                                        186408.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100HAD@g0',
                                                    created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Hadleigh Farm Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    580647.0,
                                                                    186470.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100HAD@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Hadleigh Farm Entrance Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HAD@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100HAD@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Hadleigh Farm Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100HAD@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100HAD_8100HAD@g0+8100HAD',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Hadleigh Farm Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('500'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100HAD+8100HAD_8100HAD@g0',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Hadleigh Farm Spectator Area to Gate (Exit)'
                                        ),
                                        distance=Decimal('500'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100HAD@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:ETD',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Eton Dorney'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100ETD',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Dorney'
                                        ),
                                        description=MultilingualString(
                                            value='Eton Dorney'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        492843.0,
                                                        178016.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100ETD@gTHub',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eton Dorney Transport Hub Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    494124.0,
                                                                    177441.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100ETD@gTHub@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Eton Dorney Transport Hub Gate (Entry) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100ETD@gTHub@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100ETD@gTHub@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Eton Dorney Transport Hub Gate (Exit) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100ETD@gTHub@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100ETD@gN',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Eton Dorney Northern Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    493566.0,
                                                                    177839.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100ETD@gN@SecQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Eton Dorney Northern Gate (Entry) Security Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100ETD@gN@SecQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100ETD@gN@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Eton Dorney Northern Gate (Exit) Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100ETD@gN@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT10M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100ETD_8100ETD@gN+8100ETD',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Dorney Northern Spectator Gate to Venue'
                                        ),
                                        distance=Decimal('750'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD@gN'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100ETD+8100TD_8100ETD@gN',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Dorney Venue to Northern Spectator Gate'
                                        ),
                                        distance=Decimal('750'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD@gN'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT10M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100ETD_8100ETD@gTHub+8100ETD',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Dorney Transport Hub Spectator Gate to Venue'
                                        ),
                                        distance=Decimal('1400'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD@gTHub'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT19M30S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100ETD+8100ETD_8100ETD@gTHub',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Eton Dorney Venue to Transport Hub Spectator Gate'
                                        ),
                                        distance=Decimal('1400'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100ETD@gTHub'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT19M30S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:WAP',
                            created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Weymouth and Portland'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100WAP',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Weymouth and Portland'
                                        ),
                                        description=MultilingualString(
                                            value='Weymouth and Portland - The Nothe'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        368401.0,
                                                        78574.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WAP@g0',
                                                    created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                    changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                    modification=ModificationEnumeration.REVISE,
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Weymouth and Portland Spectator Gate'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    368296.0,
                                                                    78634.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WAP@g0@EntrQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                changed=XmlDateTime(2011, 5, 27, 17, 0, 0, 0, 0),
                                                                modification=ModificationEnumeration.REVISE,
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Weymouth and Portland Entrance Secturity Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WAP@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT60M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100WAP@g0@ExitQ',
                                                                created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Weymouth and Portland Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WAP@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT30M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100WAP_8100WAP@g0+8100WAP',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Weymouth and Portland Gate (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('150'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WAP_8100WAP+8100WAP@g0',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Weymouth and Portland Spectator Area to Gate (Exit)'
                                        ),
                                        distance=Decimal('150'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WAP@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT2M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:WEM',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 6, 22, 10, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value='Wembley Stadium'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100WEM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 6, 22, 10, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Stadium'
                                        ),
                                        description=MultilingualString(
                                            value='Wembley Stadium'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        519373.0,
                                                        185548.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                PointOfInterestEntrance(
                                                    id='naptPoi:8100WEM@g0',
                                                    created=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Wembley Stadium Turnstiles'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    519231.0,
                                                                    185638.0,
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    place_types=TypeOfPlaceRefsRelStructure(
                                                        type_of_place_ref=[
                                                            TypeOfPlaceRef(
                                                                ref='napt:type_of_place@PIE',
                                                                version_ref='EXTERNAL'
                                                            ),
                                                        ]
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='oda:8100WEM@g0@EntrQ',
                                                                created=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wembley Stadium Turnstiles Ticket Check Queue'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.FORWARDS,
                                                                check_process=CheckProcessTypeEnumeration.SECURITY_CHECK,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WEM@g0@EntrQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT15M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            CheckConstraint(
                                                                id='oda:8100WEM@g0@ExitQ',
                                                                created=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Wembley Stadium Turnstiles Exit Congestion'
                                                                ),
                                                                check_direction=CheckDirectionEnumeration.BACKWARDS,
                                                                check_process=CheckProcessTypeEnumeration.EGRESS,
                                                                congestion=CongestionEnumeration.CROWDING,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='oda:8100WEM@g0@ExitQ',
                                                                            version='any',
                                                                            average_delay=XmlDuration("PT5M0S")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.GATE
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            navigation_paths=NavigationPathsInFrameRelStructure(
                                navigation_path=[
                                    NavigationPath(
                                        id='oda:8100WEM_8100WEM@g0+8100WEM',
                                        created=XmlDateTime(2011, 6, 22, 10, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Stadium Turnstiles (Entry) to Spectator Area'
                                        ),
                                        distance=Decimal('175'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM@g0'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                    NavigationPath(
                                        id='oda:8100WEM+8100WEM_8100WEM@g0',
                                        created=XmlDateTime(2011, 4, 21, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Wembley Stadium Spectator Area to Turnstiles (Exit)'
                                        ),
                                        distance=Decimal('175'),
                                        from_value=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM'
                                            )
                                        ),
                                        to=PathLinkEndStructure(
                                            place_ref=PlaceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM'
                                            ),
                                            entrance_ref=EntranceRefStructure(
                                                version='any',
                                                ref='naptPoi:8100WEM@g0'
                                            )
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M0S")
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:MIL',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            version='any',
                            name=MultilingualString(
                                value='Millennium Stadium'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100MIL',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Millennium Stadium'
                                        ),
                                        description=MultilingualString(
                                            value='Millennium Stadium'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        317988.0,
                                                        176162.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:HAM',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            version='any',
                            name=MultilingualString(
                                value='Hampden Park'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100HAM',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Hampden Park'
                                        ),
                                        description=MultilingualString(
                                            value='Hampden Park'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        259020.0,
                                                        661457.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:OLD',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            version='any',
                            name=MultilingualString(
                                value='Old Trafford'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100OLD',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Old Trafford'
                                        ),
                                        description=MultilingualString(
                                            value='Old Trafford'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        380752.0,
                                                        396300.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:COV',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            version='any',
                            name=MultilingualString(
                                value='City of Coventry Stadium'
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100COV',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='City of Coventry Stadium'
                                        ),
                                        description=MultilingualString(
                                            value='City of Coventry Stadium'
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        434253.0,
                                                        283486.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='oda:SJP',
                            created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                            changed=XmlDateTime(2011, 5, 27, 17, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='any',
                            name=MultilingualString(
                                value="St James' Park (Newcastle)"
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='naptPoi:8100SJP',
                                        created=XmlDateTime(2011, 4, 14, 17, 0, 0, 0, 0),
                                        changed=XmlDateTime(2011, 5, 27, 17, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='any',
                                        name=MultilingualString(
                                            value="St James' Park (Newcastle)"
                                        ),
                                        description=MultilingualString(
                                            value="St James' Park (Newcastle)"
                                        ),
                                        purpose_of_grouping_ref=PurposeOfGroupingRef(
                                            ref='Venue'
                                        ),
                                        types=TypeOfZoneRefsRelStructure(
                                            type_of_zone_ref=[
                                                TypeOfZoneRef(
                                                    ref='napt:type_of_zone@POI',
                                                    version_ref='EXTERNAL'
                                                ),
                                            ]
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        424272.0,
                                                        564616.0,
                                                    ]
                                                )
                                            )
                                        ),
                                        place_types=TypeOfPlaceRefsRelStructure(
                                            type_of_place_ref=[
                                                TypeOfPlaceRef(
                                                    ref='napt:type_of_place@Venue',
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
            ),
        ]
    )
)
