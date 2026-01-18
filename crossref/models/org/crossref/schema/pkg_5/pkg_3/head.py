from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.depositor import Depositor
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_batch_id import (
    DoiBatchId,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.registrant import (
    Registrant,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.timestamp import Timestamp

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Head:
    """
    Container for information related to the DOI batch submission.

    This element uniquely identifies the batch deposit to Crossref and
    contains information that will be used as a reference in error messages
    triggered during submission processing.
    """

    class Meta:
        name = "head"
        namespace = "http://www.crossref.org/schema/5.3.1"

    doi_batch_id: DoiBatchId = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    timestamp: Timestamp = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    depositor: Depositor = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    registrant: Registrant = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
