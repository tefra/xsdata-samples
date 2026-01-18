from __future__ import annotations

from dataclasses import dataclass

from .department_ref_structure import DepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDepartmentRefStructure(DepartmentRefStructure):
    pass
