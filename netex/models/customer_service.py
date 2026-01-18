from __future__ import annotations

from dataclasses import dataclass

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerService(CustomerServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
