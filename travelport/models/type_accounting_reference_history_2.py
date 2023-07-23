from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeAccountingReferenceHistory2(TypeKeyElement2):
    """
    History Element for Accounting Reference.

    Parameters
    ----------
    payment_details_ref
        Used to sync up Keys in FormOfPayment element with
        AccountingReference, PaymentDetailsRef by entering same key number.
    type_value
        A code for categorizing a reference for a Traveler’s bookings. This
        is often used by the Traveler’s employer for budgeting, internal
        billing, or other cost accounting purposes.
        Util:ReferenceDataRetrieveReq, TypeCode AccountingReferenceType
    value
        The number or alphanumeric code for an employer reference.
    account_id
        A specific reference to a particular account profile.
    priority_order
        Priority order associated with this AccountingReference.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    active
        Denotes whether the Accounting Reference is Active or Not.
    """
    class Meta:
        name = "typeAccountingReferenceHistory"

    payment_details_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    account_id: None | int = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
        }
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )
    active: None | bool = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
        }
    )
