# Example Walkthrough - Real Estate Development Project

This example demonstrates how to use the DCF Valuation Tool to evaluate a real estate development investment opportunity.

## 📋 Project Overview

**Project:** Mixed-use development (retail + residential)
**Investment Required:** $10,000,000
**Project Timeline:** 5 years
**Exit Strategy:** Sell at end of Year 5

---

## 📊 Input Data

### Year-by-Year Projections

| Year | Revenue    | Op. Margin | Tax Rate | CapEx     | Δ NWC    | Depreciation |
|------|------------|------------|----------|-----------|----------|--------------|
| 1    | $2,500,000 | 18%        | 25%      | $500,000  | $150,000 | $200,000     |
| 2    | $3,000,000 | 20%        | 25%      | $400,000  | $100,000 | $250,000     |
| 3    | $3,600,000 | 22%        | 25%      | $350,000  | $80,000  | $300,000     |
| 4    | $4,200,000 | 24%        | 25%      | $300,000  | $60,000  | $350,000     |
| 5    | $5,000,000 | 25%        | 25%      | $250,000  | $50,000  | $400,000     |

### Capital Structure & Costs

- **Cost of Equity:** 12%
- **Cost of Debt:** 6%
- **Tax Rate:** 25%
- **Equity Weight:** 60%
- **Debt Weight:** 40%

**WACC Calculation:**
```
WACC = (12% × 60%) + (6% × (1 - 25%) × 40%)
WACC = 7.2% + 1.8%
WACC = 9.0%
```

### Terminal Value Parameters

- **Terminal Growth Rate:** 3.0% (stable rental income growth)
- **Initial Outlay:** $10,000,000
- **Required Return:** 15% (private equity hurdle rate)

---

## 🧮 Step-by-Step Calculation

### Step 1: Calculate Free Cash Flows

**Year 1:**
```
Revenue:              $2,500,000
Operating Margin:     × 18%
EBIT:                 = $450,000
Tax (25%):            - $112,500
NOPAT:                = $337,500
Add: Depreciation:    + $200,000
Less: CapEx:          - $500,000
Less: Δ NWC:          - $150,000
Free Cash Flow:       = ($112,500)    ← Negative due to high initial CapEx
```

**Year 2:**
```
Revenue:              $3,000,000
EBIT (20%):          $600,000
Tax:                  - $150,000
NOPAT:                = $450,000
Add: Depreciation:    + $250,000
Less: CapEx:          - $400,000
Less: Δ NWC:          - $100,000
Free Cash Flow:       = $200,000
```

**Year 3:**
```
Revenue:              $3,600,000
EBIT (22%):          $792,000
NOPAT:                $594,000
+ Depreciation:       $300,000
- CapEx:              ($350,000)
- Δ NWC:              ($80,000)
Free Cash Flow:       = $464,000
```

**Year 4:**
```
Revenue:              $4,200,000
EBIT (24%):          $1,008,000
NOPAT:                $756,000
+ Depreciation:       $350,000
- CapEx:              ($300,000)
- Δ NWC:              ($60,000)
Free Cash Flow:       = $746,000
```

**Year 5:**
```
Revenue:              $5,000,000
EBIT (25%):          $1,250,000
NOPAT:                $937,500
+ Depreciation:       $400,000
- CapEx:              ($250,000)
- Δ NWC:              ($50,000)
Free Cash Flow:       = $1,037,500
```

### Step 2: Calculate Present Values

| Year | FCF        | Discount Factor | PV of FCF  |
|------|------------|-----------------|------------|
| 1    | ($112,500) | 0.9174          | ($103,211) |
| 2    | $200,000   | 0.8417          | $168,340   |
| 3    | $464,000   | 0.7722          | $358,301   |
| 4    | $746,000   | 0.7084          | $528,466   |
| 5    | $1,037,500 | 0.6499          | $674,370   |

**Sum of PV of FCFs:** $1,626,266

### Step 3: Calculate Terminal Value

