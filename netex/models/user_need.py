from dataclasses import dataclass
from .user_need_versioned_child_structure import (
    UserNeedVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserNeed(UserNeedVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
