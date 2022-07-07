from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfAttachment,
    Reference,
)
from xcbl.models.order_request import (
    BuyerParty,
    ListOfNameValueSet,
    ListOfPartyCoded,
    ListOfStructuredNote,
    SellerParty,
)
from xcbl.models.order_status_result import ErrorInfo


@dataclass
class OrderConfirmationType:
    order_confirmation_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AccountAssignment:
    account_assignment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountAssignmentID",
            "type": "Element",
            "required": True,
        }
    )
    distribution_percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributionPercentage",
            "type": "Element",
            "required": True,
        }
    )
    glaccount: Optional[str] = field(
        default=None,
        metadata={
            "name": "GLAccount",
            "type": "Element",
        }
    )
    cost_center: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostCenter",
            "type": "Element",
        }
    )
    account_assignment_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountAssignmentOrderNumber",
            "type": "Element",
        }
    )
    operation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationNumber",
            "type": "Element",
        }
    )
    sales_order_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesOrderReference",
            "type": "Element",
        }
    )
    business_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "BusinessArea",
            "type": "Element",
        }
    )
    controlling_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllingArea",
            "type": "Element",
        }
    )
    profit_center: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfitCenter",
            "type": "Element",
        }
    )
    work_breakdown_structure: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkBreakdownStructure",
            "type": "Element",
        }
    )
    network: Optional[str] = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
        }
    )
    fixed_asset: Optional[str] = field(
        default=None,
        metadata={
            "name": "FixedAsset",
            "type": "Element",
        }
    )
    fixed_asset_sub: Optional[str] = field(
        default=None,
        metadata={
            "name": "FixedAssetSub",
            "type": "Element",
        }
    )
    funds_center: Optional[str] = field(
        default=None,
        metadata={
            "name": "FundsCenter",
            "type": "Element",
        }
    )
    fund: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fund",
            "type": "Element",
        }
    )
    commitment_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommitmentItem",
            "type": "Element",
        }
    )
    functional_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "FunctionalArea",
            "type": "Element",
        }
    )
    generic_accounting: Optional[str] = field(
        default=None,
        metadata={
            "name": "GenericAccounting",
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


@dataclass
class OrderConfirmationResponseParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: Optional[SellerParty] = field(
        default=None,
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class SellerOrderConfirmationReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAccountAssignment:
    account_assignment: List[AccountAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AccountAssignment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderConfirmationResponseHeader:
    buyer_order_confirmation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerOrderConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_confirmation_reference: Optional[SellerOrderConfirmationReference] = field(
        default=None,
        metadata={
            "name": "SellerOrderConfirmationReference",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseIssueDate",
            "type": "Element",
        }
    )
    order_confirmation_type: Optional[OrderConfirmationType] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationType",
            "type": "Element",
        }
    )
    order_confirmation_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCodedOther",
            "type": "Element",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_party: Optional[OrderConfirmationResponseParty] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseHeaderNote",
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
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
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
class OrderConfirmationResponseDetail:
    order_confirmation_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    buyer_order_confirmation_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerOrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCode",
            "type": "Element",
        }
    )
    order_confirmation_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCodedOther",
            "type": "Element",
        }
    )
    list_of_account_assignment: Optional[ListOfAccountAssignment] = field(
        default=None,
        metadata={
            "name": "ListOfAccountAssignment",
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
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
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


@dataclass
class ListOfOrderConfirmationResponseDetail:
    order_confirmation_response_detail: List[OrderConfirmationResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderConfirmationResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderConfirmationResponse:
    order_confirmation_response_header: Optional[OrderConfirmationResponseHeader] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_order_confirmation_response_detail: Optional[ListOfOrderConfirmationResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfOrderConfirmationResponseDetail",
            "type": "Element",
        }
    )
