from dataclasses import dataclass
from netex.models.residential_qualification_version_structure import ResidentialQualificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualification(ResidentialQualificationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
