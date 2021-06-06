from dataclasses import dataclass
from .alternative_texts_rel_structure import ValidBetweenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleValidityCondition(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
