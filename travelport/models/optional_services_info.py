from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class OptionalServicesInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: AirPricingSolution = field(
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    form_of_payment_ref: list[FormOfPaymentRef1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
