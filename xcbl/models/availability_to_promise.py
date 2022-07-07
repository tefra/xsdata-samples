from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfReferenceCoded,
    Party,
    Reference,
    Transport,
)
from xcbl.models.availability_check_result import AvailabilityShipToParty
from xcbl.models.goods_receipt import TransportRouting
from xcbl.models.order_request import BaseItemDetail


@dataclass
class AtpcheckType:
    class Meta:
        name = "ATPCheckType"

    atpcheck_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATPCheckTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    atpcheck_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATPCheckTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Atpresponse:
    class Meta:
        name = "ATPResponse"

    availability_to_promise_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseResponseCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityDeliveryOption:
    availability_delivery_option_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOptionCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_delivery_option_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOptionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityToPromisePurpose:
    availability_to_promise_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityToPromiseSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityId:
    class Meta:
        name = "AvailabilityID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseBaseItemDetail:
    base_item_detail: Optional[BaseItemDetail] = field(
        default=None,
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseHeaderTransport:
    transport_routing: Optional[TransportRouting] = field(
        default=None,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseItemListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseTransportDetail:
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RespondingParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityToPromiseHeader:
    availability_id: Optional[AvailabilityId] = field(
        default=None,
        metadata={
            "name": "AvailabilityID",
            "type": "Element",
            "required": True,
        }
    )
    availability_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityIssueDate",
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
    availability_to_promise_purpose: Optional[AvailabilityToPromisePurpose] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromisePurpose",
            "type": "Element",
            "required": True,
        }
    )
    availability_delivery_option: Optional[AvailabilityDeliveryOption] = field(
        default=None,
        metadata={
            "name": "AvailabilityDeliveryOption",
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
    atpresponse: Optional[Atpresponse] = field(
        default=None,
        metadata={
            "name": "ATPResponse",
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
    availability_to_promise_header_transport: Optional[AvailabilityToPromiseHeaderTransport] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseHeaderTransport",
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
    availability_to_promise_list_of_attachment: Optional[AvailabilityToPromiseListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityToPromiseItemDetail:
    availability_to_promise_base_item_detail: Optional[AvailabilityToPromiseBaseItemDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_delivery_detail: Optional[AvailabilityToPromiseDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseDeliveryDetail",
            "type": "Element",
        }
    )
    availability_to_promise_transport_detail: Optional[AvailabilityToPromiseTransportDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseTransportDetail",
            "type": "Element",
        }
    )
    availability_to_promise_item_list_of_attachment: Optional[AvailabilityToPromiseItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseItemListOfAttachment",
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
class ListOfAvailabilityToPromiseItemDetail:
    availability_to_promise_item_detail: List[AvailabilityToPromiseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityToPromiseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AvailabilityToPromiseDetail:
    list_of_availability_to_promise_item_detail: Optional[ListOfAvailabilityToPromiseItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityToPromiseItemDetail",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityToPromise:
    availability_to_promise_header: Optional[AvailabilityToPromiseHeader] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_to_promise_detail: Optional[AvailabilityToPromiseDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseDetail",
            "type": "Element",
        }
    )
    availability_to_promise_summary: Optional[AvailabilityToPromiseSummary] = field(
        default=None,
        metadata={
            "name": "AvailabilityToPromiseSummary",
            "type": "Element",
        }
    )
