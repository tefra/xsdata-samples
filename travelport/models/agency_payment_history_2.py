from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_agency_payment_history_2 import TypeAgencyPaymentHistory2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AgencyPaymentHistory2(TypeAgencyPaymentHistory2):
    """
    Container for Agency Payment.
    """
    class Meta:
        name = "AgencyPaymentHistory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
