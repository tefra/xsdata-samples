from dataclasses import dataclass
from netex.models.validity_trigger_ref_structure import ValidityTriggerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityTriggerRef(ValidityTriggerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
