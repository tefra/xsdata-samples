from dataclasses import dataclass, field
from typing import Optional, Union
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
    <div> <h3>Publication Date</h3> </div>
    """

    class Meta:
        name = "pub-date"
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
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
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
    pub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "pub-type",
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
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
