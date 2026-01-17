from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_key_element_1 import TypeKeyElement1
from travelport.models.type_service_fee_type_1 import TypeServiceFeeType1
from travelport.models.type_supplier_type_1 import TypeSupplierType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ServiceFee1(TypeKeyElement1):
    """
    A representation of the Service Fee given to an Agent or Agency within
    a profile.

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
        Priority order associated with this ServiceFee.
    """

    class Meta:
        name = "ServiceFee"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    type_value: None | TypeServiceFeeType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        },
    )
    supplier_type: None | TypeSupplierType1 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
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
