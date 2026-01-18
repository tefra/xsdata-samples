from __future__ import annotations

from dataclasses import dataclass

from .operating_department_version_structure import (
    OperatingDepartmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDepartment(OperatingDepartmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
