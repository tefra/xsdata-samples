from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
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
    floor_area_m2: NumericType | None = field(
        default=None,
        metadata={
            "name": "FloorAreaM2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    floor_count: NumberType | None = field(
        default=None,
        metadata={
            "name": "FloorCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    floors_occupied: TextType | None = field(
        default=None,
        metadata={
            "name": "FloorsOccupied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    height_in_meter: QuantityType | None = field(
        default=None,
        metadata={
            "name": "HeightInMeter",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    lift_count: NumberType | None = field(
        default=None,
        metadata={
            "name": "LiftCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    lowest_floor_occupied: TextType | None = field(
        default=None,
        metadata={
            "name": "LowestFloorOccupied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    completition_state: BuildingTypeCompletitionState | None = field(
        default=None,
        metadata={
            "name": "CompletitionState",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    occupancy: CodeDescriptionType | None = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
