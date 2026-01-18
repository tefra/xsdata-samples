from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_agency_payment_history_1 import (
    TypeAgencyPaymentHistory1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class AgencyPaymentHistory1(TypeAgencyPaymentHistory1):
    """
    Container for Agency Payment.
    """

    class Meta:
        name = "AgencyPaymentHistory"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
