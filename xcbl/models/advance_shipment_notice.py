from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    ItemPackagingReference,
    Language,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfDimension,
    TermsOfDelivery,
)
from xcbl.models.goods_receipt import (
    ItemShipFromParty,
    ItemShipToParty,
    ListOfDestinationRef,
    ListOfTransportRouting,
    OtherItemDates,
)
from xcbl.models.invoice import (
    Asnnumber,
    AsnorderNumber,
    Asnreferences,
    ExceptionQuantities,
    PurchaseOrderReference,
)
from xcbl.models.order_request import (
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfAllowOrCharge,
    ListOfItemReferences,
    ListOfNameValueSet,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    PackageDetail,
    ParentItemNumber,
    PaymentInstructions,
    TotalQuantity,
    TransportPackagingTotals,
)
from xcbl.models.order_status_result import LineItemAttachment
from xcbl.models.request_for_quotation import OrderParty


@dataclass
class Asnpurpose:
    class Meta:
        name = "ASNPurpose"

    asnpurpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnpurpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNPurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Asnstatus:
    class Meta:
        name = "ASNStatus"

    asnstatus_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnstatus_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNStatusCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Asntype:
    class Meta:
        name = "ASNType"

    asntype_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    asntype_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AsnallowancesOrCharges:
    class Meta:
        name = "ASNAllowancesOrCharges"

    list_of_allow_or_charge: Optional[ListOfAllowOrCharge] = field(
        default=None,
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Asncurrency:
    class Meta:
        name = "ASNCurrency"

    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Asndates:
    class Meta:
        name = "ASNDates"

    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        }
    )
    shipped_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippedDate",
            "type": "Element",
        }
    )
    earliest_delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestDeliveryDate",
            "type": "Element",
        }
    )
    latest_delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryDate",
            "type": "Element",
        }
    )
    collection_date_of_cargo: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollectionDateOfCargo",
            "type": "Element",
        }
    )
    schedule_delivery_date_after: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleDeliveryDateAfter",
            "type": "Element",
        }
    )
    schedule_delivery_date_before: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleDeliveryDateBefore",
            "type": "Element",
        }
    )
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
        }
    )


@dataclass
class AsnheaderAttachments:
    class Meta:
        name = "ASNHeaderAttachments"

    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Asnlanguage:
    class Meta:
        name = "ASNLanguage"

    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AsnlineItemListOfAllowOrCharge:
    class Meta:
        name = "ASNLineItemListOfAllowOrCharge"

    list_of_allow_or_charge: Optional[ListOfAllowOrCharge] = field(
        default=None,
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AsnlineItemReferences:
    class Meta:
        name = "ASNLineItemReferences"

    asnreferences: Optional[Asnreferences] = field(
        default=None,
        metadata={
            "name": "ASNReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AsnpackageDetail:
    class Meta:
        name = "ASNPackageDetail"

    package_detail: Optional[PackageDetail] = field(
        default=None,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Asnparty:
    class Meta:
        name = "ASNParty"

    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AsnpaymentInstructions:
    class Meta:
        name = "ASNPaymentInstructions"

    payment_instructions: Optional[PaymentInstructions] = field(
        default=None,
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Asnsummary:
    class Meta:
        name = "ASNSummary"

    number_of_lines: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        }
    )
    transport_packaging_totals: Optional[TransportPackagingTotals] = field(
        default=None,
        metadata={
            "name": "TransportPackagingTotals",
            "type": "Element",
        }
    )
    summary_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummaryNote",
            "type": "Element",
        }
    )


@dataclass
class AsntermsOfDelivery:
    class Meta:
        name = "ASNTermsOfDelivery"

    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LineItemOrderReference:
    purchase_order_reference: Optional[PurchaseOrderReference] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReferenceToPackage:
    item_packaging_reference: Optional[ItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AsnbaseItemDetail:
    class Meta:
        name = "ASNBaseItemDetail"

    line_item_num: Optional[LineItemNum] = field(
        default=None,
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        }
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        }
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        }
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        }
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        }
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        }
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        }
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        }
    )
    detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    line_item_order_reference: Optional[LineItemOrderReference] = field(
        default=None,
        metadata={
            "name": "LineItemOrderReference",
            "type": "Element",
        }
    )
    asnline_item_references: Optional[AsnlineItemReferences] = field(
        default=None,
        metadata={
            "name": "ASNLineItemReferences",
            "type": "Element",
        }
    )
    exception_quantities: Optional[ExceptionQuantities] = field(
        default=None,
        metadata={
            "name": "ExceptionQuantities",
            "type": "Element",
        }
    )
    reference_to_package: List[ReferenceToPackage] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceToPackage",
            "type": "Element",
        }
    )
    list_of_destination_ref: Optional[ListOfDestinationRef] = field(
        default=None,
        metadata={
            "name": "ListOfDestinationRef",
            "type": "Element",
        }
    )
    requested_delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
        }
    )
    ship_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipByDate",
            "type": "Element",
        }
    )
    other_item_dates: Optional[OtherItemDates] = field(
        default=None,
        metadata={
            "name": "OtherItemDates",
            "type": "Element",
        }
    )
    item_ship_to_party: Optional[ItemShipToParty] = field(
        default=None,
        metadata={
            "name": "ItemShipToParty",
            "type": "Element",
        }
    )
    item_ship_from_party: Optional[ItemShipFromParty] = field(
        default=None,
        metadata={
            "name": "ItemShipFromParty",
            "type": "Element",
        }
    )