```
Final Year FCF:       $1,037,500
Growth Rate:          3.0%
WACC:                 9.0%

Terminal Value = FCF₅ × (1 + g) / (WACC - g)
Terminal Value = $1,037,500 × 1.03 / (0.09 - 0.03)
Terminal Value = $1,068,625 / 0.06
Terminal Value = $17,810,417

PV of Terminal Value = $17,810,417 × 0.6499
PV of Terminal Value = $11,575,890
```

### Step 4: Calculate Enterprise Value

```
PV of FCFs:           $1,626,266
PV of Terminal:       + $11,575,890
Enterprise Value:     = $13,202,156
```

### Step 5: Calculate NPV and IRR

```
Enterprise Value:     $13,202,156
Initial Outlay:       - $10,000,000
NPV:                  = $3,202,156    ✅ Positive!

IRR Calculation:
Cash Flows = [-$10,000,000, -$112,500, $200,000, $464,000, $746,000, $18,847,917]
                                                                      ↑ Includes terminal value
IRR ≈ 17.3%    ✅ Exceeds 15% hurdle rate!
```

---

## 🎯 Investment Decision

### Summary Metrics

| Metric              | Value        | Benchmark      | Status |
|---------------------|--------------|----------------|--------|
| **NPV**             | $3,202,156   | > 0            | ✅ Pass |
| **IRR**             | 17.3%        | > 15%          | ✅ Pass |
| **Payback Period**  | ~4.5 years   | < 5 years      | ✅ Pass |
| **MOIC (Multiple)** | 1.32x        | > 1.0x         | ✅ Pass |

### Decision: ✅ **ACCEPT**

**Reasoning:**
1. **Strong NPV:** Creates $3.2M in value above initial investment
2. **IRR Exceeds Hurdle:** 17.3% > 15% required return (230 bps spread)
3. **Positive All Years:** FCF positive from Year 2 onwards
4. **Conservative Assumptions:** 3% terminal growth is modest for real estate
5. **Multiple on Invested Capital:** 1.32x is solid for 5-year hold

---

## 📊 Sensitivity Analysis

### NPV Sensitivity to WACC

| WACC  | NPV          | Decision         |
|-------|--------------|------------------|
| 7%    | $5,234,890   | Strong Accept    |
| 8%    | $4,145,678   | Accept           |
| **9%**| **$3,202,156** | **Accept (Base)** |
| 10%   | $2,378,945   | Accept           |
| 11%   | $1,654,321   | Conditional      |
| 12%   | $1,012,456   | Marginal         |
| 13%   | $445,678     | Marginal         |

**Insight:** Project remains viable even with 2-3% higher WACC

### NPV Sensitivity to Terminal Growth

| Growth | Terminal Value | NPV         |
|--------|----------------|-------------|
| 2.0%   | $15,268,839    | $2,789,234  |
| 2.5%   | $16,443,750    | $2,956,789  |
| **3.0%** | **$17,810,417** | **$3,202,156** |
| 3.5%   | $19,400,000    | $3,498,234  |
| 4.0%   | $21,250,000    | $3,856,789  |

**Insight:** Even at conservative 2% growth, NPV is still positive

---

## 📈 Key Insights from Charts

### 1. Free Cash Flow Chart
- **Pattern:** J-curve (negative Year 1, then growing)
- **Interpretation:** Typical for development projects with upfront CapEx
- **Strength:** Strong FCF growth trend (Year 5 is 10x Year 2)

### 2. NPV Sensitivity Chart
- **Breakeven WACC:** ~13.5%
- **Current WACC:** 9% (450 bps safety margin)
- **Risk Assessment:** Moderate sensitivity - need to monitor debt costs

### 3. Revenue & EBIT Trends
- **CAGR Revenue:** 19% over 5 years
- **Margin Expansion:** 18% → 25% (700 bps improvement)
- **Driver:** Operational leverage as property stabilizes

### 4. Value Composition
- **Terminal Value:** 87.7% of enterprise value
- **Operating FCFs:** 12.3%
- **Implication:** Exit strategy critical - must achieve target sale price

---

