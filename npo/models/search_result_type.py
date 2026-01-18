from __future__ import annotations

from dataclasses import dataclass

from npo.models.result_type import ResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class SearchResultType(ResultType):
    class Meta:
        name = "searchResultType"
