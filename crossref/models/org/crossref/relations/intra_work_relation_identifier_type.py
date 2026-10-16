from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


class IntraWorkRelationIdentifierType(StrEnum):
    DOI = "doi"
    ISSN = "issn"
    ISBN = "isbn"
    URI = "uri"
    PMID = "pmid"
    PMCID = "pmcid"
    PURL = "purl"
    ARXIV = "arxiv"
    ARK = "ark"
    HANDLE = "handle"
    UUID = "uuid"
    ECLI = "ecli"
    ACCESSION = "accession"
    OTHER = "other"
