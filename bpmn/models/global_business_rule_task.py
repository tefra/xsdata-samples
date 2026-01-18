from __future__ import annotations

from dataclasses import dataclass

from .t_global_business_rule_task import TGlobalBusinessRuleTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class GlobalBusinessRuleTask(TGlobalBusinessRuleTask):
    class Meta:
        name = "globalBusinessRuleTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
