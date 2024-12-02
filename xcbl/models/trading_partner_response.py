from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.trading_partner_user_information import (
    PrimaryId,
    UserId,
)


@dataclass(kw_only=True)
class AlternateId:
    class Meta:
        name = "AlternateID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageType:
    class Meta:
        name = "MessageClass"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PrimaryReturnCodeDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PrimaryReturnCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RedirectUrl:
    class Meta:
        name = "RedirectURL"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RefDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RefNum:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReturnedIdentificationUrn:
    class Meta:
        name = "ReturnedIdentificationURN"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ServiceId:
    class Meta:
        name = "ServiceID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Reference:
    ref_num: RefNum = field(
        metadata={
            "name": "RefNum",
            "type": "Element",
            "required": True,
        }
    )
    ref_date: Optional[RefDate] = field(
        default=None,
        metadata={
            "name": "RefDate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SecondaryMessageInformation:
    message_type_coded: MessageTypeCoded = field(
        metadata={
            "name": "MessageTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    message_type_coded_other: Optional[MessageTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "MessageTypeCodedOther",
            "type": "Element",
        },
    )
    message_class: Optional[MessageType] = field(
        default=None,
        metadata={
            "name": "MessageClass",
            "type": "Element",
        },
    )
    message_number: Optional[MessageNumber] = field(
        default=None,
        metadata={
            "name": "MessageNumber",
            "type": "Element",
        },
    )
    message_description: Optional[MessageDescription] = field(
        default=None,
        metadata={
            "name": "MessageDescription",
            "type": "Element",
        },
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
class ListOfSecondaryMessageInformation:
    secondary_message_information: list[SecondaryMessageInformation] = field(
        default_factory=list,
        metadata={
            "name": "SecondaryMessageInformation",
            "type": "Element",
            "min_occurs": 1,
        },
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
class ReturnedIdentification:
    trading_partner_primary_id: Optional[TradingPartnerPrimaryId] = field(
        default=None,
        metadata={
            "name": "TradingPartnerPrimaryID",
            "type": "Element",
        },
    )
    alternate_id: Optional[AlternateId] = field(
        default=None,
        metadata={
            "name": "AlternateID",
            "type": "Element",
        },
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "name": "UserID",
            "type": "Element",
        },
    )
    returned_identification_urn: Optional[ReturnedIdentificationUrn] = field(
        default=None,
        metadata={
            "name": "ReturnedIdentificationURN",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfReturnedIdentification:
    returned_identification: list[ReturnedIdentification] = field(
        default_factory=list,
        metadata={
            "name": "ReturnedIdentification",
            "type": "Element",
            "min_occurs": 1,
        },
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
    primary_return_coded: PrimaryReturnCoded = field(
        metadata={
            "name": "PrimaryReturnCoded",
            "type": "Element",
            "required": True,
        }
    )
    primary_return_code_description: Optional[PrimaryReturnCodeDescription] = (
        field(
            default=None,
            metadata={
                "name": "PrimaryReturnCodeDescription",
                "type": "Element",
            },
        )
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
    list_of_secondary_message_information: Optional[
        ListOfSecondaryMessageInformation
    ] = field(
        default=None,
        metadata={
            "name": "ListOfSecondaryMessageInformation",
            "type": "Element",
        },
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
    list_of_returned_identification: Optional[ListOfReturnedIdentification] = (
        field(
            default=None,
            metadata={
                "name": "ListOfReturnedIdentification",
                "type": "Element",
            },
        )
    )
    redirect_url: Optional[RedirectUrl] = field(
        default=None,
        metadata={
            "name": "RedirectURL",
            "type": "Element",
        },
    )
    service_id: Optional[ServiceId] = field(
        default=None,
        metadata={
            "name": "ServiceID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerResponseInfo:
    trading_partner_response_info: list[TradingPartnerResponseInfo] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerResponseInfo",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerResponse:
    list_of_trading_partner_response_info: ListOfTradingPartnerResponseInfo = (
        field(
            metadata={
                "name": "ListOfTradingPartnerResponseInfo",
                "type": "Element",
                "required": True,
            }
        )
    )
