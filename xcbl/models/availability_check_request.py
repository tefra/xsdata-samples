from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfDimension,
    Reference,
    Transport,
)
from xcbl.models.availability_check_result import AvailabilityShipToParty
from xcbl.models.order_request import (
    AccountCode,
    BuyerParty,
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
    ListOfItemReferences,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    MaxBackOrderQuantity,
    ParentItemNumber,
    TotalQuantity,
)
from xcbl.models.order_status_result import LineItemAttachment
from xcbl.models.payment_request_acknowledgment import SupplierParty
from xcbl.models.price_check_request import RequestListOfAttachment


@dataclass(kw_only=True)
class AvailabilityCheckRequestSummary:
    total_number_of_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestId:
    class Meta:
        name = "AvailabilityCheckRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestTransport:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestBaseItemDetail:
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
    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        }
    )
    availability_check_request_transport: List[AvailabilityCheckRequestTransport] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckRequestTransport",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestHeader:
    availability_check_request_id: AvailabilityCheckRequestId = field(
        metadata={
            "name": "AvailabilityCheckRequestID",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_request_issue_date: str = field(
        metadata={
            "name": "AvailabilityCheckRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    supplier_party: SupplierParty = field(
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "required": True,
        }
    )
    supplier_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
            "type": "Element",
        }
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        }
    )
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        }
    )
    availability_ship_to_party: AvailabilityShipToParty = field(
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_request_language: Optional[AvailabilityCheckRequestLanguage] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestLanguage",
            "type": "Element",
        }
    )
    availability_check_request_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestNote",
            "type": "Element",
        }
    )
    request_list_of_attachment: Optional[RequestListOfAttachment] = field(
        default=None,
        metadata={
            "name": "RequestListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestItemDetail:
    availability_check_request_base_item_detail: AvailabilityCheckRequestBaseItemDetail = field(
        metadata={
            "name": "AvailabilityCheckRequestBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    general_line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
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


@dataclass(kw_only=True)
class ListOfAvailabilityCheckRequestItemDetail:
    availability_check_request_item_detail: List[AvailabilityCheckRequestItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckRequestItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestDetail:
    list_of_availability_check_request_item_detail: ListOfAvailabilityCheckRequestItemDetail = field(
        metadata={
            "name": "ListOfAvailabilityCheckRequestItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequest:
    availability_check_request_header: AvailabilityCheckRequestHeader = field(
        metadata={
            "name": "AvailabilityCheckRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_request_detail: Optional[AvailabilityCheckRequestDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestDetail",
            "type": "Element",
        }
    )
    availability_check_request_summary: Optional[AvailabilityCheckRequestSummary] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestSummary",
            "type": "Element",
        }
    )
