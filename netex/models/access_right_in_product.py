from dataclasses import dataclass

from .access_right_in_product_versioned_child_structure import (
    AccessRightInProductVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightInProduct(AccessRightInProductVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
