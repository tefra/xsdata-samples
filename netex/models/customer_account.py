from __future__ import annotations

from dataclasses import dataclass

from .customer_account_version_structure import CustomerAccountVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccount(CustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
