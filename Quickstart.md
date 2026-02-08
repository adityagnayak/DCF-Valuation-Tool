# Quick Start Guide - DCF Valuation Tool

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run dcf_valuation_tool.py
```

### Step 3: Use the Tool
The app will open in your browser at `http://localhost:8501`

---

## 📊 Sample Analysis Walkthrough

### Using Manual Input (Fastest Way to Start)

1. **Select "Manual Input"** in the sidebar
2. **Set projection years** to 5
3. **Enter data** (or use the pre-filled defaults):
   - Revenue growing at ~15% annually
   - Operating margins improving from 15% to 19%
   - Tax rate at 25%
   - Standard CapEx and working capital changes

4. **Click "Use Manual Input"**

5. **Enter valuation parameters**:
   - Cost of Equity: 10%
   - Cost of Debt: 5%
   - Tax Rate: 25%
   - Equity Weight: 70%
   - Debt Weight: 30%
   - Terminal Growth: 2.5%
   - Initial Outlay: $5,000,000
   - Required Return: 12%

6. **View Results**:
   - Scroll down to see NPV, IRR, and investment decision
   - Check out the 4 interactive charts
   - Download results to Excel

### Using Excel Upload

1. **Download the template** from the sidebar
2. **Open in Excel** and modify the values:
   - Keep the same column names
   - Add your projection data
   - Save the file

3. **Upload your file** using the file uploader
4. **Enter valuation parameters** as above
5. **Review results and charts**

---

## 🎯 Understanding Your Results

### Key Questions the Tool Answers

**Q: Should I make this investment?**
- Look at the "Investment Decision" section
- Green ✅ ACCEPT = Good investment
- Red ❌ REJECT = Poor investment
- Orange ⚠️ CONDITIONAL = Needs further review

**Q: What's the business worth?**
- Check "Enterprise Value" metric
- This is the total present value

**Q: What's my return?**
- NPV shows dollar value creation
- IRR shows percentage return
- Compare IRR to your hurdle rate

**Q: How sensitive is the valuation?**
- Check the "NPV Sensitivity" chart
- Shows how NPV changes with different WACC assumptions
- Steeper slope = more sensitive to discount rate

---

## 💡 Pro Tips

### For Better Valuations

1. **Use Conservative Assumptions**
   - Don't overestimate revenue growth
   - Use realistic operating margins
   - Check industry benchmarks

2. **Run Multiple Scenarios**
   - Base case (most likely)
   - Best case (optimistic)
   - Worst case (pessimistic)

3. **Validate Terminal Growth**
   - Should be ≤ GDP growth (2-4%)
   - Higher rates imply unrealistic perpetual growth

4. **Check Your WACC**
   - Typical range: 7-12% for most businesses
   - Higher for risky startups (15-20%)
   - Lower for stable companies (6-9%)

### Common Mistakes to Avoid

❌ Terminal growth > WACC (creates infinite value)
❌ Unrealistic margin expansion
❌ Forgetting to include terminal value
❌ Using cost of equity as WACC
❌ Equity + debt weights ≠ 100%

---

## 🔧 Troubleshooting

### "IRR shows N/A"
- This happens when cash flows are unusual
- NPV is still valid and primary decision metric
- Consider the cash flow pattern

### "NPV Sensitivity chart looks wrong"
- Check that WACC > Terminal Growth
- Ensure all cash flows are reasonable
- Verify initial outlay is correct

### "Upload fails"
- Ensure Excel file has all required columns
- Column names must match exactly
- Check for no empty rows at top

### "Can't install requirements"
- Update pip: `pip install --upgrade pip`
- Use Python 3.8 or higher
- Try: `pip install -r requirements.txt --user`

---

## 📚 Additional Resources

### Learning DCF
- Investment Banking textbooks (Rosenbaum & Pearl)
- CFA curriculum on equity valuation
- Online courses on corporate finance

### Improving Your Models
- Research industry benchmarks (CapIQ, Bloomberg)
- Study comparable company analyses
- Review actual company financial models

### Deployment
- Deploy to Streamlit Cloud for free
- Share link with colleagues
- Update code via GitHub

---

## 🆘 Need Help?

- Check the full README.md for detailed documentation
- Review test_dcf.py for calculation examples
- Open an issue on GitHub for bugs
- Email for support: [your-email]

---

## ✅ Checklist for Your First Valuation

- [ ] Gather 3-5 years of projection data
- [ ] Research appropriate discount rate (WACC)
- [ ] Determine terminal growth rate
- [ ] Calculate initial investment amount
- [ ] Set required return / hurdle rate
- [ ] Input all data into tool
- [ ] Review calculated FCFs for reasonableness
- [ ] Check NPV sensitivity analysis
- [ ] Export results to Excel
- [ ] Document assumptions and decision

---

**Ready to start? Run `streamlit run dcf_valuation_tool.py` now!**
