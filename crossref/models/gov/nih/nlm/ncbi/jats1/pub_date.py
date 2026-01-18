from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.era import Era
from crossref.models.gov.nih.nlm.ncbi.jats1.month import Month
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.year import Year
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class PubDate:
    """
    <div> <h3>Publication Date</h3> </div>.
    """

    class Meta:
        name = "pub-date"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    day: Day | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    month: Month | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    season: Season | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    year: Year | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    era: Era | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assigning_authority: str | None = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    calendar: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    date_type: str | None = field(
        default=None,
        metadata={
            "name": "date-type",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iso_8601_date: str | None = field(
        default=None,
        metadata={
            "name": "iso-8601-date",
            "type": "Attribute",
        },
    )
    pub_type: str | None = field(
        default=None,
        metadata={
            "name": "pub-type",
            "type": "Attribute",
        },
    )
    publication_format: str | None = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
