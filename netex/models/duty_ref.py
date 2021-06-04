from dataclasses import dataclass
from netex.models.duty_ref_structure import DutyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyRef(DutyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
