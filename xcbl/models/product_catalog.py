from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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
    partner_ref: str | None = field(
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
    description_purpose: str | None = field(
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
    partner_ref: str | None = field(
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
    max_size: str | None = field(
        default=None,
        metadata={
            "name": "MaxSize",
            "type": "Attribute",
        },
    )
    enumerated_value: list[EnumeratedValue] = field(
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
    catalog_provider_idref: CatalogProviderIdref | None = field(
        default=None,
        metadata={
            "name": "CatalogProviderIDRef",
            "type": "Element",
        },
    )
    catalog_idref: CatalogIdref | None = field(
        default=None,
        metadata={
            "name": "CatalogIDRef",
            "type": "Element",
        },
    )
    product_idref: ProductIdref | None = field(
        default=None,
        metadata={
            "name": "ProductIDRef",
            "type": "Element",
        },
    )
    item_guid: ItemGuid | None = field(
        default=None,
        metadata={
            "name": "ItemGUID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ParentCategoryRefList:
    category_idref: list[CategoryIdref] = field(
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
    partner_relationship_coded_other: PartnerRelationshipCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "PartnerRelationshipCodedOther",
                "type": "Element",
            },
        )
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
    attachment_purpose: AttachmentPurpose | None = field(
        default=None,
        metadata={
            "name": "AttachmentPurpose",
            "type": "Element",
        },
    )
    attachment_mimetype: AttachmentMimetype | None = field(
        default=None,
        metadata={
            "name": "AttachmentMIMEType",
            "type": "Element",
        },
    )
    short_description: list[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: list[LongDescription] = field(
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
    category_idref: list[CategoryIdref] = field(
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
    uomcoded_other: UomcodedOther | None = field(
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
    provider_id: str | None = field(
        default=None,
        metadata={
            "name": "ProviderID",
            "type": "Attribute",
        },
    )
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
        },
    )
    catalog_system: CatalogSystem | None = field(
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
    partner_id: str | None = field(
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
    action: Action | None = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
        },
    )
    partner_relationship: list[PartnerRelationship] = field(
        default_factory=list,
        metadata={
            "name": "PartnerRelationship",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCatalog:
    action: Action | None = field(
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
    valid_from: ValidFrom | None = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: ValidUntil | None = field(
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
    price_type: PriceType | None = field(
        default=None,
        metadata={
            "name": "PriceType",
            "type": "Element",
        },
    )
    currency: Currency | None = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        },
    )
    uom: Uom | None = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    valid_from: ValidFrom | None = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: ValidUntil | None = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    buyer: Buyer | None = field(
        default=None,
        metadata={
            "name": "Buyer",
            "type": "Element",
        },
    )
    price_basis_quant: PriceBasisQuant | None = field(
        default=None,
        metadata={
            "name": "PriceBasisQuant",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupplierAccount:
    action: Action | None = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    supplier_account_id: SupplierAccountId | None = field(
        default=None,
        metadata={
            "name": "SupplierAccountID",
            "type": "Element",
        },
    )
    buyer_identifier: BuyerIdentifier | None = field(
        default=None,
        metadata={
            "name": "BuyerIdentifier",
            "type": "Element",
        },
    )
    is_public_account: IsPublicAccount | None = field(
        default=None,
        metadata={
            "name": "IsPublicAccount",
            "type": "Element",
        },
    )
    price_catalog_idref: list[PriceCatalogIdref] = field(
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
    attribute_name: list[AttributeName] = field(
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
    default_uom: DefaultUom | None = field(
        default=None,
        metadata={
            "name": "DefaultUOM",
            "type": "Element",
        },
    )
    is_required: IsRequired | None = field(
        default=None,
        metadata={
            "name": "IsRequired",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPartners:
    partner: list[Partner] = field(
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
    attribute_unit: AttributeUnit | None = field(
        default=None,
        metadata={
            "name": "AttributeUnit",
            "type": "Element",
        },
    )
    attribute_value: list[AttributeValue] = field(
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
    product_price: list[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PricingInformation:
    price_catalog: list[PriceCatalog] = field(
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
    vendor_idref: VendorIdref | None = field(
        default=None,
        metadata={
            "name": "VendorIDRef",
            "type": "Element",
        },
    )
    vendor_part_number: VendorPartNumber | None = field(
        default=None,
        metadata={
            "name": "VendorPartNumber",
            "type": "Element",
        },
    )
    lead_time: LeadTime | None = field(
        default=None,
        metadata={
            "name": "LeadTime",
            "type": "Element",
        },
    )
    lead_time_uom: LeadTimeUom | None = field(
        default=None,
        metadata={
            "name": "LeadTimeUOM",
            "type": "Element",
        },
    )
    catalog_contract: CatalogContract | None = field(
        default=None,
        metadata={
            "name": "CatalogContract",
            "type": "Element",
        },
    )
    min_order: MinOrder | None = field(
        default=None,
        metadata={
            "name": "MinOrder",
            "type": "Element",
        },
    )
    product_price: list[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupplierAccountInformation:
    supplier_account: list[SupplierAccount] = field(
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
    catalog_date: CatalogDate | None = field(
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
    catalog_pretty_name: CatalogPrettyName | None = field(
        default=None,
        metadata={
            "name": "CatalogPrettyName",
            "type": "Element",
        },
    )
    catalog_logo_url: CatalogLogoUrl | None = field(
        default=None,
        metadata={
            "name": "CatalogLogoURL",
            "type": "Element",
        },
    )
    list_of_partners: ListOfPartners | None = field(
        default=None,
        metadata={
            "name": "ListOfPartners",
            "type": "Element",
        },
    )
    catalog_audience: CatalogAudience | None = field(
        default=None,
        metadata={
            "name": "CatalogAudience",
            "type": "Element",
        },
    )
    pricing_information: PricingInformation | None = field(
        default=None,
        metadata={
            "name": "PricingInformation",
            "type": "Element",
        },
    )
    supplier_account_information: SupplierAccountInformation | None = field(
        default=None,
        metadata={
            "name": "SupplierAccountInformation",
            "type": "Element",
        },
    )
    valid_from: ValidFrom | None = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: ValidUntil | None = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    catalog_version: CatalogVersion | None = field(
        default=None,
        metadata={
            "name": "CatalogVersion",
            "type": "Element",
        },
    )
    default_language: DefaultLanguage | None = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
        },
    )
    default_currency: DefaultCurrency | None = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
        },
    )
    is_replacement: IsReplacement | None = field(
        default=None,
        metadata={
            "name": "IsReplacement",
            "type": "Element",
        },
    )
    is_price_update: IsPriceUpdate | None = field(
        default=None,
        metadata={
            "name": "IsPriceUpdate",
            "type": "Element",
        },
    )
    is_multi_vendor: IsMultiVendor | None = field(
        default=None,
        metadata={
            "name": "IsMultiVendor",
            "type": "Element",
        },
    )
    short_description: list[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: list[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    object_attribute: list[ObjectAttribute] = field(
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
    schema_category_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SchemaCategoryRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
    action: Action | None = field(
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
    base_product_number: BaseProductNumber | None = field(
        default=None,
        metadata={
            "name": "BaseProductNumber",
            "type": "Element",
        },
    )
    schema_category_ref_list: SchemaCategoryRefList | None = field(
        default=None,
        metadata={
            "name": "SchemaCategoryRefList",
            "type": "Element",
        },
    )
    product_idextension: ProductIdextension | None = field(
        default=None,
        metadata={
            "name": "ProductIDExtension",
            "type": "Element",
        },
    )
    external_item_ref: list[ExternalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "ExternalItemRef",
            "type": "Element",
        },
    )
    product_idstandard: ProductIdstandard | None = field(
        default=None,
        metadata={
            "name": "ProductIDStandard",
            "type": "Element",
        },
    )
    product_name: list[ProductName] = field(
        default_factory=list,
        metadata={
            "name": "ProductName",
            "type": "Element",
        },
    )
    uom: Uom | None = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
        },
    )
    comparable_uom: ComparableUom | None = field(
        default=None,
        metadata={
            "name": "ComparableUOM",
            "type": "Element",
        },
    )
    comparable_uomconversion_factor: ComparableUomconversionFactor | None = (
        field(
            default=None,
            metadata={
                "name": "ComparableUOMConversionFactor",
                "type": "Element",
            },
        )
    )
    manufacturer: Manufacturer | None = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
        },
    )
    manu_part_number: ManuPartNumber | None = field(
        default=None,
        metadata={
            "name": "ManuPartNumber",
            "type": "Element",
        },
    )
    lead_time: LeadTime | None = field(
        default=None,
        metadata={
            "name": "LeadTime",
            "type": "Element",
        },
    )
    lead_time_uom: LeadTimeUom | None = field(
        default=None,
        metadata={
            "name": "LeadTimeUOM",
            "type": "Element",
        },
    )
    valid_from: ValidFrom | None = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
        },
    )
    valid_until: ValidUntil | None = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
        },
    )
    country_of_origin: CountryOfOrigin | None = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    min_order: MinOrder | None = field(
        default=None,
        metadata={
            "name": "MinOrder",
            "type": "Element",
        },
    )
    lot_size: LotSize | None = field(
        default=None,
        metadata={
            "name": "LotSize",
            "type": "Element",
        },
    )
    external_category: list[ExternalCategory] = field(
        default_factory=list,
        metadata={
            "name": "ExternalCategory",
            "type": "Element",
        },
    )
    short_description: list[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: list[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    catalog_contract: list[CatalogContract] = field(
        default_factory=list,
        metadata={
            "name": "CatalogContract",
            "type": "Element",
        },
    )
    product_price: list[ProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "ProductPrice",
            "type": "Element",
        },
    )
    product_vendor_data: list[ProductVendorData] = field(
        default_factory=list,
        metadata={
            "name": "ProductVendorData",
            "type": "Element",
        },
    )
    product_attachment: list[ProductAttachment] = field(
        default_factory=list,
        metadata={
            "name": "ProductAttachment",
            "type": "Element",
        },
    )
    related_product: list[RelatedProduct] = field(
        default_factory=list,
        metadata={
            "name": "RelatedProduct",
            "type": "Element",
        },
    )
    object_attribute: list[ObjectAttribute] = field(
        default_factory=list,
        metadata={
            "name": "ObjectAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SchemaCategory:
    category_id_attribute: str | None = field(
        default=None,
        metadata={
            "name": "CategoryID",
            "type": "Attribute",
        },
    )
    parent_category_ref: list[str] = field(
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
    parent_category_ref_list: ParentCategoryRefList | None = field(
        default=None,
        metadata={
            "name": "ParentCategoryRefList",
            "type": "Element",
        },
    )
    category_name: list[CategoryName] = field(
        default_factory=list,
        metadata={
            "name": "CategoryName",
            "type": "Element",
        },
    )
    short_description: list[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: list[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    category_attribute: list[CategoryAttribute] = field(
        default_factory=list,
        metadata={
            "name": "CategoryAttribute",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CatalogData:
    product: list[Product] = field(
        default_factory=list,
        metadata={
            "name": "Product",
            "type": "Element",
        },
    )
    pricing: list[Pricing] = field(
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
    schema_version: SchemaVersion | None = field(
        default=None,
        metadata={
            "name": "SchemaVersion",
            "type": "Element",
        },
    )
    schema_standard: SchemaStandard | None = field(
        default=None,
        metadata={
            "name": "SchemaStandard",
            "type": "Element",
        },
    )
    validate_attributes: ValidateAttributes | None = field(
        default=None,
        metadata={
            "name": "ValidateAttributes",
            "type": "Element",
        },
    )
    short_description: list[ShortDescription] = field(
        default_factory=list,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    long_description: list[LongDescription] = field(
        default_factory=list,
        metadata={
            "name": "LongDescription",
            "type": "Element",
        },
    )
    schema_source: SchemaSource | None = field(
        default=None,
        metadata={
            "name": "SchemaSource",
            "type": "Element",
        },
    )
    schema_urn: SchemaUrn | None = field(
        default=None,
        metadata={
            "name": "SchemaURN",
            "type": "Element",
        },
    )
    extension_to_schemas_urn: ExtensionToSchemasUrn | None = field(
        default=None,
        metadata={
            "name": "ExtensionToSchemasURN",
            "type": "Element",
        },
    )
    schema_category: list[SchemaCategory] = field(
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
    catalog_schema: CatalogSchema | None = field(
        default=None,
        metadata={
            "name": "CatalogSchema",
            "type": "Element",
        },
    )
    catalog_data: CatalogData | None = field(
        default=None,
        metadata={
            "name": "CatalogData",
            "type": "Element",
        },
    )
