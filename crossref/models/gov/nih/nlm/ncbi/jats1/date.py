from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.era import Era
from crossref.models.gov.nih.nlm.ncbi.jats1.month import Month
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.year import Year

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Date:
    """
    <div> <h3>Date</h3> </div>.
    """

    class Meta:
        name = "date"
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
    publication_format: str | None = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
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
