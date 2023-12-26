from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_billing_details_data_type import (
    TypeBillingDetailsDataType,
)
from travelport.models.type_billing_details_name import TypeBillingDetailsName

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BillingDetailItem:
    """
    The Billing Details Information.

    Parameters
    ----------
    name
        Detailed Billing Information Name(e.g Personal ID, Account Number)
    data_type
        Detailed Billing Information DataType (Alpha, Numeric, etc.)
    min_length
        Detailed Billing Information Minimum Length.
    max_length
        Detailed Billing Information Maximum Length.
    value
        Detailed Billing Information Value
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    name: None | TypeBillingDetailsName = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    data_type: None | TypeBillingDetailsDataType = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        },
    )
    min_length: None | str = field(
        default=None,
        metadata={
            "name": "MinLength",
            "type": "Attribute",
            "required": True,
        },
    )
    max_length: None | str = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
