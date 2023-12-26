from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_agency_payment_3 import TypeAgencyPayment3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class AgencyPayment3(TypeAgencyPayment3):
    """
    Container for Agency Payment.
    """

    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v32_0"
