from dataclasses import dataclass
from generali.models.org.w3.pkg_2005.pkg_08.addressing.problem_action_type import ProblemActionType

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemAction(ProblemActionType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
