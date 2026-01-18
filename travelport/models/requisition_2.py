from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.requisition_category_2 import RequisitionCategory2
from travelport.models.requisition_type_2 import RequisitionType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass(kw_only=True)
class Requisition2:
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
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
    category: None | RequisitionCategory2 = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    type_value: None | RequisitionType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
