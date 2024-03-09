from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_service_fee_type_2 import TypeServiceFeeType2
from travelport.models.type_supplier_type_2 import TypeSupplierType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeServiceFeeHistory2(TypeKeyElement2):
    """
    History Element for Service Fee.

    Parameters
    ----------
    type_value
        A code for categorizing service fees or charges.
    start_date
        The date a specific service fee for a profile starts to be
        applicable.
    supplier_type
        The category of supplier that a service fee may apply.
    amount
        The financial amount of a service fee.
    priority_order
        Priority order associated with this Service Fee.
    """

    class Meta:
        name = "typeServiceFeeHistory"

    type_value: None | TypeServiceFeeType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
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
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
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
