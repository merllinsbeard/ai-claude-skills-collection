# Framework Completion Pattern

For work that fills predefined business frameworks with structured sections.

## Pattern Structure

```
Input + Framework Template → Orchestrator assigns sections → Sub-agents fill sections → Validation → Output
```

Each section filled independently or with context from other sections.

## Example 1: Business Model Canvas (BMC)

**Objective**: Complete 9-block BMC for a business idea

**Framework Structure**:
1. Customer Segments
2. Value Propositions
3. Channels
4. Customer Relationships
5. Revenue Streams
6. Key Resources
7. Key Activities
8. Key Partnerships
9. Cost Structure

**Architecture**:
```
User Input (business description, industry, target market)
  ↓
Orchestrator: Analyze input, identify focus areas, assign tasks
  ↓
9 Specialized Agents (one per BMC block)
  ↓
Cross-validation Agent: Check consistency
  ↓
Output: Completed BMC
```

**Agent Definitions**:

### Orchestrator
```
Role: BMC Strategy Coordinator

Input: 
- Business description
- Industry context
- Any existing information

Task:
1. Analyze business type (B2B/B2C, product/service, stage)
2. Identify what's known vs. needs research
3. Create focused prompts for each BMC block
4. Prioritize critical blocks (usually: Customer Segments, Value Prop, Revenue)

Output:
{
  "business_type": "B2B SaaS",
  "stage": "early_stage",
  "critical_blocks": ["customer_segments", "value_propositions"],
  "tasks": [
    {
      "block": "customer_segments",
      "prompt": "Based on [business description], identify 2-3 primary customer segments...",
      "context": "Early-stage B2B SaaS typically serves..."
    }
  ]
}
```

### Customer Segments Agent
```
Role: Customer Segment Identifier

Input:
- Business description
- Task from Orchestrator
- Industry context

Task:
Identify and describe 2-4 customer segments:

For each segment:
1. **Who**: Job titles, company size, industry
2. **Problems**: Top 3 pain points
3. **Characteristics**: Budget, decision process, urgency
4. **Size**: Rough market size estimate
5. **Priority**: Primary vs. secondary segment

Output format:
"Customer Segments:

**Primary Segment: [Name]**
- Who: [Description]
- Pain points: 
  1. [Problem 1]
  2. [Problem 2]
  3. [Problem 3]
- Characteristics: [Budget, decision-making, etc.]
- Market size: [Estimate]

**Secondary Segment: [Name]**
[Same structure]

Reasoning: Why these segments are most promising..."

Quality criteria:
- Specific (not "small businesses" but "5-50 person SaaS companies")
- Validated (based on research or reasoning)
- Prioritized (clear primary segment)
```

### Value Propositions Agent
```
Role: Value Proposition Developer

Input:
- Customer Segments (from previous agent)
- Business description
- Task from Orchestrator

Task:
For each customer segment, define value proposition:

1. **Core benefit**: What outcome do they get?
2. **Differentiation**: Why choose this over alternatives?
3. **Proof points**: Evidence this works (case studies, metrics, guarantees)

Output format:
"Value Propositions:

**For [Segment Name]:**
We help [customer segment] achieve [outcome] by [unique approach].

Unlike [alternatives], we [key differentiation].

This is proven by [proof points].

**For [Segment Name]:**
[Same structure]

Alignment check: These value props directly address pain points identified in Customer Segments."

Context:
- Reference customer segments to ensure alignment
- B2B value props often emphasize ROI, time savings, risk reduction
- B2C value props often emphasize convenience, status, enjoyment
```

### Revenue Streams Agent
```
Role: Revenue Model Designer

Input:
- Customer Segments
- Value Propositions
- Business description

Task:
Define revenue model:

1. **Pricing model**: Subscription, usage-based, transaction, license, etc.
2. **Price points**: Specific tiers or ranges
3. **Payment terms**: Monthly, annual, one-time
4. **Revenue mix**: % from each segment or product line

Output format:
"Revenue Streams:

**Model**: [Subscription / Usage / Hybrid / etc.]

**Pricing tiers**:
- Tier 1: $X/month - For [segment] - Includes [features]
- Tier 2: $Y/month - For [segment] - Includes [features]
- Enterprise: Custom - For [segment] - Includes [features]

**Revenue projections** (Year 1):
- Tier 1: [X customers] × $[price] = $[revenue]
- Tier 2: [Y customers] × $[price] = $[revenue]
- Total: $[revenue]

Reasoning: This pricing aligns with [customer segment] budgets and reflects [value delivered]."

Quality criteria:
- Pricing justified (comparable to competitors, aligned with value)
- Multiple streams if appropriate
- Realistic projections
```

### [Similar agents for remaining 6 blocks]

