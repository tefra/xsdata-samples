from netex.models.activation_point import ActivationPoint
from netex.models.activation_points_in_frame_rel_structure import ActivationPointsInFrameRelStructure
from netex.models.administrative_zone_version_structure import AdministrativeZone
from netex.models.administrative_zone_version_structure import AdministrativeZonesRelStructure
from netex.models.alternative_name import AlternativeName
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.alternative_texts_rel_structure import AlternativeText
from netex.models.alternative_texts_rel_structure import AlternativeTextsRelStructure
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import OperatingDay
from netex.models.alternative_texts_rel_structure import OperatingDaysRelStructure
from netex.models.alternative_texts_rel_structure import TimebandVersionedChildStructure
from netex.models.alternative_texts_rel_structure import TimebandsRelStructure
from netex.models.alternative_texts_rel_structure import ValidBetween
from netex.models.alternative_texts_rel_structure import ValidDuring
from netex.models.alternative_texts_rel_structure import ValidityCondition
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.alternative_texts_rel_structure import ValidityTrigger
from netex.models.authority import Authority
from netex.models.beacon_point import BeaconPoint
from netex.models.blacklist import Blacklist
from netex.models.blacklists_in_frame_rel_structure import BlacklistsInFrameRelStructure
from netex.models.codespace import Codespace
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compound_train import CompoundTrain
from netex.models.control_centre import ControlCentre
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.dated_service_journey import DatedServiceJourney
from netex.models.dead_run import DeadRun
from netex.models.department import Department
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.entrance import Entrance
from netex.models.equipment_place import EquipmentPlace
from netex.models.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.models.equipments_rel_structure import EquipmentsRelStructure
from netex.models.extensions_2 import Extensions2
from netex.models.facility_requirement import FacilityRequirement
from netex.models.facility_requirements_rel_structure import FacilityRequirementsRelStructure
from netex.models.fare_zone import FareZone
from netex.models.flexible_line import FlexibleLine
from netex.models.flexible_stop_place import FlexibleStopPlace
from netex.models.flexible_stop_places_in_frame_rel_structure import FlexibleStopPlacesInFrameRelStructure
from netex.models.general_zone import GeneralZone
from netex.models.group_of_entities_in_frame_rel_structure import GroupOfEntitiesInFrameRelStructure
from netex.models.group_of_lines import GroupOfLines
from netex.models.group_of_operators import GroupOfOperators
from netex.models.group_of_stop_places import GroupOfStopPlaces
from netex.models.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.models.groups_of_operators_in_frame_rel_structure import GroupsOfOperatorsInFrameRelStructure
from netex.models.groups_of_stop_places_in_frame_rel_structure import GroupsOfStopPlacesInFrameRelStructure
from netex.models.heading_sign import HeadingSign
from netex.models.infrastructure_elements_in_frame_rel_structure import InfrastructureElementsInFrameRelStructure
from netex.models.infrastructure_frame import InfrastructureFrame
from netex.models.infrastructure_junctions_in_frame_rel_structure import InfrastructureJunctionsInFrameRelStructure
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.journeys_in_frame_rel_structure import JourneysInFrameRelStructure
from netex.models.key_list import KeyList
from netex.models.key_value_structure import KeyValueStructure
from netex.models.line import Line
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.management_agent import ManagementAgent
from netex.models.multilingual_string import MultilingualString
from netex.models.operating_department import OperatingDepartment
from netex.models.operational_context import OperationalContext
from netex.models.operational_contexts_in_frame_rel_structure import OperationalContextsInFrameRelStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_part import OrganisationPart
from netex.models.organisation_parts_rel_structure import OrganisationPartsRelStructure
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.other_organisation import OtherOrganisation
from netex.models.parking import Parking
from netex.models.parking_area import ParkingArea
from netex.models.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.models.parking_bay import ParkingBay
from netex.models.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.models.parking_capacities_rel_structure import ParkingCapacitiesRelStructure
from netex.models.parking_capacity import ParkingCapacity
from netex.models.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from netex.models.parking_entrances_for_vehicles_rel_structure import ParkingEntrancesForVehiclesRelStructure
from netex.models.parking_passenger_entrance import ParkingPassengerEntrance
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_properties_rel_structure import ParkingPropertiesRelStructure
from netex.models.parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from netex.models.passenger_capacities_rel_structure import PassengerCapacitiesRelStructure
from netex.models.passenger_capacity import PassengerCapacity
from netex.models.place_lighting import PlaceLighting
from netex.models.point_of_interest import PointOfInterest
from netex.models.point_of_interest_classification import PointOfInterestClassification
from netex.models.point_of_interest_classifications_in_frame_rel_structure import PointOfInterestClassificationsInFrameRelStructure
from netex.models.point_projection import PointProjection
from netex.models.point_ref_structure import PointRefStructure
from netex.models.point_refs_rel_structure import PointRefsRelStructure
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.points_of_interest_in_frame_rel_structure import PointsOfInterestInFrameRelStructure
from netex.models.projections_rel_structure import ProjectionsRelStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.quay import Quay
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.railway_element import RailwayElement
from netex.models.railway_junction import RailwayJunction
from netex.models.railway_point_ref_structure import RailwayPointRefStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from netex.models.road_element import RoadElement
from netex.models.road_junction import RoadJunction
from netex.models.road_point_ref_structure import RoadPointRefStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.schematic_map import SchematicMap
from netex.models.schematic_map_member_versioned_child_structure import SchematicMapMemberVersionedChildStructure
from netex.models.schematic_map_members_rel_structure import SchematicMapMembersRelStructure
from netex.models.schematic_maps_in_frame_rel_structure import SchematicMapsInFrameRelStructure
from netex.models.section_in_sequence_versioned_child_structure import JourneyPattern
from netex.models.service_facility_set import ServiceFacilitySet
from netex.models.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.models.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey import ServiceJourney
from netex.models.service_link import ServiceLink
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.serviced_organisation import ServicedOrganisation
from netex.models.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_sets_in_frame_rel_structure import SiteFacilitySetsInFrameRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.special_service import SpecialService
from netex.models.stop_area import StopArea
from netex.models.stop_areas_in_frame_rel_structure import StopAreasInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.tariff_zone import TariffZone
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.template_service_journey import TemplateServiceJourney
from netex.models.timetable_frame import TimetableFrame
from netex.models.timing_point_in_journey_pattern import TimingPointInJourneyPattern
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.train import Train
from netex.models.train_component import TrainComponent
from netex.models.train_components_rel_structure import TrainComponentsRelStructure
from netex.models.train_element import TrainElement
from netex.models.transport_organisation_refs_rel_structure import TransportOrganisationRefsRelStructure
from netex.models.travel_agent import TravelAgent
from netex.models.type_of_equipment import TypeOfEquipment
from netex.models.types_of_equipment_rel_structure import TypesOfEquipmentRelStructure
from netex.models.vehicle_equipmen_profiles_in_frame_rel_structure import VehicleEquipmenProfilesInFrameRelStructure
from netex.models.vehicle_equipment_profile import VehicleEquipmentProfile
from netex.models.vehicle_journey import VehicleJourney
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.version import Version
from netex.models.versions_rel_structure import VersionsRelStructure
from netex.models.whitelist import Whitelist
from netex.models.whitelists_in_frame_rel_structure import WhitelistsInFrameRelStructure
from netex.models.wire_element import WireElement
from netex.models.wire_junction import WireJunction
from netex.models.wire_point_ref import WirePointRef
from netex.models.wire_point_ref_structure import WirePointRefStructure
from netex.models.zone import Zone
from netex.models.zone_projection import ZoneProjection
from netex.models.zone_ref_structure import ZoneRefStructure
from netex.models.zones_in_frame_rel_structure import ZonesInFrameRelStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Uniquness check '
    ),
    data_objects=DataObjectsRelStructure(
        common_frame=[
            CompositeFrame(
                id='mybus:ntwkf001',
                version='001',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='bar',
                            xmlns='bar',
                            xmlns_url='Test'
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id='bar:foo',
                            version='001',
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                    Authority(
                                        id='bar:foo2',
                                        version='001'
                                    ),
                                    ServicedOrganisation(
                                        id='bar:foo3',
                                        version='001'
                                    ),
                                    TravelAgent(
                                        id='bar:foo4',
                                        version='001'
                                    ),
                                    ManagementAgent(
                                        id='bar:foo5',
                                        version='001'
                                    ),
                                    OtherOrganisation(
                                        id='bar:foo5',
                                        validity_conditions_or_valid_between=[
                                            ValidityConditionsRelStructure(
                                                validity_condition_ref_or_validity_condition=[
                                                    ValidityCondition(
                                                        id='bar:foo',
                                                        version='001'
                                                    ),
                                                    ValidityTrigger(
                                                        id='bar:foo1',
                                                        version='001'
                                                    ),
                                                    AvailabilityCondition(
                                                        id='bar:foo3',
                                                        version='001',
                                                        timebands=TimebandsRelStructure(
                                                            timeband_ref_or_timeband=[
                                                                TimebandVersionedChildStructure(
                                                                    id='bar:foo',
                                                                    version='001',
                                                                    start_time=XmlTime(0, 0, 0, 0)
                                                                ),
                                                            ]
                                                        ),
                                                        operating_days=OperatingDaysRelStructure(
                                                            operating_day_ref_or_operating_day=[
                                                                OperatingDay(
                                                                    id='bar:foo',
                                                                    version='001',
                                                                    calendar_date=XmlDate(2001, 1, 1)
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ValidDuring(
                                                        id='bar:foo',
                                                        version='001'
                                                    ),
                                                    ValidBetween(
                                                        id='bar:foo',
                                                        version='001'
                                                    ),
                                                ]
                                            ),
                                        ],
                                        alternative_texts=AlternativeTextsRelStructure(
                                            alternative_text=[
                                                AlternativeText(
                                                    id='bar:foo',
                                                    version='001',
                                                    text=MultilingualString(
                                                        value='Fum'
                                                    ),
                                                    attribute_name='Name',
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        version='001',
                                        key_list=KeyList(
                                            key_value=[
                                                KeyValueStructure(
                                                    key='bar',
                                                    value='foo',
                                                    type_of_key='bar:foo'
                                                ),
                                            ]
                                        ),
                                        extensions=Extensions2(

                                        ),
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    id='bar:foo',
                                                    version='001',
                                                    name=MultilingualString(
                                                        value='Foo'
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        ),
                                        parts=OrganisationPartsRelStructure(
                                            organisation_part_ref_or_organisation_part=[
                                                OrganisationPart(
                                                    id='bar:foo',
                                                    version='001',
                                                    administrative_zones=AdministrativeZonesRelStructure(
                                                        administrative_zone=[
                                                            AdministrativeZone(
                                                                id='bar:foo',
                                                                version='001'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                ControlCentre(
                                                    id='bar:foo',
                                                    version='001'
                                                ),
                                                Department(
                                                    id='bar:foo',
                                                    version='001'
                                                ),
                                                OperatingDepartment(
                                                    id='bar:foo1',
                                                    version='001'
                                                ),
                                            ]
                                        ),
                                        own_responsibility_sets=ResponsibilitySetsRelStructure(
                                            responsibility_set_ref_or_responsibility_set=[
                                                ResponsibilitySet(
                                                    id='bar:foo',
                                                    version='001',
                                                    roles=ResponsibilityRoleAssignmentsRelStructure(
                                                        responsibility_role_assignment=[
                                                            ResponsibilityRoleAssignment(
                                                                id='bar:foo',
                                                                version='001'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            groups_of_operators=GroupsOfOperatorsInFrameRelStructure(
                                group_of_operators=[
                                    GroupOfOperators(
                                        id='bar:foo',
                                        version='001',
                                        members=TransportOrganisationRefsRelStructure(
                                            transport_organisation_ref=[
                                                OperatorRef(
                                                    version='001',
                                                    ref='bar:foo'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            operational_contexts=OperationalContextsInFrameRelStructure(
                                operational_context=[
                                    OperationalContext(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                compound_train_or_train_or_vehicle_type=[
                                    Train(
                                        id='bar:foo',
                                        version='001',
                                        satisfies_facility_requirements=FacilityRequirementsRelStructure(
                                            facility_requirement_ref_or_facility_requirement=[
                                                FacilityRequirement(
                                                    id='bar:foo',
                                                    version='001'
                                                ),
                                            ]
                                        ),
                                        components=TrainComponentsRelStructure(
                                            train_component_ref_or_train_component=[
                                                TrainComponent(
                                                    id='bar:foo',
                                                    version='001',
                                                    train_element_ref_or_train_element=TrainElement(
                                                        id='bar:foo',
                                                        version='001',
                                                        capacities=PassengerCapacitiesRelStructure(
                                                            passenger_capacity_ref_or_passenger_capacity=[
                                                                PassengerCapacity(
                                                                    id='bar:foo',
                                                                    version='001'
                                                                ),
                                                            ]
                                                        ),
                                                        facilities=ServiceFacilitySetsRelStructure(
                                                            service_facility_set_ref_or_service_facility_set=[
                                                                ServiceFacilitySet(
                                                                    id='bar:foo',
                                                                    version='001',
                                                                    other_facilities=TypesOfEquipmentRelStructure(
                                                                        type_of_equipment_ref_or_type_of_equipment=[
                                                                            TypeOfEquipment(
                                                                                id='bar:foo',
                                                                                version='001'
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    order=1
                                                ),
                                            ]
                                        )
                                    ),
                                    CompoundTrain(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            vehicle_models=VehicleModelsInFrameRelStructure(
                                vehicle_model=[
                                    VehicleModel(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            vehicle_equipment_profiles=VehicleEquipmenProfilesInFrameRelStructure(
                                vehicle_equipment_profile=[
                                    VehicleEquipmentProfile(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            schematic_maps=SchematicMapsInFrameRelStructure(
                                schematic_map=[
                                    SchematicMap(
                                        id='bar:foo',
                                        version='001',
                                        members=SchematicMapMembersRelStructure(
                                            schematic_map_member=[
                                                SchematicMapMemberVersionedChildStructure(
                                                    id='bar:foo',
                                                    version='001'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            groups_of_entities=GroupOfEntitiesInFrameRelStructure(
                                choice=[
                                    Zone(
                                        id='bar:foo6',
                                        version='001'
                                    ),
                                    Entrance(
                                        id='bar:foo6',
                                        version='001'
                                    ),
                                ]
                            ),
                            zones=ZonesInFrameRelStructure(
                                choice=[
                                    GeneralZone(
                                        id='bar:foo3',
                                        version='001',
                                        members=PointRefsRelStructure(
                                            choice=[
                                                WirePointRef(
                                                    version='001',
                                                    ref='bar:foo'
                                                ),
                                            ]
                                        ),
                                        projections=ProjectionsRelStructure(
                                            projection_ref_or_projection=[
                                                PointProjection(
                                                    id='bar:foo',
                                                    version='001',
                                                    project_to_point_ref=PointRefStructure(
                                                        version='001',
                                                        ref='bar:foo'
                                                    )
                                                ),
                                                ZoneProjection(
                                                    id='bar:foo',
                                                    version='001',
                                                    projected_zone_ref=ZoneRefStructure(
                                                        version='001',
                                                        ref='bar:foo'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            blacklists=BlacklistsInFrameRelStructure(
                                blacklist=[
                                    Blacklist(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            whitelists=WhitelistsInFrameRelStructure(
                                whitelist=[
                                    Whitelist(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            )
                        ),
                        InfrastructureFrame(
                            id='bar:foo',
                            version='001',
                            name=MultilingualString(
                                value='My Network  (V1) '
                            ),
                            junctions=InfrastructureJunctionsInFrameRelStructure(
                                railway_junction_or_road_junction_or_wire_junction=[
                                    WireJunction(
                                        id='bar:foo',
                                        version='001',
                                        name=MultilingualString(
                                            value='POINT'
                                        )
                                    ),
                                    RailwayJunction(
                                        id='bar:foo1',
                                        version='001',
                                        name=MultilingualString(
                                            value='POINT'
                                        )
                                    ),
                                    RoadJunction(
                                        id='bar:foo2',
                                        version='001',
                                        name=MultilingualString(
                                            value='POINT'
                                        )
                                    ),
                                ]
                            ),
                            elements=InfrastructureElementsInFrameRelStructure(
                                railway_element_or_road_element_or_wire_element=[
                                    WireElement(
                                        id='bar:foo',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINK'
                                        ),
                                        from_point_ref=WirePointRefStructure(
                                            version='001',
                                            ref='bar:foo'
                                        ),
                                        to_point_ref=WirePointRefStructure(
                                            version='001',
                                            ref='bar:foo'
                                        )
                                    ),
                                    RailwayElement(
                                        id='bar:foo1',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINK'
                                        ),
                                        from_point_ref=RailwayPointRefStructure(
                                            version='001',
                                            ref='bar:foo1'
                                        ),
                                        to_point_ref=RailwayPointRefStructure(
                                            version='001',
                                            ref='bar:foo1'
                                        )
                                    ),
                                    RoadElement(
                                        id='bar:foo2',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINK'
                                        ),
                                        from_point_ref=RoadPointRefStructure(
                                            version='001',
                                            ref='bar:foo2'
                                        ),
                                        to_point_ref=RoadPointRefStructure(
                                            version='001',
                                            ref='bar:foo2'
                                        )
                                    ),
                                ]
                            ),
                            activation_points=ActivationPointsInFrameRelStructure(
                                activation_point=[
                                    ActivationPoint(
                                        id='bar:foo3',
                                        version='001'
                                    ),
                                    BeaconPoint(
                                        id='bar:foo4',
                                        version='001'
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='bar:foo',
                            version='001',
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='bar:foo1',
                                        version='001',
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            name=MultilingualString(
                                                value='ZONE'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            groups_of_stop_places=GroupsOfStopPlacesInFrameRelStructure(
                                group_of_stop_places=[
                                    GroupOfStopPlaces(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='bar:foo2',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        ),
                                        equipment_places=EquipmentPlacesRelStructure(
                                            equipment_place_ref_or_equipment_place=[
                                                EquipmentPlace(
                                                    id='bar:foo2-x',
                                                    version='001',
                                                    name=MultilingualString(
                                                        value='ZONE'
                                                    ),
                                                    place_equipments=EquipmentsRelStructure(
                                                        choice=[
                                                            HeadingSign(
                                                                id='bar:foo2',
                                                                version='001',
                                                                place_name=MultilingualString(
                                                                    value='SIGN'
                                                                )
                                                            ),
                                                            PlaceLighting(
                                                                id='bar:foo2',
                                                                version='001'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        quays=QuaysRelStructure(
                                            quay_ref_or_quay=[
                                                Quay(
                                                    id='bar:foo2-a',
                                                    version='001',
                                                    name=MultilingualString(
                                                        value='ZONE'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='bar:foo2-bis',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        )
                                    ),
                                ]
                            ),
                            flexible_stop_places=FlexibleStopPlacesInFrameRelStructure(
                                flexible_stop_place=[
                                    FlexibleStopPlace(
                                        id='bar:foo3',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        )
                                    ),
                                ]
                            ),
                            points_of_interest=PointsOfInterestInFrameRelStructure(
                                point_of_interest=[
                                    PointOfInterest(
                                        id='bar:foo4',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        )
                                    ),
                                ]
                            ),
                            parkings=ParkingsInFrameRelStructure(
                                parking=[
                                    Parking(
                                        id='bar:foo5',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                ParkingPassengerEntrance(
                                                    id='bar:foo5-a',
                                                    version='001'
                                                ),
                                                ParkingPassengerEntrance(
                                                    id='bar:foo5-b',
                                                    version='001'
                                                ),
                                            ]
                                        ),
                                        parking_properties=ParkingPropertiesRelStructure(
                                            parking_properties=[
                                                ParkingProperties(
                                                    id='bar:foo',
                                                    version='001',
                                                    spaces=ParkingCapacitiesRelStructure(
                                                        parking_capacity_ref_or_parking_capacity=[
                                                            ParkingCapacity(
                                                                id='bar:foo',
                                                                version='001'
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                ParkingArea(
                                                    id='bar:foo7',
                                                    version='001',
                                                    name=MultilingualString(
                                                        value='ZONE'
                                                    ),
                                                    bays=ParkingBaysRelStructure(
                                                        parking_bay_ref_or_parking_bay=[
                                                            ParkingBay(
                                                                id='bar:foo8',
                                                                version='001',
                                                                name=MultilingualString(
                                                                    value='ZONE'
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        ),
                                        vehicle_entrances=ParkingEntrancesForVehiclesRelStructure(
                                            parking_entrance_for_vehicles_ref_or_parking_entrance_for_vehicles=[
                                                ParkingEntranceForVehicles(
                                                    id='bar:foo',
                                                    version='001'
                                                ),
                                                ParkingEntranceForVehicles(
                                                    id='bar:foo1',
                                                    version='001'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            point_of_interest_classifications=PointOfInterestClassificationsInFrameRelStructure(
                                point_of_interest_classification=[
                                    PointOfInterestClassification(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=[
                                    TariffZone(
                                        id='bar:foo9',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        )
                                    ),
                                    FareZone(
                                        id='bar:foo10',
                                        version='001',
                                        name=MultilingualString(
                                            value='ZONE'
                                        )
                                    ),
                                ]
                            ),
                            site_facility_sets=SiteFacilitySetsInFrameRelStructure(
                                site_facility_set=[
                                    SiteFacilitySet(
                                        id='bar:foo',
                                        version='001',
                                        description=MultilingualString(
                                            value='FACILITY SET'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='bar:foo',
                            version='001',
                            name=MultilingualString(
                                value='FRAME '
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='bar:foo',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINE'
                                        )
                                    ),
                                    FlexibleLine(
                                        id='bar:foo1',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINE'
                                        )
                                    ),
                                ]
                            ),
                            groups_of_lines=GroupsOfLinesInFrameRelStructure(
                                group_of_lines=[
                                    GroupOfLines(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='bar:foo5',
                                        version='001',
                                        name=MultilingualString(
                                            value='POINT'
                                        )
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='bar:foo3',
                                        version='001',
                                        name=MultilingualString(
                                            value='LINK'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='bar:foo5'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='bar:foo5'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='bar:foo',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY PATTERN'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='bar:foo',
                                                    version='001',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='bar:foo5'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='bar:foo',
                                                    version='001',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='bar:foo5'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServicePattern(
                                        id='bar:foo-bis',
                                        version='001'
                                    ),
                                ]
                            ),
                            stop_areas=StopAreasInFrameRelStructure(
                                stop_area=[
                                    StopArea(
                                        id='bar:foo',
                                        version='001'
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                journey_pattern=[
                                    JourneyPattern(
                                        id='bar:foo2',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY PATTERN'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                TimingPointInJourneyPattern(
                                                    id='bar:foo2',
                                                    version='001',
                                                    order=1,
                                                    choice_1=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='bar:foo5'
                                                    )
                                                ),
                                                TimingPointInJourneyPattern(
                                                    id='bar:foo2',
                                                    version='001',
                                                    order=2,
                                                    choice_1=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='bar:foo5'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id='bar:foo',
                            version='001',
                            name=MultilingualString(
                                value='FRAME '
                            ),
                            vehicle_journeys=JourneysInFrameRelStructure(
                                choice=[
                                    VehicleJourney(
                                        id='bar:foo',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                    ServiceJourney(
                                        id='bar:foo1',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                    TemplateServiceJourney(
                                        id='bar:foo2',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                    SpecialService(
                                        id='bar:foo3',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                    DatedServiceJourney(
                                        id='bar:foo4',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                    DeadRun(
                                        id='bar:foo5',
                                        version='001',
                                        name=MultilingualString(
                                            value='JOURNEY'
                                        )
                                    ),
                                ]
                            ),
                            service_facility_sets=ServiceFacilitySetsInFrameRelStructure(
                                service_facility_set=[
                                    ServiceFacilitySet(
                                        id='bar:foo2',
                                        version='001',
                                        description=MultilingualString(
                                            value='FACILITY SET'
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
