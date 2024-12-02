from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.sourcing_result import (
    BillToParty,
    BuyerParty,
    CarrierId,
    CarrierName,
    CatalogReference,
    ConditionsOfSale,
    Contract,
    CountryOfDestination,
    CountryOfOrigin,
    CustShippingContractNum,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    ItemPackagingReference,
    LineItemNote,
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
    OffCatalogFlag,
    ParentItemNumber,
    Quantity,
    QuantityQualifierCoded,
    QuantityQualifierCodedOther,
    SellerParty,
    ServiceLevelCoded,
    ServiceLevelCodedOther,
    ShipFromParty,
    ShippingInstructions,
    ShipToParty,
    TermsOfDelivery,
    TotalQuantity,
    TransitDirection,
    TransportLegCoded,
    TransportLegCodedOther,
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
class ActualArrivalDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ActualDepartureDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerOrderNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommitmentLevelCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommitmentLevelCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DetailResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DetailResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EstimatedArrivalDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EstimatedDepartureDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ForecastFrequencyCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ForecastFrequencyCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IdassignedByCoded:
    class Meta:
        name = "IDAssignedByCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IdassignedByCodedOther:
    class Meta:
        name = "IDAssignedByCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IdassignedDate:
    class Meta:
        name = "IDAssignedDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Idnumber:
    class Meta:
        name = "IDNumber"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemReleaseStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemReleaseStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocationId:
    class Meta:
        name = "LocationID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RecordKeepingYear:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReleaseNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestedResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestedResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ResourceAuthorizationCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ResourceAuthorizationCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ResponseTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ResponseTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RouteId:
    class Meta:
        name = "RouteID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleId:
    class Meta:
        name = "ScheduleID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleIssuedDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleResponseId:
    class Meta:
        name = "ScheduleResponseID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ScheduleTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SellerOrderNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Sequence:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ServiceLevelReasonCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ServiceLevelReasonCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ServiceLevelResponsibilityCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ServiceLevelResponsibilityCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShippingScheduleHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShippingScheduleResponseHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumberOfLineItems:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TransportRequirementCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TransportRequirementCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TransportRouteId:
    class Meta:
        name = "TransportRouteID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IdassignedBy:
    class Meta:
        name = "IDAssignedBy"

    idassigned_by_coded: IdassignedByCoded = field(
        metadata={
            "name": "IDAssignedByCoded",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_by_coded_other: Optional[IdassignedByCodedOther] = field(
        default=None,
        metadata={
            "name": "IDAssignedByCodedOther",
            "type": "Element",
        },
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
    resource_authorization_coded: ResourceAuthorizationCoded = field(
        metadata={
            "name": "ResourceAuthorizationCoded",
            "type": "Element",
            "required": True,
        }
    )
    resource_authorization_coded_other: Optional[
        ResourceAuthorizationCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ResourceAuthorizationCodedOther",
            "type": "Element",
        },
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        },
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
    contract: list[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "min_occurs": 1,
        },
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
class OrderType:
    order_type_coded: OrderTypeCoded = field(
        metadata={
            "name": "OrderTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_type_coded_other: Optional[OrderTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "OrderTypeCodedOther",
            "type": "Element",
        },
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
class RequestedResponse:
    requested_response_coded: RequestedResponseCoded = field(
        metadata={
            "name": "RequestedResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    requested_response_coded_other: Optional[RequestedResponseCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "RequestedResponseCodedOther",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ResponseType:
    response_type_coded: ResponseTypeCoded = field(
        metadata={
            "name": "ResponseTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    response_type_coded_other: Optional[ResponseTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "ResponseTypeCodedOther",
            "type": "Element",
        },
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
class ServiceLevel:
    service_level_coded: Optional[ServiceLevelCoded] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCoded",
            "type": "Element",
        },
    )
    service_level_coded_other: Optional[ServiceLevelCodedOther] = field(
        default=None,
        metadata={
            "name": "ServiceLevelCodedOther",
            "type": "Element",
        },
    )
    service_level_reason_coded: Optional[ServiceLevelReasonCoded] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCoded",
            "type": "Element",
        },
    )
    service_level_reason_coded_other: Optional[
        ServiceLevelReasonCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ServiceLevelReasonCodedOther",
            "type": "Element",
        },
    )
    service_level_responsibility_coded: Optional[
        ServiceLevelResponsibilityCoded
    ] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCoded",
            "type": "Element",
        },
    )
    service_level_responsibility_coded_other: Optional[
        ServiceLevelResponsibilityCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ServiceLevelResponsibilityCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ShippingScheduleSummary:
    total_number_of_line_items: TotalNumberOfLineItems = field(
        metadata={
            "name": "TotalNumberOfLineItems",
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
    location_id: LocationId = field(
        metadata={
            "name": "LocationID",
            "type": "Element",
            "required": True,
        }
    )
    sequence: Optional[Sequence] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        },
    )
    estimated_arrival_date: Optional[EstimatedArrivalDate] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalDate",
            "type": "Element",
        },
    )
    actual_arrival_date: Optional[ActualArrivalDate] = field(
        default=None,
        metadata={
            "name": "ActualArrivalDate",
            "type": "Element",
        },
    )
    estimated_departure_date: Optional[EstimatedDepartureDate] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureDate",
            "type": "Element",
        },
    )
    actual_departure_date: Optional[ActualDepartureDate] = field(
        default=None,
        metadata={
            "name": "ActualDepartureDate",
            "type": "Element",
        },
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
class MessageId:
    class Meta:
        name = "MessageID"

    idnumber: Idnumber = field(
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
    idassigned_date: Optional[IdassignedDate] = field(
        default=None,
        metadata={
            "name": "IDAssignedDate",
            "type": "Element",
        },
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
        },
    )
    material_issuer_party: Optional[MaterialIssuerParty] = field(
        default=None,
        metadata={
            "name": "MaterialIssuerParty",
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


@dataclass(kw_only=True)
class ShipScheduleDetail:
    commitment_level_coded: CommitmentLevelCoded = field(
        metadata={
            "name": "CommitmentLevelCoded",
            "type": "Element",
            "required": True,
        }
    )
    commitment_level_coded_other: Optional[CommitmentLevelCodedOther] = field(
        default=None,
        metadata={
            "name": "CommitmentLevelCodedOther",
            "type": "Element",
        },
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
        },
    )
    schedule_note: Optional[ScheduleNote] = field(
        default=None,
        metadata={
            "name": "ScheduleNote",
            "type": "Element",
        },
    )
    route_id: Optional[RouteId] = field(
        default=None,
        metadata={
            "name": "RouteID",
            "type": "Element",
        },
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
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfMessageId:
    class Meta:
        name = "ListOfMessageID"

    message_id: list[MessageId] = field(
        default_factory=list,
        metadata={
            "name": "MessageID",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfShipScheduleDetail:
    ship_schedule_detail: list[ShipScheduleDetail] = field(
        default_factory=list,
        metadata={
            "name": "ShipScheduleDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
    interim_transport_location: list[InterimTransportLocation] = field(
        default_factory=list,
        metadata={
            "name": "InterimTransportLocation",
            "type": "Element",
        },
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
        },
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        },
    )
    list_of_ship_schedule_detail: ListOfShipScheduleDetail = field(
        metadata={
            "name": "ListOfShipScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderNumber:
    buyer_order_number: BuyerOrderNumber = field(
        metadata={
            "name": "BuyerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[SellerOrderNumber] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
        },
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TransportRouting:
    transport_route_id: TransportRouteId = field(
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
        },
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
        },
    )
    transport_means_identifier: Optional[TransportMeansIdentifier] = field(
        default=None,
        metadata={
            "name": "TransportMeansIdentifier",
            "type": "Element",
        },
    )
    transport_means_reference: Optional[TransportMeansReference] = field(
        default=None,
        metadata={
            "name": "TransportMeansReference",
            "type": "Element",
        },
    )
    transport_requirement_coded: Optional[TransportRequirementCoded] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCoded",
            "type": "Element",
        },
    )
    transport_requirement_coded_other: Optional[
        TransportRequirementCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TransportRequirementCodedOther",
            "type": "Element",
        },
    )
    carrier_name: Optional[CarrierName] = field(
        default=None,
        metadata={
            "name": "CarrierName",
            "type": "Element",
        },
    )
    carrier_id: Optional[CarrierId] = field(
        default=None,
        metadata={
            "name": "CarrierID",
            "type": "Element",
        },
    )
    transport_quantities: Optional[TransportQuantities] = field(
        default=None,
        metadata={
            "name": "TransportQuantities",
            "type": "Element",
        },
    )
    cust_shipping_contract_num: Optional[CustShippingContractNum] = field(
        default=None,
        metadata={
            "name": "CustShippingContractNum",
            "type": "Element",
        },
    )
    service_level: Optional[ServiceLevel] = field(
        default=None,
        metadata={
            "name": "ServiceLevel",
            "type": "Element",
        },
    )
    shipping_instructions: Optional[ShippingInstructions] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        },
    )
    transport_leg_coded: Optional[TransportLegCoded] = field(
        default=None,
        metadata={
            "name": "TransportLegCoded",
            "type": "Element",
        },
    )
    transport_leg_coded_other: Optional[TransportLegCodedOther] = field(
        default=None,
        metadata={
            "name": "TransportLegCodedOther",
            "type": "Element",
        },
    )
    list_of_transport_equipment: Optional[ListOfTransportEquipment] = field(
        default=None,
        metadata={
            "name": "ListOfTransportEquipment",
            "type": "Element",
        },
    )
    transit_direction: Optional[TransitDirection] = field(
        default=None,
        metadata={
            "name": "TransitDirection",
            "type": "Element",
        },
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
    location_ship_schedule: list[LocationShipSchedule] = field(
        default_factory=list,
        metadata={
            "name": "LocationShipSchedule",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfTransportRouting:
    transport_routing: list[TransportRouting] = field(
        default_factory=list,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "min_occurs": 1,
        },
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
    order_issue_date: Optional[OrderIssueDate] = field(
        default=None,
        metadata={
            "name": "OrderIssueDate",
            "type": "Element",
        },
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ScheduleReferences:
    contract_references: Optional[ContractReferences] = field(
        default=None,
        metadata={
            "name": "ContractReferences",
            "type": "Element",
        },
    )
    schedule_order_reference: Optional[ScheduleOrderReference] = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        },
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        },
    )
    other_schedle_references: Optional[OtherSchedleReferences] = field(
        default=None,
        metadata={
            "name": "OtherSchedleReferences",
            "type": "Element",
        },
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
    schedule_id: ScheduleId = field(
        metadata={
            "name": "ScheduleID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_issued_date: ScheduleIssuedDate = field(
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
        },
    )
    release_number: Optional[ReleaseNumber] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        },
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
        },
    )
    schedule_type_coded: ScheduleTypeCoded = field(
        metadata={
            "name": "ScheduleTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    schedule_type_coded_other: Optional[ScheduleTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "ScheduleTypeCodedOther",
            "type": "Element",
        },
    )
    quantity_qualifier_coded: QuantityQualifierCoded = field(
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[QuantityQualifierCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "QuantityQualifierCodedOther",
                "type": "Element",
            },
        )
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        },
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
        },
    )
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
        },
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    shipping_schedule_header_note: Optional[ShippingScheduleHeaderNote] = (
        field(
            default=None,
            metadata={
                "name": "ShippingScheduleHeaderNote",
                "type": "Element",
            },
        )
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
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
    record_keeping_year: Optional[RecordKeepingYear] = field(
        default=None,
        metadata={
            "name": "RecordKeepingYear",
            "type": "Element",
        },
    )
    item_schedule_reference: Optional[ItemScheduleReference] = field(
        default=None,
        metadata={
            "name": "ItemScheduleReference",
            "type": "Element",
        },
    )
    forecast_frequency_coded: ForecastFrequencyCoded = field(
        metadata={
            "name": "ForecastFrequencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    forecast_frequency_coded_other: Optional[ForecastFrequencyCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "ForecastFrequencyCodedOther",
                "type": "Element",
            },
        )
    )
    item_quantities: Optional[ItemQuantities] = field(
        default=None,
        metadata={
            "name": "ItemQuantities",
            "type": "Element",
        },
    )
    item_release_status_coded: Optional[ItemReleaseStatusCoded] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCoded",
            "type": "Element",
        },
    )
    item_release_status_coded_other: Optional[ItemReleaseStatusCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "ItemReleaseStatusCodedOther",
                "type": "Element",
            },
        )
    )
    item_packaging_reference: list[ItemPackagingReference] = field(
        default_factory=list,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        },
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


