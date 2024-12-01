from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.grouping_type import GroupingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataStructureComponentsBaseType(GroupingType):
    """DataStructureComponentsBaseType is an abstract base type the serves as the
    basis for the DataStructureComponentsType.

    This type is necessary to allow for valid substitutions of component
    lists.
    """

    choice: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
