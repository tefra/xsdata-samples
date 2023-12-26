from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.depositor import Depositor

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Head:
    """Container for information related to the DOI batch submission.

    This element uniquely identifies the batch deposit to Crossref and
    contains information that will be used as a reference in error
    messages triggered during submission processing.
    """

    class Meta:
        name = "head"
        namespace = "http://www.crossref.org/schema/5.3.1"

    doi_batch_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 4,
            "max_length": 100,
        },
    )
    timestamp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    depositor: Optional[Depositor] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    registrant: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
