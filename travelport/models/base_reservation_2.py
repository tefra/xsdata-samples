from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_2 import AccountingRemark2
from travelport.models.general_remark_2 import GeneralRemark2
from travelport.models.passive_info_2 import PassiveInfo2
from travelport.models.restriction_3 import Restriction3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class BaseReservation2:
    """
    Parameters
    ----------
    accounting_remark
    general_remark
    restriction
    passive_info
    locator_code
        The unique identifier for this reservation. If this is this View
        Only UR LocatorCode is '999999'.
    create_date
        The date and time that this reservation was created.
    modified_date
        The date and time that this reservation was last modified for any
        reason.
    customer_number
    """

    class Meta:
        name = "BaseReservation"

    accounting_remark: list[AccountingRemark2] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark2] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
    restriction: list[Restriction3] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
    passive_info: None | PassiveInfo2 = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    create_date: None | str = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        },
    )
    modified_date: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        },
    )
    customer_number: None | str = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        },
    )