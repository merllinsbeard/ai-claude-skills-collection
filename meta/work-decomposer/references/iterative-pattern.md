# Iterative Refinement Pattern

For work requiring multiple passes, critique, and improvement cycles.

## Pattern Structure

```
Input → Draft Agent → Critique Agent → Refine Agent → [Repeat] → Final Output
```

Work improves through cycles of generation, evaluation, and refinement.

## Example 1: Product Positioning Development

**Objective**: Develop market positioning that resonates with target audience

**Architecture**:
```
User Input (product, market, competitors)
  ↓
Research Agent: Gather market context
  ↓
Draft Positioning Agent: Create initial positioning
  ↓
Critique Agent: Evaluate against criteria
  ↓
Refinement Agent: Improve based on critique
  ↓
[Repeat critique → refinement 2-3 times]
  ↓
Validation Agent: Test with scenarios
  ↓
Final Output: Validated positioning
```

**Agent Definitions**:

### Research Agent
```
Role: Market Context Researcher

Input:
- Product description
- Target market
- Known competitors

Task:
Gather positioning context:
1. How do competitors position themselves?
2. What categories exist in market?
3. What customer problems are acknowledged?
4. What positioning approaches are saturated?
5. What language/terminology does market use?

Output format:
"Market Context:

**Competitive Positioning Map**:
- [Competitor 1]: Positions as [category] for [audience], emphasizes [key benefit]
- [Competitor 2]: Positions as [category] for [audience], emphasizes [key benefit]

**Category Analysis**:
- Established categories: [list]
- Emerging categories: [list]
- Oversaturated: [list]

**Customer Language**:
- Pain points mentioned: [list]
- Desired outcomes: [list]
- Common terminology: [list]

**White Space**:
- Positioning opportunities: [insights]"

Quality: Must be specific, based on actual competitor analysis
```

### Draft Positioning Agent
```
Role: Positioning Strategist

Input:
- Product description
- Research Agent output
- Target ICP

Task:
Create initial positioning statement:

Components:
1. **Category**: What are you? (existing category or new category)
2. **For who**: Specific target audience
3. **Key benefit**: Primary value delivered
4. **Differentiation**: Why choose this vs. alternatives
5. **Proof**: Evidence/credentials

Output format:
"Draft Positioning:

**Positioning Statement**:
[Product] is the [category] that helps [target audience] achieve [key benefit] by [unique approach].

Unlike [alternatives], we [differentiation].

**Category**: [New category OR position in existing category]
**For**: [Specific ICP description]
**Benefit**: [Outcome they get]
**Differentiator**: [What makes us unique]
**Proof**: [Why they should believe us]

**Messaging pillars** (3 key messages):
1. [Message 1]
2. [Message 2]
3. [Message 3]

**Rationale**: This positioning works because [reasoning]."

First draft emphasis: Be specific, avoid generic language
```

### Critique Agent
```
Role: Positioning Critic

Input:
- Draft positioning
- Market research
- Positioning best practices

Task:
Evaluate draft against criteria:

**Clarity** (1-10):
- Is it immediately understandable?
- Does it avoid jargon?
- Is target audience clear?

**Differentiation** (1-10):
- Does it stand out from competitors?
- Is differentiation meaningful?
- Would customers care about the difference?

**Credibility** (1-10):
- Is it believable?
- Do we have proof points?
- Does it match product reality?

**Resonance** (1-10):
- Would target audience connect with this?
- Does it address their pain points?
- Is language/tone appropriate?

**Memorability** (1-10):
- Is it simple enough to remember?
- Does it have a hook?
- Would it stick after one read?

Output format:
"Positioning Critique:

**Scores**:
- Clarity: 6/10
- Differentiation: 7/10
- Credibility: 8/10
- Resonance: 5/10
- Memorability: 6/10

**What works**:
✅ Differentiation is specific and defensible
✅ Category choice is clear
✅ We have proof points

**What needs work**:
❌ Language is too technical for target audience
❌ Key benefit is generic ("save time" - everyone says this)
❌ Messaging pillars don't connect to actual pain points

**Specific Issues**:
1. "Enterprise-grade platform" - cliché, everyone says this
2. Target audience too broad - need to narrow
3. Proof points are weak - need customer examples

**Recommendations**:
1. Replace "save time" with specific outcome (e.g., "launch products 50% faster")
2. Narrow to specific sub-segment (e.g., "Series A-B SaaS companies" instead of "startups")
3. Make messaging pillars problem-focused, not feature-focused

**Overall**: Positioning is on right track but needs sharper language and more customer empathy. Focus next iteration on resonance and memorability."

Action: Pass to Refinement Agent with specific improvement areas
```

