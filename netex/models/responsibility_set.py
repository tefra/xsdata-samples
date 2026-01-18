from __future__ import annotations

from dataclasses import dataclass

from .responsibility_set_version_structure import (
    ResponsibilitySetVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySet(ResponsibilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
