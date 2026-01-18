from __future__ import annotations

from dataclasses import dataclass

from .line_link_ref_by_value_structure import LineLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineLinkRefByValue(LineLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
