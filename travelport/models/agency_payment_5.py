from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_agency_payment_5 import TypeAgencyPayment5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class AgencyPayment5(TypeAgencyPayment5):
    """
    Container for Agency Payment.
    """
    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v37_0"
