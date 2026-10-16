from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class CmUpdateType(StrEnum):
    ADDENDUM = "addendum"
    CLARIFICATION = "clarification"
    CORRECTION = "correction"
    CORRIGENDUM = "corrigendum"
    ERRATUM = "erratum"
    EXPRESSION_OF_CONCERN = "expression_of_concern"
    NEW_EDITION = "new_edition"
    NEW_VERSION = "new_version"
    PARTIAL_RETRACTION = "partial_retraction"
    REMOVAL = "removal"
    RETRACTION = "retraction"
    WITHDRAWAL = "withdrawal"
