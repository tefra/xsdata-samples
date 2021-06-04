from dataclasses import dataclass
from netex.models.duty_part_version_structure import DutyPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyPart(DutyPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
