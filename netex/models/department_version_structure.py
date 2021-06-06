from dataclasses import dataclass, field
from typing import Optional
from .organisation_part_version_structure import OrganisationPartVersionStructure
from .organisational_unit_refs_rel_structure import OrganisationalUnitRefsRelStructure
from .type_of_operation_ref import TypeOfOperationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentVersionStructure(OrganisationPartVersionStructure):
    class Meta:
        name = "Department_VersionStructure"

    type_of_operation_ref: Optional[TypeOfOperationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    units: Optional[OrganisationalUnitRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
