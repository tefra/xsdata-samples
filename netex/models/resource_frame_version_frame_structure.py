from dataclasses import dataclass, field
from typing import Optional
from .blacklists_in_frame_rel_structure import BlacklistsInFrameRelStructure
from .common_version_frame_structure import CommonVersionFrameStructure
from .control_centres_in_frame_rel_structure import (
    ControlCentresInFrameRelStructure,
)
from .data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from .equipments_in_frame_rel_structure import EquipmentsInFrameRelStructure
from .group_of_entities_in_frame_rel_structure import (
    GroupOfEntitiesInFrameRelStructure,
)
from .groups_of_operators_in_frame_rel_structure import (
    GroupsOfOperatorsInFrameRelStructure,
)
from .operational_contexts_in_frame_rel_structure import (
    OperationalContextsInFrameRelStructure,
)
from .organisations_in_frame_rel_structure import (
    OrganisationsInFrameRelStructure,
)
from .responsibility_sets_in_frame_rel_structure import (
    ResponsibilitySetsInFrameRelStructure,
)
from .schematic_maps_in_frame_rel_structure import (
    SchematicMapsInFrameRelStructure,
)
from .types_of_value_in_frame_rel_structure import (
    TypesOfValueInFrameRelStructure,
)
from .vehicle_equipmen_profiles_in_frame_rel_structure import (
    VehicleEquipmenProfilesInFrameRelStructure,
)
from .vehicle_models_in_frame_rel_structure import (
    VehicleModelsInFrameRelStructure,
)
from .vehicle_types_in_frame_rel_structure import (
    VehicleTypesInFrameRelStructure,
)
from .vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure
from .whitelists_in_frame_rel_structure import WhitelistsInFrameRelStructure
from .zones_in_frame_rel_structure import ZonesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResourceFrameVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "ResourceFrame_VersionFrameStructure"

    data_sources: Optional[DataSourcesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dataSources",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsibility_sets: Optional[
        ResponsibilitySetsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "responsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_value: Optional[TypesOfValueInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisations: Optional[OrganisationsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_operators: Optional[
        GroupsOfOperatorsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "groupsOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_contexts: Optional[
        OperationalContextsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    control_centres: Optional[ControlCentresInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "controlCentres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: Optional[EquipmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_types: Optional[VehicleTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_models: Optional[VehicleModelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleModels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_equipment_profiles: Optional[
        VehicleEquipmenProfilesInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleEquipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicles: Optional[VehiclesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    schematic_maps: Optional[SchematicMapsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "schematicMaps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_entities: Optional[GroupOfEntitiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    zones: Optional[ZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blacklists: Optional[BlacklistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelists: Optional[WhitelistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
