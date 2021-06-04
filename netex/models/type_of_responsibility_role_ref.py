from dataclasses import dataclass
from netex.models.type_of_responsibility_role_ref_structure import TypeOfResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfResponsibilityRoleRef(TypeOfResponsibilityRoleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
