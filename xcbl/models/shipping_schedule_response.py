from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.sourcing_result import (
    BillToParty,
    BuyerParty,
    CarrierId,
    CatalogReference,
    ConditionsOfSale,
    Contract,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    ItemPackagingReference,
    LineItemNum,
    LineItemType,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfItemReferences,
    ListOfQuantityCoded,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    ListOfTransportEquipment,
    MaxBackOrderQuantity,
    ParentItemNumber,
    Quantity,
    SellerParty,
    ShipFromParty,
    ShipToParty,
    TermsOfDelivery,
    TotalQuantity,
    TransitDirection,
    TransportMeans,
    TransportMode,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfContact,
    ListOfDimension,
    ListOfPartyCoded,
    Location,
    Party,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Identifier,
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class IdassignedBy:
    class Meta:
        name = "IDAssignedBy"

    idassigned_by_coded: str = field(
        metadata={
            "name": "IDAssignedByCoded",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_by_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDAssignedByCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderType:
    order_type_coded: str = field(
        metadata={
            "name": "OrderTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RequestedResponse:
    requested_response_coded: str = field(
        metadata={
            "name": "RequestedResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    requested_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedResponseCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ResponseType:
    response_type_coded: str = field(
        metadata={
            "name": "ResponseTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    response_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ShippingScheduleSummary:
    total_number_of_line_items: str = field(
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemQuantities:
    list_of_quantity_coded: ListOfQuantityCoded = field(
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemResourceAuthorization:
    resource_authorization_coded: str = field(
        metadata={
            "name": "ResourceAuthorizationCoded",
            "type": "Element",
            "required": True,
        }
    )
    resource_authorization_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceAuthorizationCodedOther",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class LadingQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfContract:
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class MaterialIssuerParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MessageId:
    class Meta:
        name = "MessageID"

    idnumber: str = field(
        metadata={
            "name": "IDNumber",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_by: IdassignedBy = field(
        metadata={
            "name": "IDAssignedBy",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDAssignedDate",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OtherSchedleReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ScheduleDates:
    list_of_date_coded: ListOfDateCoded = field(
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SchedulePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ScheduleQuantities:
    list_of_quantity_coded: ListOfQuantityCoded = field(
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ScheduleReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShippingScheduleResponseSummary:
    shipping_schedule_summary: ShippingScheduleSummary = field(
        metadata={
            "name": "ShippingScheduleSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    location_id: str = field(
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


@dataclass(kw_only=True)
class TransportMeansIdentifier:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportMeansReference:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContractReferences:
    list_of_contract: ListOfContract = field(
        metadata={
            "name": "ListOfContract",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EndTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InterimTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfMessageId:
    class Meta:
        name = "ListOfMessageID"

    message_id: List[MessageId] = field(
        default_factory=list,
        metadata={
            "name": "MessageID",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ScheduleParty:
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    ship_from_party: ShipFromParty = field(
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
            "required": True,
        }
    )
    ship_to_party: ShipToParty = field(
        metadata={
            "name": "ShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    material_issuer_party: Optional[MaterialIssuerParty] = field(
        default=None,
        metadata={
            "name": "MaterialIssuerParty",
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


@dataclass(kw_only=True)
class ShipScheduleDetail:
    commitment_level_coded: str = field(
        metadata={
            "name": "CommitmentLevelCoded",
            "type": "Element",
            "required": True,
        }
    )
    commitment_level_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommitmentLevelCodedOther",
            "type": "Element",
        }
    )
    schedule_dates: ScheduleDates = field(
        metadata={
            "name": "ScheduleDates",
            "type": "Element",
            "required": True,
        }
    )
    schedule_quantities: ScheduleQuantities = field(
        metadata={
            "name": "ScheduleQuantities",
            "type": "Element",
            "required": True,
        }
    )
    item_resource_authorization: Optional[ItemResourceAuthorization] = field(
        default=None,
        metadata={
            "name": "ItemResourceAuthorization",
            "type": "Element",
        }
    )
    schedule_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleNote",
            "type": "Element",
        }
    )
    route_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class StartTransportLocation:
    transport_location: TransportLocation = field(
        metadata={
            "name": "TransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ListOfShipScheduleDetail:
    ship_schedule_detail: List[ShipScheduleDetail] = field(
        default_factory=list,
        metadata={
            "name": "ShipScheduleDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderNumber:
    buyer_order_number: str = field(
        metadata={
            "name": "BuyerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
        }
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TransportLocationList:
    start_transport_location: StartTransportLocation = field(
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
    end_transport_location: EndTransportLocation = field(
        metadata={
            "name": "EndTransportLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationShipSchedule:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        }
    )
    list_of_ship_schedule_detail: ListOfShipScheduleDetail = field(
        metadata={
            "name": "ListOfShipScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ScheduleOrderReference:
    order_number: OrderNumber = field(
        metadata={
            "name": "OrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderIssueDate",
            "type": "Element",
        }
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TransportRouting:
    transport_route_id: str = field(
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
    transport_location_list: TransportLocationList = field(
        metadata={
            "name": "TransportLocationList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfLocationShipSchedule:
    location_ship_schedule: List[LocationShipSchedule] = field(
        default_factory=list,
        metadata={
            "name": "LocationShipSchedule",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfTransportRouting:
    transport_routing: List[TransportRouting] = field(
        default_factory=list,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ScheduleReferences:
    contract_references: Optional[ContractReferences] = field(
        default=None,
        metadata={
            "name": "ContractReferences",
            "type": "Element",
        }
    )
    schedule_order_reference: Optional[ScheduleOrderReference] = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        }
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )
    other_schedle_references: Optional[OtherSchedleReferences] = field(
        default=None,
        metadata={
            "name": "OtherSchedleReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemScheduleReference:
    schedule_references: ScheduleReferences = field(
        metadata={
            "name": "ScheduleReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShippingScheduleHeader:
    schedule_id: str = field(
        metadata={
            "name": "ScheduleID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_issued_date: str = field(
        metadata={
            "name": "ScheduleIssuedDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_references: Optional[ScheduleReferences] = field(
        default=None,
        metadata={
            "name": "ScheduleReferences",
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
    schedule_purpose: SchedulePurpose = field(
        metadata={
            "name": "SchedulePurpose",
            "type": "Element",
            "required": True,
        }
    )
    requested_response: Optional[RequestedResponse] = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        }
    )
    schedule_type_coded: str = field(
        metadata={
            "name": "ScheduleTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    schedule_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleTypeCodedOther",
            "type": "Element",
        }
    )
    quantity_qualifier_coded: str = field(
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCodedOther",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    schedule_party: ScheduleParty = field(
        metadata={
            "name": "ScheduleParty",
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
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    shipping_schedule_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleHeaderNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BaseShippingDetail:
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
    record_keeping_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordKeepingYear",
            "type": "Element",
        }
    )
    item_schedule_reference: Optional[ItemScheduleReference] = field(
        default=None,
        metadata={
            "name": "ItemScheduleReference",
            "type": "Element",
        }
    )
    forecast_frequency_coded: str = field(
        metadata={
            "name": "ForecastFrequencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    forecast_frequency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForecastFrequencyCodedOther",
            "type": "Element",
        }
    )
    item_quantities: Optional[ItemQuantities] = field(
        default=None,
        metadata={
            "name": "ItemQuantities",
            "type": "Element",
        }
    )
    item_release_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCoded",
            "type": "Element",
        }
    )
    item_release_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCodedOther",
            "type": "Element",
        }
    )
    item_packaging_reference: List[ItemPackagingReference] = field(
        default_factory=list,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedShippingScheduleHeader:
    shipping_schedule_header: ShippingScheduleHeader = field(
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginalShippingScheduleHeader:
    shipping_schedule_header: ShippingScheduleHeader = field(
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationShippingItemDetail:
    base_shipping_detail: BaseShippingDetail = field(
        metadata={
            "name": "BaseShippingDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_ship_schedule_detail: ListOfShipScheduleDetail = field(
        metadata={
            "name": "ListOfShipScheduleDetail",
            "type": "Element",
            "required": True,
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


@dataclass(kw_only=True)
class MaterialGroupedShippingDetail:
    base_shipping_detail: BaseShippingDetail = field(
        metadata={
            "name": "BaseShippingDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_ship_schedule: ListOfLocationShipSchedule = field(
        metadata={
            "name": "ListOfLocationShipSchedule",
            "type": "Element",
            "required": True,
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


@dataclass(kw_only=True)
class ShippingScheduleResponseHeader:
    schedule_response_id: str = field(
        metadata={
            "name": "ScheduleResponseID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_response_issue_date: str = field(
        metadata={
            "name": "ScheduleResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_reference: ScheduleReference = field(
        metadata={
            "name": "ScheduleReference",
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
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )
    response_type: ResponseType = field(
        metadata={
            "name": "ResponseType",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    original_shipping_schedule_header: Optional[OriginalShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "OriginalShippingScheduleHeader",
            "type": "Element",
        }
    )
    changed_shipping_schedule_header: Optional[ChangedShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "ChangedShippingScheduleHeader",
            "type": "Element",
        }
    )
    shipping_schedule_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseHeaderNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: MaterialGroupedShippingDetail = field(
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfLocationShippingItemDetail:
    location_shipping_item_detail: List[LocationShippingItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationShippingItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OriginalMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: MaterialGroupedShippingDetail = field(
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationGroupedShippingDetail:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        }
    )
    list_of_location_shipping_item_detail: ListOfLocationShippingItemDetail = field(
        metadata={
            "name": "ListOfLocationShippingItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MaterialGroupedShippingResponse:
    detail_response_coded: str = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_material_grouped_shipping_detail: Optional[OriginalMaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "OriginalMaterialGroupedShippingDetail",
            "type": "Element",
        }
    )
    changed_material_grouped_shipping_detail: Optional[ChangedMaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ChangedMaterialGroupedShippingDetail",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedLocationGroupedShippingDetail:
    location_grouped_shipping_detail: LocationGroupedShippingDetail = field(
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfMaterialGroupedShippingResponse:
    material_grouped_shipping_response: List[MaterialGroupedShippingResponse] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OriginalLocationGroupedShippingDetail:
    location_grouped_shipping_detail: LocationGroupedShippingDetail = field(
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationGroupedShippingResponse:
    detail_response_coded: str = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_location_grouped_shipping_detail: Optional[OriginalLocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "OriginalLocationGroupedShippingDetail",
            "type": "Element",
        }
    )
    changed_location_grouped_shipping_detail: Optional[ChangedLocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ChangedLocationGroupedShippingDetail",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfLocationGroupedShippingResponse:
    location_grouped_shipping_response: List[LocationGroupedShippingResponse] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ShippingScheduleResponse:
    shipping_schedule_response_header: ShippingScheduleResponseHeader = field(
        metadata={
            "name": "ShippingScheduleResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_shipping_response: Optional[ListOfLocationGroupedShippingResponse] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedShippingResponse",
            "type": "Element",
        }
    )
    list_of_material_grouped_shipping_response: Optional[ListOfMaterialGroupedShippingResponse] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedShippingResponse",
            "type": "Element",
        }
    )
    shipping_schedule_response_summary: Optional[ShippingScheduleResponseSummary] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseSummary",
            "type": "Element",
        }
    )
