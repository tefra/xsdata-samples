from __future__ import annotations

from dataclasses import dataclass

from .responsibility_role_version_structure import (
    ResponsibilityRoleVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilityRole(ResponsibilityRoleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
