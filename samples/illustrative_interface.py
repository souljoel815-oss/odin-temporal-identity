"""
Illustrative interface excerpt — ODIN Temporal Identity Network.

Representative structure/style only. The identity nucleus, cognition loop,
judge, and inference internals are private and NOT included here.
"""

from __future__ import annotations

from typing import Protocol, Sequence


class Encoder(Protocol):
    """Embedding backend. Dev uses a hashing encoder (no model download);
    production uses SBERT on the GPU server. The runtime depends only on
    this interface, so swapping is a config flag — not a code change.
    """
    dim: int

    def encode(self, texts: Sequence[str]) -> list[list[float]]: ...


class LanguageCore(Protocol):
    """LLM backend. Dev uses a local stub; production uses vLLM + Qwen2.5-14B."""
    def generate(self, prompt: str, *, max_tokens: int = 512) -> str: ...


def build_encoder(backend: str, dim: int = 256) -> Encoder:
    """Factory selected by ODIN_ENCODER. The concrete SBERT/hashing
    implementations live in the private source; only the wiring is shown.
    """
    if backend not in {"hashing", "sbert"}:
        raise ValueError(f"unknown encoder backend: {backend!r}")
    raise NotImplementedError("concrete encoders are private")


# Memory schema (subset) — what each experience carries into pgvector.
MEMORY_TABLES = (
    "episodic",              # raw experiences, timestamped + embedded
    "semantic",              # distilled facts / concepts
    "identity_checkpoints",  # periodic snapshots of the evolving identity
    "autonomous_actions",    # actions ODIN took on its own
    "sovereignty_log",       # owner overrides + audit trail
)
