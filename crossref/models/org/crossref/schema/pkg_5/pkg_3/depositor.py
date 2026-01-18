from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.depositor_name import (
    DepositorName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.email_address import (
    EmailAddress,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Depositor:
    """
    Information about the organization submitting DOI metadata to Crossref.
    """

    class Meta:
        name = "depositor"
        namespace = "http://www.crossref.org/schema/5.3.1"

    depositor_name: DepositorName = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    email_address: EmailAddress = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
