from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_6 import AccountingRemark6
from travelport.models.general_remark_6 import GeneralRemark6
from travelport.models.passive_info_6 import PassiveInfo6
from travelport.models.restriction_7 import Restriction7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class BaseReservation6:
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

    accounting_remark: list[AccountingRemark6] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark6] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        },
    )
    restriction: list[Restriction7] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        },
    )
    passive_info: None | PassiveInfo6 = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    locator_code: str = field(
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    create_date: str = field(
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: str = field(
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    customer_number: None | str = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        },
    )
