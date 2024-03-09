from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_agency_payment_7 import TypeAgencyPayment7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class AgencyPayment7(TypeAgencyPayment7):
    """
    Container for Agency Payment.
    """

    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v38_0"
