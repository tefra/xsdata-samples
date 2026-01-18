from __future__ import annotations

from dataclasses import dataclass

from .t_partner_entity import TPartnerEntity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class PartnerEntity(TPartnerEntity):
    class Meta:
        name = "partnerEntity"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
