from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class RequiredFieldName2(StrEnum):
    CARD_TYPE = "CardType"
    NUMBER = "Number"
    CUSTOMER_REFERENCE = "CustomerReference"
    ISSUE_NUMBER = "IssueNumber"
    START_DATE = "StartDate"
    NAME_ON_CARD = "NameOnCard"
    EXPIRATION_DATE = "ExpirationDate"
    CVV = "CVV"
    ADDRESS_LINE1 = "AddressLine1"
    ADDRESS_LINE2 = "AddressLine2"
    CITY = "City"
    STATE = "State"
    POSTAL_CODE = "PostalCode"
