from enum import Enum
from dataclasses import dataclass


class Operation(Enum):
    SUM = "sum"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


@dataclass
class OperationRequest:
    a: float
    b: float
    operation: Operation


@dataclass
class OperationResult:
    a: float
    b: float
    operation: Operation
    result: float
    duration_ms: float


@dataclass
class HistoryEntry:
    id: str
    a: float
    b: float
    operation: str  # stored as enum .value for JSON portability
    result: float
    duration_ms: float
    timestamp: str  # ISO-8601 UTC
