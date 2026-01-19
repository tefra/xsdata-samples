from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_list_type import ComponentListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class GroupBaseType(ComponentListType):
    """
    GroupBaseType is an abstract base type that forms the basis for the
    GroupType.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    link: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        }
    )
