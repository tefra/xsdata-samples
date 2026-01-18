from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_service_fee_type_2 import TypeServiceFeeType2
from travelport.models.type_supplier_type_2 import TypeSupplierType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ServiceFee2(TypeKeyElement2):
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: TypeServiceFeeType2 = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    start_date: XmlDate = field(
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_type: TypeSupplierType2 = field(
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        }
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
