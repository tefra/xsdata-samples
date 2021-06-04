from dataclasses import dataclass
from netex.models.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReplacingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Replacing_VersionStructure"
