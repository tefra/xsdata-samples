from dataclasses import dataclass

from .duty_part_ref_structure import DutyPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyPartRef(DutyPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
