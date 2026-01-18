from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ReportPaperMetadataReferenceDistributionOpts(Enum):
    NONE = "none"
    QUERY = "query"
    ANY = "any"
