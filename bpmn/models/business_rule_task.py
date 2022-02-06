from dataclasses import dataclass
from .t_business_rule_task import TBusinessRuleTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class BusinessRuleTask(TBusinessRuleTask):
    class Meta:
        name = "businessRuleTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
