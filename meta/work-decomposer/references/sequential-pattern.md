# Sequential Analysis Pattern

For work with clear linear steps where each step depends on previous output.

## Pattern Structure

```
Input → Step 1 → Step 2 → Step 3 → Output
```

Each agent completes its task before next agent starts.

## Example 1: Competitive Intelligence Pipeline

**Objective**: Analyze competitors' positioning, pricing, and ICP

**Architecture**:
```
User Input (industry, product category)
  ↓
Discovery Agent: Find competitors
  ↓
Scraping Agent: Extract landing page data
  ↓
Analysis Agent: Extract positioning elements
  ↓
Synthesis Agent: Create comparison table
  ↓
Output: Structured competitor analysis
```

**Agent Definitions**:

### Discovery Agent
```
Role: Competitive Intelligence Discoverer

Input: {industry}, {product_category}, {geography}

Task:
1. Identify 10-15 direct competitors
2. Validate they are active (website accessible)
3. Filter by relevance (similar offering, similar market)

Output format:
{
  "competitors": [
    {
      "name": "Company Name",
      "website": "https://...",
      "relevance_score": 0.9,
      "reasoning": "Direct competitor because..."
    }
  ]
}

Quality criteria:
- At least 8 active competitors
- Mix of established and emerging players
- Verified website accessibility
```

### Scraping Agent
```
Role: Landing Page Extractor

Input: {competitor_list} from Discovery Agent

Task:
For each competitor:
1. Access homepage and main product pages
2. Extract text content, headlines, CTAs
3. Identify key page sections (hero, features, pricing, testimonials)

Output format:
{
  "competitor_name": "...",
  "extracted_content": {
    "hero_headline": "...",
    "hero_subheadline": "...",
    "value_props": ["...", "..."],
    "features": ["...", "..."],
    "pricing_visible": true/false,
    "social_proof": ["...", "..."]
  }
}

Error handling:
- If URL inaccessible: mark as "data_unavailable"
- If structure unclear: extract raw text, note uncertainty
```

### Analysis Agent
```
Role: Positioning Analyzer

Input: {extracted_content} from Scraping Agent

Task:
For each competitor, extract:

1. **ICP indicators**:
   - Job titles mentioned
   - Company size signals ("enterprise", "SMB", "startup")
   - Industry focus
   - Pain points addressed

2. **UVP (Unique Value Proposition)**:
   - What they claim is unique
   - Key differentiators
   - Primary benefit stated

3. **Positioning**:
   - Market category they claim
   - How they frame the problem
   - Alternative they replace

4. **Pricing signals**:
   - Price points if visible
   - Pricing model (subscription, usage-based, enterprise)
   - Free tier availability

Output format: Structured JSON per competitor

Context:
- Look for implicit signals (language, imagery, case studies)
- B2B usually emphasizes ROI, integrations, security
- B2C usually emphasizes ease, speed, personal benefit
```

### Synthesis Agent
```
Role: Insight Synthesizer

Input: {analysis_results} from Analysis Agent

Task:
1. Create comparison table with columns:
   - Competitor
   - ICP
   - UVP
   - Positioning Category
   - Pricing Model
   - Key Differentiator

2. Identify patterns:
   - Common positioning approaches
   - Pricing clusters
   - Underserved ICP segments
   - Differentiation gaps

3. Generate insights:
   - Where is market crowded?
   - What positioning is unique?
   - Pricing opportunities
   - White space for new entrant

Output format:
- Excel/CSV with comparison table
- Summary paragraph with key insights
- Recommendations for competitive differentiation

Quality gates:
- All competitors have at least 80% fields filled
- Insights are specific, not generic
- Recommendations are actionable
```

## Example 2: Market Research Pipeline

**Objective**: Understand market size, trends, and customer needs

**Architecture**:
```
User Input (market to research)
  ↓
Data Collection Agent: Gather reports, articles, data
  ↓
Trend Analysis Agent: Extract key trends
  ↓
Sizing Agent: Estimate market size, growth
  ↓
Needs Agent: Identify customer pain points
  ↓
Synthesis Agent: Create market brief
```

**Implementation Tips**:
- Use web search for data collection
- Store intermediate results for review
- Allow human validation between agents
- Cache expensive operations (web scraping)

## When to Use Sequential Pattern

Use when:
- Each step clearly depends on previous output
- Order matters (can't parallelize)
- Work is primarily analytical (not creative)
- Single correct path exists

Avoid when:
- Steps are independent (use Parallel Pattern)
- Multiple iterations needed (use Iterative Pattern)
- Filling predefined structure (use Framework Pattern)
