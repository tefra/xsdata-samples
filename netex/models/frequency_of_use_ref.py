from dataclasses import dataclass
from netex.models.frequency_of_use_ref_structure import FrequencyOfUseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyOfUseRef(FrequencyOfUseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
