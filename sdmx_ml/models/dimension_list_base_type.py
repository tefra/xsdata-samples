from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_list_type import ComponentListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DimensionListBaseType(ComponentListType):
    """
    DimensionListBaseType is an abstract base type used as the basis for
    the DimensionListType.

    :ivar choice:
    :ivar id: The id attribute is provided in this case for
        completeness. However, its value is fixed to
        DimensionDescriptor.
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
        default="DimensionDescriptor",
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
