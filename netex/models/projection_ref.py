from __future__ import annotations

from dataclasses import dataclass

from .projection_ref_structure import ProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ProjectionRef(ProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
