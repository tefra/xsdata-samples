from dataclasses import dataclass
from .emv_card_version_structure import EmvCardVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EmvCard(EmvCardVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
