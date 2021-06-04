from dataclasses import dataclass
from netex.models.companion_profile_version_structure import CompanionProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompanionProfile(CompanionProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
