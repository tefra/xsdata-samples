from dataclasses import dataclass
from .residential_qualification_ref_structure import (
    ResidentialQualificationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationRef(ResidentialQualificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
