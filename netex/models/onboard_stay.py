from dataclasses import dataclass
from netex.models.onboard_stay_versioned_chlld_structure import OnboardStayVersionedChlldStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnboardStay(OnboardStayVersionedChlldStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
