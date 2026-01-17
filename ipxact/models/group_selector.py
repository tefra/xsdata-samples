from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.group_selector_multiple_group_selection_operator import (
    GroupSelectorMultipleGroupSelectionOperator,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class GroupSelector:
    """
    Specifies a set of group names used to select subsequent generators.

    The attribute "multipleGroupOperator" specifies the OR or AND selection
    operator if there is more than one group name (default=OR).

    :ivar name: Specifies a generator group name or a generator chain
        group name to be selected for inclusion in the generator chain.
    :ivar multiple_group_selection_operator: Specifies the OR or AND
        selection operator if there is more than one group name.
    :ivar id:
    """

    class Meta:
        name = "groupSelector"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: list["GroupSelector.Name"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    multiple_group_selection_operator: GroupSelectorMultipleGroupSelectionOperator = field(
        default=GroupSelectorMultipleGroupSelectionOperator.OR,
        metadata={
            "name": "multipleGroupSelectionOperator",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class Name:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
