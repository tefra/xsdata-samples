from dataclasses import dataclass, field
from typing import Optional
from netex.models.department_ref import DepartmentRef
from netex.models.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationalUnitVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "OrganisationalUnit_VersionStructure"

    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
