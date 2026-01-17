from dataclasses import dataclass, field
from typing import Optional, Union

from sdmx_ml.models.exclude_root_type import ExcludeRootType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MemberValueType:
    """
    Allows for a ditinct reference or a wildcard expression for selecting
    codes from a codelist.

    :ivar value:
    :ivar cascade_values: Indicates whether child codes should be
        selected when the codelist is hierarchical. Possible values are
        true (include the selected and child codes), false (only include
        the selected code(s)), and excluderoot (include the children but
        not the selected code(s)).
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[A-Za-z0-9_@$-%]+",
        },
    )
    cascade_values: Optional[Union[bool, ExcludeRootType]] = field(
        default=None,
        metadata={
            "name": "cascadeValues",
            "type": "Attribute",
        },
    )
