from dataclasses import dataclass

from .activation_link_ref_structure import ActivationLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationLinkRef(ActivationLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
