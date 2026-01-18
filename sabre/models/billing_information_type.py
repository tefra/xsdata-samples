from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class BillingInformationType:
    user_station: int = field(
        default=0,
        metadata={
            "name": "UserStation",
            "type": "Attribute",
        },
    )
    user_branch: int = field(
        default=0,
        metadata={
            "name": "UserBranch",
            "type": "Attribute",
        },
    )
    partition_id: None | str = field(
        default=None,
        metadata={
            "name": "PartitionID",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,4}",
        },
    )
    user_set_address: None | str = field(
        default=None,
        metadata={
            "name": "UserSetAddress",
            "type": "Attribute",
            "pattern": r"[0-9A-F]{6}",
        },
    )
    aaacity: None | str = field(
        default=None,
        metadata={
            "name": "AAACity",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    agent_sine_in: None | str = field(
        default=None,
        metadata={
            "name": "AgentSineIn",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    service_name: None | str = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z,]{1,8}",
        },
    )
    action_code: None | str = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
