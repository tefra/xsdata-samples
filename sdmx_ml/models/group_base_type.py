from dataclasses import dataclass, field
from typing import Any, Optional

from sdmx_ml.models.component_list_type import ComponentListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GroupBaseType(ComponentListType):
    """
    GroupBaseType is an abstract base type that forms the basis for the GroupType.
    """

    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    link: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
