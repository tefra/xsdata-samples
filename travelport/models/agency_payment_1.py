from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_agency_payment_1 import TypeAgencyPayment1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AgencyPayment1(TypeAgencyPayment1):
    """
    Container for Agency Payment.
    """
    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v52_0"
