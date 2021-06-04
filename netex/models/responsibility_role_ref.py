from dataclasses import dataclass
from netex.models.responsibility_role_ref_structure import ResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRoleRef(ResponsibilityRoleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
