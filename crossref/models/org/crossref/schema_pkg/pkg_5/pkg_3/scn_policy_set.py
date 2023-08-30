from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ScnPolicySet:
    """
    A group of related SCN policies.
    """
    class Meta:
        name = "scn_policy_set"
        namespace = "http://www.crossref.org/schema/5.3.1"

    scn_policy_ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 2048,
            "pattern": r"([hH][tT][tT][pP]|[hH][tT][tT][pP][sS]|[fF][tT][pP])://.*",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
