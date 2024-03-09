from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import SubjGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.series_text import SeriesText
from crossref.models.gov.nih.nlm.ncbi.jats1.series_title import SeriesTitle

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ArticleCategories:
    """
    <div> <h3>Article Grouping Data</h3> </div>
    """

    class Meta:
        name = "article-categories"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    series_title: List[SeriesTitle] = field(
        default_factory=list,
        metadata={
            "name": "series-title",
            "type": "Element",
        },
    )
    series_text: List[SeriesText] = field(
        default_factory=list,
        metadata={
            "name": "series-text",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
