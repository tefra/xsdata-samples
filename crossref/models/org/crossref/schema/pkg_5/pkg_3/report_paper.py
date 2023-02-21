from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import ComponentList
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item import ContentItem
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_type_atts_publication_type import PublicationTypeAttsPublicationType
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_metadata import ReportPaperMetadata
from crossref.models.org.crossref.schema.pkg_5.pkg_3.report_paper_series_metadata import ReportPaperSeriesMetadata

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReportPaper:
    """
    report-paper is the top level element for deposit of metadata about one or more
    reports or working papers.
    """
    class Meta:
        name = "report-paper"
        namespace = "http://www.crossref.org/schema/5.3.1"

    report_paper_metadata: Optional[ReportPaperMetadata] = field(
        default=None,
        metadata={
            "name": "report-paper_metadata",
            "type": "Element",
        }
    )
    report_paper_series_metadata: Optional[ReportPaperSeriesMetadata] = field(
        default=None,
        metadata={
            "name": "report-paper_series_metadata",
            "type": "Element",
        }
    )
    content_item: List[ContentItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    component_list: Optional[ComponentList] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    publication_type: PublicationTypeAttsPublicationType = field(
        default=PublicationTypeAttsPublicationType.FULL_TEXT,
        metadata={
            "type": "Attribute",
        }
    )
