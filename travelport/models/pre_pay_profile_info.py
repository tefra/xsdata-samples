from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_related_rules import AccountRelatedRules
from travelport.models.affiliations import Affiliations
from travelport.models.pre_pay_account import PrePayAccount
from travelport.models.pre_pay_customer import PrePayCustomer
from travelport.models.pre_pay_id import PrePayId

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrePayProfileInfo:
    """
    PrePay Profile associated with the customer.

    Parameters
    ----------
    pre_pay_id
        Pre pay unique identifier detail.This information block is returned
        both in list and  detail retrieve transactions.Example flight pass
        number
    pre_pay_customer
        Pre pay customer detail.This information block is returned both in
        list and  detail retrieve transactions.
    pre_pay_account
        Pre pay account detail.This information block is returned both in
        list and  detail retrieve transactions.
    affiliations
        Pre pay affiliations detail.This information block is returned only
        in detail retrieve transactions.
    account_related_rules
        Pre pay account related rules.This information block is returned
        only in detail retrieve transactions.
    status_code
        Customer pre pay profile status code(One of Marked for
        deletion,Lapsed,Terminated,Active,Inactive)
    creator_id
        This is the loyalty card number of the person who originally
        purchased/setup the flight pass
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    pre_pay_id: None | PrePayId = field(
        default=None,
        metadata={
            "name": "PrePayId",
            "type": "Element",
            "required": True,
        },
    )
    pre_pay_customer: None | PrePayCustomer = field(
        default=None,
        metadata={
            "name": "PrePayCustomer",
            "type": "Element",
        },
    )
    pre_pay_account: None | PrePayAccount = field(
        default=None,
        metadata={
            "name": "PrePayAccount",
            "type": "Element",
        },
    )
    affiliations: None | Affiliations = field(
        default=None,
        metadata={
            "name": "Affiliations",
            "type": "Element",
        },
    )
    account_related_rules: None | AccountRelatedRules = field(
        default=None,
        metadata={
            "name": "AccountRelatedRules",
            "type": "Element",
        },
    )
    status_code: None | str = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
        },
    )
    creator_id: None | str = field(
        default=None,
        metadata={
            "name": "CreatorID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 36,
        },
    )
