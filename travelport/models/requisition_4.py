from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.requisition_category_4 import RequisitionCategory4
from travelport.models.requisition_type_4 import RequisitionType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Requisition4:
    """
    Requisition Form of Payment.

    Parameters
    ----------
    number
        Requisition number used for accounting
    category
        Classification Category for the requisition payment
    type_value
        Type can be Cash or Credit for category as Government
    """

    class Meta:
        name = "Requisition"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    category: None | RequisitionCategory4 = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    type_value: None | RequisitionType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
