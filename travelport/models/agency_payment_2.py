from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_agency_payment_2 import TypeAgencyPayment2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class AgencyPayment2(TypeAgencyPayment2):
    """
    Container for Agency Payment.
    """

    class Meta:
        name = "AgencyPayment"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"
