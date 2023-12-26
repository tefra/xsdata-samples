from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_commission_category_2 import (
    TypeCommissionCategory2,
)
from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_supplier_type_2 import TypeSupplierType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeCommissionHistory2(TypeKeyElement2):
    """
    History Element for Commission.

    Parameters
    ----------
    type_value
        A type that represents a category of commissions. Example include
        per booking, by monetary amount, etc.
    supplier_type
        The commission's supplier type
    supplier
        The commission's supplier
    amount
        A financial amount for a specific commission type for a travel
        supplier.
    percentage
        A percentage for a specific commission type for a travel supplier.
    priority_order
        Priority order associated with this Commission.
    """

    class Meta:
        name = "typeCommissionHistory"

    type_value: None | TypeCommissionCategory2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    supplier_type: None | TypeSupplierType2 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        },
    )
    supplier: None | str = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
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
