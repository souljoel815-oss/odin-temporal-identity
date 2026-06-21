# ODIN — Temporal Identity Network

An experimental **persistent AI entity** that exists in time, forms an identity through experience, and evolves — built on a vector-memory backbone and a local LLM inference stack. ODIN remembers past interactions (episodic + semantic memory), accumulates identity from experience, and keeps the owner in absolute control.

> 🎥 **Demo:** _add your Loom link here_ · 🖼️ Screenshots in [`docs/screenshots/`](./docs/screenshots/)
>
> 🔒 This is a **showcase repo**. Full source available on request.

---

## The idea

Most chatbots are stateless — every conversation starts from zero. ODIN explores the opposite: an agent with **continuity of self**. It stores experiences in a vector database, recalls relevant memories, lets identity drift naturally from what it lives through, and periodically runs a "conscience" judge that only corrects harmful drift — all under a hard **owner-override** safety layer.

## Design highlights

- **Memory system** — working + episodic + semantic memory backed by **Postgres + pgvector**; store-and-recall over vector embeddings.
- **Identity model (Hebbian free evolution)** — identity accumulates from experience; a periodic judge corrects drift rather than dictating behavior.
- **Sovereignty layer** — **owner = absolute override**, enforced at the system level (wipe / reset / stop / audit) above the model and the judge.
- **One code path, two environments** — env-driven config runs a light **dev** stack (hashing encoder, local language core) on a GPU-less Windows host, and flips to the **production** stack (SBERT embeddings, **vLLM + Qwen2.5-14B**) on an NVIDIA L4 server via environment variables only.

## Architecture

See [`docs/architecture.md`](./docs/architecture.md).

## Tech stack

| Layer | Tools |
|---|---|
| Memory store | PostgreSQL + **pgvector** (`psycopg`) |
| Embeddings | `HashingEncoder` (dev) / `sentence-transformers` SBERT (prod) |
| Inference | local language core (dev) / **vLLM + Qwen2.5-14B** (L4 GPU) |
| Service | `FastAPI` + `uvicorn` (always-on server); stdlib CLI client |
| Config & models | `pydantic`, `python-dotenv` |
| Tests | `pytest` |

## Engineering highlights

- **Environment-portable ML**: the heavy GPU stack never runs on the dev box; the same code targets dev and the L4 by config alone (`ODIN_LLM_BACKEND`, `ODIN_ENCODER`).
- **Schema-first memory**: episodic, semantic, identity-checkpoint, autonomous-action, and sovereignty-log tables with pgvector indexes.
- **Safety by construction**: guaranteed controls (wipe/reset/stop/audit) sit *outside* the learned components.

## Illustrative code

A representative, non-proprietary excerpt (the encoder interface + dev/prod split) is in
[`samples/illustrative_interface.py`](./samples/illustrative_interface.py).
The identity nucleus, cognition, and inference internals are private.

---

> Research project exploring persistent agent identity and memory. Not a product; safety controls are owner-enforced.
