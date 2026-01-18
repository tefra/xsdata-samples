from __future__ import annotations

from dataclasses import dataclass

from .responsibility_role_ref_structure import ResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilityRoleRef(ResponsibilityRoleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
