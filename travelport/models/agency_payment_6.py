from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_agency_payment_6 import TypeAgencyPayment6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AgencyPayment6(TypeAgencyPayment6):
    """
    Container for Agency Payment.
    """

    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/common_v34_0"
