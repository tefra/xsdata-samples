from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agent_idoverride_5 import AgentIdoverride5
from travelport.models.billing_point_of_sale_info_5 import (
    BillingPointOfSaleInfo5,
)
from travelport.models.terminal_session_info_5 import TerminalSessionInfo5
from travelport.models.type_logging_level_5 import TypeLoggingLevel5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class BaseCoreReq5:
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
        ISO 639 two-character language codes are used to retrieve specific
        information in the requested language. For Rich Content and
        Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS
        (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese
        Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE,
        DECH can also be used. Only certain services support this attribute.
        Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """

    class Meta:
        name = "BaseCoreReq"

    billing_point_of_sale_info: BillingPointOfSaleInfo5 = field(
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "required": True,
        }
    )
    agent_idoverride: list[AgentIdoverride5] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    terminal_session_info: None | TerminalSessionInfo5 = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
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
    override_logging: None | TypeLoggingLevel5 = field(
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
