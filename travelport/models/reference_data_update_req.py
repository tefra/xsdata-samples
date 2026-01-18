from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.additional_element import AdditionalElement
from travelport.models.base_req_1 import BaseReq1
from travelport.models.reference_data_update_req_action import (
    ReferenceDataUpdateReqAction,
)
from travelport.models.type_reference_data import TypeReferenceData

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class ReferenceDataUpdateReq(BaseReq1):
    """
    Request to update reference data.

    Parameters
    ----------
    item
    action
    type_code
        The type code of the reference data to update.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    item: list[ReferenceDataUpdateReq.Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    action: ReferenceDataUpdateReqAction = field(
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    type_code: str = field(
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )

    @dataclass(kw_only=True)
    class Item(TypeReferenceData):
        """
        Parameters
        ----------
        additional_element
            To provide other optional values.
        """

        additional_element: list[AdditionalElement] = field(
            default_factory=list,
            metadata={
                "name": "AdditionalElement",
                "type": "Element",
                "max_occurs": 998001,
            },
        )
