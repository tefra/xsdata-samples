from __future__ import annotations

from dataclasses import dataclass, field

from .department_version_structure import DepartmentVersionStructure
from .operational_contex_refs_rel_structure import (
    OperationalContexRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDepartmentVersionStructure(DepartmentVersionStructure):
    class Meta:
        name = "OperatingDepartment_VersionStructure"

    operational_contexts: None | OperationalContexRefsRelStructure = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
