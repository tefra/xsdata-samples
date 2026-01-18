from __future__ import annotations

from dataclasses import dataclass, field

from .department_ref import DepartmentRef
from .organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationalUnitVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "OrganisationalUnit_VersionStructure"

    department_ref: DepartmentRef | None = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
