from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policy_set import (
    ScnPolicySet,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ScnPolicies:
    """
    A wrapper for Scholarly Sharing Network (SCN) policy information.
    """

    class Meta:
        name = "scn_policies"
        namespace = "http://www.crossref.org/schema/5.3.1"

    scn_policy_set: list[ScnPolicySet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
