from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xcbl.models.sourcing_create import AttributeName
from xcbl.models.sourcing_result import (
    AttachmentPurpose,
    CatalogId,
    CategoryId,
    CountryOfOrigin,
)
from xcbl.models.time_series_response import (
    Party,
    Uomcoded,
    UomcodedOther,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import Identifier


class ActionValue(Enum):
    ADD = "Add"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"


@dataclass(kw_only=True)
class Amount:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttachmentMimetype:
    class Meta:
        name = "AttachmentMIMEType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttachmentUrl:
    class Meta:
        name = "AttachmentURL"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttributeId:
    class Meta:
        name = "AttributeID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class AttributeTypeScalarType(Enum):
    STRING = "String"
    INTEGER = "Integer"
    NUMERIC = "Numeric"
    CURRENCY = "Currency"
    DATE = "Date"
    ENUMERATION = "Enumeration"


@dataclass(kw_only=True)
class AttributeValue:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BaseProductNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Buyer:
    partner_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerRef",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class CatalogAudienceCatalogAudienceCoded(Enum):
    ENUMERATED_BUYERS_ONLY = "EnumeratedBuyersOnly"
    PUBLIC = "Public"


@dataclass(kw_only=True)
class CatalogContractId:
    class Meta:
        name = "CatalogContractID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogContractItemId:
    class Meta:
        name = "CatalogContractItemID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class CatalogContractType(Enum):
    OTHER = "Other"
    BUYER = "Buyer"
    SUPPLIER = "Supplier"


@dataclass(kw_only=True)
class CatalogDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogIdref:
    class Meta:
        name = "CatalogIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogLogoUrl:
    class Meta:
        name = "CatalogLogoURL"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogPrettyName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogProviderIdref:
    class Meta:
        name = "CatalogProviderIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class CatalogSchemaType(Enum):
    OTHER = "Other"
    BUYER = "Buyer"
    SUPPLIER = "Supplier"


@dataclass(kw_only=True)
class CatalogVersion:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CategoryIdref:
    class Meta:
        name = "CategoryIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CategoryName:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ComparableUomconversionFactor:
    class Meta:
        name = "ComparableUOMConversionFactor"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DefaultLanguage:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EnumeratedValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ExtensionToSchemasUrn:
    class Meta:
        name = "ExtensionToSchemasURN"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ExternalCategory:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IsMultiVendor:
    pass


@dataclass(kw_only=True)
class IsPriceUpdate:
    pass


@dataclass(kw_only=True)
class IsPublicAccount:
    pass


@dataclass(kw_only=True)
class IsReplacement:
    pass


@dataclass(kw_only=True)
class IsRequired:
    pass


@dataclass(kw_only=True)
class ItemGuid:
    class Meta:
        name = "ItemGUID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LeadTime:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LongDescription:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    description_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescriptionPurpose",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LotSize:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ManuPartNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Manufacturer:
    partner_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerRef",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MinOrder:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MinimumQuantity:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartnerRelationshipCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartnerRelationshipCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class PartnerRelationship1(Enum):
    SUPPLIER = "Supplier"
    SUPPLIER_AGENT = "SupplierAgent"
    BUYER = "Buyer"
    INFO_PROVIDER = "InfoProvider"
    MANUFACTURER = "Manufacturer"


@dataclass(kw_only=True)
class PriceBasisQuant:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCatalogId:
    class Meta:
        name = "PriceCatalogID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCatalogIdref:
    class Meta:
        name = "PriceCatalogIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductIdextension:
    class Meta:
        name = "ProductIDExtension"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductIdref:
    class Meta:
        name = "ProductIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ProductIdstandardAgency(Enum):
    OTHER = "Other"
    GTIN = "GTIN"
    EAN = "EAN"
    UCC = "UCC"


class ProductIdType(Enum):
    OTHER = "Other"
    BUYER = "Buyer"
    SUPPLIER = "Supplier"


@dataclass(kw_only=True)
class ProductName:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ProductType(Enum):
    OTHER = "Other"
    GOOD = "Good"
    SERVICE = "Service"


class RelatedProductTargetType(Enum):
    COMPONENT = "Component"
    SUBSTITUTE = "Substitute"
    ALTERNATIVE = "Alternative"
    ACCESSORY = "Accessory"


@dataclass(kw_only=True)
class SchemaName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SchemaSource:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SchemaStandard:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SchemaUrn:
    class Meta:
        name = "SchemaURN"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SchemaVersion:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShortDescription:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SupplierAccountId:
    class Meta:
        name = "SupplierAccountID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SystemAddress:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SystemType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ValidFrom:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ValidUntil:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ValidateAttributes:
    pass


@dataclass(kw_only=True)
class VendorIdref:
    class Meta:
        name = "VendorIDRef"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VendorPartNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Action:
    value: ActionValue = field(
        default=ActionValue.ADD,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttributeType:
    scalar_type: AttributeTypeScalarType = field(
        default=AttributeTypeScalarType.STRING,
        metadata={
            "name": "ScalarType",
            "type": "Attribute",
            "required": True,
        },
    )
    max_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxSize",
            "type": "Attribute",
        },
    )
    enumerated_value: List[EnumeratedValue] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class BuyerIdentifier:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CatalogAudience:
    catalog_audience_coded: CatalogAudienceCatalogAudienceCoded = field(
        default=CatalogAudienceCatalogAudienceCoded.PUBLIC,
        metadata={
            "name": "CatalogAudienceCoded",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CatalogContract:
    type_value: CatalogContractType = field(
        default=CatalogContractType.BUYER,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    catalog_contract_id: CatalogContractId = field(
        metadata={
            "name": "CatalogContractID",
            "type": "Element",
            "required": True,
        }
    )
    catalog_contract_item_id: CatalogContractItemId = field(
        metadata={
            "name": "CatalogContractItemID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CatalogSystem:
    system_address: SystemAddress = field(
        metadata={
            "name": "SystemAddress",
            "type": "Element",
            "required": True,
        }
    )
    system_type: SystemType = field(
        metadata={
            "name": "SystemType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DefaultCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ExternalItemRef:
    catalog_provider_idref: Optional[CatalogProviderIdref] = field(
        default=None,
        metadata={
            "name": "CatalogProviderIDRef",
            "type": "Element",
        },
    )
    catalog_idref: Optional[CatalogIdref] = field(
        default=None,
        metadata={
            "name": "CatalogIDRef",
            "type": "Element",
        },
    )
    product_idref: Optional[ProductIdref] = field(
        default=None,
        metadata={
            "name": "ProductIDRef",
            "type": "Element",
        },
    )
    item_guid: Optional[ItemGuid] = field(
        default=None,
        metadata={
            "name": "ItemGUID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ParentCategoryRefList:
    category_idref: List[CategoryIdref] = field(
        default_factory=list,
        metadata={
            "name": "CategoryIDRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PartnerRelationship:
    partner_relationship_coded: PartnerRelationshipCoded = field(
        metadata={
            "name": "PartnerRelationshipCoded",
            "type": "Element",
            "required": True,
        }
    )
    partner_relationship_coded_other: Optional[
        PartnerRelationshipCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "PartnerRelationshipCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProductAttachment:
    attachment_url: AttachmentUrl = field(
        metadata={
            "name": "AttachmentURL",
            "type": "Element",
            "required": True,
        }
    )
    attachment_purpose: Optional[AttachmentPurpose] = field(
        default=None,
        metadata={
            "name": "AttachmentPurpose",
            "type": "Element",
        },
    )
    attachment_mimetype: Optional[AttachmentMimetype] = field(
        default=None,
        metadata={
            "name": "AttachmentMIMEType",
            "type": "Element",
        },
    )
    short_description: List[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: List[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProductId:
    class Meta:
        name = "ProductID"

    type_value: ProductIdType = field(
        default=ProductIdType.SUPPLIER,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProductIdstandard:
    class Meta:
        name = "ProductIDStandard"

    agency: ProductIdstandardAgency = field(
        default=ProductIdstandardAgency.OTHER,
        metadata={
            "name": "Agency",
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RelatedProduct:
    target_type: RelatedProductTargetType = field(
        default=RelatedProductTargetType.COMPONENT,
        metadata={
            "name": "TargetType",
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SchemaCategoryRefList:
    category_idref: List[CategoryIdref] = field(
        default_factory=list,
        metadata={
            "name": "CategoryIDRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Uom:
    class Meta:
        name = "UOM"

    uomcoded: Uomcoded = field(
        metadata={
            "name": "UOMCoded",
            "type": "Element",
            "required": True,
        }
    )
    uomcoded_other: Optional[UomcodedOther] = field(
        default=None,
        metadata={
            "name": "UOMCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AttributeUnit:
    uom: Uom = field(
        metadata={
            "name": "UOM",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CatalogProvider:
    provider_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderID",
            "type": "Attribute",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
        },
    )
    catalog_system: Optional[CatalogSystem] = field(
        default=None,
        metadata={
            "name": "CatalogSystem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ComparableUom:
    class Meta:
        name = "ComparableUOM"

    uom: Uom = field(
        metadata={
            "name": "UOM",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DefaultUom:
    class Meta:
        name = "DefaultUOM"

    uom: Uom = field(
        metadata={
            "name": "UOM",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LeadTimeUom:
    class Meta:
        name = "LeadTimeUOM"

    uom: Uom = field(
        metadata={
            "name": "UOM",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Partner:
    partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerID",
            "type": "Attribute",
        },
    )
    relationship: PartnerRelationship1 = field(
        default=PartnerRelationship1.SUPPLIER,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        },
    )
    action: Optional[Action] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
        },
    )
    partner_relationship: List[PartnerRelationship] = field(
        default_factory=list,
        metadata={
            "name": "PartnerRelationship",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCatalog:
    action: Optional[Action] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    price_catalog_id: PriceCatalogId = field(
        metadata={
            "name": "PriceCatalogID",
            "type": "Element",
            "required": True,
        }
    )
    valid_from: Optional[ValidFrom] = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: Optional[ValidUntil] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProductPrice:
    amount: Amount = field(
        metadata={
            "name": "Amount",
            "type": "Element",
            "required": True,
        }
    )
    price_type: Optional[PriceType] = field(
        default=None,
        metadata={
            "name": "PriceType",
            "type": "Element",
        },
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        },
    )
    uom: Optional[Uom] = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    valid_from: Optional[ValidFrom] = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: Optional[ValidUntil] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    buyer: Optional[Buyer] = field(
        default=None,
        metadata={
            "name": "Buyer",
            "type": "Element",
        },
    )
    price_basis_quant: Optional[PriceBasisQuant] = field(
        default=None,
        metadata={
            "name": "PriceBasisQuant",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupplierAccount:
    action: Optional[Action] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    supplier_account_id: Optional[SupplierAccountId] = field(
        default=None,
        metadata={
            "name": "SupplierAccountID",
            "type": "Element",
        },
    )
    buyer_identifier: Optional[BuyerIdentifier] = field(
        default=None,
        metadata={
            "name": "BuyerIdentifier",
            "type": "Element",
        },
    )
    is_public_account: Optional[IsPublicAccount] = field(
        default=None,
        metadata={
            "name": "IsPublicAccount",
            "type": "Element",
        },
    )
    price_catalog_idref: List[PriceCatalogIdref] = field(
        default_factory=list,
        metadata={
            "name": "PriceCatalogIDRef",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CategoryAttribute:
    attribute_id: AttributeId = field(
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "required": True,
        }
    )
    attribute_name: List[AttributeName] = field(
        default_factory=list,
        metadata={
            "name": "AttributeName",
            "type": "Element",
        },
    )
    attribute_type: AttributeType = field(
        metadata={
            "name": "AttributeType",
            "type": "Element",
            "required": True,
        }
    )
    default_uom: Optional[DefaultUom] = field(
        default=None,
        metadata={
            "name": "DefaultUOM",
            "type": "Element",
        },
    )
    is_required: Optional[IsRequired] = field(
        default=None,
        metadata={
            "name": "IsRequired",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPartners:
    partner: List[Partner] = field(
        default_factory=list,
        metadata={
            "name": "Partner",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ObjectAttribute:
    attribute_id: AttributeId = field(
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "required": True,
        }
    )
    attribute_unit: Optional[AttributeUnit] = field(
        default=None,
        metadata={
            "name": "AttributeUnit",
            "type": "Element",
        },
    )
    attribute_value: List[AttributeValue] = field(
        default_factory=list,
        metadata={
            "name": "AttributeValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Pricing:
    product_idref: ProductIdref = field(
        metadata={
            "name": "ProductIDRef",
            "type": "Element",
            "required": True,
        }
    )
    price_catalog_idref: PriceCatalogIdref = field(
        metadata={
            "name": "PriceCatalogIDRef",
            "type": "Element",
            "required": True,
        }
    )
    product_price: List[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PricingInformation:
    price_catalog: List[PriceCatalog] = field(
        default_factory=list,
        metadata={
            "name": "PriceCatalog",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ProductVendorData:
    partner_ref: str = field(
        metadata={
            "name": "PartnerRef",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_idref: Optional[VendorIdref] = field(
        default=None,
        metadata={
            "name": "VendorIDRef",
            "type": "Element",
        },
    )
    vendor_part_number: Optional[VendorPartNumber] = field(
        default=None,
        metadata={
            "name": "VendorPartNumber",
            "type": "Element",
        },
    )
    lead_time: Optional[LeadTime] = field(
        default=None,
        metadata={
            "name": "LeadTime",
            "type": "Element",
        },
    )
    lead_time_uom: Optional[LeadTimeUom] = field(
        default=None,
        metadata={
            "name": "LeadTimeUOM",
            "type": "Element",
        },
    )
    catalog_contract: Optional[CatalogContract] = field(
        default=None,
        metadata={
            "name": "CatalogContract",
            "type": "Element",
        },
    )
    min_order: Optional[MinOrder] = field(
        default=None,
        metadata={
            "name": "MinOrder",
            "type": "Element",
        },
    )
    product_price: List[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupplierAccountInformation:
    supplier_account: List[SupplierAccount] = field(
        default_factory=list,
        metadata={
            "name": "SupplierAccount",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CatalogHeader:
    catalog_id: CatalogId = field(
        metadata={
            "name": "CatalogID",
            "type": "Element",
            "required": True,
        }
    )
    catalog_date: Optional[CatalogDate] = field(
        default=None,
        metadata={
            "name": "CatalogDate",
            "type": "Element",
        },
    )
    catalog_provider: CatalogProvider = field(
        metadata={
            "name": "CatalogProvider",
            "type": "Element",
            "required": True,
        }
    )
    catalog_pretty_name: Optional[CatalogPrettyName] = field(
        default=None,
        metadata={
            "name": "CatalogPrettyName",
            "type": "Element",
        },
    )
    catalog_logo_url: Optional[CatalogLogoUrl] = field(
        default=None,
        metadata={
            "name": "CatalogLogoURL",
            "type": "Element",
        },
    )
    list_of_partners: Optional[ListOfPartners] = field(
        default=None,
        metadata={
            "name": "ListOfPartners",
            "type": "Element",
        },
    )
    catalog_audience: Optional[CatalogAudience] = field(
        default=None,
        metadata={
            "name": "CatalogAudience",
            "type": "Element",
        },
    )
    pricing_information: Optional[PricingInformation] = field(
        default=None,
        metadata={
            "name": "PricingInformation",
            "type": "Element",
        },
    )
    supplier_account_information: Optional[SupplierAccountInformation] = field(
        default=None,
        metadata={
            "name": "SupplierAccountInformation",
            "type": "Element",
        },
    )
    valid_from: Optional[ValidFrom] = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: Optional[ValidUntil] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    catalog_version: Optional[CatalogVersion] = field(
        default=None,
        metadata={
            "name": "CatalogVersion",
            "type": "Element",
        },
    )
    default_language: Optional[DefaultLanguage] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        },
    )
    default_currency: Optional[DefaultCurrency] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
        },
    )
    is_replacement: Optional[IsReplacement] = field(
        default=None,
        metadata={
            "name": "IsReplacement",
            "type": "Element",
        },
    )
    is_price_update: Optional[IsPriceUpdate] = field(
        default=None,
        metadata={
            "name": "IsPriceUpdate",
            "type": "Element",
        },
    )
    is_multi_vendor: Optional[IsMultiVendor] = field(
        default=None,
        metadata={
            "name": "IsMultiVendor",
            "type": "Element",
        },
    )
    short_description: List[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: List[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    object_attribute: List[ObjectAttribute] = field(
        default_factory=list,
        metadata={
            "name": "ObjectAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Product:
    type_value: ProductType = field(
        default=ProductType.GOOD,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    schema_category_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SchemaCategoryRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
    action: Optional[Action] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    product_id: ProductId = field(
        metadata={
            "name": "ProductID",
            "type": "Element",
            "required": True,
        }
    )
    base_product_number: Optional[BaseProductNumber] = field(
        default=None,
        metadata={
            "name": "BaseProductNumber",
            "type": "Element",
        },
    )
    schema_category_ref_list: Optional[SchemaCategoryRefList] = field(
        default=None,
        metadata={
            "name": "SchemaCategoryRefList",
            "type": "Element",
        },
    )
    product_idextension: Optional[ProductIdextension] = field(
        default=None,
        metadata={
            "name": "ProductIDExtension",
            "type": "Element",
        },
    )
    external_item_ref: List[ExternalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "ExternalItemRef",
            "type": "Element",
        },
    )
    product_idstandard: Optional[ProductIdstandard] = field(
        default=None,
        metadata={
            "name": "ProductIDStandard",
            "type": "Element",
        },
    )
    product_name: List[ProductName] = field(
        default_factory=list,
        metadata={
            "name": "ProductName",
            "type": "Element",
        },
    )
    uom: Optional[Uom] = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
        },
    )
    comparable_uom: Optional[ComparableUom] = field(
        default=None,
        metadata={
            "name": "ComparableUOM",
            "type": "Element",
        },
    )
    comparable_uomconversion_factor: Optional[
        ComparableUomconversionFactor
    ] = field(
        default=None,
        metadata={
            "name": "ComparableUOMConversionFactor",
            "type": "Element",
        },
    )
    manufacturer: Optional[Manufacturer] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
        },
    )
    manu_part_number: Optional[ManuPartNumber] = field(
        default=None,
        metadata={
            "name": "ManuPartNumber",
            "type": "Element",
        },
    )
    lead_time: Optional[LeadTime] = field(
        default=None,
        metadata={
            "name": "LeadTime",
            "type": "Element",
        },
    )
    lead_time_uom: Optional[LeadTimeUom] = field(
        default=None,
        metadata={
            "name": "LeadTimeUOM",
            "type": "Element",
        },
    )
    valid_from: Optional[ValidFrom] = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: Optional[ValidUntil] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    min_order: Optional[MinOrder] = field(
        default=None,
        metadata={
            "name": "MinOrder",
            "type": "Element",
        },
    )
    lot_size: Optional[LotSize] = field(
        default=None,
        metadata={
            "name": "LotSize",
            "type": "Element",
        },
    )
    external_category: List[ExternalCategory] = field(
        default_factory=list,
        metadata={
            "name": "ExternalCategory",
            "type": "Element",
        },
    )
    short_description: List[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: List[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    catalog_contract: List[CatalogContract] = field(
        default_factory=list,
        metadata={
            "name": "CatalogContract",
            "type": "Element",
        },
    )
    product_price: List[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )
    product_vendor_data: List[ProductVendorData] = field(
        default_factory=list,
        metadata={
            "name": "ProductVendorData",
            "type": "Element",
        },
    )
    product_attachment: List[ProductAttachment] = field(
        default_factory=list,
        metadata={
            "name": "ProductAttachment",
            "type": "Element",
        },
    )
    related_product: List[RelatedProduct] = field(
        default_factory=list,
        metadata={
            "name": "RelatedProduct",
            "type": "Element",
        },
    )
    object_attribute: List[ObjectAttribute] = field(
        default_factory=list,
        metadata={
            "name": "ObjectAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SchemaCategory:
    category_id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryID",
            "type": "Attribute",
        },
    )
    parent_category_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ParentCategoryRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
    category_id: CategoryId = field(
        metadata={
            "name": "CategoryID",
            "type": "Element",
            "required": True,
        }
    )
    parent_category_ref_list: Optional[ParentCategoryRefList] = field(
        default=None,
        metadata={
            "name": "ParentCategoryRefList",
            "type": "Element",
        },
    )
    category_name: List[CategoryName] = field(
        default_factory=list,
        metadata={
            "name": "CategoryName",
            "type": "Element",
        },
    )
    short_description: List[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: List[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    category_attribute: List[CategoryAttribute] = field(
        default_factory=list,
        metadata={
            "name": "CategoryAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CatalogData:
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "name": "Product",
            "type": "Element",
        },
    )
    pricing: List[Pricing] = field(
        default_factory=list,
        metadata={
            "name": "Pricing",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CatalogSchema:
    type_value: CatalogSchemaType = field(
        default=CatalogSchemaType.SUPPLIER,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    schema_name: SchemaName = field(
        metadata={
            "name": "SchemaName",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Optional[SchemaVersion] = field(
        default=None,
        metadata={
            "name": "SchemaVersion",
            "type": "Element",
        },
    )
    schema_standard: Optional[SchemaStandard] = field(
        default=None,
        metadata={
            "name": "SchemaStandard",
            "type": "Element",
        },
    )
    validate_attributes: Optional[ValidateAttributes] = field(
        default=None,
        metadata={
            "name": "ValidateAttributes",
            "type": "Element",
        },
    )
    short_description: List[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: List[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    schema_source: Optional[SchemaSource] = field(
        default=None,
        metadata={
            "name": "SchemaSource",
            "type": "Element",
        },
    )
    schema_urn: Optional[SchemaUrn] = field(
        default=None,
        metadata={
            "name": "SchemaURN",
            "type": "Element",
        },
    )
    extension_to_schemas_urn: Optional[ExtensionToSchemasUrn] = field(
        default=None,
        metadata={
            "name": "ExtensionToSchemasURN",
            "type": "Element",
        },
    )
    schema_category: List[SchemaCategory] = field(
        default_factory=list,
        metadata={
            "name": "SchemaCategory",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProductCatalog:
    catalog_header: CatalogHeader = field(
        metadata={
            "name": "CatalogHeader",
            "type": "Element",
            "required": True,
        }
    )
    catalog_schema: Optional[CatalogSchema] = field(
        default=None,
        metadata={
            "name": "CatalogSchema",
            "type": "Element",
        },
    )
    catalog_data: Optional[CatalogData] = field(
        default=None,
        metadata={
            "name": "CatalogData",
            "type": "Element",
        },
    )
