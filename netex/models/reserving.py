from dataclasses import dataclass

from .reserving_version_structure import ReservingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Reserving(ReservingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
