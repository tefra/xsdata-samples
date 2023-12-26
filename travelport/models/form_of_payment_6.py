from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_form_of_payment_type_2 import (
    TypeFormOfPaymentType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FormOfPayment6(TypeFormOfPaymentType2):
    class Meta:
        name = "FormOfPayment"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
