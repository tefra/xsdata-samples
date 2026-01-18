from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.availability_to_promise_response import (
    AvailabilityShipToParty,
)
from xcbl.models.price_check_request import RequestListOfAttachment
from xcbl.models.price_check_result import (
    BuyerIdreferenceDate,
    GeneralLineItemNote,
    LineItemAttachment,
    SupplierIdreferenceDate,
    TotalNumberOfLineItem,
)
from xcbl.models.remittance_advice import SupplierParty
from xcbl.models.shipping_schedule import AccountCode
from xcbl.models.sourcing_create import DeliveryDate
from xcbl.models.sourcing_result import (
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
    ListOfQuantityCoded,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    ParentItemNumber,
    TotalQuantity,
    Transport,
)
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AvailabilityCheckRequestIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityCheckRequestNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
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
class AvailabilityCheckRequestSummary:
    total_number_of_line_item: TotalNumberOfLineItem | None = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
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
    line_item_type: LineItemType | None = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        },
    )
    parent_item_number: ParentItemNumber | None = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: ItemIdentifiers | None = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: ListOfDimension | None = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: TotalQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: MaxBackOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: ListOfQuantityCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: OffCatalogFlag | None = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: CatalogReference | None = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: ItemContractReferences | None = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: ListOfItemReferences | None = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
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
    country_of_destination: CountryOfDestination | None = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: FinalRecipient | None = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: ConditionsOfSale | None = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: HazardousMaterials | None = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    delivery_date: DeliveryDate | None = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    availability_check_request_transport: list[
        AvailabilityCheckRequestTransport
    ] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckRequestTransport",
            "type": "Element",
            "min_occurs": 1,
        },
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
    availability_check_request_issue_date: AvailabilityCheckRequestIssueDate = field(
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
    supplier_idreference_date: SupplierIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
            "type": "Element",
        },
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_idreference_date: BuyerIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        },
    )
    account_code: AccountCode | None = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        },
    )
    availability_ship_to_party: AvailabilityShipToParty = field(
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_request_language: AvailabilityCheckRequestLanguage | None = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestLanguage",
            "type": "Element",
        },
    )
    availability_check_request_note: AvailabilityCheckRequestNote | None = (
        field(
            default=None,
            metadata={
                "name": "AvailabilityCheckRequestNote",
                "type": "Element",
            },
        )
    )
    request_list_of_attachment: RequestListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "RequestListOfAttachment",
            "type": "Element",
        },
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
    general_line_item_note: GeneralLineItemNote | None = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        },
    )
    line_item_attachment: LineItemAttachment | None = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAvailabilityCheckRequestItemDetail:
    availability_check_request_item_detail: list[
        AvailabilityCheckRequestItemDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckRequestItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
    availability_check_request_detail: AvailabilityCheckRequestDetail | None = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestDetail",
            "type": "Element",
        },
    )
    availability_check_request_summary: AvailabilityCheckRequestSummary | None = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckRequestSummary",
            "type": "Element",
        },
    )
