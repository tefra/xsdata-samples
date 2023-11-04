from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Depositor:
    """
    Information about the organization submitting DOI metadata to Crossref.
    """
    class Meta:
        name = "depositor"
        namespace = "http://www.crossref.org/schema/5.3.1"

    depositor_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 130,
        }
    )
    email_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 6,
            "max_length": 200,
        }
    )
