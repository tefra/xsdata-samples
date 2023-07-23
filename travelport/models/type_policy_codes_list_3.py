from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypePolicyCodesList3:
    """
    Parameters
    ----------
    policy_code
        A code that indicates why an item was determined to be ‘out of
        policy’.
    min_policy_code
        A code that indicates why the minimum fare or rate was determined to
        be ‘out of policy’.
    max_policy_code
        A code that indicates why the maximum fare or rate was determined to
        be ‘out of policy’.
    """
    class Meta:
        name = "typePolicyCodesList"

    policy_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 10,
        }
    )
    min_policy_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MinPolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 10,
        }
    )
    max_policy_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MaxPolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 10,
        }
    )
