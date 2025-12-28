---
name: deep-research
description: Deep research with sequential thinking and parallel agents
---

# Deep Research: $ARGUMENTS

Execute comprehensive multi-angle research using structured thinking and parallel investigation.

## Phase 1: Decompose
Use `mcp__MCP_DOCKER__sequentialthinking` to break the topic into 3-5 independent research aspects:
- Identify key questions per aspect
- Define what "understanding" looks like for each
- Create focused research prompts

ultrathink

## Phase 2: Parallel Research
Launch **one Task agent per aspect** simultaneously (in a single message):
```
Task tool:
  subagent_type: "Explore"
  run_in_background: true
  prompt: "Research [aspect]: [questions]. Return key findings and insights."
```

Wait for all agents with `TaskOutput` (block: true).

## Phase 3: Synthesize
Use `mcp__MCP_DOCKER__sequentialthinking` to:
- Cross-reference findings from all agents
- Identify patterns, contradictions, connections
- Form conclusions

## Phase 4: Present
Structure response as:
- **Key Findings** (bullets)
- **Insights & Connections** (cross-cutting themes)
- **Conclusions** (synthesis)
- **Next Steps** (if applicable)

## Constraints
- Minimum 3 agents, maximum 5
- Always use sequential thinking for decomposition AND synthesis
- Output in chat only
