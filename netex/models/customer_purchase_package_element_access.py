from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .customer_purchase_package_element_access_versioned_child_structure import (
    CustomerPurchasePackageElementAccessVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementAccess(
    CustomerPurchasePackageElementAccessVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
