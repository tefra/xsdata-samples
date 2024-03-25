from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.group_dimension_base_type import GroupDimensionBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupDimensionType(GroupDimensionBaseType):
    """GroupDimensionType defines a dimension component with a group key descriptor
    component list.

    Although technically a component, this is essentially a reference to
    a dimension defined in the key descriptor. Therefore, the
    identification, name, and description, concept identity and
    representation properties that are typically available for a
    component are not allowed here, as they are all inherited from the
    referenced dimension.

    :ivar dimension_reference: DimensionReference provides a reference
        to a dimension defined in the key descriptor of the data
        structure definition in which this group key descriptor is
        defined.
    """

    dimension_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "DimensionReference",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
