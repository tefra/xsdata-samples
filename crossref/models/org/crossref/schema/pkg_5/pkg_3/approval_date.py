from __future__ import annotations

from dataclasses import dataclass

from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class ApprovalDate(DateT):
    """
    The date on which a dissertation was accepted by the institution
    awarding the degree, a report was approved, or a standard was accepted.
    """

    class Meta:
        name = "approval_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
