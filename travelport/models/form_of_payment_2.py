from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_form_of_payment_type_1 import (
    TypeFormOfPaymentType1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class FormOfPayment2(TypeFormOfPaymentType1):
    class Meta:
        name = "FormOfPayment"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
