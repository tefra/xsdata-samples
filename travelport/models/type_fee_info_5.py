from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeFeeInfo5:
    """
    A generic type of fee for those charges which are incurred by the passenger,
    but not necessarily shown on tickets.

    Parameters
    ----------
    tax_info_ref
        This reference elements will associate relevant taxes to this fee
    base_amount
    description
    sub_code
    key
    amount
    code
    fee_token
    payment_ref
        The reference to the one of the air reservation payments if fee
        included in charge
    booking_traveler_ref
        Reference to booking traveler
    passenger_type_code
    provider_code
    supplier_code
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
        name = "typeFeeInfo"

    tax_info_ref: list[TypeFeeInfo5.TaxInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 999,
        },
    )
    base_amount: None | str = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    sub_code: None | str = field(
        default=None,
        metadata={
            "name": "SubCode",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    fee_token: None | str = field(
        default=None,
        metadata={
            "name": "FeeToken",
            "type": "Attribute",
        },
    )
    payment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    passenger_type_code: None | str = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
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
            "min_length": 2,
            "max_length": 5,
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

    @dataclass
    class TaxInfoRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            },
        )
