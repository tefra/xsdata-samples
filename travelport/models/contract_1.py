from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_supplier_type_1 import TypeSupplierType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class Contract1(TypeKeyTaggedElement1):
    """
    A representation of a contract given between the agency and a
    supplier/provider.

    Parameters
    ----------
    supplier
        The supplier associated with the contract.
    supplier_type
        The supplier type associated with the contract. (Air, Hotel, etc)
    provider
        The provider associated with the contract.
    start_date
        The date that contract terms start to be applied.
    expiration_date
        The date that contract terms terminate being applied.
    discount_percentage
        The percentage of discount applicable to a contract.
    discount_value
        The amount of discount applicable to a contract.
    supplier_contract_number
        An eternally assigned or managed number or alphanumeric data.
    promotional_designator_name
        An eternally assigned or managed number or alphanumeric data for a
        ticket designator.
    description
        Description of the contract.
    priority_order
        Priority order associated with this Contract.
    """

    class Meta:
        name = "Contract"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    supplier: None | str = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        },
    )
    supplier_type: None | TypeSupplierType1 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        },
    )
    provider: None | str = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        },
    )
    expiration_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
        },
    )
    discount_percentage: None | str = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    discount_value: None | str = field(
        default=None,
        metadata={
            "name": "DiscountValue",
            "type": "Attribute",
        },
    )
    supplier_contract_number: None | str = field(
        default=None,
        metadata={
            "name": "SupplierContractNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    promotional_designator_name: None | str = field(
        default=None,
        metadata={
            "name": "PromotionalDesignatorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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
