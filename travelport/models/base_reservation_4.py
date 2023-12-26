from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.accounting_remark_4 import AccountingRemark4
from travelport.models.general_remark_4 import GeneralRemark4
from travelport.models.passive_info_4 import PassiveInfo4
from travelport.models.restriction_5 import Restriction5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class BaseReservation4:
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

    accounting_remark: list[AccountingRemark4] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark4] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    restriction: list[Restriction5] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    passive_info: None | PassiveInfo4 = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
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
