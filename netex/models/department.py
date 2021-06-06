from dataclasses import dataclass
from .department_version_structure import DepartmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Department(DepartmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
