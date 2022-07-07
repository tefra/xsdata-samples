from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    CarrierId,
    Identifier,
    ItemPackagingReference,
    Language,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfReferenceCoded,
    ListOfTransportEquipment,
    Location,
    Party,
    Purpose,
    Quantity,
    Reference,
    TermsOfDelivery,
    TransitDirection,
    TransportMeans,
    TransportMode,
)
from xcbl.models.order_request import (
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfNameValueSet,
    ListOfPackageDetail,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    ParentItemNumber,
)
from xcbl.models.planning_schedule import (
    ScheduleOrderReference,
    ScheduleParty,
)


@dataclass
class DestinationRef:
    route_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteID",
            "type": "Element",
            "required": True,
        }
    )
    location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsCondition:
    element_identifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCoded",
            "type": "Element",
        }
    )
    element_identifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementIdentifierCodedOther",
            "type": "Element",
        }
    )
    identifying_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifyingReference",
            "type": "Element",
        }
    )
    delivery_stage_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierCoded",
            "type": "Element",
        }
    )
    delivery_stage_qualifier_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryStageQualifierOther",
            "type": "Element",
        }
    )
    goods_condition_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsConditionCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_condition_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsConditionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ServiceLevel:
    service_level_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCoded",
            "type": "Element",
        }
    )
    service_level_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCodedOther",
            "type": "Element",
        }
    )
    service_level_reason_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCoded",
            "type": "Element",
        }
    )
    service_level_reason_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCodedOther",
            "type": "Element",
        }
    )
    service_level_responsibility_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCoded",
            "type": "Element",
        }
    )
    service_level_responsibility_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCodedOther",
            "type": "Element",
        }
    )


@dataclass
class Asnreference:
    class Meta:
        name = "ASNReference"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptOrderReference:
    schedule_order_reference: Optional[ScheduleOrderReference] = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        }
    )
    release_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        }
    )
    change_order_sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderSequenceNumber",
            "type": "Element",
        }
    )


@dataclass
class GoodsReceiptParty:
    schedule_party: Optional[ScheduleParty] = field(
        default=None,
        metadata={
            "name": "ScheduleParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptPurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemShipFromParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemShipToParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LadingQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LineItemGoodsCondition:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )
    goods_condition: Optional[GoodsCondition] = field(
        default=None,
        metadata={
            "name": "GoodsCondition",
            "type": "Element",
            "required": True,
        }
    )
    discrepancy_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscrepancyCoded",
            "type": "Element",
        }
    )
    discrepancy_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscrepancyCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ListOfDestinationRef:
    destination_ref: List[DestinationRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfGoodsCondition:
    goods_condition: List[GoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "GoodsCondition",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfGoodsReceiptPackageDetail:
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OtherItemDates:
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuantityDifference:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuantityReceived:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuantityShipped:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TransportLocation:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        }
    )
    estimated_arrival_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalDate",
            "type": "Element",
        }
    )
    actual_arrival_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualArrivalDate",
            "type": "Element",
        }
    )
    estimated_departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureDate",
            "type": "Element",
        }
    )
    actual_departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualDepartureDate",
            "type": "Element",
        }
    )


@dataclass
class TransportMeansIdentifier:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TransportMeansReference:
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EndTransportLocation:
    transport_location: Optional[TransportLocation] = field(
        default=None,
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptDeliveryDetail:
    item_packaging_reference: Optional[ItemPackagingReference] = field(
        default=None,
        metadata={
            "name": "ItemPackagingReference",
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
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        }
    )


@dataclass
class GoodsReceiptItemOrderReference:
    goods_receipt_order_reference: Optional[GoodsReceiptOrderReference] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptOrderReference",
            "type": "Element",
            "required": True,
        }
    )
    purchase_order_line_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderLineItemNumber",
            "type": "Element",
        }
    )


