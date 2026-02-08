import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="DCF Business Valuation Tool", layout="wide", page_icon="📊")

st.title("📊 DCF Business Valuation Tool")
st.markdown("---")

def calculate_wacc(cost_of_equity, cost_of_debt, tax_rate, equity_weight, debt_weight):
    """Calculate Weighted Average Cost of Capital"""
    return (cost_of_equity * equity_weight) + (cost_of_debt * (1 - tax_rate) * debt_weight)

def calculate_terminal_value(final_fcf, wacc, terminal_growth_rate):
    """Calculate terminal value using perpetuity growth method"""
    return final_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)

def calculate_npv_irr(cash_flows, discount_rate, initial_outlay):
    """Calculate NPV and IRR"""
    npv = -initial_outlay
    for i, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate) ** (i + 1))
    
    # IRR calculation using Newton-Raphson method
    all_cash_flows = np.array([-initial_outlay] + list(cash_flows))
    
    def npv_calc(rate, cash_flows):
        """Calculate NPV for a given rate"""
        return sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))
    
    def npv_derivative(rate, cash_flows):
        """Calculate derivative of NPV for Newton-Raphson"""
        return sum(-i * cf / (1 + rate) ** (i + 1) for i, cf in enumerate(cash_flows))
    
    try:
        # Newton-Raphson method for IRR
        rate = 0.1  # Initial guess
        for _ in range(100):  # Max iterations
            npv_val = npv_calc(rate, all_cash_flows)
            if abs(npv_val) < 1e-6:  # Converged
                break
            derivative = npv_derivative(rate, all_cash_flows)
            if abs(derivative) < 1e-10:  # Avoid division by zero
                rate = None
                break
            rate = rate - npv_val / derivative
            if rate < -0.99:  # IRR too negative, invalid
                rate = None
                break
        else:
            rate = None  # Did not converge
        
        irr = rate if rate is not None and not np.isnan(rate) else None
    except:
        irr = None
    
    return npv, irr

def create_sample_template():
    """Create a sample Excel template for users to download"""
    data = {
        'Year': [1, 2, 3, 4, 5],
        'Revenue': [1000000, 1150000, 1322500, 1520875, 1749006],
        'Operating_Margin_%': [15, 16, 17, 18, 19],
        'Tax_Rate_%': [25, 25, 25, 25, 25],
        'CapEx': [50000, 55000, 60000, 65000, 70000],
        'Change_in_NWC': [20000, 22000, 24000, 26000, 28000],
        'Depreciation': [40000, 44000, 48000, 52000, 56000]
    }
    return pd.DataFrame(data)

# Sidebar for input method selection
st.sidebar.header("Input Method")
input_method = st.sidebar.radio("Choose input method:", ["Manual Input", "Excel Upload"])

