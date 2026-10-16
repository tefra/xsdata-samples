from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ProceedingsSeriesMetadataReferenceDistributionOpts(StrEnum):
    NONE = "none"
    QUERY = "query"
    ANY = "any"
