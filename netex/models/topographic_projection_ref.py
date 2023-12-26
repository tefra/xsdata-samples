from dataclasses import dataclass
from .topographic_projection_ref_structure import (
    TopographicProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicProjectionRef(TopographicProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
