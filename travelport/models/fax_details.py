from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.remark_1 import Remark1
from travelport.models.term_conditions import TermConditions

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FaxDetails:
    """
    The Fax Details Information.

    Parameters
    ----------
    phone_number
        Send type as Fax for fax number.
    term_conditions
        Term and Conditions for the fax .
    remark
    include_cover_sheet
        Specifies whether to include a cover page with fax or not.
    to
        To address.
    from_value
        From address.
    dept_billing_code
        Department billing code.
    invoice_number
        Invoice number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    phone_number: None | PhoneNumber1 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    term_conditions: None | TermConditions = field(
        default=None,
        metadata={
            "name": "TermConditions",
            "type": "Element",
        }
    )
    remark: list[Remark1] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    include_cover_sheet: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeCoverSheet",
            "type": "Attribute",
        }
    )
    to: None | str = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Attribute",
        }
    )
    from_value: None | str = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Attribute",
        }
    )
    dept_billing_code: None | str = field(
        default=None,
        metadata={
            "name": "DeptBillingCode",
            "type": "Attribute",
        }
    )
    invoice_number: None | str = field(
        default=None,
        metadata={
            "name": "InvoiceNumber",
            "type": "Attribute",
        }
    )
