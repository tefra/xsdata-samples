from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_agency_payment_4 import TypeAgencyPayment4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class AgencyPayment4(TypeAgencyPayment4):
    """
    Container for Agency Payment.
    """
    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v33_0"
