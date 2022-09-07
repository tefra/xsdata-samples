from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ArticleIdPubIdType(Enum):
    ACCESSION = "accession"
    ARCHIVE = "archive"
    ARK = "ark"
    ART_ACCESS_ID = "art-access-id"
    ARXIV = "arxiv"
    CODEN = "coden"
    CUSTOM = "custom"
    DOAJ = "doaj"
    DOI = "doi"
    HANDLE = "handle"
    INDEX = "index"
    ISBN = "isbn"
    MANUSCRIPT = "manuscript"
    MEDLINE = "medline"
    MR = "mr"
    OTHER = "other"
    PII = "pii"
    PMCID = "pmcid"
    PMID = "pmid"
    PUBLISHER_ID = "publisher-id"
    SICI = "sici"
    STD_DESIGNATION = "std-designation"
    ZBL = "zbl"
