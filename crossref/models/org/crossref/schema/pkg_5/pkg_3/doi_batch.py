from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.body import Body
from crossref.models.org.crossref.schema.pkg_5.pkg_3.head import Head

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DoiBatch:
    """
    Top level element for a metadata record submission.

    This element indicates the start and end of the XML file. The version
    number is fixed to the version of the schema.
    """

    class Meta:
        name = "doi_batch"
        namespace = "http://www.crossref.org/schema/5.3.1"

    head: Optional[Head] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: str = field(
        init=False,
        default="5.3.1",
        metadata={
            "type": "Attribute",
        },
    )
