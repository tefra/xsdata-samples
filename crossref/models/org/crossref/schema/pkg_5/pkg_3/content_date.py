from __future__ import annotations

from dataclasses import dataclass

from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t import DateT

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ContentDate(DateT):
    """
    The date a piece of content was created.
    """

    class Meta:
        name = "content_date"
        namespace = "http://www.crossref.org/schema/5.3.1"
