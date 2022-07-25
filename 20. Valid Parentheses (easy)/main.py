import logging
from typing import Dict, List


class Solution:
    @classmethod
    def isValid(cls, s: str) -> bool:
        closing_to_opening: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        closing = {")", "]", "}"}
        opening = {"(", "[", "{"}
        openings: List[str] = []

        for ch in s:
            if ch in opening:
                openings.append(ch)
            if ch in closing:
                if len(openings) == 0:
                    return False
                last_opening = openings[-1]
                expected_opening = closing_to_opening[ch]
                if last_opening == expected_opening:
                    openings = openings[:-1]
                else:
                    return False

        return len(openings) == 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.isValid("()") is True
    assert Solution.isValid("()[]{}") is True
    assert Solution.isValid("(()]") is False
    assert Solution.isValid("(]") is False
    assert Solution.isValid("(") is False
    assert Solution.isValid("}") is False
