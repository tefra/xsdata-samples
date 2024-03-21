from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.complex_feature import ComplexFeature
from netex.models.complex_feature_member_versioned_child_structure import ComplexFeatureMemberVersionedChildStructure
from netex.models.complex_feature_members_rel_structure import ComplexFeatureMembersRelStructure
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.direction_type import DirectionType
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.infrastructure_elements_in_frame_rel_structure import InfrastructureElementsInFrameRelStructure
from netex.models.infrastructure_frame import InfrastructureFrame
from netex.models.infrastructure_junctions_in_frame_rel_structure import InfrastructureJunctionsInFrameRelStructure
from netex.models.journey_pattern_wait_time import JourneyPatternWaitTime
from netex.models.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.line import Line
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.link_projection import LinkProjection
from netex.models.link_ref_structure import LinkRefStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.point_on_link_by_value_structure import PointOnLinkByValueStructure
from netex.models.point_on_route import PointOnRoute
from netex.models.point_projection import PointProjection
from netex.models.point_ref_structure import PointRefStructure
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.points_on_route_rel_structure import PointsOnRouteRelStructure
from netex.models.pos import Pos
from netex.models.projections_rel_structure import ProjectionsRelStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay import Quay
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
from netex.models.road_element import RoadElement
from netex.models.road_junction import RoadJunction
from netex.models.road_point_ref_structure import RoadPointRefStructure
from netex.models.route import Route
from netex.models.route_link import RouteLink
from netex.models.route_link_ref_structure import RouteLinkRefStructure
from netex.models.route_links_in_frame_rel_structure import RouteLinksInFrameRelStructure
from netex.models.route_point import RoutePoint
from netex.models.route_point_ref import RoutePointRef
from netex.models.route_point_ref_structure import RoutePointRefStructure
from netex.models.route_points_in_frame_rel_structure import RoutePointsInFrameRelStructure
from netex.models.route_ref import RouteRef
from netex.models.route_ref_structure import RouteRefStructure
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.spatial_feature_ref import SpatialFeatureRef
from netex.models.spatial_features_in_frame_rel_structure import SpatialFeaturesInFrameRelStructure
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.time_demand_type import TimeDemandType
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.timing_link import TimingLink
from netex.models.timing_link_ref_structure import TimingLinkRefStructure
from netex.models.timing_links_in_frame_rel_structure import TimingLinksInFrameRelStructure
from netex.models.timing_pattern import TimingPattern
from netex.models.timing_pattern_ref import TimingPatternRef
from netex.models.timing_patterns_in_frame_rel_structure import TimingPatternsInFrameRelStructure
from netex.models.timing_point import TimingPoint
from netex.models.timing_point_in_journey_pattern import TimingPointInJourneyPattern
from netex.models.timing_point_ref import TimingPointRef
from netex.models.timing_point_ref_structure import TimingPointRefStructure
from netex.models.timing_points_in_frame_rel_structure import TimingPointsInFrameRelStructure
from netex.models.timing_points_in_journey_pattern_rel_structure import TimingPointsInJourneyPatternRelStructure
from netex.models.type_of_projection_ref_structure import TypeOfProjectionRefStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_of_object_ref import VersionOfObjectRef
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        CompositeFrameRef(
                            ref='spqes:Fr1234'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex simple Paris Network Example'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='spqes:Fr1234',
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='spq',
                            xmlns='spq',
                            xmlns_url='http://www.spqes.eu/stuff',
                            description='My buses'
                        ),
                        Codespace(
                            id='hde',
                            xmlns='hde',
                            xmlns_url='http://www.halt.de/',
                            description='Stop data  data'
                        ),
                        Codespace(
                            id='gis',
                            xmlns='gis',
                            xmlns_url='http://www.gisdata.com/data',
                            description='Gis data '
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='spq'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='spq:Fr1234',
                            version='any',
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='spq:RS_01',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='2.0',
                                        name=MultilingualString(
                                            value='Responsible for STOP PLACEs'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='spq:RS_01_01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='2.0',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.COLLECTS,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='spq:RS_02',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='3.0',
                                        name=MultilingualString(
                                            value='Responsible for SERVICE PATTERN.'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='spq:RS_02_01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='3.0',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.COLLECTS,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='spq:RS_03',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='1.1',
                                        name=MultilingualString(
                                            value='Responsible for TIMING PATTERN.'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='spq:RS_03_01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='1.1',
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.COLLECTS,
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='spq:Fr1234',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    ref='spq:RS_02'
                                )
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='spq:SP1',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 1'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 1 Rue de Paris'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP1_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Rue de Paris'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 1'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 1'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP2',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 2'
                                        ),
                                        short_name=MultilingualString(
                                            value="Stop 2 Eue de l'est"
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP2_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Rue de Paris'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 2'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 2'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP3',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 3'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 3 Rue Galieni'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP3_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Rue Thiere'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP3',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 3'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 3'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP4',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 4'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 4 Rue du Dome'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP4_04',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Rue Thiere'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP4',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 4'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 4'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP5',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 5'
                                        ),
                                        short_name=MultilingualString(
                                            value="Stop 5 Rue d'Issy"
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP5_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value="Rue d'Issy"
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP5',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 5'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 5'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP6',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 6'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 6 Boulevard Jean Juares'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP6_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Boulevard Jean Juares'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP6',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 6'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop6'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP7',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 7'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 7 Boulogne Billancourt'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP7_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Avenue de General Leclerc'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP7',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 7'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 7'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP8',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 8'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 8'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP8_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Avenue de General Leclerc'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP8',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 8'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 8'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP9',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 9'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 9 Pont de Sevres'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='EPSG:9801'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='spq:Addr_SP9_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Avenue de General Leclerc'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='spq:SSP9',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Stop 9'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop 9'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='spq:SP10',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop 10'
                                        ),
                                        short_name=MultilingualString(
                                            value='Stop 10'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='spq:Fr1234',
                            version='any',
                            route_points=RoutePointsInFrameRelStructure(
                                route_point=[
                                    RoutePoint(
                                        id='spq:Rtpt1',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt2',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt3',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt4',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt5',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt6',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt7',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt8',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt9',
                                        version='any'
                                    ),
                                    RoutePoint(
                                        id='spq:Rtpt10',
                                        version='any'
                                    ),
                                ]
                            ),
                            route_links=RouteLinksInFrameRelStructure(
                                route_link=[
                                    RouteLink(
                                        id='spq:RL_Rt001o_01to02',
                                        version='any',
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='spq:LP_RL_Rt001o_01to02_PJ01',
                                                    version='any',
                                                    type_of_projection_ref=TypeOfProjectionRefStructure(
                                                        ref='spq:Spatial'
                                                    ),
                                                    spatial_feature_ref=SpatialFeatureRef(
                                                        version='any',
                                                        ref='gis:St_RueDeParis_01'
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt1'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt2'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_02to03',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt2'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt3'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_03to04',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt3'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt4'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_04to05',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt4'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt5'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_05to06',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt5'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt6'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_06to07',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt6'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt7'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_07to08',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt7'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt8'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_08to09',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt8'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt9'
                                        )
                                    ),
                                    RouteLink(
                                        id='spq:RL_Rt001o_09to10',
                                        version='any',
                                        from_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt9'
                                        ),
                                        to_point_ref=RoutePointRefStructure(
                                            version='any',
                                            ref='spq:Rtpt10'
                                        )
                                    ),
                                ]
                            ),
                            routes=RoutesInFrameRelStructure(
                                route=[
                                    Route(
                                        id='spq:Rt001o',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='004',
                                        responsibility_set_ref_attribute='spq:RS_01',
                                        name=MultilingualString(
                                            value='Route 66b outbound'
                                        ),
                                        line_ref=LineRef(
                                            version='002',
                                            ref='spq:LN0066'
                                        ),
                                        direction_type=DirectionType(

                                        ),
                                        points_in_sequence=PointsOnRouteRelStructure(
                                            point_on_route=[
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_001',
                                                    version='any',
                                                    order=1,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt1'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_01to02'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_002',
                                                    version='any',
                                                    order=2,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt2'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_02to03'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_003',
                                                    version='any',
                                                    order=3,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt3'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_03to04'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_004',
                                                    version='any',
                                                    order=4,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt4'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_005',
                                                    version='any',
                                                    order=5,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt5'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_006',
                                                    version='any',
                                                    order=6,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt6'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_06to07'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_007',
                                                    version='any',
                                                    order=7,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt7'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_07to08'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_008',
                                                    version='any',
                                                    order=8,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt8'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_009',
                                                    version='any',
                                                    order=9,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt9'
                                                    ),
                                                    onward_route_link_ref=RouteLinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    )
                                                ),
                                                PointOnRoute(
                                                    id='spq:RPIS_Rt001o_010',
                                                    version='any',
                                                    order=10,
                                                    choice_1=RoutePointRef(
                                                        version='any',
                                                        ref='spq:Rtpt10'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='spq:LN0066',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='002',
                                        name=MultilingualString(
                                            value='Line 66'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='ssp:SSP1',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 1'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_SSP1_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR1'
                                                    )
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP2',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 2'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP2_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_02to03'
                                                    ),
                                                    distance=Decimal('50')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP3',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 3'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP3_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    ),
                                                    distance=Decimal('30')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP4',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 4'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP4_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    ),
                                                    distance=Decimal('25')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP5',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 5'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP5_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_07to08'
                                                    ),
                                                    distance=Decimal('20')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP6',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 6'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP6_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    distance=Decimal('20')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP7',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 7'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP7_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    ),
                                                    distance=Decimal('5')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP8',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 8'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='ssp:LPJ_SSP8_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    ),
                                                    distance=Decimal('50')
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(
                                            value='Towards SSSP9'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP9',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 9'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_SSP9_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR10'
                                                    )
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(

                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='ssp:SSP10',
                                        created=XmlDateTime(2001, 6, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='Stop 10'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('-180'),
                                            latitude=Decimal('53')
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_SSP10_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR10'
                                                    )
                                                ),
                                            ]
                                        ),
                                        label=MultilingualString(

                                        )
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_1to2',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='1 to 2'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_1to2_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link SL 1-2::>RL 2-3 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_02to03'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('40')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP1'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP2'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_2to3',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='2 to 3 '
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_2to3_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link SL 2-3::>RL2-3 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_02to03'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('40')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_2to3_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole  link SL 2-3::>RL 3-4 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_03to04'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_2to3_PJ03',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part  link SL 2-3::>RL 4-5 x '
                                                    ),
                                                    order=3,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('35')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP2'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP3'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_3to4',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='3  to 4'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_3to4_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link SL 3-4::>RL4-5 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('40')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_3to4_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part  link SL 3-4::>RL 5-6 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('35')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP3'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP4'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_4to5',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='4  to 5'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_4to5_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link SL 4-5::>RL5-6 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('35')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_4to5_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole  link SL 4-5::>RL 6-7 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_06to07'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_4to5_PJ03',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part  link SL 4-5::>RL 7-8 x '
                                                    ),
                                                    order=3,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_07to08'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('45')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP4'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP5'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_5to6',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='5  to6'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_5to6_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link SL 5-6::>RL7-8 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_07to08'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('45')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_5to6_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part  link SL 5-6::>RL 8-9 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('20')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP5'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP6'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_6to7',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='6  to 7'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_6to7_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part along link SL 6-7::>RL8-9 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('20')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_6to7_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part  link SL 6-7::>RL 9-10 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('10')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP6'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP7'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_7to8',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='7  to 8'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_7to8_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way   along link SL 7-8::>RL9-10 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('10')
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('50')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP7'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP8'
                                        )
                                    ),
                                    ServiceLink(
                                        id='ssp:SL_SvP001o_8to9',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='8 to 9'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='ssp:LP_SL_SvP001o_8to9_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way   along link SL 8-9::>RL9-10 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('50')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP8'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='ssp:SSP9'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='ssp:SvP001o',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='SSP1 - SSP9'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            version='004',
                                            ref='spq:Rt001o'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP1'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_1to2'
                                                    ),
                                                    for_alighting=False,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP2'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_2to3'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP3'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_3to4'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_04',
                                                    version='any',
                                                    order=4,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP4'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_4to5'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_05',
                                                    version='any',
                                                    order=5,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP5'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_5to6'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_06',
                                                    version='any',
                                                    order=6,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP6'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_6to7'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_07',
                                                    version='any',
                                                    order=7,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP7'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_7to8'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_08',
                                                    version='any',
                                                    order=8,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP8'
                                                    ),
                                                    onward_service_link_ref=ServiceLinkRefStructure(
                                                        version='001',
                                                        ref='ssp:SL_SvP001o_8to9'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:SvPip_001o_09',
                                                    version='any',
                                                    order=9,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP9'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=False
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    PassengerStopAssignment(
                                        id='ssp:PSA_01',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 1'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP1'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP1'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP1'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_02',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 2'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP2'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP2'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP2'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_03',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 3'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP3'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP3'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP3'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_04',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 4'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP4'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP4'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP4'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_05',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 5'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP5'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP5'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP5'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_06',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 6'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP6'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP6'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP6'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_07',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 7'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP7'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP7'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP7'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_08',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 8'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP8'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP8'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP8'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_09',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment 9'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP9'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP9'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='any',
                                            ref='spq:SSP9'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ssp:PSA_10',
                                        version='any',
                                        description=MultilingualString(
                                            value='Bus Assignment10'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='001',
                                            ref='ssp:SSP10'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='spq:SP10'
                                        )
                                    ),
                                ]
                            ),
                            timing_points=TimingPointsInFrameRelStructure(
                                timing_point=[
                                    TimingPoint(
                                        id='tim:TP1',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT 1'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP1_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR1'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPoint(
                                        id='tim:TP2',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT 2'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP2_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR2'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPoint(
                                        id='tim:TP3',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT3'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP3_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR5'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPoint(
                                        id='tim:TP4',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT 4'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP4_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR8'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPoint(
                                        id='tim:TP5',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT 5'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP5_pj01',
                                                    version='any',
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    ),
                                                    distance=Decimal('25')
                                                ),
                                            ]
                                        )
                                    ),
                                    TimingPoint(
                                        id='tim:TP6',
                                        version='any',
                                        name=MultilingualString(
                                            value='TIMING POINT 6'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='tim:PPJ_TP6_pj01',
                                                    version='any',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='any',
                                                        ref='tim:PorR10'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            timing_links=TimingLinksInFrameRelStructure(
                                timing_link=[
                                    TimingLink(
                                        id='tim:TL_TP001o_TP1toTP2',
                                        version='any',
                                        name=MultilingualString(
                                            value='TP1 to TP2'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP1toTP2_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Exact projection  of links TL  1-2 ::>RL  1-2 '
                                                    ),
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_01to02'
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP1'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP2'
                                        )
                                    ),
                                    TimingLink(
                                        id='tim:TL_TP001o_TP2toTP3',
                                        version='any',
                                        name=MultilingualString(
                                            value='TP2 to TP3'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP2toTP3_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole link TL 2-3 ::>RL  2-3  '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_02to03'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP2toTP3_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection whole link TL 2-3 ::>RL  3-4  '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_03to04'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP2toTP3_PJ03',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part way along link TL2-3 ::>RL 4-5 '
                                                    ),
                                                    order=3,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('55')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP2'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP3'
                                        )
                                    ),
                                    TimingLink(
                                        id='tim:TL_TP001o_TP3toTP4',
                                        version='any',
                                        name=MultilingualString(
                                            value='TP3 to TP4'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP3toTP4_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection part way along  along linkTL 3-4  ::> RL : 4-5:'
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_04to05'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('55')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP3toTP4_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole link  TL 3-4::>RL 5-6'
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_05to06'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP3toTP4_PJ03',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole link TL 3-4::>RL 6-7 '
                                                    ),
                                                    order=3,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_06to07'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP3toTP4_PJ04',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole link TL 3-4::>RL 7-8 '
                                                    ),
                                                    order=4,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_07to08'
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP3toTP4_PJ05',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  part way along link TL 3-4::>RL 8-9 x '
                                                    ),
                                                    order=5,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('5')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP3'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP4'
                                        )
                                    ),
                                    TimingLink(
                                        id='tim:TL_TP001o_TP4toTP5',
                                        version='any',
                                        name=MultilingualString(
                                            value='TP4 to TP5'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP4toTP5_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link TL 4-5::>RL 8-9 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('5')
                                                    ),
                                                    end_point_on_link_ref_or_end_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('40')
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP4'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP5'
                                        )
                                    ),
                                    TimingLink(
                                        id='tim:TL_TP001o_TP5toTP6',
                                        version='any',
                                        name=MultilingualString(
                                            value='TP5 to TP6'
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP5toTP6_PJ01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  mid way along link TL 5-6::>RL 8-9 x '
                                                    ),
                                                    order=1,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_08to09'
                                                    ),
                                                    start_point_on_link_ref_or_start_point_on_link_by_value=PointOnLinkByValueStructure(
                                                        distance_from_start=Decimal('40')
                                                    )
                                                ),
                                                LinkProjection(
                                                    id='tim:LP_TL_TP001o_TP5toTP6_PJ02',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Projection  whole link TL 5-6::>RL 9-10 x '
                                                    ),
                                                    order=2,
                                                    project_to_link_ref=LinkRefStructure(
                                                        version='any',
                                                        ref='spq:RL_Rt001o_09to10'
                                                    )
                                                ),
                                            ]
                                        ),
                                        from_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP5'
                                        ),
                                        to_point_ref=TimingPointRefStructure(
                                            version='any',
                                            ref='tim:TP6'
                                        )
                                    ),
                                ]
                            ),
                            timing_patterns=TimingPatternsInFrameRelStructure(
                                timing_pattern=[
                                    TimingPattern(
                                        id='tim:TP001o',
                                        created=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='tim:RS_03',
                                        route_ref=RouteRefStructure(
                                            version='004',
                                            ref='spq:Rt001o'
                                        ),
                                        direction_type=DirectionType(

                                        ),
                                        time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                            version='any',
                                            ref='tim:TDT001'
                                        ),
                                        points_in_sequence=TimingPointsInJourneyPatternRelStructure(
                                            timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_01',
                                                    version='any',
                                                    order=1,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='tim:TL_TP001o_TP1toTP2'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_02',
                                                    version='any',
                                                    order=2,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='tim:TL_TP001o_TP1toTP2'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_03',
                                                    version='any',
                                                    order=3,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='tim:TL_TP001o_TP3toTP4'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_04',
                                                    version='any',
                                                    order=4,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='tim:TL_TP001o_TP4toTP5'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_05',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    onward_timing_link_ref=TimingLinkRefStructure(
                                                        version='any',
                                                        ref='tim:TL_TP001o_TP5toTP6'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='tim:TPIJP_TP001o_06',
                                                    version='any',
                                                    order=6,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                choice=[
                                    ServiceJourneyPattern(
                                        id='ssp:JP001o',
                                        version='any',
                                        route_ref_or_route_view=RouteRef(
                                            version='004',
                                            ref='spq:Rt001o'
                                        ),
                                        timing_pattern_ref=TimingPatternRef(
                                            version='001',
                                            ref='tim:TP001o'
                                        ),
                                        wait_times=JourneyPatternWaitTimesRelStructure(
                                            journey_pattern_wait_time_ref_or_journey_pattern_wait_time=[
                                                JourneyPatternWaitTime(
                                                    id='tim:JPRT_001',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='tim:TDT001'
                                                    ),
                                                    choice=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    wait_time=XmlDuration("PT5M")
                                                ),
                                                JourneyPatternWaitTime(
                                                    id='tim:JPRT_002',
                                                    version='any',
                                                    time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                        version='any',
                                                        ref='tim:TDT002'
                                                    ),
                                                    choice=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    wait_time=XmlDuration("PT10M")
                                                ),
                                            ]
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0001',
                                                    version='any',
                                                    order=1,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP1'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0002',
                                                    version='any',
                                                    projections=ProjectionsRelStructure(
                                                        projection_ref_or_projection=[
                                                            PointProjection(
                                                                id='tim:PIP_JP001o_0002',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Additional projection because there is a separate TimingPointIdID as well as a SSP'
                                                                ),
                                                                project_to_point_ref=PointRefStructure(
                                                                    name_of_ref_class='TimingPoint',
                                                                    version='001',
                                                                    ref='tim:TP2'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP1'
                                                    ),
                                                    is_wait_point=False,
                                                    wait_time_or_wait_times=JourneyPatternWaitTimesRelStructure(
                                                        journey_pattern_wait_time_ref_or_journey_pattern_wait_time=[
                                                            JourneyPatternWaitTime(
                                                                id='tim:JPRT_003',
                                                                version='any',
                                                                time_demand_type_ref_or_timeband_ref=TimeDemandTypeRef(
                                                                    version='any',
                                                                    ref='tim:TDT001'
                                                                ),
                                                                wait_time=XmlDuration("PT10M")
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0003',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP2'
                                                    ),
                                                    is_wait_point=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0004',
                                                    version='any',
                                                    order=4,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP3'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0005',
                                                    version='any',
                                                    order=5,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP3'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0006',
                                                    version='any',
                                                    order=6,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP4'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0007',
                                                    version='any',
                                                    order=7,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP5'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0008',
                                                    version='any',
                                                    order=8,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP4'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0009',
                                                    version='any',
                                                    order=9,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP6'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0010',
                                                    version='any',
                                                    order=10,
                                                    choice_1=TimingPointRef(
                                                        version='any',
                                                        ref='tim:TP5'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0011',
                                                    version='any',
                                                    order=11,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP7'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0012',
                                                    version='any',
                                                    order=12,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP8'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='ssp:PIP_JP001o_0013',
                                                    version='any',
                                                    projections=ProjectionsRelStructure(
                                                        projection_ref_or_projection=[
                                                            PointProjection(
                                                                id='tim:PIP_JP001o_0013',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Additional projection because there is a separate TimingPointIdID as well as a SSP'
                                                                ),
                                                                project_to_point_ref=PointRefStructure(
                                                                    name_of_ref_class='TimingPoint',
                                                                    version='001',
                                                                    ref='tim:TP6'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    order=13,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='ssp:SSP9'
                                                    ),
                                                    is_wait_point=True
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            time_demand_types=TimeDemandTypesInFrameRelStructure(
                                time_demand_type=[
                                    TimeDemandType(
                                        id='tim:TDT001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Time demand Peak'
                                        )
                                    ),
                                    TimeDemandType(
                                        id='tim:TDT002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Time demand  off Peak'
                                        )
                                    ),
                                ]
                            )
                        ),
                        InfrastructureFrame(
                            id='spq:InfrastructureFrame:Fr1234',
                            version='any',
                            spatial_features=SpatialFeaturesInFrameRelStructure(
                                simple_feature_or_complex_feature=[
                                    ComplexFeature(
                                        id='gis:Road_RueDeParis1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue de Paris'
                                        ),
                                        feature_members=ComplexFeatureMembersRelStructure(
                                            complex_feature_member=[
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_P001',
                                                    version='any',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueDeParis1_001'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_P002',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueDeParis1_002'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_P003',
                                                    version='any',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueDeParis1_003'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_P004',
                                                    version='any',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueDeParis1_004'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_L001',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueDeParis1_002to003'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:Road_RueDeParis1_L002',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueDeParis1_003to004'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ComplexFeature(
                                        id='gis:RdP_RouteDeLaReine1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Route De la Reine'
                                        ),
                                        feature_members=ComplexFeatureMembersRelStructure(
                                            complex_feature_member=[
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RouteDeLaReine1_P001',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RouteDeLaReine_021'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RouteDeLaReine1_P002',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RouteDeLaReine_022'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RouteDeLaReine1_L001',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RouteDeLaReine_004to005'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ComplexFeature(
                                        id='gis:RdP_RueThiere1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere'
                                        ),
                                        feature_members=ComplexFeatureMembersRelStructure(
                                            complex_feature_member=[
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_P002',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueThiere_002'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_P003',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueThiere_003'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_P004',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueThiere_004'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_P005',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadJunction',
                                                        ref='gis:RdP_RueThiere_005'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_L001',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueThiere_X022to002'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_L002',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueThiere_002to003'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_L003',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueThiere_003to004'
                                                    )
                                                ),
                                                ComplexFeatureMemberVersionedChildStructure(
                                                    id='gis:RdP_RueThiere1_L004',
                                                    choice=VersionOfObjectRef(
                                                        name_of_ref_class='RoadElement',
                                                        ref='gis:RdE_RueThiere_004to005'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ComplexFeature(
                                        id='gis:RdP_RueDuPointDuJour1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue du Point du Jour'
                                        )
                                    ),
                                    ComplexFeature(
                                        id='gis:RdE_BvdJeanJaures',
                                        version='any',
                                        name=MultilingualString(
                                            value='Boulevard  Jean Jaures'
                                        )
                                    ),
                                    ComplexFeature(
                                        id='gis:RdE_AvGenLeclerc',
                                        version='any',
                                        name=MultilingualString(
                                            value='Avenue General Leclerc'
                                        )
                                    ),
                                ]
                            ),
                            junctions=InfrastructureJunctionsInFrameRelStructure(
                                railway_junction_or_road_junction_or_wire_junction=[
                                    RoadJunction(
                                        id='gis:RdP_RueDeParis1_001',
                                        version='any',
                                        name=MultilingualString(
                                            value='start at PontCLoud end>'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueDeParis1_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue de Paris x  Rue de Silly'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueDeParis1_003',
                                        version='any',
                                        name=MultilingualString(
                                            value="Rue de Paris x  Rue d'Agguesseau"
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueDeParis1_004',
                                        version='any',
                                        name=MultilingualString(
                                            value="Rue de Paris x  Rue de L'Est"
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RouteDeLaReine_021',
                                        version='any',
                                        name=MultilingualString(
                                            value="Route De la Reine x  Rue de L'Est"
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RouteDeLaReine_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Route De la Reine x Av Victor Hugo '
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueThiere_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere x Rue Galieni  '
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueThiere_003',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere x Av Edouard Vaillant  '
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueThiere_004',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere x Rue Marcel Dassault'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_RueThiere_005',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere x Rue du Pon du Jour '
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_DuPointDuJour_041',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Du Point du Jour x  Rue de Seine'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_BvdJeanJaures_021',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Du Point du Jour x Bvd  Jean Jaures'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_BvdJeanJaures_022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bvd  Jean Jaures x Rue Du Dome'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_AvGenLeclerc_050',
                                        version='any',
                                        name=MultilingualString(
                                            value='Av Gen Leclerc  x Bvd  Jean Jaures'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_AvGenLeclerc_051',
                                        version='any',
                                        name=MultilingualString(
                                            value='Av Gen Leclerc  x Rue de la ferme'
                                        )
                                    ),
                                    RoadJunction(
                                        id='gis:RdP_AvGenLeclerc_052',
                                        version='any',
                                        name=MultilingualString(
                                            value='Av Gen Leclerc   x Pont de Sevres'
                                        )
                                    ),
                                ]
                            ),
                            elements=InfrastructureElementsInFrameRelStructure(
                                railway_element_or_road_element_or_wire_element=[
                                    RoadElement(
                                        id='gis:RdE_RueDeParis1_002to003',
                                        version='any',
                                        name=MultilingualString(
                                            value="Rue de Paris:  x Rue de Silly to Rue de Paris x Rue d'Agguesseau"
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueDeParis1_002'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueDeParis1_003'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueDeParis_003to004',
                                        version='any',
                                        name=MultilingualString(
                                            value="Rue de Paris:  x  Rue d'Agguesseau to Rue de Paris x Rue de l'est"
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueDeParis1_003'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueDeParis1_004'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RouteDeLaReine_004to005',
                                        version='any',
                                        name=MultilingualString(
                                            value="Rue de l'est : x Rue de Silly to Route De la Reine x Rue de l'est "
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueDeParis1_004'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RouteDeLaReine_021'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RouteDeLaReine_021to022',
                                        version='any',
                                        name=MultilingualString(
                                            value="Route De la Reine:  x Rue de l'est to Route De la Reine  x Av Victor Hugo   "
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RouteDeLaReine_021'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RouteDeLaReine_022'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueThiere_X022to002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere: Route De la Reine  x AV Victor Hugo   to Rue Thiere x Rue Galieni '
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RouteDeLaReine_022'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_002'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueThiere_002to003',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere : x Rue Galieni    to Rue Thiere x Av Edouard Vaillant  '
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_002'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_003'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueThiere_003to004',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere : x Av Eiouard Vaillant  to  Rue Thiere x Rue Marcel Dassault'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_003'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_004'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueThiere_004to005',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Thiere:  x  Rue Marcel Dassault to   Rue Thiere x DuPontDuJour '
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_004'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_005'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueDuPontDuJour_005toX041',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue  Du Point du Jour: Rue Thiere x  Rue du Pont du Jourto  Rue Du Point du Jour x  Rue de Seine'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_RueThiere_005'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_DuPointDuJour_041'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_RueDuPointDuJour_041to042',
                                        version='any',
                                        name=MultilingualString(
                                            value='Rue Du Point du Jour : x  Rue de Seine to   Rue du Pont du Jour  x Bvd  Jean Jaures'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_DuPointDuJour_041'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_BvdJeanJaures_021'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_BvdJeanJaures_021to022',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bvd Jean Jaures:  Rue du Pont du Jour  x Bvd  Jean Jaures to  Bvd  Jean Jaures x Rue Du Dome'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_BvdJeanJaures_021'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_BvdJeanJaures_022'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_BvdJeanJaures_022to023',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bvd Jean Jaures:   Bvd  Jean Jaures x Rue Du Dome to    Av Gen Leclerc :   x Bvd  Jean Jaures'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_BvdJeanJaures_022'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_AvGenLeclerc_050'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_AvGenLeclerc_050to051',
                                        version='any',
                                        name=MultilingualString(
                                            value='Av Gen Leclerc :   x Bvd  Jean Jaures  to  Av Gen Leclerc x Rue de la ferme'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_AvGenLeclerc_050'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_AvGenLeclerc_051'
                                        )
                                    ),
                                    RoadElement(
                                        id='gis:RdE_AvGenLeclerc_051to052',
                                        version='any',
                                        name=MultilingualString(
                                            value='Av Gen Leclerc : Av Gen Leclerc x Rue de la ferme to    Av Gen Leclerc   x Pont de Sevres'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_AvGenLeclerc_051'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='any',
                                            ref='gis:RdP_AvGenLeclerc_052'
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
