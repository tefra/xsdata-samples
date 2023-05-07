from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version import ArticleVersion

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ArticleVersionAlternatives:
    """
    <div> <h3>Article Version Alternatives</h3> </div>
    """
    class Meta:
        name = "article-version-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    article_version: List[ArticleVersion] = field(
        default_factory=list,
        metadata={
            "name": "article-version",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
