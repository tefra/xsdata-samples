from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.price_check_result import ErrorInfo
from xcbl.models.remittance_advice import (
    FixedAsset,
    WorkBreakdownStructure,
)
from xcbl.models.sourcing_result import (
    BuyerParty,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfStructuredNote,
    SellerParty,
)
from xcbl.models.time_series_response import ListOfPartyCoded
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AccountAssignmentId:
    class Meta:
        name = "AccountAssignmentID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountAssignmentOrderNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BusinessArea:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerOrderConfirmationId:
    class Meta:
        name = "BuyerOrderConfirmationID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerOrderConfirmationItemNum:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommitmentItem:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ControllingArea:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CostCenter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DistributionPercentage:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FixedAssetSub:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalArea:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Fund:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FundsCenter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Glaccount:
    class Meta:
        name = "GLAccount"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GenericAccounting:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Network:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OperationNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationItemNum:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseCode:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProfitCenter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SalesOrderReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountAssignment:
    account_assignment_id: AccountAssignmentId = field(
        metadata={
            "name": "AccountAssignmentID",
            "type": "Element",
            "required": True,
        }
    )
    distribution_percentage: DistributionPercentage = field(
        metadata={
            "name": "DistributionPercentage",
            "type": "Element",
            "required": True,
        }
    )
    glaccount: None | Glaccount = field(
        default=None,
        metadata={
            "name": "GLAccount",
            "type": "Element",
        },
    )
    cost_center: None | CostCenter = field(
        default=None,
        metadata={
            "name": "CostCenter",
            "type": "Element",
        },
    )
    account_assignment_order_number: None | AccountAssignmentOrderNumber = (
        field(
            default=None,
            metadata={
                "name": "AccountAssignmentOrderNumber",
                "type": "Element",
            },
        )
    )
    operation_number: None | OperationNumber = field(
        default=None,
        metadata={
            "name": "OperationNumber",
            "type": "Element",
        },
    )
    sales_order_reference: None | SalesOrderReference = field(
        default=None,
        metadata={
            "name": "SalesOrderReference",
            "type": "Element",
        },
    )
    business_area: None | BusinessArea = field(
        default=None,
        metadata={
            "name": "BusinessArea",
            "type": "Element",
        },
    )
    controlling_area: None | ControllingArea = field(
        default=None,
        metadata={
            "name": "ControllingArea",
            "type": "Element",
        },
    )
    profit_center: None | ProfitCenter = field(
        default=None,
        metadata={
            "name": "ProfitCenter",
            "type": "Element",
        },
    )
    work_breakdown_structure: None | WorkBreakdownStructure = field(
        default=None,
        metadata={
            "name": "WorkBreakdownStructure",
            "type": "Element",
        },
    )
    network: None | Network = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
        },
    )
    fixed_asset: None | FixedAsset = field(
        default=None,
        metadata={
            "name": "FixedAsset",
            "type": "Element",
        },
    )
    fixed_asset_sub: None | FixedAssetSub = field(
        default=None,
        metadata={
            "name": "FixedAssetSub",
            "type": "Element",
        },
    )
    funds_center: None | FundsCenter = field(
        default=None,
        metadata={
            "name": "FundsCenter",
            "type": "Element",
        },
    )
    fund: None | Fund = field(
        default=None,
        metadata={
            "name": "Fund",
            "type": "Element",
        },
    )
    commitment_item: None | CommitmentItem = field(
        default=None,
        metadata={
            "name": "CommitmentItem",
            "type": "Element",
        },
    )
    functional_area: None | FunctionalArea = field(
        default=None,
        metadata={
            "name": "FunctionalArea",
            "type": "Element",
        },
    )
    generic_accounting: None | GenericAccounting = field(
        default=None,
        metadata={
            "name": "GenericAccounting",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseParty:
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
    list_of_party_coded: None | ListOfPartyCoded = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationType:
    order_confirmation_type_coded: OrderConfirmationTypeCoded = field(
        metadata={
            "name": "OrderConfirmationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_type_coded_other: (
        None | OrderConfirmationTypeCodedOther
    ) = field(
        default=None,
        metadata={
            "name": "OrderConfirmationTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SellerOrderConfirmationReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAccountAssignment:
    account_assignment: list[AccountAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AccountAssignment",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseHeader:
    buyer_order_confirmation_id: BuyerOrderConfirmationId = field(
        metadata={
            "name": "BuyerOrderConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_confirmation_reference: SellerOrderConfirmationReference = (
        field(
            metadata={
                "name": "SellerOrderConfirmationReference",
                "type": "Element",
                "required": True,
            }
        )
    )
    order_confirmation_response_issue_date: (
        None | OrderConfirmationResponseIssueDate
    ) = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseIssueDate",
            "type": "Element",
        },
    )
    order_confirmation_type: None | OrderConfirmationType = field(
        default=None,
        metadata={
            "name": "OrderConfirmationType",
            "type": "Element",
        },
    )
    order_confirmation_response_coded: OrderConfirmationResponseCoded = field(
        metadata={
            "name": "OrderConfirmationResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_coded_other: (
        None | OrderConfirmationResponseCodedOther
    ) = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCodedOther",
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
    order_confirmation_response_party: OrderConfirmationResponseParty = field(
        metadata={
            "name": "OrderConfirmationResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_header_note: (
        None | OrderConfirmationResponseHeaderNote
    ) = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    error_info: None | ErrorInfo = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: None | ListOfAttachment = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponseDetail:
    order_confirmation_item_num: OrderConfirmationItemNum = field(
        metadata={
            "name": "OrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    buyer_order_confirmation_item_num: BuyerOrderConfirmationItemNum = field(
        metadata={
            "name": "BuyerOrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_response_code: None | OrderConfirmationResponseCode = (
        field(
            default=None,
            metadata={
                "name": "OrderConfirmationResponseCode",
                "type": "Element",
            },
        )
    )
    order_confirmation_response_coded_other: (
        None | OrderConfirmationResponseCodedOther
    ) = field(
        default=None,
        metadata={
            "name": "OrderConfirmationResponseCodedOther",
            "type": "Element",
        },
    )
    list_of_account_assignment: None | ListOfAccountAssignment = field(
        default=None,
        metadata={
            "name": "ListOfAccountAssignment",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    error_info: None | ErrorInfo = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfOrderConfirmationResponseDetail:
    order_confirmation_response_detail: list[
        OrderConfirmationResponseDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "OrderConfirmationResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationResponse:
    order_confirmation_response_header: OrderConfirmationResponseHeader = (
        field(
            metadata={
                "name": "OrderConfirmationResponseHeader",
                "type": "Element",
                "required": True,
            }
        )
    )
    list_of_order_confirmation_response_detail: (
        None | ListOfOrderConfirmationResponseDetail
    ) = field(
        default=None,
        metadata={
            "name": "ListOfOrderConfirmationResponseDetail",
            "type": "Element",
        },
    )
