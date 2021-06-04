from dataclasses import dataclass
from netex.models.pricing_parameter_set_versioned_structure import PricingParameterSetVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingParameterSet(PricingParameterSetVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
