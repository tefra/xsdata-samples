from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.billing_detail_item import BillingDetailItem
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class DetailedBillingInformation:
    """
    Container to send Detailed Billing Information for ticketing.

    Parameters
    ----------
    form_of_payment_ref
    air_pricing_info_ref
        Returns related air pricing infos.
    billing_detail_item
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
    billing_detail_item: list[BillingDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "BillingDetailItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
