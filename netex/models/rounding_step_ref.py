from dataclasses import dataclass

from .rounding_step_ref_structure import RoundingStepRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingStepRef(RoundingStepRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
