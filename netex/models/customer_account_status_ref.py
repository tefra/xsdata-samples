from __future__ import annotations

from dataclasses import dataclass

from .customer_account_status_ref_structure import (
    CustomerAccountStatusRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatusRef(CustomerAccountStatusRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
