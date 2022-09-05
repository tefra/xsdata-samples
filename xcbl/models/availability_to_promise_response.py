from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfReferenceCoded,
    Reference,
    Transport,
)
from xcbl.models.availability_check_result import AvailabilityShipToParty
from xcbl.models.availability_to_promise import (
    AtpcheckType,
    Atpresponse,
    AvailabilityDeliveryOption,
    AvailabilityToPromisePurpose,
    RespondingParty,
)
from xcbl.models.goods_receipt import TransportRouting
from xcbl.models.order_request import BaseItemDetail


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseDeliveryOption:
    availability_delivery_option: AvailabilityDeliveryOption = field(
        metadata={
            "name": "AvailabilityDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseHeaderTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseId:
    class Meta:
        name = "AvailabilityResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityResponseListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseId:
    class Meta:
        name = "AvailabilityToPromiseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseItemResponse:
    availability_to_promise_purpose: AvailabilityToPromisePurpose = field(
        metadata={
            "name": "AvailabilityToPromisePurpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseBaseItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseTransportDetail:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseHeader:
    availability_response_id: AvailabilityResponseId = field(
        metadata={
            "name": "AvailabilityResponseID",
            "type": "Element",
            "required": True,
        }
    )
    availability_response_issue_date: str = field(
        metadata={
            "name": "AvailabilityResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_id: AvailabilityToPromiseId = field(
        metadata={
            "name": "AvailabilityToPromiseID",
            "type": "Element",
            "required": True,
        }
    )
    atpresponse: Atpresponse = field(
        metadata={
            "name": "ATPResponse",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    availability_response_delivery_option: AvailabilityResponseDeliveryOption = field(
        metadata={
            "name": "AvailabilityResponseDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type: Optional[AtpcheckType] = field(
        default=None,
        metadata={
            "name": "ATPCheckType",
            "type": "Element",
        }
    )
    initiating_party: InitiatingParty = field(
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
            "required": True,
        }
    )
    responding_party: Optional[RespondingParty] = field(
        default=None,
        metadata={
            "name": "RespondingParty",
            "type": "Element",
        }
    )
    availability_ship_to_party: Optional[AvailabilityShipToParty] = field(
        default=None,
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
        }
    )
    availability_response_header_transport: Optional[AvailabilityResponseHeaderTransport] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseHeaderTransport",
            "type": "Element",
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
    availability_response_list_of_attachment: Optional[AvailabilityResponseListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseItemDetail:
    availability_to_promise_item_response: Optional[AvailabilityToPromiseItemResponse] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseItemResponse",
            "type": "Element",
        }
    )
    availability_to_promise_response_base_item_detail: AvailabilityToPromiseResponseBaseItemDetail = field(
        metadata={
            "name": "AvailabilityToPromiseResponseBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_delivery_detail: Optional[AvailabilityToPromiseResponseDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseDeliveryDetail",
            "type": "Element",
        }
    )
    availability_to_promise_response_transport_detail: Optional[AvailabilityToPromiseResponseTransportDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseTransportDetail",
            "type": "Element",
        }
    )
    availability_to_promise_response_item_list_of_attachment: Optional[AvailabilityToPromiseResponseItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseItemListOfAttachment",
            "type": "Element",
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAvailabilityToPromiseResponseItemDetail:
    availability_to_promise_response_item_detail: List[AvailabilityToPromiseResponseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityToPromiseResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponseDetail:
    list_of_availability_to_promise_response_item_detail: Optional[ListOfAvailabilityToPromiseResponseItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityToPromiseResponseItemDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AvailabilityToPromiseResponse:
    availability_to_promise_response_header: AvailabilityToPromiseResponseHeader = field(
        metadata={
            "name": "AvailabilityToPromiseResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_detail: Optional[AvailabilityToPromiseResponseDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseDetail",
            "type": "Element",
        }
    )
    availability_to_promise_response_summary: Optional[AvailabilityToPromiseResponseSummary] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseSummary",
            "type": "Element",
        }
    )
