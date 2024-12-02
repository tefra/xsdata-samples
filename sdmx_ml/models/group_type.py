from dataclasses import dataclass, field

from sdmx_ml.models.group_base_type import GroupBaseType
from sdmx_ml.models.group_dimension import GroupDimension

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupType(GroupBaseType):
    """GroupType describes the structure of a group descriptor in a data structure
    definition.

    A group may consist of a of partial key, or collection of distinct cube regions or key sets to which attributes may be attached. The purpose of a group is to specify attributes values which have the same value based on some common dimensionality. All groups declared in the data structure must be unique - that is, you may not have duplicate partial keys. All groups must be given unique identifiers.
    """

    group_dimension: tuple[GroupDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GroupDimension",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
