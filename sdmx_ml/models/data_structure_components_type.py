from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.attribute_list import AttributeList
from sdmx_ml.models.data_structure_components_base_type import (
    DataStructureComponentsBaseType,
)
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.group import Group
from sdmx_ml.models.measure_list import MeasureList

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataStructureComponentsType(DataStructureComponentsBaseType):
    """
    DataStructureComponentsType describes the structure of the grouping to
    the sets of metadata concepts that have a defined structural role in
    the data structure definition.

    At a minimum at least one dimension must be defined.
    """

    dimension_list: Optional[DimensionList] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    group: tuple[Group, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    attribute_list: Optional[AttributeList] = field(
        default=None,
        metadata={
            "name": "AttributeList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    measure_list: Optional[MeasureList] = field(
        default=None,
        metadata={
            "name": "MeasureList",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
