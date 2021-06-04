from dataclasses import dataclass
from netex.models.luggage_allowance_version_structure import LuggageAllowanceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageAllowance(LuggageAllowanceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
