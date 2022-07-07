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


@dataclass
class AvailabilityToPromiseResponseSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityResponseDeliveryOption:
    availability_delivery_option: Optional[AvailabilityDeliveryOption] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOption",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityResponseHeaderTransport:
    transport_routing: Optional[TransportRouting] = field(
        default=None,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityResponseId:
    class Meta:
        name = "AvailabilityResponseID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityResponseListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseId:
    class Meta:
        name = "AvailabilityToPromiseID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseItemResponse:
    availability_to_promise_purpose: Optional[AvailabilityToPromisePurpose] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseResponseBaseItemDetail:
    base_item_detail: Optional[BaseItemDetail] = field(
        default=None,
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseResponseDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseResponseItemListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseResponseTransportDetail:
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseResponseHeader:
    availability_response_id: Optional[AvailabilityResponseId] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseID",
            "type": "Element",
            "required": True,
        }
    )
    availability_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_id: Optional[AvailabilityToPromiseId] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseID",
            "type": "Element",
            "required": True,
        }
    )
    atpresponse: Optional[Atpresponse] = field(
        default=None,
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
    availability_response_delivery_option: Optional[AvailabilityResponseDeliveryOption] = field(
        default=None,
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
    initiating_party: Optional[InitiatingParty] = field(
        default=None,
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


@dataclass
class AvailabilityToPromiseResponseItemDetail:
    availability_to_promise_item_response: Optional[AvailabilityToPromiseItemResponse] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseItemResponse",
            "type": "Element",
        }
    )
    availability_to_promise_response_base_item_detail: Optional[AvailabilityToPromiseResponseBaseItemDetail] = field(
        default=None,
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


@dataclass
class ListOfAvailabilityToPromiseResponseItemDetail:
    availability_to_promise_response_item_detail: List[AvailabilityToPromiseResponseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityToPromiseResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AvailabilityToPromiseResponseDetail:
    list_of_availability_to_promise_response_item_detail: Optional[ListOfAvailabilityToPromiseResponseItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityToPromiseResponseItemDetail",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityToPromiseResponse:
    availability_to_promise_response_header: Optional[AvailabilityToPromiseResponseHeader] = field(
        default=None,
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