@dataclass
class InterimTransportLocation:
    transport_location: Optional[TransportLocation] = field(
        default=None,
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfGoodsReceiptOrderReference:
    goods_receipt_order_reference: List[GoodsReceiptOrderReference] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptOrderReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfLineItemGoodsCondition:
    line_item_goods_condition: List[LineItemGoodsCondition] = field(
        default_factory=list,
        metadata={
            "name": "LineItemGoodsCondition",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class StartTransportLocation:
    transport_location: Optional[TransportLocation] = field(
        default=None,
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TransportQuantities:
    lading_quantity: Optional[LadingQuantity] = field(
        default=None,
        metadata={
            "name": "LadingQuantity",
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


@dataclass
class GoodsReceiptReferences:
    asnreference: Optional[Asnreference] = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        }
    )
    list_of_goods_receipt_order_reference: Optional[ListOfGoodsReceiptOrderReference] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptOrderReference",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )


@dataclass
class ListOfGoodsReceiptItemOrderReference:
    goods_receipt_item_order_reference: List[GoodsReceiptItemOrderReference] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemOrderReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TransportLocationList:
    start_transport_location: Optional[StartTransportLocation] = field(
        default=None,
        metadata={
            "name": "StartTransportLocation",
            "type": "Element",
            "required": True,
        }
    )
    interim_transport_location: List[InterimTransportLocation] = field(
        default_factory=list,
        metadata={
            "name": "InterimTransportLocation",
            "type": "Element",
        }
    )
    end_transport_location: Optional[EndTransportLocation] = field(
        default=None,
        metadata={
            "name": "EndTransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptLineItemReferences:
    asnreference: Optional[Asnreference] = field(
        default=None,
        metadata={
            "name": "ASNReference",
            "type": "Element",
        }
    )
    asnline_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNLineItemNumber",
            "type": "Element",
        }
    )
    list_of_goods_receipt_item_order_reference: Optional[ListOfGoodsReceiptItemOrderReference] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptItemOrderReference",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )


@dataclass
class TransportRouting:
    transport_route_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportRouteID",
            "type": "Element",
            "required": True,
        }
    )
    transport_mode: Optional[TransportMode] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
        }
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
        }
    )
    transport_means_identifier: Optional[TransportMeansIdentifier] = field(
        default=None,
        metadata={
            "name": "TransportMeansIdentifier",
            "type": "Element",
        }
    )
    transport_means_reference: Optional[TransportMeansReference] = field(
        default=None,
        metadata={
            "name": "TransportMeansReference",
            "type": "Element",
        }
    )
    transport_requirement_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCoded",
            "type": "Element",
        }
    )
    transport_requirement_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCodedOther",
            "type": "Element",
        }
    )
    carrier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierName",
            "type": "Element",
        }
    )
    carrier_id: Optional[CarrierId] = field(
        default=None,
        metadata={
            "name": "CarrierID",
            "type": "Element",
        }
    )
    transport_quantities: Optional[TransportQuantities] = field(
        default=None,
        metadata={
            "name": "TransportQuantities",
            "type": "Element",
        }
    )
    cust_shipping_contract_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustShippingContractNum",
            "type": "Element",
        }
    )
    service_level: Optional[ServiceLevel] = field(
        default=None,
        metadata={
            "name": "ServiceLevel",
            "type": "Element",
        }
    )
    shipping_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        }
    )
    transport_leg_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCoded",
            "type": "Element",
        }
    )
    transport_leg_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportLegCodedOther",
            "type": "Element",
        }
    )
    list_of_transport_equipment: Optional[ListOfTransportEquipment] = field(
        default=None,
        metadata={
            "name": "ListOfTransportEquipment",
            "type": "Element",
        }
    )
    transit_direction: Optional[TransitDirection] = field(
        default=None,
        metadata={
            "name": "TransitDirection",
            "type": "Element",
        }
    )
    transport_location_list: Optional[TransportLocationList] = field(
        default=None,
        metadata={
            "name": "TransportLocationList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GoodsReceiptItemDetail:
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
            "required": True,
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
            "required": True,
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
            "required": True,
        }
    )
    quantity_shipped: Optional[QuantityShipped] = field(
        default=None,
        metadata={
            "name": "QuantityShipped",
            "type": "Element",
            "required": True,
        }
    )
    quantity_received: Optional[QuantityReceived] = field(
        default=None,
        metadata={
            "name": "QuantityReceived",
            "type": "Element",
            "required": True,
        }
    )
    quantity_difference: Optional[QuantityDifference] = field(
        default=None,
        metadata={
            "name": "QuantityDifference",
            "type": "Element",
        }
    )
    list_of_line_item_goods_condition: Optional[ListOfLineItemGoodsCondition] = field(
        default=None,
        metadata={
            "name": "ListOfLineItemGoodsCondition",
            "type": "Element",
        }
    )
    unacceptable_packaging: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnacceptablePackaging",
            "type": "Element",
        }
    )
    goods_receipt_line_item_references: Optional[GoodsReceiptLineItemReferences] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptLineItemReferences",
            "type": "Element",
        }
    )
    goods_receipt_delivery_detail: Optional[GoodsReceiptDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDeliveryDetail",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )
    goods_receipt_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetailNote",
            "type": "Element",
        }
    )


@dataclass
class ListOfTransportRouting:
    transport_routing: List[TransportRouting] = field(
        default_factory=list,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GoodsReceiptHeader:
    goods_receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptID",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_purpose: Optional[GoodsReceiptPurpose] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptPurpose",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_goods_condition: Optional[ListOfGoodsCondition] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsCondition",
            "type": "Element",
        }
    )
    goods_receipt_references: Optional[GoodsReceiptReferences] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptReferences",
            "type": "Element",
        }
    )
    delivery_complete: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryComplete",
            "type": "Element",
        }
    )
    goods_receipt_language: Optional[GoodsReceiptLanguage] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptLanguage",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_party: Optional[GoodsReceiptParty] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptParty",
            "type": "Element",
            "required": True,
        }
    )
    terms_of_delivery: List[TermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        }
    )
    list_of_transport_routing: Optional[ListOfTransportRouting] = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        }
    )
    goods_receipt_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptHeaderNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfGoodsReceiptItemDetail:
    goods_receipt_item_detail: List[GoodsReceiptItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "GoodsReceiptItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GoodsReceiptDetail:
    list_of_goods_receipt_item_detail: Optional[ListOfGoodsReceiptItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_goods_receipt_package_detail: Optional[ListOfGoodsReceiptPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfGoodsReceiptPackageDetail",
            "type": "Element",
        }
    )


@dataclass
class GoodsReceipt:
    goods_receipt_header: Optional[GoodsReceiptHeader] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptHeader",
            "type": "Element",
            "required": True,
        }
    )
    goods_receipt_detail: Optional[GoodsReceiptDetail] = field(
        default=None,
        metadata={
            "name": "GoodsReceiptDetail",
            "type": "Element",
        }
    )
