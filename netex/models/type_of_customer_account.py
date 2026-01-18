from __future__ import annotations

from dataclasses import dataclass

from .type_of_customer_account_version_structure import (
    TypeOfCustomerAccountVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfCustomerAccount(TypeOfCustomerAccountVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
