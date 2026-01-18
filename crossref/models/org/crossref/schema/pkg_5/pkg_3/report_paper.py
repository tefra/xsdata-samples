from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import (
    ComponentList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item import (
    ContentItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_metadata import (
    ReportPaperMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_publication_type import (
    ReportPaperPublicationType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata import (
    ReportPaperSeriesMetadata,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReportPaper:
    """
    report-paper is the top level element for deposit of metadata about one
    or more reports or working papers.
    """

    class Meta:
        name = "report-paper"
        namespace = "http://www.crossref.org/schema/5.3.1"

    report_paper_metadata: ReportPaperMetadata | None = field(
        default=None,
        metadata={
            "name": "report-paper_metadata",
            "type": "Element",
        },
    )
    report_paper_series_metadata: ReportPaperSeriesMetadata | None = field(
        default=None,
        metadata={
            "name": "report-paper_series_metadata",
            "type": "Element",
        },
    )
    content_item: list[ContentItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    component_list: ComponentList | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_type: ReportPaperPublicationType = field(
        default=ReportPaperPublicationType.FULL_TEXT,
        metadata={
            "type": "Attribute",
        },
    )
