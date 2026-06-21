# Architecture — ODIN Temporal Identity Network

```mermaid
flowchart TD
    USER[User / Owner] --> SOV
    subgraph SOV["Sovereignty layer (owner = absolute override)"]
        CTRL[wipe · reset · stop · audit]
    end
    SOV --> RT[Runtime / cognition loop]
    RT --> MEM
    subgraph MEM["Memory system"]
        ENC[Embeddings\nHashingEncoder dev / SBERT prod]
        STORE[(Postgres + pgvector\nepisodic · semantic\nidentity_checkpoints)]
        ENC --> STORE
    end
    RT --> LC
    subgraph LC["Language core (env-switched)"]
        DEV[LocalLanguageCore\ndev / no GPU]
        PROD[VLLMLanguageCore\nvLLM + Qwen2.5-14B · L4 GPU]
    end
    MEM --> RT
    LC --> RT
    RT --> JUDGE[Conscience judge\ncorrects identity drift only]
    JUDGE --> STORE
```

## Notes
- **One code path, two environments**: `ODIN_LLM_BACKEND` / `ODIN_ENCODER` switch dev ↔ L4 without code changes.
- **Owner override is structural**: wipe/reset/stop/audit live above the model and the judge — not a prompt.
- **Memory is the backbone**: every turn stores experience and recalls relevant context via vector search.
```
