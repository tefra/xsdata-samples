from __future__ import annotations

from dataclasses import dataclass

from .customer_ref_structure import CustomerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerRef(CustomerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
