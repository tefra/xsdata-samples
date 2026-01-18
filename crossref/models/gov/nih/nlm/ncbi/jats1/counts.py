from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.count import Count
from crossref.models.gov.nih.nlm.ncbi.jats1.equation_count import EquationCount
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_count import FigCount
from crossref.models.gov.nih.nlm.ncbi.jats1.page_count import PageCount
from crossref.models.gov.nih.nlm.ncbi.jats1.ref_count import RefCount
from crossref.models.gov.nih.nlm.ncbi.jats1.table_count import TableCount
from crossref.models.gov.nih.nlm.ncbi.jats1.word_count import WordCount

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Counts:
    """
    <div> <h3>Counts</h3> </div>.
    """

    class Meta:
        name = "counts"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    count: list[Count] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_count: None | FigCount = field(
        default=None,
        metadata={
            "name": "fig-count",
            "type": "Element",
        },
    )
    table_count: None | TableCount = field(
        default=None,
        metadata={
            "name": "table-count",
            "type": "Element",
        },
    )
    equation_count: None | EquationCount = field(
        default=None,
        metadata={
            "name": "equation-count",
            "type": "Element",
        },
    )
    ref_count: None | RefCount = field(
        default=None,
        metadata={
            "name": "ref-count",
            "type": "Element",
        },
    )
    page_count: None | PageCount = field(
        default=None,
        metadata={
            "name": "page-count",
            "type": "Element",
        },
    )
    word_count: None | WordCount = field(
        default=None,
        metadata={
            "name": "word-count",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
