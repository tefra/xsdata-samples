from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class QuestionQuestionResponseType(StrEnum):
    ESSAY = "essay"
    FILL_IN_THE_BLANK = "fill-in-the-blank"
    MULTI_SELECT = "multi-select"
    MULTIPLE_CHOICE = "multiple-choice"
    SHORT_ANSWER = "short-answer"
    TRUE_FALSE = "true-false"
