from dataclasses import dataclass, field
from typing import Optional

from .payment_method_enumeration import PaymentMethodEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPaymentMethodValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfPaymentMethod_ValueStructure"

    payment_method: PaymentMethodEnumeration | None = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automated_use: bool | None = field(
        default=None,
        metadata={
            "name": "AutomatedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
