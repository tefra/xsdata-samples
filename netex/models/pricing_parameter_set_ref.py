from dataclasses import dataclass

from .pricing_parameter_set_ref_structure import (
    PricingParameterSetRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingParameterSetRef(PricingParameterSetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
