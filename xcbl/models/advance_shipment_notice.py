from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.goods_receipt import (
    ItemShipFromParty,
    ItemShipToParty,
    ListOfDestinationRef,
    OtherItemDates,
    ShipByDate,
)
from xcbl.models.order_response import (
    NumberOfLines,
    TransportPackagingTotals,
)
from xcbl.models.price_check_result import LineItemAttachment
from xcbl.models.remittance_advice import (
    Asnnumber,
    AsnorderNumber,
    Asnreferences,
    ExceptionQuantities,
    PurchaseOrderReference,
    SummaryNote,
)
from xcbl.models.request_for_quotation import PaymentInstructions
from xcbl.models.shipping_schedule import PackageDetail
from xcbl.models.shipping_schedule_response import (
    DetailResponseCoded,
    DetailResponseCodedOther,
    ListOfTransportRouting,
)
from xcbl.models.sourcing_create import DeliveryDate
from xcbl.models.sourcing_result import (
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    ItemPackagingReference,
    LineItemNote,
    LineItemNum,
    LineItemType,
    ListOfAllowOrCharge,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfItemReferences,
    ListOfNameValueSet,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    OrderParty,
    ParentItemNumber,
    RequestedDeliveryDate,
    TermsOfDelivery,
    TotalQuantity,
)
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AsnheaderNote:
    class Meta:
        name = "ASNHeaderNote"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnissueDate:
    class Meta:
        name = "ASNIssueDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnpurposeCoded:
    class Meta:
        name = "ASNPurposeCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnpurposeCodedOther:
    class Meta:
        name = "ASNPurposeCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnstatusCoded:
    class Meta:
        name = "ASNStatusCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnstatusCodedOther:
    class Meta:
        name = "ASNStatusCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsntypeCoded:
    class Meta:
        name = "ASNTypeCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsntypeCodedOther:
    class Meta:
        name = "ASNTypeCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CollectionDateOfCargo:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EarliestDeliveryDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LatestDeliveryDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleDeliveryDateAfter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleDeliveryDateBefore:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShippedDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnallowancesOrCharges:
    class Meta:
        name = "ASNAllowancesOrCharges"

    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asncurrency:
    class Meta:
        name = "ASNCurrency"

    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asndates:
    class Meta:
        name = "ASNDates"

    delivery_date: Optional[DeliveryDate] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    shipped_date: Optional[ShippedDate] = field(
        default=None,
        metadata={
            "name": "ShippedDate",
            "type": "Element",
        },
    )
    earliest_delivery_date: Optional[EarliestDeliveryDate] = field(
        default=None,
        metadata={
            "name": "EarliestDeliveryDate",
            "type": "Element",
        },
    )
    latest_delivery_date: Optional[LatestDeliveryDate] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryDate",
            "type": "Element",
        },
    )
    collection_date_of_cargo: Optional[CollectionDateOfCargo] = field(
        default=None,
        metadata={
            "name": "CollectionDateOfCargo",
            "type": "Element",
        },
    )
    schedule_delivery_date_after: Optional[ScheduleDeliveryDateAfter] = field(
        default=None,
        metadata={
            "name": "ScheduleDeliveryDateAfter",
            "type": "Element",
        },
    )
    schedule_delivery_date_before: Optional[
        ScheduleDeliveryDateBefore
    ] = field(
        default=None,
        metadata={
            "name": "ScheduleDeliveryDateBefore",
            "type": "Element",
        },
    )
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AsnheaderAttachments:
    class Meta:
        name = "ASNHeaderAttachments"

    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asnlanguage:
    class Meta:
        name = "ASNLanguage"

    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnlineItemListOfAllowOrCharge:
    class Meta:
        name = "ASNLineItemListOfAllowOrCharge"

    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnlineItemReferences:
    class Meta:
        name = "ASNLineItemReferences"

    asnreferences: Asnreferences = field(
        metadata={
            "name": "ASNReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnpackageDetail:
    class Meta:
        name = "ASNPackageDetail"

    package_detail: PackageDetail = field(
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asnparty:
    class Meta:
        name = "ASNParty"

    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnpaymentInstructions:
    class Meta:
        name = "ASNPaymentInstructions"

    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asnpurpose:
    class Meta:
        name = "ASNPurpose"

    asnpurpose_coded: AsnpurposeCoded = field(
        metadata={
            "name": "ASNPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnpurpose_coded_other: Optional[AsnpurposeCodedOther] = field(
        default=None,
        metadata={
            "name": "ASNPurposeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Asnstatus:
    class Meta:
        name = "ASNStatus"

    asnstatus_coded: AsnstatusCoded = field(
        metadata={
            "name": "ASNStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnstatus_coded_other: Optional[AsnstatusCodedOther] = field(
        default=None,
        metadata={
            "name": "ASNStatusCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Asnsummary:
    class Meta:
        name = "ASNSummary"

    number_of_lines: Optional[NumberOfLines] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    transport_packaging_totals: Optional[TransportPackagingTotals] = field(
        default=None,
        metadata={
            "name": "TransportPackagingTotals",
            "type": "Element",
        },
    )
    summary_note: Optional[SummaryNote] = field(
        default=None,
        metadata={
            "name": "SummaryNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AsntermsOfDelivery:
    class Meta:
        name = "ASNTermsOfDelivery"

    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Asntype:
    class Meta:
        name = "ASNType"

    asntype_coded: AsntypeCoded = field(
        metadata={
            "name": "ASNTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    asntype_coded_other: Optional[AsntypeCodedOther] = field(
        default=None,
        metadata={
            "name": "ASNTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LineItemOrderReference:
    purchase_order_reference: PurchaseOrderReference = field(
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReferenceToPackage:
    item_packaging_reference: ItemPackagingReference = field(
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnbaseItemDetail:
    class Meta:
        name = "ASNBaseItemDetail"

    line_item_num: LineItemNum = field(
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
        },
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: Optional[OffCatalogFlag] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
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
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    detail_response_coded: Optional[DetailResponseCoded] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
        },
    )
    detail_response_coded_other: Optional[DetailResponseCodedOther] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        },
    )
    line_item_order_reference: Optional[LineItemOrderReference] = field(
        default=None,
        metadata={
            "name": "LineItemOrderReference",
            "type": "Element",
        },
    )
    asnline_item_references: Optional[AsnlineItemReferences] = field(
        default=None,
        metadata={
            "name": "ASNLineItemReferences",
            "type": "Element",
        },
    )
    exception_quantities: Optional[ExceptionQuantities] = field(
        default=None,
        metadata={
            "name": "ExceptionQuantities",
            "type": "Element",
        },
    )
    reference_to_package: List[ReferenceToPackage] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceToPackage",
            "type": "Element",
        },
    )
    list_of_destination_ref: Optional[ListOfDestinationRef] = field(
        default=None,
        metadata={
            "name": "ListOfDestinationRef",
            "type": "Element",
        },
    )
    requested_delivery_date: Optional[RequestedDeliveryDate] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
        },
    )
    ship_by_date: Optional[ShipByDate] = field(
        default=None,
        metadata={
            "name": "ShipByDate",
            "type": "Element",
        },
    )
    other_item_dates: Optional[OtherItemDates] = field(
        default=None,
        metadata={
            "name": "OtherItemDates",
            "type": "Element",
        },
    )
    item_ship_to_party: Optional[ItemShipToParty] = field(
        default=None,
        metadata={
            "name": "ItemShipToParty",
            "type": "Element",
        },
    )
    item_ship_from_party: Optional[ItemShipFromParty] = field(
        default=None,
        metadata={
            "name": "ItemShipFromParty",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Asnheader:
    class Meta:
        name = "ASNHeader"

    asnnumber: Asnnumber = field(
        metadata={
            "name": "ASNNumber",
            "type": "Element",
            "required": True,
        }
    )
    asnissue_date: AsnissueDate = field(
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
        },
    )
    asnreferences: Optional[Asnreferences] = field(
        default=None,
        metadata={
            "name": "ASNReferences",
            "type": "Element",
        },
    )
    asnpurpose: Asnpurpose = field(
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
        },
    )
    asnstatus: Optional[Asnstatus] = field(
        default=None,
        metadata={
            "name": "ASNStatus",
            "type": "Element",
        },
    )
    asncurrency: Optional[Asncurrency] = field(
        default=None,
        metadata={
            "name": "ASNCurrency",
            "type": "Element",
        },
    )
    asnlanguage: Optional[Asnlanguage] = field(
        default=None,
        metadata={
            "name": "ASNLanguage",
            "type": "Element",
        },
    )
    asndates: Asndates = field(
        metadata={
            "name": "ASNDates",
            "type": "Element",
            "required": True,
        }
    )
    asnparty: Asnparty = field(
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
        },
    )
    asnterms_of_delivery: Optional[AsntermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "ASNTermsOfDelivery",
            "type": "Element",
        },
    )
    asnpayment_instructions: Optional[AsnpaymentInstructions] = field(
        default=None,
        metadata={
            "name": "ASNPaymentInstructions",
            "type": "Element",
        },
    )
    asnallowances_or_charges: Optional[AsnallowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "ASNAllowancesOrCharges",
            "type": "Element",
        },
    )
    asnheader_note: Optional[AsnheaderNote] = field(
        default=None,
        metadata={
            "name": "ASNHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    asnheader_attachments: Optional[AsnheaderAttachments] = field(
        default=None,
        metadata={
            "name": "ASNHeaderAttachments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAsnpackageDetail:
    class Meta:
        name = "ListOfASNPackageDetail"

    asnpackage_detail: List[AsnpackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "ASNPackageDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AsnitemDetail:
    class Meta:
        name = "ASNItemDetail"

    asnbase_item_detail: AsnbaseItemDetail = field(
        metadata={
            "name": "ASNBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    asnline_item_list_of_allow_or_charge: Optional[
        AsnlineItemListOfAllowOrCharge
    ] = field(
        default=None,
        metadata={
            "name": "ASNLineItemListOfAllowOrCharge",
            "type": "Element",
        },
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAsnitemDetail:
    class Meta:
        name = "ListOfASNItemDetail"

    asnitem_detail: List[AsnitemDetail] = field(
        default_factory=list,
        metadata={
            "name": "ASNItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Asndetail:
    class Meta:
        name = "ASNDetail"

    list_of_asnitem_detail: ListOfAsnitemDetail = field(
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
        },
    )


@dataclass(kw_only=True)
class AdvanceShipmentNotice:
    asnheader: Asnheader = field(
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
        },
    )
    asnsummary: Optional[Asnsummary] = field(
        default=None,
        metadata={
            "name": "ASNSummary",
            "type": "Element",
        },
    )
