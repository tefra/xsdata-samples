from dataclasses import dataclass

from .key_list_structure import KeyListStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class KeyList(KeyListStructure):
    class Meta:
        name = "keyList"
        namespace = "http://www.netex.org.uk/netex"
