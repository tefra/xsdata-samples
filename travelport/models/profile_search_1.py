from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.field_data_search_1 import FieldDataSearch1
from travelport.models.type_search_accounting_reference_1 import TypeSearchAccountingReference1
from travelport.models.type_search_contact_1 import TypeSearchContact1
from travelport.models.type_search_loyalty_program_1 import TypeSearchLoyaltyProgram1
from travelport.models.type_search_payment_details_1 import TypeSearchPaymentDetails1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileSearch1:
    """
    All the fixed fields allowed for searching.
    """
    class Meta:
        name = "ProfileSearch"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    contract_number: None | str = field(
        default=None,
        metadata={
            "name": "ContractNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 50,
        }
    )
    travel_document_number: None | str = field(
        default=None,
        metadata={
            "name": "TravelDocumentNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        }
    )
    accounting_reference: None | TypeSearchAccountingReference1 = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
        }
    )
    alternate_contact: None | TypeSearchContact1 = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
        }
    )
    loyalty_program: None | TypeSearchLoyaltyProgram1 = field(
        default=None,
        metadata={
            "name": "LoyaltyProgram",
            "type": "Element",
        }
    )
    payment_details: None | TypeSearchPaymentDetails1 = field(
        default=None,
        metadata={
            "name": "PaymentDetails",
            "type": "Element",
        }
    )
    field_data_search: list[FieldDataSearch1] = field(
        default_factory=list,
        metadata={
            "name": "FieldDataSearch",
            "type": "Element",
        }
    )
