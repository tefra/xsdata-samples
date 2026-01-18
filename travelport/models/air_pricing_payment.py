from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1
from travelport.models.payment_1 import Payment1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirPricingPayment:
    """
    AirPricing Payment information - used to associate a FormOfPayment
    withiin the UR with one or more AirPricingInfos.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
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
    form_of_payment_ref: None | FormOfPaymentRef1 = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
