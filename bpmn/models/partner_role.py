from __future__ import annotations

from dataclasses import dataclass

from .t_partner_role import TPartnerRole

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class PartnerRole(TPartnerRole):
    class Meta:
        name = "partnerRole"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
