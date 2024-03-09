from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class TypeAgencyPayment2:
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
        name = "typeAgencyPayment"

    agency_billing_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AgencyBillingIdentifier",
            "type": "Attribute",
            "required": True,
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
