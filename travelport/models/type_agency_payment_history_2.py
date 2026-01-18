from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeAgencyPaymentHistory2:
    """
    Type for Agency Payment.

    Parameters
    ----------
    agency_billing_identifier
        Value of the billing id
    agency_billing_number
        Value of billing number
    agency_billing_password
        Value of billing password
    """

    class Meta:
        name = "typeAgencyPaymentHistory"

    agency_billing_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AgencyBillingIdentifier",
            "type": "Attribute",
            "max_length": 128,
        },
    )
    agency_billing_number: None | str = field(
        default=None,
        metadata={
            "name": "AgencyBillingNumber",
            "type": "Attribute",
            "max_length": 128,
        },
    )
    agency_billing_password: None | str = field(
        default=None,
        metadata={
            "name": "AgencyBillingPassword",
            "type": "Attribute",
            "max_length": 128,
        },
    )
