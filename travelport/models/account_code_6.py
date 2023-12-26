from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class AccountCode6:
    """
    Account Code is used to get Private Fares.If ProviderCode or SupplierCode is
    not specified, it will be considered a default AccounCode to be sent to all the
    Providers or Suppliers.

    Parameters
    ----------
    code
    provider_code
    supplier_code
    type_value
        An identifier to categorize this account code. For example,
        FlightPass for AC Flight Pass or RFB for AC corporate Rewards for
        Business.
    """

    class Meta:
        name = "AccountCode"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "max_length": 36,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
