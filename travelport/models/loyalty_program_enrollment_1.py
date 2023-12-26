from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_supplier_type_1 import TypeSupplierType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class LoyaltyProgramEnrollment1(TypeKeyTaggedElement1):
    """
    Used for maintaining data for loyalty programs between a supplier and a
    traveler.

    Parameters
    ----------
    supplier_type
        The commission's supplier type
    supplier
        The commission's supplier
    number
        A traveler's specific loyalty program number or alphanumeric
        identifier.
    program_name
        Supplier's loyalty program name such as Frontier-EarlyReturns,
        Renaissance Intl-Marriott Rewards,Alamo-QuickSilver Service etc.
    status
        Categorize a status within a loyalty program.  Examples include
        Super Elite, Elite, Premier, Prestige, Platinum, regular, etc.
    priority_order
        Priority order associated with this LoyaltyProgramEnrollment.
    """

    class Meta:
        name = "LoyaltyProgramEnrollment"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    supplier_type: None | TypeSupplierType1 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        },
    )
    supplier: None | str = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    program_name: None | str = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
