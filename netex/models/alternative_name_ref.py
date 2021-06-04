from dataclasses import dataclass
from netex.models.alternative_name_ref_structure import AlternativeNameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeNameRef(AlternativeNameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
