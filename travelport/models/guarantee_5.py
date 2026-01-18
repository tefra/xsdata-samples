from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_7 import CreditCard7
from travelport.models.guarantee_type_10 import GuaranteeType10
from travelport.models.other_guarantee_info_5 import OtherGuaranteeInfo5
from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class Guarantee5:
    """
    Payment Guarantee Guarantee, Deposit.

    Parameters
    ----------
    credit_card
    other_guarantee_info
    type_value
        Guarantee only or Deposit
    key
        Key for update/delete of the element
    reuse_fop
        Key of the FOP Key to be reused as this Form of Payment.Only Credit
        and Debit Card will be supported for FOP Reuse.
    external_reference
    reusable
        Indicates whether the form of payment can be reused or not.
        Currently applicable for Credit and Debit form of payment
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "Guarantee"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    credit_card: None | CreditCard7 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        },
    )
    other_guarantee_info: None | OtherGuaranteeInfo5 = field(
        default=None,
        metadata={
            "name": "OtherGuaranteeInfo",
            "type": "Element",
        },
    )
    type_value: GuaranteeType10 = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    reuse_fop: None | str = field(
        default=None,
        metadata={
            "name": "ReuseFOP",
            "type": "Attribute",
        },
    )
    external_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    reusable: bool = field(
        default=False,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