## ⚠️ Risk Factors to Monitor

### High Risks
1. **Terminal Value Reliance:** 88% of value depends on exit
   - **Mitigation:** Build in alternative exit strategies
   
2. **Negative Year 1 FCF:** Puts pressure on financing
   - **Mitigation:** Ensure adequate equity cushion

3. **Market Cycle:** 5-year hold exposes to real estate cycles
   - **Mitigation:** Consider flexible exit timeline

### Medium Risks
4. **Operating Margin Assumptions:** 700 bps improvement is aggressive
   - **Mitigation:** Benchmark against comparable properties
   
5. **Occupancy Risk:** Revenue assumes stable leasing
   - **Mitigation:** Pre-lease anchor tenants

### Low Risks
6. **Interest Rate Risk:** Current WACC has 450 bps buffer
   - **Monitor:** Fed policy and refinancing needs

---

## 💡 Recommendations

### Before Proceeding
1. **✅ Conduct Market Study:** Validate revenue projections
2. **✅ Stress Test:** Run downside scenarios (recession, delayed lease-up)
3. **✅ Legal Review:** Ensure zoning and permits are secured
4. **✅ Financial Close:** Lock in debt terms before WACC changes
5. **✅ Operational Plan:** Detail path to 25% operating margin

### Deal Structure Suggestions
1. **Hurdle:** Use 15% preferred return for LP investors
2. **Waterfall:** Consider 80/20 split after hurdle
3. **Reserves:** Build in $500K contingency for CapEx overruns
4. **Guarantees:** Negotiate completion guarantee from developer

### Ongoing Monitoring
- **Quarterly:** Compare actual vs. projected FCF
- **Annual:** Update terminal value assumptions
- **Continuous:** Track comparable property sales for exit timing

---

## 📥 Using This in the Tool

### Manual Input Method
1. Set projection years to **5**
2. Enter each year's data as shown in the table
3. Set WACC components as specified
4. Set terminal growth to **3.0%**
5. Set initial outlay to **$10,000,000**
6. Set hurdle rate to **15%**

### Excel Upload Method
1. Download the template
2. Replace sample data with project data
3. Upload the file
4. Enter valuation parameters
5. Review results

---

## 🎓 Learning Points

### What This Example Teaches

1. **J-Curve Pattern:** Real estate projects often have negative early FCF
2. **Terminal Value Dominance:** Common in growth investments
3. **Margin Expansion:** Operating leverage can drive returns
4. **Sensitivity Testing:** Always stress test key assumptions
5. **Decision Framework:** Use multiple metrics (NPV, IRR, MOIC)

### Common Pitfalls to Avoid

❌ Ignoring negative early FCF in working capital planning
❌ Over-relying on terminal value without alternative exits
❌ Using aggressive growth rates without market validation
❌ Forgetting to include taxes in FCF calculation
❌ Mixing up WACC and cost of equity

---

## 📊 Results Summary

```
═══════════════════════════════════════════════════
       INVESTMENT RECOMMENDATION: ✅ ACCEPT
═══════════════════════════════════════════════════

Enterprise Value:        $13,202,156
Initial Investment:     -$10,000,000
                        ─────────────
Net Present Value:       $3,202,156

Internal Rate of Return:      17.3%
Required Return:              15.0%
Spread to Hurdle:             2.3%

Value Creation:          $3.2M (32% of investment)
Multiple on Investment:  1.32x

PRIMARY STRENGTHS:
• Strong IRR exceeding hurdle rate
• Positive NPV with margin of safety
• Clear path to value creation
• Improving operational metrics

KEY RISKS TO MANAGE:
• High terminal value dependence
• Negative Year 1 cash flow
• Operating margin expansion execution
• Market timing for exit

RECOMMENDATION: Proceed with investment, subject to:
1. Satisfactory due diligence
2. Locked-in debt terms
3. Operational plan validation
4. Exit strategy flexibility

═══════════════════════════════════════════════════
```

---

**This example demonstrates the complete workflow for evaluating a real investment opportunity using the DCF Valuation Tool.**
