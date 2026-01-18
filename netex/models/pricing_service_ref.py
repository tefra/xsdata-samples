from __future__ import annotations

from dataclasses import dataclass

from .pricing_service_ref_structure import PricingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingServiceRef(PricingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
