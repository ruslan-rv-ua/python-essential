from typing import List, Iterable, Any

def to_pairs(seq: Iterable, fill: Any = None) -> List[List]:
	return [list(pair) for pair in zip(seq[::2], (*seq[1::2], fill))]

r = to_pairs([1, 2, 3, 4])
assert to_pairs([1, 2, 3, 4]) == [[1, 2], [3, 4]]
assert to_pairs([1, 2, 3, 4, 5]) == [[1, 2], [3, 4], [5, None]]
assert to_pairs([1, 2, 3, 4, 5, 0], fill = 0) == [[1, 2], [3, 4], [5, 0]]