# Download template button
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Download Template")
template_df = create_sample_template()
buffer = BytesIO()
template_df.to_excel(buffer, index=False)
st.sidebar.download_button(
    label="Download Excel Template",
    data=buffer.getvalue(),
    file_name="dcf_template.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Initialize session state for data
if 'projection_data' not in st.session_state:
    st.session_state.projection_data = None

# Main content area
if input_method == "Excel Upload":
    st.subheader("📁 Upload Excel File")
    uploaded_file = st.file_uploader("Upload your Excel file with projections", type=['xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.session_state.projection_data = df
            st.success("✅ File uploaded successfully!")
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"Error reading file: {e}")

else:  # Manual Input
    st.subheader("✏️ Enter Projection Data Manually")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_years = st.number_input("Number of projection years:", min_value=1, max_value=10, value=5)
    
    with col2:
        st.write("")  # Spacing
    
    # Create input fields for each year
    projection_dict = {
        'Year': [],
        'Revenue': [],
        'Operating_Margin_%': [],
        'Tax_Rate_%': [],
        'CapEx': [],
        'Change_in_NWC': [],
        'Depreciation': []
    }
    
    st.markdown("#### Year-by-Year Projections")
    
    for year in range(1, num_years + 1):
        st.markdown(f"**Year {year}**")
        cols = st.columns(4)
        
        with cols[0]:
            revenue = st.number_input(f"Revenue (Y{year})", value=1000000.0 * (1.15 ** (year-1)), key=f"rev_{year}")
        with cols[1]:
            op_margin = st.number_input(f"Op. Margin % (Y{year})", value=15.0 + year - 1, key=f"margin_{year}")
        with cols[2]:
            tax_rate = st.number_input(f"Tax Rate % (Y{year})", value=25.0, key=f"tax_{year}")
        with cols[3]:
            depreciation = st.number_input(f"Depreciation (Y{year})", value=40000.0 * (1.1 ** (year-1)), key=f"dep_{year}")
        
        cols2 = st.columns(4)
        with cols2[0]:
            capex = st.number_input(f"CapEx (Y{year})", value=50000.0 * (1.1 ** (year-1)), key=f"capex_{year}")
        with cols2[1]:
            nwc_change = st.number_input(f"Δ NWC (Y{year})", value=20000.0 * (1.1 ** (year-1)), key=f"nwc_{year}")
        
        projection_dict['Year'].append(year)
        projection_dict['Revenue'].append(revenue)
        projection_dict['Operating_Margin_%'].append(op_margin)
        projection_dict['Tax_Rate_%'].append(tax_rate)
        projection_dict['CapEx'].append(capex)
        projection_dict['Change_in_NWC'].append(nwc_change)
        projection_dict['Depreciation'].append(depreciation)
        
        st.markdown("---")
    
    if st.button("📊 Use Manual Input"):
        st.session_state.projection_data = pd.DataFrame(projection_dict)
        st.success("✅ Manual data loaded successfully!")

# If we have projection data, proceed with valuation
if st.session_state.projection_data is not None:
    st.markdown("---")
    st.header("💰 Valuation Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Cost of Capital")
        cost_of_equity = st.number_input("Cost of Equity (%)", value=10.0, min_value=0.0, max_value=100.0) / 100
        cost_of_debt = st.number_input("Cost of Debt (%)", value=5.0, min_value=0.0, max_value=100.0) / 100
        tax_rate_wacc = st.number_input("Corporate Tax Rate (%)", value=25.0, min_value=0.0, max_value=100.0) / 100
    
    with col2:
        st.subheader("Capital Structure")
        equity_weight = st.number_input("Equity Weight (%)", value=70.0, min_value=0.0, max_value=100.0) / 100
        debt_weight = st.number_input("Debt Weight (%)", value=30.0, min_value=0.0, max_value=100.0) / 100
        
        if abs((equity_weight + debt_weight) - 1.0) > 0.01:
            st.warning("⚠️ Equity + Debt weights should equal 100%")
    
    with col3:
        st.subheader("Terminal Value & Investment")
        terminal_growth = st.number_input("Terminal Growth Rate (%)", value=2.5, min_value=0.0, max_value=10.0) / 100
        initial_outlay = st.number_input("Initial Investment Outlay ($)", value=5000000.0, min_value=0.0)
        required_return = st.number_input("Required Return/Hurdle Rate (%)", value=12.0, min_value=0.0, max_value=100.0) / 100
    
    # Calculate WACC
    wacc = calculate_wacc(cost_of_equity, cost_of_debt, tax_rate_wacc, equity_weight, debt_weight)
    
    st.markdown("---")
    st.header("📈 DCF Calculation")
    
    # Calculate Free Cash Flows
    df = st.session_state.projection_data.copy()
    
    df['EBIT'] = df['Revenue'] * (df['Operating_Margin_%'] / 100)
    df['Taxes'] = df['EBIT'] * (df['Tax_Rate_%'] / 100)
    df['NOPAT'] = df['EBIT'] - df['Taxes']
    df['Free_Cash_Flow'] = df['NOPAT'] + df['Depreciation'] - df['CapEx'] - df['Change_in_NWC']
    df['Discount_Factor'] = [(1 / (1 + wacc) ** i) for i in df['Year']]
    df['PV_of_FCF'] = df['Free_Cash_Flow'] * df['Discount_Factor']
    
    # Display calculation table
    st.subheader("Free Cash Flow Projections")
    
    # Format for display
    display_df = df.copy()
    currency_cols = ['Revenue', 'EBIT', 'Taxes', 'NOPAT', 'CapEx', 'Change_in_NWC', 
                     'Depreciation', 'Free_Cash_Flow', 'PV_of_FCF']
    
    for col in currency_cols:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(lambda x: f"${x:,.0f}")
    
    percentage_cols = ['Operating_Margin_%', 'Tax_Rate_%']
    for col in percentage_cols:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(lambda x: f"{x:.1f}%")
    
    display_df['Discount_Factor'] = display_df['Discount_Factor'].apply(lambda x: f"{x:.4f}")
    
    st.dataframe(display_df, use_container_width=True)
    
    # Calculate Terminal Value
    final_fcf = df['Free_Cash_Flow'].iloc[-1]
    terminal_value = calculate_terminal_value(final_fcf, wacc, terminal_growth)
    pv_terminal_value = terminal_value * df['Discount_Factor'].iloc[-1]
    
    # Calculate Enterprise Value
    pv_fcf_sum = df['PV_of_FCF'].sum()
    enterprise_value = pv_fcf_sum + pv_terminal_value
    
    # Calculate NPV and IRR
    cash_flows = df['Free_Cash_Flow'].values
    # Include terminal value in final year cash flow for NPV/IRR
    cash_flows_with_terminal = cash_flows.copy()
    cash_flows_with_terminal[-1] += terminal_value
    
    npv, irr = calculate_npv_irr(cash_flows_with_terminal, wacc, initial_outlay)
    
    # Investment Decision
    if npv > 0 and (irr is not None and irr > required_return):
        decision = "✅ ACCEPT"
        decision_color = "green"
        decision_reason = "NPV is positive and IRR exceeds the required return."
    elif npv > 0:
        decision = "⚠️ CONDITIONAL ACCEPT"
        decision_color = "orange"
        decision_reason = "NPV is positive but IRR may not exceed required return."
    else:
        decision = "❌ REJECT"
        decision_color = "red"
        decision_reason = "NPV is negative - project destroys value."
    
    # Display results
    st.markdown("---")
    st.header("🎯 Valuation Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("WACC", f"{wacc*100:.2f}%")
        st.metric("PV of FCFs", f"${pv_fcf_sum:,.0f}")
    
    with col2:
        st.metric("Terminal Value", f"${terminal_value:,.0f}")
        st.metric("PV of Terminal Value", f"${pv_terminal_value:,.0f}")
    
    with col3:
        st.metric("Enterprise Value", f"${enterprise_value:,.0f}")
        st.metric("Initial Outlay", f"${initial_outlay:,.0f}")
    
    with col4:
        st.metric("NPV", f"${npv:,.0f}", delta=f"{npv:,.0f}")
        if irr is not None:
            st.metric("IRR", f"{irr*100:.2f}%", delta=f"{(irr-required_return)*100:.2f}% vs hurdle")
        else:
            st.metric("IRR", "N/A")
    
    # Investment Decision Box
    st.markdown("---")
    st.markdown(f"### Investment Decision: <span style='color:{decision_color}; font-size:28px;'>{decision}</span>", unsafe_allow_html=True)
    st.info(f"**Reasoning:** {decision_reason}")
    
    st.markdown("---")
    st.header("📊 Visualizations")
    
    # Create tabs for different charts
    tab1, tab2, tab3, tab4 = st.tabs(["Free Cash Flows", "NPV Sensitivity", "Revenue & EBIT", "Valuation Breakdown"])
    
    with tab1:
        # FCF Chart
        fig_fcf = go.Figure()
        fig_fcf.add_trace(go.Bar(
            x=df['Year'],
            y=df['Free_Cash_Flow'],
            name='Free Cash Flow',
            marker_color='rgb(55, 83, 109)'
        ))
        fig_fcf.add_trace(go.Bar(
            x=df['Year'],
            y=df['PV_of_FCF'],
            name='PV of FCF',
            marker_color='rgb(26, 118, 255)'
        ))
        fig_fcf.update_layout(
            title='Free Cash Flows and Present Values',
            xaxis_title='Year',
            yaxis_title='Amount ($)',
            barmode='group',
            height=400
        )
        st.plotly_chart(fig_fcf, use_container_width=True)
    
    with tab2:
        # NPV Sensitivity Analysis
        wacc_range = np.linspace(max(0.01, wacc - 0.05), wacc + 0.05, 20)
        npv_values = []
        
        for w in wacc_range:
            discount_factors = [(1 / (1 + w) ** i) for i in df['Year']]
            pv_fcfs = df['Free_Cash_Flow'] * discount_factors
            tv = calculate_terminal_value(final_fcf, w, terminal_growth)
            pv_tv = tv * discount_factors[-1]
            ev = pv_fcfs.sum() + pv_tv
            npv_temp = ev - initial_outlay
            npv_values.append(npv_temp)
        
        fig_sensitivity = go.Figure()
        fig_sensitivity.add_trace(go.Scatter(
            x=wacc_range * 100,
            y=npv_values,
            mode='lines+markers',
            name='NPV',
            line=dict(color='rgb(26, 118, 255)', width=3)
        ))
        fig_sensitivity.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="NPV = 0")
        fig_sensitivity.add_vline(x=wacc*100, line_dash="dot", line_color="green", annotation_text="Current WACC")
        fig_sensitivity.update_layout(
            title='NPV Sensitivity to WACC',
            xaxis_title='WACC (%)',
            yaxis_title='NPV ($)',
            height=400
        )
        st.plotly_chart(fig_sensitivity, use_container_width=True)
    
    with tab3:
        # Revenue and EBIT over time
        fig_revenue = go.Figure()
        fig_revenue.add_trace(go.Scatter(
            x=df['Year'],
            y=df['Revenue'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color='rgb(55, 83, 109)', width=3)
        ))
        fig_revenue.add_trace(go.Scatter(
            x=df['Year'],
            y=df['EBIT'],
            mode='lines+markers',
            name='EBIT',
            line=dict(color='rgb(26, 118, 255)', width=3)
        ))
        fig_revenue.update_layout(
            title='Revenue and EBIT Projections',
            xaxis_title='Year',
            yaxis_title='Amount ($)',
            height=400
        )
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with tab4:
        # Valuation breakdown pie chart
        fig_pie = go.Figure(data=[go.Pie(
            labels=['PV of FCFs', 'PV of Terminal Value'],
            values=[pv_fcf_sum, pv_terminal_value],
            hole=.3
        )])
        fig_pie.update_layout(
            title='Enterprise Value Composition',
            height=400
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Export results
    st.markdown("---")
    st.subheader("📥 Export Results")
    
    # Create comprehensive results dataframe
    results_df = df[['Year', 'Revenue', 'EBIT', 'NOPAT', 'Free_Cash_Flow', 
                     'Discount_Factor', 'PV_of_FCF']].copy()
    
    # Add summary rows
    summary_data = {
        'Year': ['', 'Terminal Value', 'PV Terminal Value', '', 'Enterprise Value', 
                 'Initial Outlay', 'NPV', 'IRR', 'Decision'],
        'Revenue': ['', '', '', '', '', '', '', '', ''],
        'EBIT': ['', '', '', '', '', '', '', '', ''],
        'NOPAT': ['', '', '', '', '', '', '', '', ''],
        'Free_Cash_Flow': ['', terminal_value, '', '', '', '', '', '', ''],
        'Discount_Factor': ['', '', df['Discount_Factor'].iloc[-1], '', '', '', '', '', ''],
        'PV_of_FCF': [pv_fcf_sum, '', pv_terminal_value, '', enterprise_value, 
                      -initial_outlay, npv, irr if irr else 'N/A', decision]
    }
    
    summary_df = pd.DataFrame(summary_data)
    export_df = pd.concat([results_df, summary_df], ignore_index=True)
    
    buffer = BytesIO()
    export_df.to_excel(buffer, index=False, sheet_name='DCF Results')
    
    st.download_button(
        label="📊 Download Complete Results (Excel)",
        data=buffer.getvalue(),
        file_name="dcf_valuation_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.info("👈 Please select an input method and provide your projection data to begin the valuation.")
    
    # Show sample data explanation
    st.markdown("---")
    st.subheader("📋 Required Data Fields")
    st.markdown("""
    Your Excel file or manual input should include the following for each projection year:
    
    - **Year**: Projection year number (1, 2, 3, ...)
    - **Revenue**: Total revenue/sales
    - **Operating_Margin_%**: Operating margin as a percentage
    - **Tax_Rate_%**: Corporate tax rate as a percentage
    - **CapEx**: Capital expenditures
    - **Change_in_NWC**: Change in net working capital
    - **Depreciation**: Depreciation and amortization
    
    The tool will calculate EBIT, NOPAT, and Free Cash Flow automatically.
    """)

# Footer
st.markdown("---")
st.markdown("**DCF Business Valuation Tool** | Built with Streamlit | © 2024")
