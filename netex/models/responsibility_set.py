from dataclasses import dataclass
from .responsibility_set_version_structure import (
    ResponsibilitySetVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySet(ResponsibilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
