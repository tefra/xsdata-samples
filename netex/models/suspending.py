from dataclasses import dataclass
from netex.models.suspending_version_structure import SuspendingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Suspending(SuspendingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
