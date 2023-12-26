from dataclasses import dataclass, field
from typing import Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.era import Era
from crossref.models.gov.nih.nlm.ncbi.jats1.month import Month
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.year import Year

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Date:
    """
    <div> <h3>Date</h3> </div>
    """

    class Meta:
        name = "date"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    day: Optional[Day] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    month: Optional[Month] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    season: Optional[Season] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    year: Optional[Year] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    era: Optional[Era] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    calendar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    date_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iso_8601_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "iso-8601-date",
            "type": "Attribute",
        },
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
