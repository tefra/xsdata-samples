from __future__ import annotations

from dataclasses import dataclass

from .operating_department_ref_structure import OperatingDepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDepartmentRef(OperatingDepartmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
