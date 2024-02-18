from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agent_idoverride_2 import AgentIdoverride2
from travelport.models.billing_point_of_sale_info_2 import (
    BillingPointOfSaleInfo2,
)
from travelport.models.terminal_session_info_2 import TerminalSessionInfo2
from travelport.models.type_logging_level_2 import TypeLoggingLevel2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class BaseCoreReq2:
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
        ISO  639 Language Code used to receive specific information in the
        requested  language. Supported  Provider: ACH. Supported Carriers:U2
    """

    class Meta:
        name = "BaseCoreReq"

    billing_point_of_sale_info: None | BillingPointOfSaleInfo2 = field(
        default=None,
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
            "required": True,
        },
    )
    agent_idoverride: list[AgentIdoverride2] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    terminal_session_info: None | TerminalSessionInfo2 = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
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
    override_logging: None | TypeLoggingLevel2 = field(
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
