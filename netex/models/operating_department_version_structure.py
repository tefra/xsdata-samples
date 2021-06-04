from dataclasses import dataclass, field
from typing import Optional
from netex.models.department_version_structure import DepartmentVersionStructure
from netex.models.operational_contex_refs_rel_structure import OperationalContexRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDepartmentVersionStructure(DepartmentVersionStructure):
    class Meta:
        name = "OperatingDepartment_VersionStructure"

    operational_contexts: Optional[OperationalContexRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
