from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


class IntraWorkRelationIdentifierType(Enum):
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
