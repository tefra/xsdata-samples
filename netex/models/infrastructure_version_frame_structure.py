from __future__ import annotations

from dataclasses import dataclass, field

from .activated_equipments_in_frame_rel_structure import (
    ActivatedEquipmentsInFrameRelStructure,
)
from .activation_links_in_frame_rel_structure import (
    ActivationLinksInFrameRelStructure,
)
from .activation_points_in_frame_rel_structure import (
    ActivationPointsInFrameRelStructure,
)
from .common_version_frame_structure import CommonVersionFrameStructure
from .crew_bases_in_frame_rel_structure import CrewBasesInFrameRelStructure
from .garages_in_frame_rel_structure import GaragesInFrameRelStructure
from .infrastructure_elements_in_frame_rel_structure import (
    InfrastructureElementsInFrameRelStructure,
)
from .infrastructure_junctions_in_frame_rel_structure import (
    InfrastructureJunctionsInFrameRelStructure,
)
from .network_restrictions_in_frame_rel_structure import (
    NetworkRestrictionsInFrameRelStructure,
)
from .relief_points_in_frame_rel_structure import (
    ReliefPointsInFrameRelStructure,
)
from .spatial_features_in_frame_rel_structure import (
    SpatialFeaturesInFrameRelStructure,
)
from .traffic_control_points_in_frame_rel_structure import (
    TrafficControlPointsInFrameRelStructure,
)
from .vehicle_equipmen_profiles_in_frame_rel_structure import (
    VehicleEquipmenProfilesInFrameRelStructure,
)
from .vehicle_model_profiles_in_frame_rel_structure import (
    VehicleModelProfilesInFrameRelStructure,
)
from .vehicle_models_in_frame_rel_structure import (
    VehicleModelsInFrameRelStructure,
)
from .vehicle_types_in_frame_rel_structure import (
    VehicleTypesInFrameRelStructure,
)
from .vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Infrastructure_VersionFrameStructure"

    meetings_restricted: bool | None = field(
        default=None,
        metadata={
            "name": "MeetingsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    restricted_manoeuvres: bool | None = field(
        default=None,
        metadata={
            "name": "RestrictedManoeuvres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaking_possibilities_restricted: bool | None = field(
        default=None,
        metadata={
            "name": "OvertakingPossibilitiesRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spatial_features: SpatialFeaturesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "spatialFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    junctions: InfrastructureJunctionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    elements: InfrastructureElementsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    restrictions: NetworkRestrictionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    crew_bases: CrewBasesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "crewBases",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    garages: GaragesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_and_crew_points: ReliefPointsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleAndCrewPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    traffic_control_points: TrafficControlPointsInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "trafficControlPoints",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    activation_points: ActivationPointsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "activationPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    activation_links: ActivationLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "activationLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    activated_equipments: ActivatedEquipmentsInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "activatedEquipments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    vehicle_types: VehicleTypesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_models: VehicleModelsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleModels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_equipment_profiles: (
        VehicleEquipmenProfilesInFrameRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "vehicleEquipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_model_profiles: VehicleModelProfilesInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "vehicleModelProfiles",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    vehicles: VehiclesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