### Refinement Agent
```
Role: Positioning Refiner

Input:
- Previous draft
- Critique with specific recommendations
- Original research

Task:
Improve positioning based on critique:

1. Address each critique point systematically
2. Keep what worked, fix what didn't
3. Make changes specific (not "make it clearer" but actual text changes)
4. Verify improvements against criteria

Output format:
"Refined Positioning (Iteration 2):

**Changes Made**:
- Narrowed audience from "startups" to "Series A-B SaaS companies (10-100 employees)"
- Replaced "save time" with specific outcome: "ship features 50% faster"
- Rewrote messaging pillars to be pain-focused:
  OLD: "Built for scalability"
  NEW: "Stop rebuilding your infrastructure every 6 months"

**Updated Positioning Statement**:
[Product] is the [category] that helps [target audience] achieve [key benefit] by [unique approach].

Unlike [alternatives], we [differentiation].

[Full positioning with improvements]

**How this addresses critique**:
- Clarity: Improved from 6 to 8 - more specific language
- Resonance: Improved from 5 to 7 - pain-focused messaging
- Memorability: Improved from 6 to 8 - specific metric (50% faster)

**Remaining questions**:
- Is "50% faster" credible? Need customer data.
- Does "Series A-B" resonate or is it too narrow?"

Next step: Pass back to Critique Agent or proceed to Validation Agent
```

### Validation Agent
```
Role: Positioning Validator

Input:
- Final refined positioning (after 2-3 iterations)
- Target customer profiles

Task:
Test positioning with scenarios:

**Scenario 1: Elevator pitch test**
"Explain positioning in 30 seconds to target customer. Does it land?"

**Scenario 2: Competitor comparison**
"Put positioning side-by-side with top 3 competitors. Does ours stand out?"

**Scenario 3: Sales objection test**
"What would skeptical customer say? Do we have answers?"

**Scenario 4: Internal alignment test**
"Would product, sales, marketing all agree this is accurate?"

Output format:
"Positioning Validation:

**Elevator Pitch Test**: ✅ Pass
- Clear value in 30 seconds
- Sparks interest/questions

**Competitor Comparison**: ✅ Pass  
- Clearly differentiated from [Competitor 1]
- Different enough from [Competitor 2]

**Objection Test**: ⚠️ Partial
- Objection: "How do you do 50% faster?"
- Answer: [Need to prepare proof points]

**Internal Alignment**: ✅ Pass
- Product team confirms feasibility
- Sales team confirms it addresses real objections

**Overall**: Positioning is validated and ready for market testing. Recommend preparing detailed proof points for "50% faster" claim.

**Next Steps**:
1. Create proof point document
2. Test with 5 target customers
3. Refine based on feedback"
```

## Example 2: Strategic Plan Development

**Objective**: Create 3-year strategic plan

**Architecture**:
```
Input (vision, current state, constraints)
  ↓
Draft Strategy Agent: Create initial plan
  ↓
Devil's Advocate Agent: Challenge assumptions
  ↓
Risk Agent: Identify risks
  ↓
Refinement Agent: Address weaknesses
  ↓
[Repeat 2-3 times]
  ↓
Scenario Planning Agent: Test under different futures
  ↓
Final Strategy
```

**Key Insight**: Good strategy emerges from multiple perspectives attacking the same problem.

### Devil's Advocate Agent
```
Role: Strategic Challenger

Task:
Challenge every major assumption in draft strategy:

1. **Market assumptions**: "What if market grows slower than expected?"
2. **Competitive assumptions**: "What if incumbent launches competing product?"
3. **Capability assumptions**: "Can we really execute this with current team?"
4. **Financial assumptions**: "What if funding environment worsens?"
5. **Customer assumptions**: "What if customers don't adopt as quickly?"

Output:
"Strategy Challenges:

**Weakest Assumptions**:
1. [Assumption] - Risk: [What could go wrong] - Impact: [High/Med/Low]
2. [Assumption] - Risk: [What could go wrong] - Impact: [High/Med/Low]

**Critical Questions**:
- [Question that must be answered]
- [Question that must be answered]

**Stress Tests**:
- What if revenue is 50% of projection?
- What if key competitor drops price by 40%?
- What if we can't hire planned headcount?

**Forced Trade-offs**:
If you could only keep ONE strategic initiative, which one? Why?"

This forces hard thinking about priorities and dependencies.
```

## Example 3: Messaging & Copy Development

**Architecture**:
```
Brief → Draft Copy → A/B Variation → Critique → Refine → Repeat
```

**Agents**:
- **Draft Agent**: Creates initial copy
- **Variation Agent**: Creates 2-3 different approaches
- **Critique Agent**: Evaluates against conversion criteria
- **Refinement Agent**: Improves based on critique
- **Testing Agent**: Simulates customer reactions

Multiple iterations until copy is sharp, clear, compelling.

## When to Use Iterative Pattern

Use when:
- Quality emerges through refinement (positioning, strategy, messaging)
- Multiple valid approaches exist
- Subjective judgment matters
- First draft is rarely final
- Critique improves output

Avoid when:
- Single correct answer exists (use Sequential Pattern)
- Speed matters more than quality
- Framework is rigid (use Framework Pattern)

## Implementation Guidelines

**Number of iterations**:
- Minimum: 2 (draft + 1 refinement)
- Typical: 3-4 (draft + 2-3 refinements)
- Maximum: 5 (diminishing returns after)

**When to stop iterating**:
- Critique scores stabilize (no improvement in successive iterations)
- Changes become minor (diminishing returns)
- Validation passes all scenarios
- Time/budget constraints

**Critique quality**:
- Specific, not generic ("Make it better" vs. "Replace 'save time' with specific metric")
- Actionable (agent can act on the feedback)
- Prioritized (what matters most)
- Balanced (what works + what needs work)

**Common pitfall**: Iterating without clear criteria leads to endless loops. Define "good enough" upfront.
