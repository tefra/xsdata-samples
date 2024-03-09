from dataclasses import dataclass, field
from typing import Any

from .abstract_group_member_versioned_child_structure import (
    AbstractGroupMemberVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AbstractGroupMember(AbstractGroupMemberVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
