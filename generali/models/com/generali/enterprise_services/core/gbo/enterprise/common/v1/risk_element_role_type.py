from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_optional_type import (
    BaseReferenceComponentOptionalType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.aircraft_type import (
    AircraftType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.building_type import (
    BuildingType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.expansive_structure_type import (
    ExpansiveStructureType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.helicopter_type import (
    HelicopterType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.hovercraft_type import (
    HovercraftType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.land_type import (
    LandType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.liability_type import (
    LiabilityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.pipe_line_type import (
    PipeLineType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.railway_track_type import (
    RailwayTrackType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.ship_type import (
    ShipType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.single_point_structure_type import (
    SinglePointStructureType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.train_type import (
    TrainType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.vessel_type import (
    VesselType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class RiskElementRoleType(BaseReferenceComponentOptionalType):
    building: None | BuildingType = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    pipe_line: None | PipeLineType = field(
        default=None,
        metadata={
            "name": "PipeLine",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    land: None | LandType = field(
        default=None,
        metadata={
            "name": "Land",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    railway_track: None | RailwayTrackType = field(
        default=None,
        metadata={
            "name": "RailwayTrack",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    liability: None | LiabilityType = field(
        default=None,
        metadata={
            "name": "Liability",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    train: None | TrainType = field(
        default=None,
        metadata={
            "name": "Train",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    aircraft: None | AircraftType = field(
        default=None,
        metadata={
            "name": "Aircraft",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    helicopter: None | HelicopterType = field(
        default=None,
        metadata={
            "name": "Helicopter",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    ship: None | ShipType = field(
        default=None,
        metadata={
            "name": "Ship",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    hovercraft: None | HovercraftType = field(
        default=None,
        metadata={
            "name": "Hovercraft",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    vessel: None | VesselType = field(
        default=None,
        metadata={
            "name": "Vessel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    single_point: None | SinglePointStructureType = field(
        default=None,
        metadata={
            "name": "SinglePoint",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    expansive_structure: None | ExpansiveStructureType = field(
        default=None,
        metadata={
            "name": "ExpansiveStructure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    owner: None | str = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    floater: None | bool = field(
        default=None,
        metadata={
            "name": "Floater",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
