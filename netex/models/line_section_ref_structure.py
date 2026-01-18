from __future__ import annotations

from dataclasses import dataclass

from .section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionRefStructure(SectionRefStructure):
    pass
