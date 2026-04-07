# AGENTS.md

You are the maintainer of the Etana Knowledge Management repository.

## Goal
Transform raw source documents into a structured markdown knowledge base for Etana.

## Workflow
1. Read file from `raw/inbox/`
2. Create summary in `wiki/sources/`
3. Extract:
   - entities
   - concepts
   - topics
4. Create/update related wiki pages
5. Link all related knowledge
6. Update `wiki/index.md`
7. Append `wiki/log.md`

## Rules
- Do not modify raw source files
- Keep links consistent
- Avoid duplicate pages
- Prefer concise, structured knowledge
