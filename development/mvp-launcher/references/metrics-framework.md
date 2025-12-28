# Metrics Framework by Stage

## Stage 0: Idea Validation (Pre-MVP)

**Focus:** Does anyone care?

**Track:**
- Number of problem interviews conducted (target: 20-50)
- % who say problem is "urgent" or "must-have" (need: >40%)
- Current solution spend/time investment
- Willingness to pay (specific $ amount, not "maybe")

**Output:** Go/No-Go decision based on problem intensity

## Stage 1: MVP Launch (Weeks 1-8)

**Focus:** Does the solution work?

**Critical metrics:**
1. **Activation rate** = (Users who complete core action) / (Total signups)
   - Target: >40% within first session
   - Below 20% = major UX/value prop problem

2. **Time to first value**
   - Target: <5 minutes ideal, <15 minutes acceptable
   - Measure: signup → first successful action

3. **D1/D7 retention**
   - D1 (next day): >40% good
   - D7 (week): >20% good
   - Below 10% = not sticky enough

4. **Payment conversion** (even if beta pricing)
   - >10% of activated users = problem validated
   - <5% = reconsider pricing or target audience

**Ignore:**
- Total user count (vanity metric)
- Traffic sources (too early to optimize)
- Social media followers
- Press coverage

**Weekly review:**
- 10 user interviews (why staying/leaving)
- Top 3 friction points identified
- 1 hypothesis tested

## Stage 2: Product-Market Fit Hunt (Months 2-6)

**Focus:** Who loves it and why?

**North Star Metric:** Choose ONE based on business model:
- SaaS: Weekly/Monthly Active Users (WAU/MAU)
- Marketplace: Gross Merchandise Volume (GMV)
- Usage-based: API calls / Actions completed
- Content: Time spent / Return visits

**Core metrics:**
1. **Retention cohorts**
   - Week 1: X% → Week 4: Y% → Week 12: Z%
   - Flatten curve = product-market fit signal
   - Target: 30%+ retained at Week 8

2. **NPS (Net Promoter Score)**
   - Survey: "How likely recommend 0-10?"
   - NPS = % Promoters (9-10) - % Detractors (0-6)
   - Target: >50 = strong product-market fit

3. **Organic growth rate**
   - % new users from referrals/word-of-mouth
   - Target: >20% = natural virality exists

4. **Revenue per user (ARPU)**
   - Track by cohort, by channel
   - Should be increasing MoM if learning/improving

**Unit economics (emerging):**
- LTV calculation (still early, use retention proxies)
- CAC by channel (start measuring)
- Contribution margin per user

**PMF signals:**
- Users complaining if product goes down
- Organic word-of-mouth referrals happening
- Pulling product from market would disappoint segment
- Usage becoming habitual (80%+ of users return weekly)

## Stage 3: Growth & Scale (Post-PMF)

**Focus:** Efficient customer acquisition

**Financial metrics:**
1. **LTV:CAC ratio**
   - Target: ≥3:1
   - Calculate: (ARPU × Gross Margin% × 1/Churn%) / CAC

2. **CAC Payback Period**
   - Target: ≤12 months
   - Calculate: CAC / (ARPU × Gross Margin%)

3. **Monthly Recurring Revenue (MRR) growth**
   - Early stage: 15-20% MoM
   - Later stage: 5-10% MoM sustainable

4. **Net Revenue Retention (NRR)**
   - Target: >100% (expansion > churn)
   - Great: >120%
   - Calculate: (Starting MRR + Expansion - Churn) / Starting MRR

5. **Churn rate**
   - Gross churn: <5% monthly (SaaS)
   - Net churn: negative ideal (expansion > churn)

**Operational metrics:**
1. **Customer Acquisition Cost (CAC) by channel**
   - Paid ads, content, referral, partnerships
   - Focus budget on CAC < 1/3 LTV channels

2. **Conversion funnel**
   - Visitor → Signup → Activation → Payment
   - Optimize bottleneck step only

3. **Sales efficiency**
   - Magic Number = (Net New MRR × 4) / Sales & Marketing Spend
   - Target: >0.75

**Growth channels:**
- Track CAC, conversion rate, volume potential per channel
- Double down on what works (power law distribution)
- Kill underperforming channels ruthlessly

## Stage 4: Mature Business

**Focus:** Profitability & defensibility

**Executive dashboard:**
1. **Rule of 40**
   - Growth Rate% + Profit Margin% ≥ 40
   - Benchmark for SaaS health

2. **Gross Margin**
   - Target: >70% (SaaS), >50% (marketplace)

3. **Operating Margin**
   - Path to profitability visible
   - Target: 20%+ at scale

4. **Cash flow & runway**
   - Months of runway remaining
   - Burn multiple = Cash Burned / Net New ARR

## Metric Anti-Patterns

**Vanity metrics (ignore these):**
- Registered users (vs active users)
- App downloads (vs usage)
- Page views (vs time spent / actions)
- Social media followers (unless core to model)
- Press mentions (unless drives revenue)

**Premature optimization:**
- Conversion funnel before product-market fit
- Complex attribution before meaningful volume
- A/B testing with <1000 users per variant
- Paid acquisition before unit economics proven

**Metrics that lie:**
- Average (use median and distribution)
- Cumulative charts (use cohorts)
- Monthly actives hiding declining engagement
- Revenue without churn/retention context

## Weekly Metrics Review Template

**For MVP/early stage:**

1. **Growth**
   - New users this week
   - Activation rate trend
   - D7 retention by cohort

2. **Engagement**
   - WAU/MAU ratio
   - Time spent / actions per user
   - Feature usage breakdown

3. **Revenue**
   - New MRR
   - Churn MRR
   - ARPU trend

4. **Qualitative**
   - User interviews completed
   - Top feature requests
   - Main churn reasons

5. **Decision**
   - What we learned
   - What we're testing next week
   - What we're stopping

## When Metrics Conflict

**Example:** High signups, low activation
→ Fix: Onboarding flow, value prop clarity

**Example:** Good retention, no growth
→ Fix: Distribution strategy, not product

**Example:** Growth + churn both high
→ Fix: Wrong target audience or unmet expectation

**Example:** Good engagement, won't pay
→ Fix: Pricing too high OR wrong monetization model OR targeting wrong segment

## Metric Calculation Scripts

Use provided scripts for quick calculation:
- `unit_economics.py` - LTV, CAC, payback period
- `market_sizer.py` - TAM/SAM/SOM
- `cohort_retention.py` - Retention curves (if you provide data)

## Red Flags in Metrics

🚨 **Kill signals:**
- Flat or declining engagement after 3 months
- Retention curve doesn't flatten (keeps dropping)
- LTV:CAC < 1:1 with no path to improvement
- Churn accelerating despite product improvements

⚠️ **Warning signals:**
- Growth slowing without intentional focus shift
- CAC rising faster than LTV
- Lengthening sales cycles
- Increasing support burden per user

✅ **Green lights:**
- Organic growth emerging
- Retention curves flattening
- Users self-organizing (communities forming)
- Expansion revenue > churn
- Decreasing support tickets per user over time
