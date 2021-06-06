from dataclasses import dataclass
from .authority_version_structure import AuthorityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Authority(AuthorityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
