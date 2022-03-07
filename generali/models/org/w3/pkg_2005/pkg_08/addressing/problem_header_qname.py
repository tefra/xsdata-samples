from dataclasses import dataclass
from generali.models.org.w3.pkg_2005.pkg_08.addressing.attributed_qname_type import AttributedQnameType

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemHeaderQname(AttributedQnameType):
    class Meta:
        name = "ProblemHeaderQName"
        namespace = "http://www.w3.org/2005/08/addressing"
