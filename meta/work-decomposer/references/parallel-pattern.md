# Parallel Research Pattern

For work with independent research threads that can run simultaneously.

## Pattern Structure

```
Input → Orchestrator splits into N independent tasks → N agents work in parallel → Synthesis Agent combines → Output
```

Each agent works independently, then results are merged.

## Example 1: Multi-Source Market Research

**Objective**: Comprehensive market analysis from multiple data sources

**Architecture**:
```
User Input (market to research)
  ↓
Orchestrator: Define research questions, assign sources
  ↓
┌────────────┬────────────┬────────────┬────────────┐
│ Agent 1:   │ Agent 2:   │ Agent 3:   │ Agent 4:   │
│ Industry   │ Competitor │ Customer   │ Trend      │
│ Reports    │ Analysis   │ Interviews │ Analysis   │
└────────────┴────────────┴────────────┴────────────┘
  ↓            ↓            ↓            ↓
Synthesis Agent: Combine insights, identify patterns
  ↓
Output: Comprehensive market brief
```

**Agent Definitions**:

### Orchestrator
```
Role: Research Coordinator

Input:
- Market to research
- Research objectives
- Time/resource constraints

Task:
1. Define key research questions
2. Identify required sources
3. Assign one agent per source type
4. Set success criteria for each agent

Output:
{
  "research_questions": [
    "What is the market size and growth rate?",
    "Who are the key players and what are their strategies?",
    "What are emerging customer needs?",
    "What trends will shape the market?"
  ],
  "agent_assignments": [
    {
      "agent": "industry_reports_agent",
      "sources": ["Gartner", "Forrester", "IDC"],
      "questions": ["Market size", "Growth trends"],
      "deadline": "2 hours"
    },
    {
      "agent": "competitor_analysis_agent",
      "sources": ["Competitor websites", "G2", "Product Hunt"],
      "questions": ["Key players", "Positioning", "Pricing"],
      "deadline": "2 hours"
    }
  ]
}
```

### Industry Reports Agent (runs in parallel)
```
Role: Industry Data Researcher

Input:
- Research questions
- Source list (Gartner, Forrester, IDC, etc.)

Task:
Extract from industry reports:
1. Market size (TAM, SAM, SOM)
2. Growth rates (historical and projected)
3. Market segmentation
4. Key drivers and barriers

Output format:
"Industry Reports Findings:

**Market Size**:
- TAM: $X billion
- SAM: $Y billion  
- Growth rate: Z% CAGR (2024-2028)
- Source: [Report name, date]

**Segments**:
- Segment 1: $X billion (Y% share)
- Segment 2: $A billion (B% share)

**Key Drivers**:
1. [Driver 1] - [Explanation]
2. [Driver 2] - [Explanation]

**Barriers**:
1. [Barrier 1] - [Impact]

**Citations**: [Full source references]"

Note: Works independently, doesn't need other agents' outputs
```

### Competitor Analysis Agent (runs in parallel)
```
Role: Competitive Intelligence Analyst

Input:
- Research questions
- Competitor list or discovery prompt

Task:
Analyze top 10 competitors:
1. Market positioning
2. Product offerings
3. Pricing models
4. Customer base
5. Recent moves (funding, launches, partnerships)

Output format:
"Competitor Analysis:

**Market Leaders**:
1. [Company]: [$X revenue], [X% share], positioned as [category]
   - Strengths: [List]
   - Weaknesses: [List]
   - Recent: [Funding/product launches]

**Emerging Players**:
[Same format]

**Positioning Map**:
[Text-based matrix showing competitor positions]

**Pricing Landscape**:
- Low-end: $X-Y
- Mid-market: $A-B
- Enterprise: $C+

**Key Takeaways**:
- Market is [consolidated/fragmented]
- [Insight on competitive dynamics]"

Note: Can work while other agents research other topics
```

### Customer Insights Agent (runs in parallel)
```
Role: Voice of Customer Researcher

Input:
- Target customer profile
- Research questions about needs/pain points

Task:
Gather customer perspective through:
1. Review sites (G2, Capterra, TrustRadius)
2. Forums (Reddit, Quora, industry forums)
3. Social media mentions
4. Interview transcripts (if available)

Output format:
"Customer Insights:

**Top Pain Points** (by frequency):
1. [Pain point] - Mentioned by X% of sources
   - Quote: "[Customer quote]"
   - Impact: [How this affects them]

2. [Pain point] - Mentioned by Y%

**Unmet Needs**:
- [Need] - "[Evidence]"

**Buying Criteria** (what matters when choosing):
1. [Criterion] - [Why it matters]
2. [Criterion] - [Why it matters]

**Customer Journey Issues**:
- Discovery: [Challenge]
- Evaluation: [Challenge]  
- Onboarding: [Challenge]

**Sentiment Analysis**:
- Satisfaction with current solutions: [%]
- Willingness to switch: [High/Medium/Low]"

Note: Customer research happens independently of competitor analysis
```

