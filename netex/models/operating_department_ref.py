from dataclasses import dataclass

from .operating_department_ref_structure import OperatingDepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDepartmentRef(OperatingDepartmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
