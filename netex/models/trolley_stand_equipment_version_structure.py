from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from .payment_method_enumeration import PaymentMethodEnumeration
from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrolleyStandEquipmentVersionStructure(SiteEquipmentVersionStructure):
    class Meta:
        name = "TrolleyStandEquipment_VersionStructure"

    free_to_use: None | bool = field(
        default=None,
        metadata={
            "name": "FreeToUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charge: None | Decimal = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    payment_methods: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