### Trend Analysis Agent (runs in parallel)
```
Role: Market Trend Analyst

Input:
- Market/industry
- Timeframe (3-5 years forward)

Task:
Identify trends shaping market:

1. **Technology trends**: Emerging tech impacting market
2. **Regulatory trends**: Laws/compliance changes
3. **Economic trends**: Macro factors (funding, spending)
4. **Social trends**: Changing behaviors/preferences
5. **Competitive trends**: New business models, disruption

Output format:
"Trend Analysis:

**Technology Trends**:
1. [Trend]: [Description]
   - Impact on market: [How it changes things]
   - Timeline: [When this matters]
   - Opportunity/Threat: [Analysis]

**Critical Trends** (highest impact):
1. [Trend] - Will cause [change] within [timeframe]
2. [Trend] - Creates opportunity for [new approach]

**Weak Signals** (early indicators):
- [Signal]: Could lead to [potential disruption]

**Trend Intersections**:
- [Trend A] + [Trend B] = [Potential outcome]"

Note: Trend research is independent from current state analysis
```

### Synthesis Agent
```
Role: Research Synthesizer

Input:
- Industry Reports findings
- Competitor Analysis findings
- Customer Insights findings
- Trend Analysis findings

Task:
Combine all research into coherent story:

1. **Cross-validate**: Do sources agree? Where do they conflict?
2. **Find patterns**: What themes emerge across sources?
3. **Identify gaps**: What's missing? What needs more research?
4. **Create narrative**: Connect dots into insights
5. **Generate recommendations**: What should be done based on this?

Output format:
"Market Research Synthesis:

**Executive Summary** (3-4 paragraphs):
[Market size, competitive dynamics, customer needs, key trends - integrated story]

**Key Insights**:
1. [Insight combining multiple sources]
   - Evidence: [From industry reports + customer data]
2. [Insight about gap or opportunity]
   - Evidence: [From competitor analysis + trend analysis]

**Market Opportunities**:
1. [Opportunity]: Based on [customer need] + [trend] + [competitive gap]
2. [Opportunity]: [Reasoning]

**Strategic Recommendations**:
1. [Action]: Because [multi-source reasoning]
2. [Action]: Because [multi-source reasoning]

**Confidence Levels**:
- High confidence: [Claims with multiple source validation]
- Medium confidence: [Claims with limited sources]
- Low confidence: [Claims needing more research]

**Next Steps for Further Research**:
- [Gap 1]: Need [specific data]
- [Gap 2]: Need [validation]"

Quality criteria:
- Integrates ALL source agents
- Identifies contradictions explicitly
- Distinguishes facts from interpretation
- Provides actionable recommendations
```

## Example 2: Due Diligence (M&A or Investment)

**Objective**: Comprehensive company assessment

**Architecture**:
```
Target Company
  ↓
Orchestrator
  ↓
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ Financial│ Product  │ Customer │ Team     │ Legal    │
│ Agent    │ Agent    │ Agent    │ Agent    │ Agent    │
└──────────┴──────────┴──────────┴──────────┴──────────┘
  ↓
Risk Assessment Agent
  ↓
Investment Recommendation
```

**Parallel Agents**:
- **Financial Agent**: Revenue, burn, unit economics, projections
- **Product Agent**: Tech stack, roadmap, differentiation, IP
- **Customer Agent**: Retention, NPS, pipeline, concentration risk
- **Team Agent**: Key people, org structure, culture, retention
- **Legal Agent**: Cap table, contracts, litigation, compliance

Each investigates independently, then Risk Agent synthesizes.

## Example 3: Content Creation at Scale

**Objective**: Create 20 blog posts on related topics

**Architecture**:
```
Content Strategy
  ↓
Orchestrator: Define 20 topics, assign to agents
  ↓
┌─────────┬─────────┬─────────┐
│ Agent 1 │ Agent 2 │ Agent N │  (Each handles 1 post)
│ Topics  │ Topics  │ Topics  │
│ 1-5     │ 6-10    │ 16-20   │
└─────────┴─────────┴─────────┘
  ↓
Quality Check Agent
  ↓
SEO Optimization Agent
  ↓
20 Published Posts
```

Each agent writes posts independently, then batch processed for quality/SEO.

## When to Use Parallel Pattern

Use when:
- Tasks are independent (Agent A doesn't need Agent B's output)
- Time matters (parallelization speeds completion)
- Multiple perspectives needed (different angles on same problem)
- Scale matters (need to process many items)

Avoid when:
- Steps are sequential (Agent B needs Agent A's result)
- Synthesis is trivial (just concatenating results)
- Orchestration overhead exceeds benefits

## Implementation Guidelines

**Orchestrator design**:
- Define clear boundaries between parallel tasks
- Ensure tasks are truly independent
- Set uniform output formats (easier to synthesize)
- Build in error handling (what if one agent fails?)

**Synthesis strategy**:
- Look for convergence (multiple agents say same thing → high confidence)
- Flag contradictions (agents disagree → needs investigation)
- Weight by source quality (some sources more reliable)
- Identify gaps (what did no agent cover?)

**Parallelization benefits**:
- 4 agents in parallel = 4x faster (if truly parallel)
- More perspectives = better coverage
- Redundancy reduces risk of missing key info

**Common pitfall**: False parallelization
- If Agent B needs Agent A's output, they're not parallel
- Better to make sequential than force parallelization

## Optimization Strategies

**Caching**:
- If multiple agents need same data, fetch once and share
- Example: All agents need company description → fetch once

**Load balancing**:
- Distribute work evenly across agents
- Don't give one agent 80% of work

**Graceful degradation**:
- If one agent fails, others continue
- Synthesis notes what's missing
- Partial output still valuable

**Progressive synthesis**:
- Don't wait for all agents to finish
- Synthesize available results, update as more come in
- Useful for large-scale parallel work
