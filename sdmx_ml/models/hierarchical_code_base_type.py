from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.identifiable_type import IdentifiableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class HierarchicalCodeBaseType(IdentifiableType):
    """
    HierarchicalCodeBaseType is an abstract base type the creates the basis
    for the HierarchicalCodeType.

    It removes the urn and uri.

    :ivar id: The id attribute allows for an id to be assigned to the
        use of the particular code at that specific point in the
        hierarchy. This value is unique within the hierarchy being
        created, and is used to map the hierarchy against external
        structures.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
