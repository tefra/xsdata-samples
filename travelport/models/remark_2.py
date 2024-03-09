from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_general_remark_type_1 import TypeGeneralRemarkType1
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_remark_type_1 import TypeRemarkType1
from travelport.models.type_supplier_type_1 import TypeSupplierType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class Remark2(TypeKeyTaggedElement1):
    """
    Remark given to a profile.

    Parameters
    ----------
    remark_text
        The remark text
    type_value
        A code for categorizing a remark.  This may include General Remarks,
        Itinerary Remarks, Accounting Remark, Name Remark, etc.
    accounting_remark_type
        A code for categorizing an Accounting remark. This may include
        Account, Canned, Fare, Ticket, Other, etc...
        Util:ReferenceDataRetrieveReq, TypeCode AccountingRemarkType
    provider
        A code for categorizing providers of information (GDS source of
        information).
    general_remark_type
        A code for categorizing remark based on the GDS's categorization
        scheme.
    category_type
        A code for categorizing a remark.
    supplier_type
        The type of supplier associated with the remark. (Air, Car, Hotel,
        etc)
    supplier
        The supplier associated with the remark.
    priority_order
        Priority order associated with this Remark.
    """

    class Meta:
        name = "Remark"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    remark_text: None | str = field(
        default=None,
        metadata={
            "name": "RemarkText",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    type_value: None | TypeRemarkType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    accounting_remark_type: None | str = field(
        default=None,
        metadata={
            "name": "AccountingRemarkType",
            "type": "Attribute",
        },
    )
    provider: None | str = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    general_remark_type: None | TypeGeneralRemarkType1 = field(
        default=None,
        metadata={
            "name": "GeneralRemarkType",
            "type": "Attribute",
        },
    )
    category_type: None | str = field(
        default=None,
        metadata={
            "name": "CategoryType",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    supplier_type: None | TypeSupplierType1 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        },
    )
    supplier: None | str = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
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
