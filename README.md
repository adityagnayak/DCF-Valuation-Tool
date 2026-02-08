# DCF-Valuation-Tool
This package contains everything you need to deploy and run a professional DCF Business Valuation Tool.
# DCF Business Valuation Tool

A comprehensive Discounted Cash Flow (DCF) business valuation tool built with Streamlit. This interactive application allows users to perform DCF analysis either through manual input or Excel file upload, complete with visualizations, NPV/IRR calculations, and investment decision recommendations.

## Features

- **Flexible Input Methods**
  - Manual year-by-year data entry
  - Excel file upload for bulk data import
  - Downloadable Excel template

- **Comprehensive DCF Analysis**
  - Free Cash Flow (FCF) calculations
  - Weighted Average Cost of Capital (WACC)
  - Terminal Value using perpetuity growth method
  - Net Present Value (NPV)
  - Internal Rate of Return (IRR)

- **Investment Decision Framework**
  - Automatic accept/reject/conditional recommendations
  - Hurdle rate comparison
  - Clear decision reasoning

- **Interactive Visualizations**
  - Free Cash Flow projections with Present Values
  - NPV sensitivity analysis to WACC changes
  - Revenue and EBIT trends
  - Enterprise value composition breakdown

- **Export Capabilities**
  - Download complete results to Excel
  - All calculations and summaries included

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone this repository:
```bash
git clone <your-repo-url>
cd dcf-valuation-tool
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

1. Navigate to the project directory
2. Run the Streamlit app:
```bash
streamlit run dcf_valuation_tool.py
```

3. The app will open in your default browser at `http://localhost:8501`

### Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select the main branch and `dcf_valuation_tool.py` as the main file
5. Deploy!

## How to Use the Tool

### Method 1: Excel Upload

1. Download the sample template using the sidebar button
2. Fill in your projection data in the Excel file:
   - Year
   - Revenue
   - Operating_Margin_%
   - Tax_Rate_%
   - CapEx
   - Change_in_NWC
   - Depreciation

3. Upload the completed file
4. Enter valuation parameters (WACC components, terminal growth, initial outlay)
5. View results and charts

### Method 2: Manual Input

1. Select "Manual Input" from the sidebar
2. Choose the number of projection years
3. Enter data for each year in the form fields
4. Click "Use Manual Input"
5. Enter valuation parameters
6. View results and charts

## Valuation Parameters Explained

### Cost of Capital
- **Cost of Equity**: Expected return required by equity investors (typically 8-15%)
- **Cost of Debt**: Interest rate on debt (pre-tax)
- **Corporate Tax Rate**: Effective tax rate for tax shield calculation

### Capital Structure
- **Equity Weight**: Proportion of firm value financed by equity
- **Debt Weight**: Proportion of firm value financed by debt
- (Must sum to 100%)

### Terminal Value & Investment
- **Terminal Growth Rate**: Perpetual growth rate beyond projection period (typically 2-4%)
- **Initial Investment Outlay**: Upfront investment required
- **Required Return/Hurdle Rate**: Minimum acceptable IRR

## Understanding the Results

### Key Metrics

- **WACC**: Your discount rate for all cash flows
- **Enterprise Value**: Total present value of the business
- **NPV**: Net Present Value = Enterprise Value - Initial Outlay
- **IRR**: Internal Rate of Return on the investment

### Investment Decision Logic

- **ACCEPT ✅**: NPV > 0 AND IRR > Required Return
- **CONDITIONAL ACCEPT ⚠️**: NPV > 0 but IRR concerns
- **REJECT ❌**: NPV < 0 (investment destroys value)

## File Structure

```
dcf-valuation-tool/
│
├── dcf_valuation_tool.py    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file (optional)
```

## Technical Details

### Cash Flow Calculations

```
EBIT = Revenue × Operating Margin
Taxes = EBIT × Tax Rate
NOPAT = EBIT - Taxes
Free Cash Flow = NOPAT + Depreciation - CapEx - Δ NWC
```

### WACC Formula

```
WACC = (Cost of Equity × Equity Weight) + (Cost of Debt × (1 - Tax Rate) × Debt Weight)
```

### Terminal Value

```
Terminal Value = Final FCF × (1 + Terminal Growth Rate) / (WACC - Terminal Growth Rate)
```

### NPV Calculation

```
NPV = Σ [FCFt / (1 + WACC)^t] + [Terminal Value / (1 + WACC)^n] - Initial Outlay
```

## Common Use Cases

1. **Private Equity Investments**: Evaluate acquisition opportunities
2. **Startup Valuations**: Assess growth company valuations
3. **Capital Budgeting**: Decide on major capital projects
4. **Business Acquisitions**: Determine fair value for M&A
5. **Strategic Planning**: Test financial projections and scenarios

## Tips for Best Results

1. **Use Realistic Assumptions**: Conservative projections are better than optimistic
2. **Sensitivity Analysis**: Adjust WACC and terminal growth to test different scenarios
3. **Industry Benchmarks**: Use industry-standard margins and growth rates
4. **Multiple Scenarios**: Run best case, base case, and worst case
5. **Validate Inputs**: Ensure operating margins and growth rates are sustainable

## Limitations

- Uses perpetuity growth method for terminal value (alternatives: exit multiple method)
- Assumes constant WACC throughout projection period
- NPV uses numpy's IRR function which may not converge for complex cash flow patterns
- Does not account for:
  - Mid-year discounting convention
  - Excess cash or debt adjustments
  - Minority interest adjustments
  - Non-operating assets

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Changelog

### Version 1.0.0
- Initial release
- Manual and Excel input methods
- Full DCF valuation with NPV/IRR
- Interactive charts and visualizations
- Excel export functionality
- Investment decision framework
