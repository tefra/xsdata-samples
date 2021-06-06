from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ResponsibilitySet_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    roles: Optional[ResponsibilityRoleAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
