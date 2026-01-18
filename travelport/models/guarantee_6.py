from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_8 import CreditCard8
from travelport.models.guarantee_type_11 import GuaranteeType11
from travelport.models.other_guarantee_info_6 import OtherGuaranteeInfo6
from travelport.models.type_element_status_7 import TypeElementStatus7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class Guarantee6:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    credit_card: None | CreditCard8 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        },
    )
    other_guarantee_info: None | OtherGuaranteeInfo6 = field(
        default=None,
        metadata={
            "name": "OtherGuaranteeInfo",
            "type": "Element",
        },
    )
    type_value: GuaranteeType11 = field(
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
    el_stat: None | TypeElementStatus7 = field(
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
