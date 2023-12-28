from decimal import Decimal
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.accessibility_info_facility_enumeration import AccessibilityInfoFacilityEnumeration
from netex.models.accessibility_limitation import AccessibilityLimitation
from netex.models.accessibility_limitations_rel_structure import AccessibilityLimitationsRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.limitation_status_enumeration import LimitationStatusEnumeration
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.pos import Pos
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay import Quay
from netex.models.quay_ref import QuayRef
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.road_address import RoadAddress
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_place_view import TopographicPlaceView
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        description=MultilingualString(
            value='Filter used to reest these contnets Get all STOP PLACEs, STOP ASSIGNMENTs and reponsib ilitySets  for Network TNET1 in topgraphic area    :TP_0032A.\n\t\t\t\tAlso get details for \n\t\t\t\t'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    version_frame_ref=[
                        NetworkFilterByValueStructure(
                            object_references=ObjectFilterByValueStructure.ObjectReferences(
                                choice=[
                                    TopographicPlaceRef(
                                        ref='detop:TP_0032A'
                                    ),
                                ]
                            ),
                            places=NetworkFilterByValueStructure.Places(
                                choice=[
                                    TopographicPlaceRef(
                                        version='any',
                                        ref='detop:TP_0032A'
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P3M"),
    description=MultilingualString(
        value='Simple Stop pair On street example'
    ),
    data_objects=DataObjectsRelStructure(
        common_frame=[
            CompositeFrame(
                id='mybus:CF002',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        validity_condition_ref_or_validity_condition=[
                            AvailabilityCondition(
                                id='jqx:CF002',
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
                            id='jqx',
                            xmlns='jqx',
                            xmlns_url='http://www.VKWzn.de/',
                            description='Bus data  namesapce'
                        ),
                        Codespace(
                            id='detop',
                            xmlns='detop',
                            xmlns_url='http://www.pttopog.de',
                            description='German locality data'
                        ),
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.busfahrt.de',
                            description='German locality data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='jqx'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        SiteFrame(
                            id='detop:SF00121',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    value='EXTERNAL',
                                    ref='detop:RS_24'
                                )
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='detop:TP_0032A',
                                        version='any',
                                        name=MultilingualString(
                                            value='Keinstadt',
                                            lang='de'
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Keinstadt auf dem Fluss',
                                                lang='de'
                                            ),
                                            short_name=MultilingualString(
                                                value='Keinstadt',
                                                lang='de'
                                            ),
                                            qualify=TopographicPlaceDescriptorVersionedChildStructure.Qualify(
                                                qualifier_name=MultilingualString(
                                                    value='Mittleland',
                                                    lang='de'
                                                ),
                                                topographic_place_ref=TopographicPlaceRef(
                                                    version='any',
                                                    ref='detop:TP_0100'
                                                )
                                            )
                                        )
                                    ),
                                    TopographicPlace(
                                        id='detop:TP_0100',
                                        version='any',
                                        name=MultilingualString(
                                            value='Mittleland',
                                            lang='de'
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='Mittleland',
                                                lang='de'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='mybus:SP_0751A',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='01',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Stadtmuseum',
                                            lang='de'
                                        ),
                                        short_name=MultilingualString(
                                            value='Museum ',
                                            lang='de'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='DEGrid'
                                                )
                                            )
                                        ),
                                        accessibility_assessment=AccessibilityAssessment(
                                            id='mybus:SP_0751A',
                                            version='any',
                                            mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                            limitations=AccessibilityLimitationsRelStructure(
                                                accessibility_limitation=AccessibilityLimitation(
                                                    wheelchair_access=LimitationStatusEnumeration.TRUE,
                                                    step_free_access=LimitationStatusEnumeration.TRUE
                                                )
                                            )
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceView(
                                            topographic_place_ref=TopographicPlaceRef(
                                                version='any',
                                                ref='detop:TP_0032A'
                                            )
                                        ),
                                        transport_mode=VehicleModeEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP_0751A_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Stadtmuseum Haltstelle A',
                                                        lang='de'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Zum Ecke Museum Strasse und Kohlstrasse - 50 m nach Museum eingang .',
                                                            lang='de'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    road_address=RoadAddress(
                                                        id='mybus:Rad_SP001A_01',
                                                        version='any',
                                                        road_name=MultilingualString(
                                                            value='Museumstrasse'
                                                        )
                                                    ),
                                                    cross_road=MultilingualString(
                                                        value='Kohlstrasse',
                                                        lang='de'
                                                    ),
                                                    landmark=MultilingualString(
                                                        value='Stadtmuseum',
                                                        lang='de'
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    lighting=LightingEnumeration.WELL_LIT,
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            PassengerInformationEquipment(
                                                                id='mybus:Rad_SP001A_01',
                                                                version='any',
                                                                accessibility_info_facility_list=[
                                                                    AccessibilityInfoFacilityEnumeration.AUDIO_FOR_HEARING_IMPAIRED,
                                                                    AccessibilityInfoFacilityEnumeration.VISUAL_DISPLAYS,
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    label=MultilingualString(
                                                        value='A',
                                                        lang='de'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP_0751A_2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Stadtmuseum Haltstelle B',
                                                        lang='de'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Zum Ecke Museum Strasse und Kohlstrasse - 50 m nach Museum eingang am anderen seit .',
                                                            lang='de'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397148'),
                                                            latitude=Decimal('51.4217482063')
                                                        )
                                                    ),
                                                    road_address=RoadAddress(
                                                        id='mybus:Rad_Q_SP_0751A_2',
                                                        version='any',
                                                        road_name=MultilingualString(
                                                            value='Museumstrasse'
                                                        )
                                                    ),
                                                    cross_road=MultilingualString(
                                                        value='Kohlstrasse',
                                                        lang='de'
                                                    ),
                                                    landmark=MultilingualString(
                                                        value='Stadtmuseum',
                                                        lang='de'
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    lighting=LightingEnumeration.WELL_LIT,
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            PassengerInformationEquipment(
                                                                id='mybus:Q_SP_0751A_2',
                                                                version='any',
                                                                accessibility_info_facility_list=[
                                                                    AccessibilityInfoFacilityEnumeration.AUDIO_FOR_HEARING_IMPAIRED,
                                                                    AccessibilityInfoFacilityEnumeration.VISUAL_DISPLAYS,
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    label=MultilingualString(
                                                        value='B',
                                                        lang='de'
                                                    ),
                                                    public_code='1-3455 ',
                                                    compass_octant=CompassBearing8Enumeration.N,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='jqx:SV0021',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    value='EXTERNAL',
                                    ref='jqx:RS_22'
                                )
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='jqx:SSP0021A',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='032',
                                        name=MultilingualString(
                                            value='Stadtmuseum'
                                        ),
                                        label=MultilingualString(
                                            value='Stadmuseum Zum Bahnhof'
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    PassengerStopAssignment(
                                        id='jqx:PSA_20012_A',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Museum timetable ref to physical stop - regardless of quay ',
                                            lang='en'
                                        ),
                                        order=1,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='032',
                                            ref='jqx:SSP0021A'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='mybus:SP_0751A'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='jqx:PSA_20012_A1',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Eastbound Museum timetable ref to physical stop',
                                            lang='en'
                                        ),
                                        order=2,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='032',
                                            ref='jqx:SSP0021A'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='mybus:SP_0751A'
                                        ),
                                        quay_ref_or_quay=QuayRef(
                                            version='01',
                                            ref='mybus:Q_SP_0751A_1'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='jqx:PSA_20012_A2',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns Westbound Museum timetable ref to physical stop',
                                            lang='en'
                                        ),
                                        order=3,
                                        scheduled_stop_point_ref=ScheduledStopPointRef(
                                            version='032',
                                            ref='jqx:SSP0021A'
                                        ),
                                        stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='mybus:SP_0751A'
                                        ),
                                        quay_ref_or_quay=QuayRef(
                                            version='01',
                                            ref='mybus:Q_SP_0751A_2'
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
