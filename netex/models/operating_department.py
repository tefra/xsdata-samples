from dataclasses import dataclass
from netex.models.operating_department_version_structure import OperatingDepartmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDepartment(OperatingDepartmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
