from dataclasses import dataclass, field
from typing import Optional
from netex.models.activated_equipments_in_frame_rel_structure import ActivatedEquipmentsInFrameRelStructure
from netex.models.activation_links_in_frame_rel_structure import ActivationLinksInFrameRelStructure
from netex.models.activation_points_in_frame_rel_structure import ActivationPointsInFrameRelStructure
from netex.models.common_version_frame_structure import CommonVersionFrameStructure
from netex.models.crew_bases_in_frame_rel_structure import CrewBasesInFrameRelStructure
from netex.models.garages_in_frame_rel_structure import GaragesInFrameRelStructure
from netex.models.infrastructure_elements_in_frame_rel_structure import InfrastructureElementsInFrameRelStructure
from netex.models.infrastructure_junctions_in_frame_rel_structure import InfrastructureJunctionsInFrameRelStructure
from netex.models.network_restrictions_in_frame_rel_structure import NetworkRestrictionsInFrameRelStructure
from netex.models.relief_points_in_frame_rel_structure import ReliefPointsInFrameRelStructure
from netex.models.spatial_features_in_frame_rel_structure import SpatialFeaturesInFrameRelStructure
from netex.models.traffic_control_points_in_frame_rel_structure import TrafficControlPointsInFrameRelStructure
from netex.models.vehicle_equipmen_profiles_in_frame_rel_structure import VehicleEquipmenProfilesInFrameRelStructure
from netex.models.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.models.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.models.vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Infrastructure_VersionFrameStructure"

    meetings_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MeetingsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_manoeuvres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictedManoeuvres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaking_possibilities_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OvertakingPossibilitiesRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    spatial_features: Optional[SpatialFeaturesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "spatialFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    junctions: Optional[InfrastructureJunctionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    elements: Optional[InfrastructureElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restrictions: Optional[NetworkRestrictionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crew_bases: Optional[CrewBasesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "crewBases",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garages: Optional[GaragesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_and_crew_points: Optional[ReliefPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleAndCrewPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_points: Optional[TrafficControlPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "trafficControlPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_points: Optional[ActivationPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activationPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_links: Optional[ActivationLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activationLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activated_equipments: Optional[ActivatedEquipmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activatedEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_types: Optional[VehicleTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_models: Optional[VehicleModelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleModels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_profiles: Optional[VehicleEquipmenProfilesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleEquipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicles: Optional[VehiclesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
