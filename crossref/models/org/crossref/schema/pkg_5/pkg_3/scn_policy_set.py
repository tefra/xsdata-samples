from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.scn_policy_ref import (
    ScnPolicyRef,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ScnPolicySet:
    """
    A group of related SCN policies.
    """

    class Meta:
        name = "scn_policy_set"
        namespace = "http://www.crossref.org/schema/5.3.1"

    scn_policy_ref: List[ScnPolicyRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
