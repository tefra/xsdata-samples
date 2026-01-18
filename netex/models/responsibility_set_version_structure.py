from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .responsibility_role_assignments_rel_structure import (
    ResponsibilityRoleAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ResponsibilitySet_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roles: None | ResponsibilityRoleAssignmentsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
