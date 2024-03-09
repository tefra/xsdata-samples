from decimal import Decimal
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.accessibility_info_facility_enumeration import AccessibilityInfoFacilityEnumeration
from netex.models.accessibility_info_facility_list import AccessibilityInfoFacilityList
from netex.models.accessibility_limitation import AccessibilityLimitation
from netex.models.accessibility_limitations_rel_structure import AccessibilityLimitationsRelStructure
from netex.models.accessibility_tool_enumeration import AccessibilityToolEnumeration
from netex.models.accessibility_tool_list import AccessibilityToolList
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.authority import Authority
from netex.models.bounding_box_structure_2 import BoundingBoxStructure2
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.key_list import KeyList
from netex.models.key_value_structure import KeyValueStructure
from netex.models.level import Level
from netex.models.levels_rel_structure import LevelsRelStructure
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.limitation_status_enumeration import LimitationStatusEnumeration
from netex.models.location_structure_2 import LocationStructure2
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.network_ref import NetworkRef
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.operator import Operator
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.passenger_information_facility_list import PassengerInformationFacilityList
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.point_refs_rel_structure import PointRefsRelStructure
from netex.models.private_code import PrivateCode
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay_1 import Quay1
from netex.models.quay_ref import QuayRef
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.models.road_address import RoadAddress
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.step_free_access import StepFreeAccess
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place_1 import StopPlace1
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.tariff_zone_1 import TariffZone1
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.wheelchair_access import WheelchairAccess
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
        description=MultilingualString(
            value='Filter used to get  these contents: Get all STOP PLACEs, STOP ASSIGNMENTs and TOPOGRAPHIC PLACEfor Network TNET1 in specified  area    :TP_0032A.  Also return any  RESPONSIBILITY SETs  used.\n\t\t\t\tAlso get details for \n\t\t\t\t'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        NetworkFilterByValueStructure(
                            bounding_box=BoundingBoxStructure2(
                                upper_left=LocationStructure2(
                                    longitude=Decimal('-0.2071300000'),
                                    latitude=Decimal('51.4217400000')
                                ),
                                lower_right=LocationStructure2(
                                    longitude=Decimal('-0.2071400000'),
                                    latitude=Decimal('51.4217500000')
                                )
                            ),
                            object_references=ObjectFilterByValueStructure.ObjectReferences(
                                choice=[
                                    ScheduledStopPointRef(
                                        ref=''
                                    ),
                                    StopPlaceRef(
                                        ref=''
                                    ),
                                    TopographicPlaceRef(
                                        ref=''
                                    ),
                                ]
                            ),
                            network_ref=NetworkRef(
                                value='REQUEST',
                                ref='mynet'
                            )
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P3M"),
    description=MultilingualString(
        value='Single Stop On street example'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='frtop:RF01',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            AvailabilityCondition(
                                id='mybus:RF01',
                                version='any',
                                from_date=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                to_date=XmlDateTime(2011, 12, 17, 9, 30, 47, 0, 0)
                            ),
                        ]
                    ),
                ],
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
                        ),
                        Codespace(
                            id='frtop',
                            xmlns='frtop',
                            xmlns_url='http://www.ptgazetteer.fr',
                            description='French Stop data  data'
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
                        SiteFrame(
                            id='frtop:SF005',
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id='frtop:SF005',
                                            version='any',
                                            from_date=XmlDateTime(2012, 7, 26, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2012, 8, 12, 0, 0, 0, 0, 0)
                                        ),
                                    ]
                                ),
                            ],
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    version='3.0',
                                    ref='frtop:RS_22'
                                )
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='frtop:TP_0032A',
                                        version='any',
                                        name=MultilingualString(
                                            value='St Jean des Fous',
                                            lang='fr'
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='St Jean des Fous',
                                                lang='fr'
                                            ),
                                            short_name=MultilingualString(
                                                value='St Jean',
                                                lang='fr'
                                            ),
                                            qualify=TopographicPlaceDescriptorVersionedChildStructure.Qualify(
                                                qualifier_name=MultilingualString(
                                                    value='Normandie',
                                                    lang='fr'
                                                ),
                                                topographic_place_ref=TopographicPlaceRef(
                                                    version='any',
                                                    ref='frtop:TP_0082A'
                                                )
                                            )
                                        )
                                    ),
                                    TopographicPlace(
                                        id='frtop:TP_0082A',
                                        version='any',
                                        name=MultilingualString(
                                            value='Normandie',
                                            lang='fr'
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Normandie',
                                                lang='fr'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace1(
                                        id='mybus:SSP_02456A',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        key_list=KeyList(
                                            key_value=[
                                                KeyValueStructure(
                                                    key='abc:System',
                                                    value='12345'
                                                ),
                                                KeyValueStructure(
                                                    key='xxx:altkey2',
                                                    value='kkkk12345'
                                                ),
                                            ]
                                        ),
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Poste, St Jean',
                                            lang='fr'
                                        ),
                                        short_name=MultilingualString(
                                            value='Poste ',
                                            lang='fr'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('-0.2071397147'),
                                                latitude=Decimal('51.4217482061')
                                            )
                                        ),
                                        accessibility_assessment=AccessibilityAssessment(
                                            id='mybus:SSP_02456A',
                                            version='any',
                                            mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                            limitations=AccessibilityLimitationsRelStructure(
                                                accessibility_limitation=AccessibilityLimitation(
                                                    wheelchair_access=WheelchairAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    step_free_access=StepFreeAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    )
                                                )
                                            )
                                        ),
                                        facilities=SiteFacilitySetsRelStructure(
                                            site_facility_set_ref_or_site_facility_set=[
                                                SiteFacilitySet(
                                                    id='mybus:SSP_02456A',
                                                    version='any',
                                                    accessibility_tool_list=AccessibilityToolList(
                                                        value=[
                                                            AccessibilityToolEnumeration.WALKINGSTICK,
                                                            AccessibilityToolEnumeration.AUDIO_NAVIGATOR,
                                                            AccessibilityToolEnumeration.PASSENGER_CART,
                                                        ]
                                                    ),
                                                    passenger_information_facility_list=PassengerInformationFacilityList(
                                                        value=[
                                                            PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY,
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceRef(
                                            version='any',
                                            ref='frtop:TP_0032A'
                                        ),
                                        levels=LevelsRelStructure(
                                            level_ref_or_level=[
                                                Level(
                                                    id='mybus:SSP_02456A_0',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Erde '
                                                    ),
                                                    public_code='E'
                                                ),
                                            ]
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay1(
                                                    id='mybus:Q_SSP_02456A_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Poste',
                                                        lang='fr'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Pres de la Gare 20m a droit .',
                                                            lang='fr'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.207139714'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    road_address=RoadAddress(
                                                        id='mybus:Rad_SP001A_01',
                                                        version='any',
                                                        road_name=MultilingualString(
                                                            value='Rue  de la Gare'
                                                        )
                                                    ),
                                                    cross_road=MultilingualString(
                                                        value='Rue du Chene',
                                                        lang='fr'
                                                    ),
                                                    landmark=MultilingualString(
                                                        value='Place Victoire',
                                                        lang='fr'
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    lighting=LightingEnumeration.UNLIT,
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            PassengerInformationEquipment(
                                                                id='mybus:Q_SSP_02456A_1',
                                                                version='any',
                                                                accessibility_info_facility_list=AccessibilityInfoFacilityList(
                                                                    value=[
                                                                        AccessibilityInfoFacilityEnumeration.VISUAL_DISPLAYS,
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    label=MultilingualString(
                                                        value='A',
                                                        lang='fr'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.NW,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='frtop:SVF004',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    version='3.0',
                                    ref='frtop:RS_24'
                                )
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='frtop:SSP0042A',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='032',
                                        name=MultilingualString(
                                            value='Poste, St Jean'
                                        ),
                                        private_code=PrivateCode(
                                            value='legacy3452'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ],
                                        for_alighting=True,
                                        for_boarding=True
                                    ),
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone1(
                                        id='frtop:TZ_0010',
                                        version='001',
                                        name=MultilingualString(
                                            value='Zone A',
                                            lang='fr'
                                        ),
                                        members=PointRefsRelStructure(
                                            choice=[
                                                ScheduledStopPointRef(
                                                    version='032',
                                                    ref='frtop:SSP0042A'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    PassengerStopAssignment(
                                        id='frtop:PSA_40016_A1',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Timetable timetable ref to physical stop',
                                            lang='en'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='032',
                                            ref='frtop:SSP0042A'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SSP_02456A'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SSP_02456A_1'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='frtop:RF01',
                            version='any',
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='frtop:RS_22',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='3.0',
                                        name=MultilingualString(
                                            value='Stop data on street'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='frtop:RS_22_01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='3.0',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.COLLECTS,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        version='any',
                                                        ref='mybus:Org_Mb042'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='frtop:RS_24',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='3.0',
                                        name=MultilingualString(
                                            value='Stop data on timetable'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='frtop:RS_24_01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='3.0',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.COLLECTS,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        version='any',
                                                        ref='frtop:Org_Hd001'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Authority(
                                        id='mybus:Org_Mb042',
                                        version='any',
                                        name=MultilingualString(
                                            value='Pays De Fou Transport '
                                        ),
                                        short_name=MultilingualString(
                                            value='PDFT'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.AUTHORITY,
                                        ]
                                    ),
                                    Operator(
                                        id='frtop:Org_Hd001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Voyages Fou '
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
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
