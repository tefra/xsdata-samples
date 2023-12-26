from dataclasses import dataclass
from generali.models.org.w3.pkg_2005.pkg_08.addressing.attributed_uritype import (
    AttributedUritype,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class MessageId(AttributedUritype):
    class Meta:
        name = "MessageID"
        namespace = "http://www.w3.org/2005/08/addressing"
