from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.requisition_category_5 import RequisitionCategory5
from travelport.models.requisition_type_5 import RequisitionType5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class Requisition5:
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
        namespace = "http://www.travelport.com/schema/common_v37_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    category: None | RequisitionCategory5 = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    type_value: None | RequisitionType5 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
