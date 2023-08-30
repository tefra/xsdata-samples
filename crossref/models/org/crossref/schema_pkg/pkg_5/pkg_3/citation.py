from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.citation_t import CitationT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Citation(CitationT):
    """Citation is used to deposit each reference in the reference list of the item
    for which the DOI is being deposited.

    For details see:
    https://www.crossref.org/education/metadata-stewardship/maintaining-your-metadata/add-references/
    """
    class Meta:
        name = "citation"
        namespace = "http://www.crossref.org/schema/5.3.1"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
            "white_space": "collapse",
        }
    )
