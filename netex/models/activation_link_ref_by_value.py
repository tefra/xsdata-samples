from dataclasses import dataclass
from .activation_link_ref_by_value_structure import (
    ActivationLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationLinkRefByValue(ActivationLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
