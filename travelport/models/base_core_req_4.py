from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agent_idoverride_4 import AgentIdoverride4
from travelport.models.billing_point_of_sale_info_4 import (
    BillingPointOfSaleInfo4,
)
from travelport.models.terminal_session_info_4 import TerminalSessionInfo4
from travelport.models.type_logging_level_4 import TypeLoggingLevel4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BaseCoreReq4:
    """
    Parameters
    ----------
    billing_point_of_sale_info
    agent_idoverride
    terminal_session_info
    trace_id
        Unique identifier for this atomic transaction traced by the user.
        Use is optional.
    token_id
        Authentication Token ID used when running in statefull operation.
        Obtained from the LoginRsp. Use is optional.
    authorized_by
        Used in showing who authorized the request. Use is optional.
    target_branch
        Used for Emulation - If authorised will execute the request as if
        the agent's parent branch is the TargetBranch specified.
    override_logging
        Use to override the default logging level
    language_code
        ISO 639 LanguageCode is used to retrieve specific information in the
        requested language.  Use a 2 or 4 character language code, example
        FR or FRFR for French, EN or ENGB for English.  The supported
        providers: ACH, RCH.
    """

    class Meta:
        name = "BaseCoreReq"

    billing_point_of_sale_info: None | BillingPointOfSaleInfo4 = field(
        default=None,
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        },
    )
    agent_idoverride: list[AgentIdoverride4] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        },
    )
    terminal_session_info: None | TerminalSessionInfo4 = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    trace_id: None | str = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        },
    )
    token_id: None | str = field(
        default=None,
        metadata={
            "name": "TokenId",
            "type": "Attribute",
        },
    )
    authorized_by: None | str = field(
        default=None,
        metadata={
            "name": "AuthorizedBy",
            "type": "Attribute",
        },
    )
    target_branch: None | str = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
    override_logging: None | TypeLoggingLevel4 = field(
        default=None,
        metadata={
            "name": "OverrideLogging",
            "type": "Attribute",
        },
    )
    language_code: None | str = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        },
    )
