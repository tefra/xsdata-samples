from dataclasses import dataclass

from .general_section_ref_structure import GeneralSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionRefStructure(GeneralSectionRefStructure):
    pass
