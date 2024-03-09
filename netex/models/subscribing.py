from dataclasses import dataclass

from .subscribing_version_structure import SubscribingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Subscribing(SubscribingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