@dataclass
class Asnheader:
    class Meta:
        name = "ASNHeader"

    asnnumber: Optional[Asnnumber] = field(
        default=None,
        metadata={
            "name": "ASNNumber",
            "type": "Element",
            "required": True,
        }
    )
    asnissue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    asnorder_number: List[AsnorderNumber] = field(
        default_factory=list,
        metadata={
            "name": "ASNOrderNumber",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    asnreferences: Optional[Asnreferences] = field(
        default=None,
        metadata={
            "name": "ASNReferences",
            "type": "Element",
        }
    )
    asnpurpose: Optional[Asnpurpose] = field(
        default=None,
        metadata={
            "name": "ASNPurpose",
            "type": "Element",
            "required": True,
        }
    )
    asntype: Optional[Asntype] = field(
        default=None,
        metadata={
            "name": "ASNType",
            "type": "Element",
        }
    )
    asnstatus: Optional[Asnstatus] = field(
        default=None,
        metadata={
            "name": "ASNStatus",
            "type": "Element",
        }
    )
    asncurrency: Optional[Asncurrency] = field(
        default=None,
        metadata={
            "name": "ASNCurrency",
            "type": "Element",
        }
    )
    asnlanguage: Optional[Asnlanguage] = field(
        default=None,
        metadata={
            "name": "ASNLanguage",
            "type": "Element",
        }
    )
    asndates: Optional[Asndates] = field(
        default=None,
        metadata={
            "name": "ASNDates",
            "type": "Element",
            "required": True,
        }
    )
    asnparty: Optional[Asnparty] = field(
        default=None,
        metadata={
            "name": "ASNParty",
            "type": "Element",
            "required": True,
        }
    )
    list_of_transport_routing: Optional[ListOfTransportRouting] = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        }
    )
    asnterms_of_delivery: Optional[AsntermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "ASNTermsOfDelivery",
            "type": "Element",
        }
    )
    asnpayment_instructions: Optional[AsnpaymentInstructions] = field(
        default=None,
        metadata={
            "name": "ASNPaymentInstructions",
            "type": "Element",
        }
    )
    asnallowances_or_charges: Optional[AsnallowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "ASNAllowancesOrCharges",
            "type": "Element",
        }
    )
    asnheader_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNHeaderNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    asnheader_attachments: Optional[AsnheaderAttachments] = field(
        default=None,
        metadata={
            "name": "ASNHeaderAttachments",
            "type": "Element",
        }
    )


@dataclass
class ListOfAsnpackageDetail:
    class Meta:
        name = "ListOfASNPackageDetail"

    asnpackage_detail: List[AsnpackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "ASNPackageDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AsnitemDetail:
    class Meta:
        name = "ASNItemDetail"

    asnbase_item_detail: Optional[AsnbaseItemDetail] = field(
        default=None,
        metadata={
            "name": "ASNBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    asnline_item_list_of_allow_or_charge: Optional[AsnlineItemListOfAllowOrCharge] = field(
        default=None,
        metadata={
            "name": "ASNLineItemListOfAllowOrCharge",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfAsnitemDetail:
    class Meta:
        name = "ListOfASNItemDetail"

    asnitem_detail: List[AsnitemDetail] = field(
        default_factory=list,
        metadata={
            "name": "ASNItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Asndetail:
    class Meta:
        name = "ASNDetail"

    list_of_asnitem_detail: Optional[ListOfAsnitemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfASNItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_asnpackage_detail: Optional[ListOfAsnpackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfASNPackageDetail",
            "type": "Element",
        }
    )


@dataclass
class AdvanceShipmentNotice:
    asnheader: Optional[Asnheader] = field(
        default=None,
        metadata={
            "name": "ASNHeader",
            "type": "Element",
            "required": True,
        }
    )
    asndetail: Optional[Asndetail] = field(
        default=None,
        metadata={
            "name": "ASNDetail",
            "type": "Element",
        }
    )
    asnsummary: Optional[Asnsummary] = field(
        default=None,
        metadata={
            "name": "ASNSummary",
            "type": "Element",
        }
    )
