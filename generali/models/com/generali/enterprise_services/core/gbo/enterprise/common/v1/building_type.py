from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.quantity_type import (
    QuantityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.building_type_completition_state import (
    BuildingTypeCompletitionState,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.single_point_structure_type import (
    SinglePointStructureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class BuildingType(SinglePointStructureType):
    floor_area_m2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FloorAreaM2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    floor_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FloorCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    floors_occupied: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FloorsOccupied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    height_in_meter: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "HeightInMeter",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    lift_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "LiftCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    lowest_floor_occupied: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LowestFloorOccupied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    completition_state: Optional[BuildingTypeCompletitionState] = field(
        default=None,
        metadata={
            "name": "CompletitionState",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    occupancy: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