### Cross-validation Agent
```
Role: BMC Consistency Checker

Input: All 9 completed BMC blocks

Task:
Validate internal consistency:

1. **Segments ↔ Value Props**: Does each segment have matching value prop?
2. **Value Props ↔ Revenue**: Does pricing reflect value delivered?
3. **Key Activities ↔ Value Props**: Do activities support delivering value?
4. **Key Resources ↔ Activities**: Do resources enable activities?
5. **Partnerships ↔ Resources/Activities**: Do partnerships fill gaps?
6. **Costs ↔ Resources/Activities**: Are costs aligned with operations?

Output format:
"Consistency Check:

✅ Aligned:
- Customer segments and value props are well-matched
- Revenue model reflects value delivered

⚠️ Gaps identified:
- Key Activities don't mention [critical activity]
- Cost Structure seems low given [resource requirements]

🔧 Recommendations:
1. Add [activity] to Key Activities
2. Revise Cost Structure to include [cost category]"

Action: If gaps found, flag for human review or trigger revision agents
```

## Example 2: OKR Planning

**Objective**: Create company OKRs (Objectives & Key Results)

**Framework Structure**:
- Company Objective
- 3-5 Key Results per Objective
- Team-level OKRs (cascaded)

**Architecture**:
```
User Input (company goals, context)
  ↓
Objective Agent: Define 3-5 company objectives
  ↓
Key Results Agent: Create measurable KRs for each objective
  ↓
Cascade Agent: Break down to team-level OKRs
  ↓
Validation Agent: Check SMART criteria, alignment
  ↓
Output: Complete OKR tree
```

**Key Principles for OKRs**:

### Objective Agent
```
Role: Strategic Objective Setter

Input:
- Company vision/mission
- Current state
- Desired outcomes
- Timeframe (quarter/year)

Task:
Create 3-5 company-level objectives that are:
- **Aspirational**: Stretching but achievable
- **Qualitative**: Directional, not metric-based
- **Inspiring**: Motivating to teams
- **Time-bound**: Clear time horizon

Output format:
"Company Objectives (Q4 2025):

1. **Become the go-to platform for [market]**
   - Why: [Strategic reasoning]
   - Impact: [What success looks like]

2. **Deliver exceptional customer experience**
   - Why: [Strategic reasoning]
   - Impact: [What success looks like]

3. **Build scalable operational foundation**
   - Why: [Strategic reasoning]
   - Impact: [What success looks like]"

Quality criteria:
- 3-5 objectives (not more)
- Ambitious but realistic
- Aligned with company strategy
```

### Key Results Agent
```
Role: Key Results Definer

Input:
- Company Objectives (from previous agent)
- Current metrics baseline
- Available data/measurement capability

Task:
For each objective, create 3-5 Key Results:

**SMART criteria**:
- Specific: Exact metric
- Measurable: Number-based
- Achievable: Stretch but possible
- Relevant: Directly ladders to objective
- Time-bound: Due date

Output format:
"Objective 1: Become the go-to platform for [market]

Key Results:
1. Increase market share from 5% to 12%
   - Current: 5%
   - Target: 12%
   - Measurement: Monthly market survey
   
2. Achieve 40 NPS (currently 25)
   - Current: 25 NPS
   - Target: 40 NPS
   - Measurement: Quarterly NPS survey

3. Grow brand awareness from 15% to 35%
   - Current: 15%
   - Target: 35%
   - Measurement: Brand tracking study"

Quality criteria:
- Leading AND lagging indicators
- Baseline → target clearly defined
- Measurement method specified
- Ambitious (70% confidence to achieve)
```

## Example 3: GTM Strategy Framework

**Framework Structure**:
1. Market & Opportunity
2. Target Customers (ICP)
3. Value Proposition & Messaging
4. Go-to-Market Motion
5. Channels & Tactics
6. Success Metrics

**Implementation Tips**:
- Orchestrator ensures section dependencies are handled
- Some sections may need multiple passes (Value Prop often needs refinement)
- Build in validation checkpoints
- Allow human input between sections

## When to Use Framework Pattern

Use when:
- Work fits predefined structure (BMC, OKRs, SWOT, GTM)
- Sections have clear boundaries
- Framework is well-established
- Output must follow specific format

Avoid when:
- No clear framework exists (use Iterative Pattern)
- Linear dependency between steps (use Sequential Pattern)
- Framework needs to be created first

## Implementation Guide

1. **Map framework to agents**: One agent per section or combine related sections
2. **Define section dependencies**: Which sections need others completed first?
3. **Create validation checklist**: SMART criteria, internal consistency checks
4. **Build feedback loops**: Allow sections to be revised based on later sections
5. **Specify output format**: Exact structure for each section
