from dataclasses import dataclass
from .type_of_payment_method_ref_structure import (
    TypeOfPaymentMethodRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPaymentMethodRef(TypeOfPaymentMethodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