@dataclass(kw_only=True)
class ShippingScheduleResponseHeader:
    schedule_response_id: ScheduleResponseId = field(
        metadata={
            "name": "ScheduleResponseID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_response_issue_date: ScheduleResponseIssueDate = field(
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
        },
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
    original_shipping_schedule_header: Optional[
        OriginalShippingScheduleHeader
    ] = field(
        default=None,
        metadata={
            "name": "OriginalShippingScheduleHeader",
            "type": "Element",
        },
    )
    changed_shipping_schedule_header: Optional[
        ChangedShippingScheduleHeader
    ] = field(
        default=None,
        metadata={
            "name": "ChangedShippingScheduleHeader",
            "type": "Element",
        },
    )
    shipping_schedule_response_header_note: Optional[
        ShippingScheduleResponseHeaderNote
    ] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseHeaderNote",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
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
    location_shipping_item_detail: list[LocationShippingItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationShippingItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
        },
    )
    list_of_location_shipping_item_detail: ListOfLocationShippingItemDetail = (
        field(
            metadata={
                "name": "ListOfLocationShippingItemDetail",
                "type": "Element",
                "required": True,
            }
        )
    )


@dataclass(kw_only=True)
class MaterialGroupedShippingResponse:
    detail_response_coded: DetailResponseCoded = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[DetailResponseCodedOther] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        },
    )
    original_material_grouped_shipping_detail: Optional[
        OriginalMaterialGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "OriginalMaterialGroupedShippingDetail",
            "type": "Element",
        },
    )
    changed_material_grouped_shipping_detail: Optional[
        ChangedMaterialGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "ChangedMaterialGroupedShippingDetail",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
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
    material_grouped_shipping_response: list[
        MaterialGroupedShippingResponse
    ] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        },
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
    detail_response_coded: DetailResponseCoded = field(
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[DetailResponseCodedOther] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        },
    )
    original_location_grouped_shipping_detail: Optional[
        OriginalLocationGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "OriginalLocationGroupedShippingDetail",
            "type": "Element",
        },
    )
    changed_location_grouped_shipping_detail: Optional[
        ChangedLocationGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "ChangedLocationGroupedShippingDetail",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfLocationGroupedShippingResponse:
    location_grouped_shipping_response: list[
        LocationGroupedShippingResponse
    ] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        },
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
    list_of_location_grouped_shipping_response: Optional[
        ListOfLocationGroupedShippingResponse
    ] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedShippingResponse",
            "type": "Element",
        },
    )
    list_of_material_grouped_shipping_response: Optional[
        ListOfMaterialGroupedShippingResponse
    ] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedShippingResponse",
            "type": "Element",
        },
    )
    shipping_schedule_response_summary: Optional[
        ShippingScheduleResponseSummary
    ] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseSummary",
            "type": "Element",
        },
    )
