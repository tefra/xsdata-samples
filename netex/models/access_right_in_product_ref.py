from dataclasses import dataclass
from netex.models.access_right_in_product_ref_structure import AccessRightInProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightInProductRef(AccessRightInProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
