from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.requisition_category_1 import RequisitionCategory1
from travelport.models.requisition_type_1 import RequisitionType1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Requisition1:
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
        namespace = "http://www.travelport.com/schema/common_v52_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    category: None | RequisitionCategory1 = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    type_value: None | RequisitionType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
