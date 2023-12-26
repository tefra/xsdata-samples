from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.field_data_search_2 import FieldDataSearch2
from travelport.models.type_search_accounting_reference_2 import (
    TypeSearchAccountingReference2,
)
from travelport.models.type_search_contact_2 import TypeSearchContact2
from travelport.models.type_search_loyalty_program_2 import (
    TypeSearchLoyaltyProgram2,
)
from travelport.models.type_search_payment_details_2 import (
    TypeSearchPaymentDetails2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearch2:
    """
    All the fixed fields allowed for searching.
    """

    class Meta:
        name = "ProfileSearch"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    contract_number: None | str = field(
        default=None,
        metadata={
            "name": "ContractNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 50,
        },
    )
    travel_document_number: None | str = field(
        default=None,
        metadata={
            "name": "TravelDocumentNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        },
    )
    accounting_reference: None | TypeSearchAccountingReference2 = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
        },
    )
    alternate_contact: None | TypeSearchContact2 = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
        },
    )
    loyalty_program: None | TypeSearchLoyaltyProgram2 = field(
        default=None,
        metadata={
            "name": "LoyaltyProgram",
            "type": "Element",
        },
    )
    payment_details: None | TypeSearchPaymentDetails2 = field(
        default=None,
        metadata={
            "name": "PaymentDetails",
            "type": "Element",
        },
    )
    field_data_search: list[FieldDataSearch2] = field(
        default_factory=list,
        metadata={
            "name": "FieldDataSearch",
            "type": "Element",
            "max_occurs": 999,
        },
    )
