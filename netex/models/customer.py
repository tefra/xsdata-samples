from __future__ import annotations

from dataclasses import dataclass

from .customer_version_structure import CustomerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Customer(CustomerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
