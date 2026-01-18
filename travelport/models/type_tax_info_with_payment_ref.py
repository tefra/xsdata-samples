from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.payment_ref_2 import PaymentRef2
from travelport.models.type_tax_info_1 import TypeTaxInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeTaxInfoWithPaymentRef(TypeTaxInfo1):
    """
    Parameters
    ----------
    payment_ref
        This reference elements will associate relevant payment to this tax
    """

    class Meta:
        name = "typeTaxInfoWithPaymentRef"

    payment_ref: list[PaymentRef2] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
