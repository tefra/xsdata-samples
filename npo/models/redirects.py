from dataclasses import dataclass
from npo.models.redirect_list import RedirectList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class Redirects(RedirectList):
    class Meta:
        name = "redirects"
        namespace = "urn:vpro:api:2013"
