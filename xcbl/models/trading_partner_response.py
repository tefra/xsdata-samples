from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import Reference
from xcbl.models.trading_partner_organization_delete import PrimaryId
from xcbl.models.trading_partner_user_delete import UserId


@dataclass
class SecondaryMessageInformation:
    message_type_coded: Optional[str] = field(
        default=None,
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


@dataclass
class ListOfSecondaryMessageInformation:
    secondary_message_information: List[SecondaryMessageInformation] = field(
        default_factory=list,
        metadata={
            "name": "SecondaryMessageInformation",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class MessageResponseIdentifier:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TradingPartnerPrimaryId:
    class Meta:
        name = "TradingPartnerPrimaryID"

    primary_id: Optional[PrimaryId] = field(
        default=None,
        metadata={
            "name": "PrimaryID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PrimaryMessageInformation:
    message_response_identifier: Optional[MessageResponseIdentifier] = field(
        default=None,
        metadata={
            "name": "MessageResponseIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    primary_return_coded: Optional[str] = field(
        default=None,
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


@dataclass
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


@dataclass
class ListOfReturnedIdentification:
    returned_identification: List[ReturnedIdentification] = field(
        default_factory=list,
        metadata={
            "name": "ReturnedIdentification",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ReturnMessageInformation:
    primary_message_information: Optional[PrimaryMessageInformation] = field(
        default=None,
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


@dataclass
class TradingPartnerResponseInfo:
    return_message_information: Optional[ReturnMessageInformation] = field(
        default=None,
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


@dataclass
class ListOfTradingPartnerResponseInfo:
    trading_partner_response_info: List[TradingPartnerResponseInfo] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerResponseInfo",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TradingPartnerResponse:
    list_of_trading_partner_response_info: Optional[ListOfTradingPartnerResponseInfo] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerResponseInfo",
            "type": "Element",
            "required": True,
        }
    )
