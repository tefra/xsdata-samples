from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_list_type import ComponentListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeListBaseType(ComponentListType):
    """
    AttributeListBaseType is an abstract base type used as the basis for the
    AttributeListType.

    :ivar choice:
    :ivar id: The id attribute is provided in this case for
        completeness. However, its value is fixed to
        AttributeDescriptor.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    id: str = field(
        init=False,
        default="AttributeDescriptor",
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
