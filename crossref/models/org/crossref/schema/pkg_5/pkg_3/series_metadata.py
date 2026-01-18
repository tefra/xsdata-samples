from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import Abstract
from crossref.models.org.crossref.access_indicators.program import (
    Program as AccessIndicatorsProgram,
)
from crossref.models.org.crossref.fundref.program import (
    Program as FundrefProgram,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.coden import Coden
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark import Crossmark
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issn import Issn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_item import (
    PublisherItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_number import (
    SeriesNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class SeriesMetadata:
    """
    Container for metadata about a series publication.

    :ivar contributors:
    :ivar titles:
    :ivar abstract: The abstract element allows depositors to include
        abstracts extracted from NLM or JATS XML in Crossref deposits.
        The jats: namespace prefix must be included.
    :ivar issn:
    :ivar coden:
    :ivar series_number:
    :ivar publisher_item:
    :ivar crossmark:
    :ivar program:
    :ivar crossref_org_access_indicators_program:
    :ivar archive_locations:
    :ivar doi_data:
    """

    class Meta:
        name = "series_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: None | Contributors = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    titles: Titles = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ncbi.nlm.nih.gov/JATS1",
        },
    )
    issn: list[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
        },
    )
    coden: None | Coden = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    series_number: None | SeriesNumber = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publisher_item: None | PublisherItem = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crossmark: None | Crossmark = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    program: None | FundrefProgram = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/fundref.xsd",
        },
    )
    crossref_org_access_indicators_program: None | AccessIndicatorsProgram = (
        field(
            default=None,
            metadata={
                "name": "program",
                "type": "Element",
                "namespace": "http://www.crossref.org/AccessIndicators.xsd",
            },
        )
    )
    archive_locations: None | ArchiveLocations = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: None | DoiData = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
