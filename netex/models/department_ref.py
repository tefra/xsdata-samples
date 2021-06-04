from dataclasses import dataclass
from netex.models.department_ref_structure import DepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DepartmentRef(DepartmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
