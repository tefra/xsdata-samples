from __future__ import annotations

from dataclasses import dataclass

from .type_of_payment_method_value_structure import (
    TypeOfPaymentMethodValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPaymentMethod(TypeOfPaymentMethodValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
