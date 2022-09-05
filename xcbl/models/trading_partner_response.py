from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import Reference
from xcbl.models.trading_partner_organization_delete import PrimaryId
from xcbl.models.trading_partner_user_delete import UserId


@dataclass(kw_only=True)
class SecondaryMessageInformation:
    message_type_coded: str = field(
        metadata={
            "name": "MessageTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    message_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageTypeCodedOther",
            "type": "Element",
        }
    )
    message_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageClass",
            "type": "Element",
        }
    )
    message_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageNumber",
            "type": "Element",
        }
    )
    message_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageDescription",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfSecondaryMessageInformation:
    secondary_message_information: List[SecondaryMessageInformation] = field(
        default_factory=list,
        metadata={
            "name": "SecondaryMessageInformation",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class MessageResponseIdentifier:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerPrimaryId:
    class Meta:
        name = "TradingPartnerPrimaryID"

    primary_id: PrimaryId = field(
        metadata={
            "name": "PrimaryID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PrimaryMessageInformation:
    message_response_identifier: MessageResponseIdentifier = field(
        metadata={
            "name": "MessageResponseIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    primary_return_coded: str = field(
        metadata={
            "name": "PrimaryReturnCoded",
            "type": "Element",
            "required": True,
        }
    )
    primary_return_code_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryReturnCodeDescription",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ReturnedIdentification:
    trading_partner_primary_id: Optional[TradingPartnerPrimaryId] = field(
        default=None,
        metadata={
            "name": "TradingPartnerPrimaryID",
            "type": "Element",
        }
    )
    alternate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateID",
            "type": "Element",
        }
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "name": "UserID",
            "type": "Element",
        }
    )
    returned_identification_urn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnedIdentificationURN",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfReturnedIdentification:
    returned_identification: List[ReturnedIdentification] = field(
        default_factory=list,
        metadata={
            "name": "ReturnedIdentification",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ReturnMessageInformation:
    primary_message_information: PrimaryMessageInformation = field(
        metadata={
            "name": "PrimaryMessageInformation",
            "type": "Element",
            "required": True,
        }
    )
    list_of_secondary_message_information: Optional[ListOfSecondaryMessageInformation] = field(
        default=None,
        metadata={
            "name": "ListOfSecondaryMessageInformation",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TradingPartnerResponseInfo:
    return_message_information: ReturnMessageInformation = field(
        metadata={
            "name": "ReturnMessageInformation",
            "type": "Element",
            "required": True,
        }
    )
    list_of_returned_identification: Optional[ListOfReturnedIdentification] = field(
        default=None,
        metadata={
            "name": "ListOfReturnedIdentification",
            "type": "Element",
        }
    )
    redirect_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "RedirectURL",
            "type": "Element",
        }
    )
    service_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerResponseInfo:
    trading_partner_response_info: List[TradingPartnerResponseInfo] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerResponseInfo",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerResponse:
    list_of_trading_partner_response_info: ListOfTradingPartnerResponseInfo = field(
        metadata={
            "name": "ListOfTradingPartnerResponseInfo",
            "type": "Element",
            "required": True,
        }
    )
