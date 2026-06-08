import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Ramco Cement - NextGen Dealer Finance Lab",
    page_icon="🏗️",
    layout="wide"
)

# =========================================================
# STYLING
# =========================================================

st.markdown("""
<style>

.main-header{
background:linear-gradient(
135deg,
#8B0000 0%,
#B22222 50%,
#D64531 100%
);

padding:30px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;
}

.author-box{
font-size:14px;
color:#F8F8F8;
margin-top:15px;
}

.metric-card{
background:#FFF5F5;
padding:10px;
border-radius:10px;
border:1px solid #E74C3C;
}

.section-title{
background:#F8F9FA;
padding:10px;
border-radius:8px;
border-left:5px solid #B22222;
margin-top:10px;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""

<div class="main-header">

<h1>
🏗️ Ramco Cement — NextGen Dealer Finance Lab
</h1>

<h2>
Management Development Programme
</h2>

<h3>
Financial Management for Next Generation Dealers
</h3>

<p style="font-size:20px;">
Run Smarter • Grow Stronger • Lead the Future
</p>

<div class="author-box">

Developed and Designed by<br>

<b>Prof. Shalini Velappan</b><br>

Indian Institute of Management Tiruchirappalli

</div>

</div>

""", unsafe_allow_html=True)

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def currency(x):
    return f"₹{x:,.0f}"

def pct(x):
    return f"{x:.1f}%"

# =========================================================
# TAMIL INSIGHTS
# =========================================================

def tamil_insight(topic):

    insights = {

        "pnl": """
💡 தமிழ் விளக்கம்

Sales அதிகமாக இருப்பது மட்டும் போதாது.

Contribution தான் business-ஐ ஓட்டுகிறது.

Contribution =
Selling Price − Variable Cost

Contribution அதிகமானால்
Profit அதிகரிக்கும்.
""",

        "pricing": """
💡 தமிழ் விளக்கம்

Price குறைத்தால் volume அதிகரிக்கலாம்.

Price அதிகரித்தால் margin அதிகரிக்கலாம்.

சரியான balance முக்கியம்.
""",

        "credit": """
💡 தமிழ் விளக்கம்

Credit கொடுத்தால் sales அதிகரிக்கலாம்.

ஆனால் cash collection தாமதமாகும்.

Profit மட்டும் போதாது.

Cash Flow முக்கியம்.
""",

        "inventory": """
💡 தமிழ் விளக்கம்

Inventory அதிகமாக இருந்தால்

Cash stock-ல் சிக்கிக்கொள்ளும்.

Inventory குறைவாக இருந்தால்

Sales miss ஆகும்.
""",

        "cashflow": """
💡 தமிழ் விளக்கம்

Profit இருக்கலாம்.

ஆனால் Cash இல்லையென்றால்

Business கஷ்டப்படும்.

Cash Flow is King.
""",

        "growth": """
💡 தமிழ் விளக்கம்

Growth நல்லது.

ஆனால் uncontrolled growth

Cash crisis உருவாக்கலாம்.

Sustainable growth முக்கியம்.
""",

        "leadership": """
💡 தமிழ் விளக்கம்

Next Generation Dealer:

• Data பார்க்க வேண்டும்

• Team build செய்ய வேண்டும்

• Technology பயன்படுத்த வேண்டும்

• Long-term vision வைத்திருக்க வேண்டும்
"""
    }

    st.info(insights.get(topic, ""))

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/business.png",
    width=80
)

st.sidebar.title("🏗️ Finance Learning Lab")

language = st.sidebar.selectbox(

    "Language",

    [

        "English",

        "English + தமிழ்"

    ]

)

menu = st.sidebar.radio(
    "Choose Learning Module",
    [

        "🏠 Home Dashboard",

        "📊 Dealer P&L Lab",
        "🏗️ Dealer Economics Simulator",

        "💰 Pricing Decision Simulator",

        "🤝 Credit Management Lab",

        "📦 Inventory Management Lab",

        "💵 Working Capital & Cash Flow Lab",

        "🚨 Cash Flow Crisis Simulation",

        "🌤️ Seasonal Planning",

        "🎁 Scheme & Target Planner",

        "📈 Growth Decision Simulator",

        "💻 Digital Transformation Readiness",

        "🌟 NextGen Leadership",

        "📊 Dealer Reflection & Financial Scorecard",

        "📝 90-Day Action Plan",

        "🏆 Hall of Fame",

        "🏆 Graduation Certificate"

    ]
)

# =========================================================
# HOME DASHBOARD
# =========================================================

if menu == "🏠 Home Dashboard":

    st.title("Welcome to the NextGen Dealer Finance Lab")

    st.markdown("""
This experiential learning platform helps you understand:

✅ Profitability

✅ Pricing

✅ Credit Management

✅ Inventory Management

✅ Working Capital

✅ Cash Flow

✅ Growth Decisions

✅ Digital Transformation

✅ Leadership

through simulations, visual dashboards and business decision exercises.
""")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Modules", "17")

    col2.metric("Simulations", "7")

    col3.metric("Business Cases", "10")

    col4.metric("Reflection Exercises", "5")

    st.markdown("---")

    roadmap = pd.DataFrame({

        "Learning Journey":[

            "Understand Profit",

            "Price Correctly",

            "Manage Credit",

            "Control Inventory",

            "Improve Cash Flow",

            "Grow Smartly",

            "Lead the Future"

        ]

    })

    st.dataframe(
        roadmap,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.success("""

🎯 இந்த Finance Lab மூலம்

• Profit எப்படி உருவாகிறது

• Cash Flow எப்படி improve செய்வது

• Inventory எப்படி control செய்வது

• Growth எப்படி plan செய்வது

• Business எப்படி scale செய்வது

என்பதை கற்றுக்கொள்வீர்கள்.

""")
# =========================================================
# DEALER P&L LAB
# =========================================================

elif menu == "📊 Dealer P&L Lab":

    st.header("📊 Dealer P&L Lab")

    st.markdown("""
### How Does a Cement Dealer Make Money?

Revenue

− Purchase Cost

− Transport Cost

− Labour Cost

= Contribution

Contribution

− Fixed Expenses

= Profit
""")

    # ==========================================
    # INPUTS
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        monthly_bags = st.number_input(
            "Monthly Bags Sold",
            value=5000
        )

        selling_price = st.number_input(
            "Selling Price per Bag (₹)",
            value=390.0
        )

        purchase_price = st.number_input(
            "Purchase Price per Bag (₹)",
            value=340.0
        )

    with col2:

        transport_cost = st.number_input(
            "Transport Cost per Bag (₹)",
            value=15.0
        )

        labour_cost = st.number_input(
            "Labour Cost per Bag (₹)",
            value=5.0
        )

        fixed_cost = st.number_input(
            "Monthly Fixed Expenses (₹)",
            value=60000.0
        )

    # ==========================================
    # CALCULATIONS
    # ==========================================

    revenue = monthly_bags * selling_price

    variable_cost = monthly_bags * (
        purchase_price +
        transport_cost +
        labour_cost
    )

    contribution = revenue - variable_cost

    profit = contribution - fixed_cost

    contribution_per_bag = (

        selling_price
        - purchase_price
        - transport_cost
        - labour_cost

    )

    contribution_ratio = (

        contribution_per_bag /
        selling_price

    ) * 100

    break_even_bags = (

        fixed_cost /
        contribution_per_bag

        if contribution_per_bag > 0

        else 0

    )

    margin_of_safety = (

        (monthly_bags - break_even_bags)

        /

        monthly_bags

    ) * 100

    # ==========================================
    # KPI CARDS
    # ==========================================

    st.subheader("📈 Dealer Financial Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Revenue",
        currency(revenue)
    )

    c2.metric(
        "Contribution",
        currency(contribution)
    )

    c3.metric(
        "Profit",
        currency(profit)
    )

    c4.metric(
        "Contribution/Bag",
        currency(contribution_per_bag)
    )

    # ==========================================
    # VISUAL CHART
    # ==========================================

    pnl_df = pd.DataFrame({

        "Item":[

            "Revenue",
            "Variable Cost",
            "Fixed Cost",
            "Profit"

        ],

        "Amount":[

            revenue,
            variable_cost,
            fixed_cost,
            profit

        ]

    })

    fig = px.bar(

        pnl_df,

        x="Item",

        y="Amount",

        title="Dealer Profit Structure"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # BREAK EVEN
    # ==========================================

    st.subheader("🎯 Break-even Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Break-even Bags",
        round(break_even_bags)
    )

    col2.metric(
        "Contribution Ratio",
        pct(contribution_ratio)
    )

    col3.metric(
        "Margin of Safety",
        pct(margin_of_safety)
    )

    # ==========================================
    # BREAK EVEN VISUAL
    # ==========================================

    sales_range = np.arange(
        0,
        monthly_bags * 1.5,
        100
    )

    total_revenue = sales_range * selling_price

    total_cost = (

        sales_range *

        (
            purchase_price +
            transport_cost +
            labour_cost
        )

        +

        fixed_cost

    )

    fig2 = go.Figure()

    fig2.add_trace(

        go.Scatter(

            x=sales_range,

            y=total_revenue,

            mode="lines",

            name="Revenue"

        )

    )

    fig2.add_trace(

        go.Scatter(

            x=sales_range,

            y=total_cost,

            mode="lines",

            name="Total Cost"

        )

    )

    fig2.add_vline(

        x=break_even_bags,

        line_dash="dash"

    )

    fig2.update_layout(

        title="Break-even Chart",

        xaxis_title="Bags Sold",

        yaxis_title="₹"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ==========================================
    # FORMULA EXPLANATION
    # ==========================================

    st.subheader("📘 Learn the Formula")

    with st.expander("Contribution Formula"):

        st.latex(r'''
Contribution
=
Revenue
-
Variable\ Cost
''')

        st.write(f"""

Revenue = {currency(revenue)}

Variable Cost = {currency(variable_cost)}

Contribution = {currency(contribution)}

""")

    with st.expander("Break-even Formula"):

        st.latex(r'''
BreakEven
=
\frac{FixedCost}
{ContributionPerBag}
''')

        st.write(f"""

Break-even Bags

=

{fixed_cost:,.0f}

÷

{contribution_per_bag:.2f}

=

{break_even_bags:.0f} bags

""")

    # ==========================================
    # KNOWLEDGE CHECK
    # ==========================================

    st.subheader("🎯 Quick Knowledge Check")

    answer = st.radio(

        "If contribution per bag increases, what happens to break-even sales?",

        [

            "Increase",

            "Decrease",

            "No Change"

        ]

    )

    if st.button("Check Answer"):

        if answer == "Decrease":

            st.success(
                "Correct! Higher contribution means fewer bags required to cover fixed costs."
            )

        else:

            st.error(
                "Not quite. Higher contribution lowers break-even sales."
            )

    # ==========================================
    # TAMIL LEARNING
    # ==========================================

    if language == "English + தமிழ்":

        tamil_insight("pnl")

    # ==========================================
    # REFLECTION
    # ==========================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What is the biggest cost driver in your dealership?"
    )

    st.text_area(
        "How can you improve contribution per bag?"
    )

    st.success("""

Key Learning:

Revenue is vanity.

Contribution is reality.

Cash flow is survival.

Profit is reward.

""")
# =========================================================
# DEALER ECONOMICS SIMULATOR
# =========================================================

elif menu == "🏗️ Dealer Economics Simulator":

    st.header("🏗️ Dealer Economics Simulator")

    st.markdown("""
    ### Understanding Real Dealer Profitability

    This simulator helps visualize how:

    - Quantity Discounts
    - Target Incentives
    - Cash Discounts
    - Price Discounts
    - Labour Costs
    - Delivery Costs
    - Credit Days
    - Inventory Days

    impact dealer profitability and cash flow.
    """)

    # =====================================================
    # INPUTS
    # =====================================================

    st.subheader("📥 Dealer Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:

        billing_price = st.number_input(
            "Billing Price (₹/Bag)",
            value=365.0
        )

        selling_price = st.number_input(
            "Selling Price (₹/Bag)",
            value=330.0
        )

        monthly_volume = st.number_input(
            "Monthly Volume (Bags)",
            value=5000
        )

    with col2:

        quantity_discount = st.number_input(
            "Quantity Discount (₹/Bag)",
            value=3.0
        )

        target_incentive = st.number_input(
            "Target Incentive (₹/Bag)",
            value=5.0
        )

        cash_discount = st.number_input(
            "Cash Discount (₹/Bag)",
            value=2.0
        )

    with col3:

        price_discount = st.number_input(
            "Price Discount Given to Customer (₹/Bag)",
            value=5.0
        )

        labour_cost = st.number_input(
            "Labour Cost (₹/Bag)",
            value=5.5
        )

        delivery_cost = st.number_input(
            "Delivery Cost (₹/Bag)",
            value=2.0
        )

        other_cost = st.number_input(
            "Other Cost (₹/Bag)",
            value=1.0
        )

    # =====================================================
    # CALCULATIONS
    # =====================================================

    effective_cost = (
        billing_price
        - quantity_discount
        - target_incentive
        - cash_discount
    )

    effective_selling_price = (
        selling_price
        - price_discount
    )

    trading_margin = (
        effective_selling_price
        - effective_cost
    )

    net_profit_per_bag = (
        trading_margin
        - labour_cost
        - delivery_cost
        - other_cost
    )

    monthly_profit = (
        net_profit_per_bag
        * monthly_volume
    )

    total_incentives = (
        quantity_discount
        + target_incentive
        + cash_discount
    )

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.subheader("📊 Dealer Economics Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Effective Cost",
        f"₹{effective_cost:.2f}"
    )

    c2.metric(
        "Effective Selling Price",
        f"₹{effective_selling_price:.2f}"
    )

    c3.metric(
        "Trading Margin",
        f"₹{trading_margin:.2f}"
    )

    c4.metric(
        "Net Profit/Bag",
        f"₹{net_profit_per_bag:.2f}"
    )

    st.metric(
        "Monthly Profit",
        f"₹{monthly_profit:,.0f}"
    )

    # =====================================================
    # INCENTIVE ANALYSIS
    # =====================================================

    st.subheader("🎯 Incentive Contribution Analysis")

    incentive_df = pd.DataFrame({

        "Incentive":[
            "Quantity Discount",
            "Target Incentive",
            "Cash Discount"
        ],

        "₹/Bag":[
            quantity_discount,
            target_incentive,
            cash_discount
        ]

    })

    st.dataframe(
        incentive_df,
        use_container_width=True
    )

    st.success(
        f"Total Incentive Benefit = ₹{total_incentives:.2f}/Bag"
    )

    # =====================================================
    # PROFITABILITY BRIDGE
    # =====================================================

    st.subheader("🌉 Dealer Profitability Bridge")

    bridge_df = pd.DataFrame({

        "Particulars":[

            "Billing Price",
            "Quantity Discount",
            "Target Incentive",
            "Cash Discount",
            "Effective Cost",

            "Selling Price",
            "Price Discount",
            "Effective Selling Price",

            "Trading Margin",

            "Labour Cost",
            "Delivery Cost",
            "Other Cost",

            "Net Profit"

        ],

        "₹":[

            billing_price,
            -quantity_discount,
            -target_incentive,
            -cash_discount,
            effective_cost,

            selling_price,
            -price_discount,
            effective_selling_price,

            trading_margin,

            -labour_cost,
            -delivery_cost,
            -other_cost,

            net_profit_per_bag

        ]

    })

    st.dataframe(
        bridge_df,
        use_container_width=True
    )

    # =====================================================
    # PROFIT DRIVER CHART
    # =====================================================

    st.subheader("📈 Profit Driver Analysis")

    chart_df = pd.DataFrame({

        "Component":[
            "Trading Margin",
            "Incentives",
            "Labour",
            "Delivery",
            "Other Cost",
            "Net Profit"
        ],

        "Amount":[
            trading_margin,
            total_incentives,
            -labour_cost,
            -delivery_cost,
            -other_cost,
            net_profit_per_bag
        ]

    })

    fig = px.bar(
        chart_df,
        x="Component",
        y="Amount",
        title="Dealer Profit Drivers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # WORKING CAPITAL ANALYSIS
    # =====================================================

    st.subheader("💰 Working Capital Analysis")

    col1, col2 = st.columns(2)

    with col1:

        credit_days = st.slider(
            "Customer Credit Days",
            0,
            120,
            30
        )

    with col2:

        inventory_days = st.slider(
            "Inventory Days",
            0,
            120,
            30
        )

    monthly_sales_value = (
        effective_selling_price
        * monthly_volume
    )

    receivables = (
        monthly_sales_value
        * credit_days
        / 30
    )

    inventory_value = (
        effective_cost
        * monthly_volume
        * inventory_days
        / 30
    )

    working_capital = (
        receivables
        + inventory_value
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Receivables",
        f"₹{receivables:,.0f}"
    )

    c2.metric(
        "Inventory Investment",
        f"₹{inventory_value:,.0f}"
    )

    c3.metric(
        "Working Capital",
        f"₹{working_capital:,.0f}"
    )

    # =====================================================
    # DEALER HEALTH SCORE
    # =====================================================

    st.subheader("🚦 Dealer Health Score")

    health_score = 100

    if credit_days > 60:
        health_score -= 20

    if inventory_days > 60:
        health_score -= 20

    if net_profit_per_bag < 0:
        health_score -= 30

    if price_discount > 10:
        health_score -= 10

    health_score = max(0, health_score)

    st.progress(health_score / 100)

    st.metric(
        "Dealer Health Score",
        f"{health_score}/100"
    )

    if health_score >= 80:
        st.success("🟢 Healthy Dealer")

    elif health_score >= 60:
        st.warning("🟠 Moderate Risk")

    else:
        st.error("🔴 High Financial Risk")

    # =====================================================
    # SMART INSIGHTS
    # =====================================================

    st.subheader("🧠 Dealer Insights")

    if price_discount > trading_margin:
        st.warning(
            "Price discount is consuming most of your margin."
        )

    if credit_days > 60:
        st.error(
            "High collection risk detected."
        )

    if inventory_days > 60:
        st.warning(
            "Inventory is locking significant working capital."
        )

    if net_profit_per_bag < 0:
        st.error(
            "Current configuration is loss-making."
        )

    if net_profit_per_bag > 10:
        st.success(
            "Healthy profitability detected."
        )

    # =====================================================
    # FINAL LEARNING
    # =====================================================

    st.info("""

### Key Takeaways

✓ Sales ≠ Profit

✓ Profit ≠ Cash

✓ Quantity Discounts improve effective cost

✓ Target Incentives drive dealer behaviour

✓ Cash Discounts improve liquidity

✓ Credit Days increase receivables

✓ Inventory Days increase working capital

### Sustainable Dealer Success

Margin
+
Incentives
+
Collections
+
Inventory Control
+
Cost Discipline

=
Long-Term Profitability

""")
# =========================================================
# PRICING DECISION SIMULATOR
# =========================================================

elif menu == "💰 Pricing Decision Simulator":

    st.header("💰 Pricing Decision Simulator")

    st.markdown("""

### Pricing is one of the most powerful decisions in a dealership.

A small change in price can significantly impact:

✅ Sales Volume

✅ Profitability

✅ Market Share

✅ Customer Retention

""")

    # =====================================================
    # INPUTS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        current_price = st.slider(
            "Current Selling Price (₹ per Bag)",
            300,
            500,
            390
        )

        proposed_price = st.slider(
            "Proposed Selling Price (₹ per Bag)",
            300,
            500,
            400
        )

    with col2:

        monthly_volume = st.number_input(
            "Current Monthly Volume",
            value=5000
        )

        purchase_cost = st.number_input(
            "Purchase Cost per Bag",
            value=340
        )

    # =====================================================
    # ELASTICITY ASSUMPTION
    # =====================================================

    elasticity = -1.5

    price_change_pct = (

        (proposed_price - current_price)

        /

        current_price

    )

    volume_change_pct = (

        elasticity *

        price_change_pct

    )

    projected_volume = (

        monthly_volume *

        (1 + volume_change_pct)

    )

    projected_volume = max(
        projected_volume,
        0
    )

    # =====================================================
    # CURRENT BUSINESS
    # =====================================================

    current_profit = (

        current_price -
        purchase_cost

    ) * monthly_volume

    # =====================================================
    # NEW BUSINESS
    # =====================================================

    projected_profit = (

        proposed_price -
        purchase_cost

    ) * projected_volume

    # =====================================================
    # KPI DISPLAY
    # =====================================================

    st.subheader("📊 Pricing Impact Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Projected Volume",
        f"{projected_volume:,.0f}"
    )

    c2.metric(
        "Current Profit",
        currency(current_profit)
    )

    c3.metric(
        "Projected Profit",
        currency(projected_profit)
    )

    # =====================================================
    # PROFIT COMPARISON
    # =====================================================

    compare_df = pd.DataFrame({

        "Scenario":[

            "Current",
            "Proposed"

        ],

        "Profit":[

            current_profit,
            projected_profit

        ]

    })

    fig = px.bar(

        compare_df,

        x="Scenario",

        y="Profit",

        title="Profit Comparison"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # DEALER INSIGHT
    # =====================================================

    st.subheader("🎯 Business Insight")

    if projected_profit > current_profit:

        st.success("""

Price change improves profitability.

Higher price is generating better business performance.

""")

    elif projected_profit < current_profit:

        st.warning("""

Price change reduces profitability.

Volume loss is larger than margin gain.

""")

    else:

        st.info("""

No major change in profitability.

""")

    # =====================================================
    # COMPETITOR SIMULATION
    # =====================================================

    st.subheader("⚔️ Competitor Response Simulation")

    competitor_price = st.slider(

        "Competitor Selling Price",

        300,
        500,
        385

    )

    if proposed_price > competitor_price + 15:

        st.error("""

Competitor has pricing advantage.

Risk of losing market share.

""")

    elif proposed_price < competitor_price:

        st.success("""

Your pricing is competitive.

Potential volume gain possible.

""")

    else:

        st.warning("""

Prices are closely matched.

Service quality becomes important.

""")

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("Price Elasticity Concept"):

        st.latex(r'''
\%\ Change\ in\ Volume

=

Elasticity

\times

\%\ Change\ in\ Price
''')

        st.markdown("""

### Interpretation

If elasticity is -1.5:

1% increase in price

↓

1.5% decrease in volume

Customers react to pricing changes.

""")

    with st.expander("Profit Formula"):

        st.latex(r'''
Profit

=

(Price - Cost)

\times

Quantity
''')

        st.markdown(f"""

Example:

Profit

=

({proposed_price} - {purchase_cost})

×

{projected_volume:,.0f}

=

₹{projected_profit:,.0f}

""")

    # =====================================================
    # KNOWLEDGE CHECK
    # =====================================================

    st.subheader("🎯 Quick Knowledge Check")

    answer = st.radio(

        "Which is more important?",

        [

            "Highest Volume",

            "Highest Revenue",

            "Highest Sustainable Profit"

        ]

    )

    if st.button("Evaluate Pricing Understanding"):

        if answer == "Highest Sustainable Profit":

            st.success("""

Correct!

Smart dealers focus on sustainable profitability.

Not just sales volume.

""")

        else:

            st.warning("""

Sales volume alone does not guarantee success.

Profitability matters.

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        tamil_insight("pricing")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(

        "How do you currently decide selling prices?"

    )

    st.text_area(

        "What factors influence your pricing decisions?"

    )

    st.success("""

Pricing Lesson:

Low price does not always mean more profit.

High price does not always mean less demand.

The goal is to find the optimal balance between:

✅ Margin

✅ Volume

✅ Customer Value

""")
# =========================================================
# CREDIT MANAGEMENT LAB
# =========================================================

elif menu == "🤝 Credit Management Lab":

    st.header("🤝 Credit Management Lab")

    st.markdown("""

### Every credit decision affects cash flow.

Good customers create growth.

Bad credit decisions create working capital stress.

In this module, evaluate customer risk and understand
the impact of credit policies.

""")

    # =====================================================
    # CUSTOMER PROFILE
    # =====================================================

    st.subheader("👤 Customer Profile")

    customer_name = st.text_input(
        "Customer Name",
        "ABC Constructions"
    )

    annual_purchase = st.number_input(
        "Expected Annual Purchase (₹)",
        value=5000000
    )

    requested_credit = st.number_input(
        "Credit Period Requested (Days)",
        value=60
    )

    payment_history = st.slider(
        "Payment Discipline Score",
        1,
        10,
        7
    )

    years_relationship = st.slider(
        "Years of Relationship",
        1,
        20,
        5
    )

    # =====================================================
    # CREDIT SCORE
    # =====================================================

    credit_score = (

        payment_history * 6 +

        min(years_relationship,10) * 4

    )

    st.subheader("📊 Credit Risk Assessment")

    st.metric(
        "Credit Score",
        f"{credit_score}/100"
    )

    if credit_score >= 80:

        st.success("🟢 Low Credit Risk")

    elif credit_score >= 60:

        st.warning("🟠 Moderate Credit Risk")

    else:

        st.error("🔴 High Credit Risk")

    # =====================================================
    # DEBTOR DAYS IMPACT
    # =====================================================

    st.subheader("📅 Debtor Days Analysis")

    annual_sales = st.number_input(
        "Your Annual Sales (₹)",
        value=60000000
    )

    receivables = (

        annual_purchase *

        requested_credit

        /

        365

    )

    debtor_days = (

        receivables

        /

        annual_sales

    ) * 365

    col1, col2 = st.columns(2)

    col1.metric(
        "Expected Receivables",
        currency(receivables)
    )

    col2.metric(
        "Debtor Days Impact",
        f"{debtor_days:.1f}"
    )

    # =====================================================
    # APPROVAL DECISION
    # =====================================================

    st.subheader("🎯 Credit Approval Decision")

    decision = st.radio(

        "Choose Decision",

        [

            "Approve Full Credit",

            "Approve Partial Credit",

            "Reject Credit"

        ]

    )

    if decision == "Approve Full Credit":

        st.warning("""

Higher sales possible.

Higher collection risk.

Monitor carefully.

""")

    elif decision == "Approve Partial Credit":

        st.success("""

Balanced approach.

Growth + Risk control.

""")

    else:

        st.error("""

Risk minimized.

Potential sales opportunity lost.

""")

    # =====================================================
    # VISUAL
    # =====================================================

    risk_df = pd.DataFrame({

        "Metric":[

            "Credit Score",

            "Payment Discipline",

            "Relationship"

        ],

        "Value":[

            credit_score,

            payment_history * 10,

            years_relationship * 5

        ]

    })

    fig = px.bar(

        risk_df,

        x="Metric",

        y="Value",

        title="Customer Risk Profile"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("Debtor Days Formula"):

        st.latex(r'''
Debtor\ Days

=

\frac{Receivables}
{Annual\ Sales}

\times

365
''')

        st.markdown(f"""

Example

Debtor Days

=

{receivables:,.0f}

÷

{annual_sales:,.0f}

× 365

=

{debtor_days:.1f} days

""")

    # =====================================================
    # KNOWLEDGE CHECK
    # =====================================================

    st.subheader("🎯 Quick Knowledge Check")

    answer = st.radio(

        "Which customer is usually safer?",

        [

            "Large Order + Poor Payment History",

            "Moderate Order + Excellent Payment History",

            "Both Equal"

        ]

    )

    if st.button("Check Credit Understanding"):

        if answer == "Moderate Order + Excellent Payment History":

            st.success("""

Correct.

Collections are often more important than sales volume.

""")

        else:

            st.error("""

Think about cash flow risk.

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        tamil_insight("credit")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What percentage of your sales are on credit?"
    )

    st.text_area(
        "What is your biggest collection challenge?"
    )

    st.success("""

Credit Lesson:

Sales do not become cash immediately.

A profitable customer can still create
cash-flow problems if collections are delayed.

""")
# =========================================================
# INVENTORY MANAGEMENT LAB
# =========================================================

elif menu == "📦 Inventory Management Lab":

    st.header("📦 Inventory Management Lab")

    st.markdown("""

### Inventory is cash sitting in the warehouse.

Too much inventory:
- blocks working capital
- increases storage costs

Too little inventory:
- causes stockouts
- loses customers

The goal is to maintain optimal inventory.

""")

    # =====================================================
    # INPUTS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        annual_demand = st.number_input(
            "Annual Demand (Bags)",
            value=60000
        )

        ordering_cost = st.number_input(
            "Ordering Cost per Order (₹)",
            value=5000
        )

        carrying_cost = st.number_input(
            "Carrying Cost per Bag per Year (₹)",
            value=20
        )

    with col2:

        daily_demand = st.number_input(
            "Average Daily Demand",
            value=200
        )

        lead_time = st.number_input(
            "Supplier Lead Time (Days)",
            value=7
        )

        safety_stock = st.number_input(
            "Safety Stock (Bags)",
            value=500
        )

    # =====================================================
    # EOQ
    # =====================================================

    eoq = np.sqrt(

        (2 * annual_demand * ordering_cost)

        /

        carrying_cost

    )

    reorder_point = (

        daily_demand *

        lead_time

    ) + safety_stock

    # =====================================================
    # KPI DISPLAY
    # =====================================================

    st.subheader("📊 Inventory Dashboard")

    c1, c2 = st.columns(2)

    c1.metric(
        "Economic Order Quantity (EOQ)",
        f"{eoq:,.0f} Bags"
    )

    c2.metric(
        "Reorder Point",
        f"{reorder_point:,.0f} Bags"
    )

    # =====================================================
    # CURRENT INVENTORY
    # =====================================================

    current_inventory = st.slider(
        "Current Inventory Level",
        0,
        10000,
        3000
    )

    st.subheader("🚦 Inventory Health")

    if current_inventory < reorder_point:

        st.error("""
🔴 Reorder Immediately

Inventory is below reorder level.
Risk of stockout exists.
""")

    elif current_inventory < reorder_point * 1.5:

        st.warning("""
🟠 Inventory Level Moderate

Monitor inventory closely.
""")

    else:

        st.success("""
🟢 Healthy Inventory Position
""")

    # =====================================================
    # INVENTORY DAYS
    # =====================================================

    inventory_value = st.number_input(
        "Inventory Value (₹)",
        value=7000000
    )

    annual_cogs = st.number_input(
        "Annual Cost of Goods Sold (₹)",
        value=45000000
    )

    inventory_days = (

        inventory_value

        /

        annual_cogs

    ) * 365

    st.metric(
        "Inventory Days",
        f"{inventory_days:.1f}"
    )

    # =====================================================
    # INVENTORY VISUAL
    # =====================================================

    inventory_df = pd.DataFrame({

        "Metric":[

            "EOQ",

            "Current Inventory",

            "Reorder Point"

        ],

        "Value":[

            eoq,

            current_inventory,

            reorder_point

        ]

    })

    fig = px.bar(

        inventory_df,

        x="Metric",

        y="Value",

        title="Inventory Position"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # SLOW MOVING INVENTORY SIMULATION
    # =====================================================

    st.subheader("📉 Slow Moving Inventory Simulation")

    slow_inventory = st.slider(

        "Percentage of Slow-Moving Inventory",

        0,
        100,
        20

    )

    blocked_cash = (

        inventory_value *

        slow_inventory

        /

        100

    )

    st.metric(
        "Cash Blocked in Slow Stock",
        currency(blocked_cash)
    )

    if slow_inventory > 30:

        st.error("""
Large amount of working capital
is blocked in inventory.
""")

    elif slow_inventory > 15:

        st.warning("""
Inventory review recommended.
""")

    else:

        st.success("""
Healthy inventory movement.
""")

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("EOQ Formula"):

        st.latex(r'''
EOQ

=

\sqrt{

\frac{
2DS
}
{
H
}

}
''')

        st.markdown("""

Where:

D = Annual Demand

S = Ordering Cost

H = Carrying Cost

EOQ helps determine
the most economical order size.

""")

    with st.expander("Reorder Point Formula"):

        st.latex(r'''
ROP

=

Daily\ Demand

\times

Lead\ Time

+

Safety\ Stock
''')

        st.markdown(f"""

ROP

=

{daily_demand}

×

{lead_time}

+

{safety_stock}

=

{reorder_point:,.0f}

bags

""")

    with st.expander("Inventory Days Formula"):

        st.latex(r'''
Inventory\ Days

=

\frac{
Inventory
}
{
COGS
}

\times

365
''')

        st.markdown(f"""

Inventory Days

=

{inventory_value:,.0f}

÷

{annual_cogs:,.0f}

× 365

=

{inventory_days:.1f} days

""")

    # =====================================================
    # KNOWLEDGE CHECK
    # =====================================================

    st.subheader("🎯 Quick Knowledge Check")

    answer = st.radio(

        "Which inventory level creates maximum working capital stress?",

        [

            "Too High",

            "Too Low",

            "Both"

        ]

    )

    if st.button("Check Inventory Understanding"):

        if answer == "Too High":

            st.success("""
Correct.

Excess inventory blocks cash.
""")

        else:

            st.warning("""
Think about working capital.
""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        tamil_insight("inventory")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What causes inventory buildup in your dealership?"
    )

    st.text_area(
        "How can inventory planning be improved?"
    )

    st.success("""

Inventory Lesson:

Inventory is not just stock.

Inventory is cash.

The faster inventory moves,
the healthier the business.

""")
# =========================================================
# WORKING CAPITAL & CASH FLOW LAB
# =========================================================

elif menu == "💵 Working Capital & Cash Flow Lab":

    st.header("💵 Working Capital & Cash Flow Lab")

    st.markdown("""

### Working Capital is the lifeblood of a dealership.

Working Capital is money tied up in:

✅ Customers (Receivables)

✅ Inventory

Minus

✅ Supplier Credit

The faster cash moves,
the stronger the business.

""")

    # =====================================================
    # INPUTS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        annual_sales = st.number_input(
            "Annual Sales (₹)",
            value=60000000
        )

        receivables = st.number_input(
            "Receivables (₹)",
            value=5000000
        )

        inventory = st.number_input(
            "Inventory (₹)",
            value=7000000
        )

    with col2:

        cogs = st.number_input(
            "Annual Cost of Goods Sold (₹)",
            value=45000000
        )

        payables = st.number_input(
            "Payables (₹)",
            value=4000000
        )

    # =====================================================
    # CALCULATIONS
    # =====================================================

    receivable_days = (

        receivables /
        annual_sales

    ) * 365

    inventory_days = (

        inventory /
        cogs

    ) * 365

    payable_days = (

        payables /
        cogs

    ) * 365

    cash_conversion_cycle = (

        receivable_days +
        inventory_days -
        payable_days

    )

    working_capital = (

        receivables +
        inventory -
        payables

    )

    # =====================================================
    # KPI DASHBOARD
    # =====================================================

    st.subheader("📊 Working Capital Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Receivable Days",
        f"{receivable_days:.1f}"
    )

    c2.metric(
        "Inventory Days",
        f"{inventory_days:.1f}"
    )

    c3.metric(
        "Payable Days",
        f"{payable_days:.1f}"
    )

    c4.metric(
        "Cash Conversion Cycle",
        f"{cash_conversion_cycle:.1f}"
    )

    st.metric(
        "Net Working Capital",
        currency(working_capital)
    )

    # =====================================================
    # CASH CYCLE VISUAL
    # =====================================================

    cycle_df = pd.DataFrame({

        "Stage":[

            "Receivable Days",
            "Inventory Days",
            "Payable Days"

        ],

        "Days":[

            receivable_days,
            inventory_days,
            payable_days

        ]

    })

    fig = px.bar(

        cycle_df,

        x="Stage",

        y="Days",

        title="Cash Conversion Cycle Components"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.subheader("🧠 Interpretation")

    if cash_conversion_cycle <= 45:

        st.success("""

🟢 Excellent Working Capital Management

Cash moves efficiently through business.

""")

    elif cash_conversion_cycle <= 90:

        st.warning("""

🟠 Moderate Working Capital Pressure

Monitor collections and inventory.

""")

    else:

        st.error("""

🔴 High Working Capital Stress

Too much cash is blocked in operations.

""")

    # =====================================================
    # WHAT-IF SIMULATION
    # =====================================================

    st.subheader("🎮 Improve Your Cash Cycle")

    collection_improvement = st.slider(

        "Reduce Receivable Days By",

        0,
        60,
        10

    )

    inventory_reduction = st.slider(

        "Reduce Inventory Days By",

        0,
        60,
        10

    )

    improved_ccc = (

        (receivable_days - collection_improvement)

        +

        (inventory_days - inventory_reduction)

        -

        payable_days

    )

    st.metric(
        "Improved CCC",
        f"{improved_ccc:.1f} days"
    )

    improvement = (

        cash_conversion_cycle -
        improved_ccc

    )

    st.success(f"""
Cash cycle improved by
{improvement:.1f} days
""")

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("Receivable Days Formula"):

        st.latex(r'''
Receivable\ Days

=

\frac{Receivables}
{Sales}

\times

365
''')

        st.write(f"""

= {receivables:,.0f}

÷

{annual_sales:,.0f}

× 365

=

{receivable_days:.1f} days

""")

    with st.expander("Inventory Days Formula"):

        st.latex(r'''
Inventory\ Days

=

\frac{Inventory}
{COGS}

\times

365
''')

        st.write(f"""

= {inventory:,.0f}

÷

{cogs:,.0f}

× 365

=

{inventory_days:.1f} days

""")

    with st.expander("Payable Days Formula"):

        st.latex(r'''
Payable\ Days

=

\frac{Payables}
{COGS}

\times

365
''')

        st.write(f"""

= {payables:,.0f}

÷

{cogs:,.0f}

× 365

=

{payable_days:.1f} days

""")

    with st.expander("Cash Conversion Cycle Formula"):

        st.latex(r'''
CCC

=

Receivable\ Days

+

Inventory\ Days

-

Payable\ Days
''')

        st.write(f"""

CCC

=

{receivable_days:.1f}

+

{inventory_days:.1f}

-

{payable_days:.1f}

=

{cash_conversion_cycle:.1f} days

""")

    # =====================================================
    # KNOWLEDGE CHECK
    # =====================================================

    st.subheader("🎯 Quick Knowledge Check")

    answer = st.radio(

        "What improves cash flow the most?",

        [

            "Faster Collections",

            "Higher Inventory",

            "Longer Customer Credit"

        ]

    )

    if st.button("Check Understanding"):

        if answer == "Faster Collections":

            st.success("""
Correct.

Cash flow improves when customers pay faster.
""")

        else:

            st.error("""
Think about how cash enters the business.
""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        tamil_insight("cashflow")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What causes working capital stress in your dealership?"
    )

    st.text_area(
        "What action can reduce cash blockage?"
    )

    st.success("""

Working Capital Lesson:

Profit is important.

But survival depends on cash.

The faster cash rotates,

the stronger the dealership.

""")
# =========================================================
# CASH FLOW CRISIS SIMULATION
# =========================================================

elif menu == "🚨 Cash Flow Crisis Simulation":

    st.header("🚨 Cash Flow Crisis Simulation")

    st.markdown("""

### Scenario

A sudden slowdown has affected your dealership.

Problems:

✅ Customers are delaying payments

✅ Inventory has increased

✅ Supplier payments are due

✅ Bank limit is almost exhausted

You must take decisions quickly.

""")

    # =====================================================
    # STARTING POSITION
    # =====================================================

    cash_balance = 1500000

    receivables = 7000000

    inventory = 9000000

    supplier_due = 4000000

    st.subheader("📊 Current Situation")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Cash Balance",
            currency(cash_balance)
        )

        st.metric(
            "Receivables",
            currency(receivables)
        )

    with col2:

        st.metric(
            "Inventory",
            currency(inventory)
        )

        st.metric(
            "Supplier Due",
            currency(supplier_due)
        )

    # =====================================================
    # DECISION OPTIONS
    # =====================================================

    st.subheader("🎯 Choose Your Actions")

    collect_fast = st.checkbox(
        "Launch aggressive collection drive"
    )

    reduce_inventory = st.checkbox(
        "Offer discount to clear inventory"
    )

    negotiate_supplier = st.checkbox(
        "Negotiate supplier credit extension"
    )

    take_bank_loan = st.checkbox(
        "Take short-term working capital loan"
    )

    delay_expansion = st.checkbox(
        "Postpone expansion investment"
    )

    # =====================================================
    # IMPACT CALCULATIONS
    # =====================================================

    final_cash = cash_balance

    actions = []

    if collect_fast:

        final_cash += 2000000
        actions.append("Collections Improved")

    if reduce_inventory:

        final_cash += 1500000
        actions.append("Inventory Reduced")

    if negotiate_supplier:

        final_cash += 1000000
        actions.append("Supplier Credit Extended")

    if take_bank_loan:

        final_cash += 2500000
        actions.append("Bank Funding Added")

    if delay_expansion:

        final_cash += 1200000
        actions.append("Capex Deferred")

    # =====================================================
    # RESULTS
    # =====================================================

    st.subheader("📈 Simulation Outcome")

    st.metric(
        "Final Cash Position",
        currency(final_cash)
    )

    st.write("### Actions Taken")

    if len(actions) > 0:

        for a in actions:

            st.write(f"✅ {a}")

    else:

        st.write("❌ No corrective actions taken")

    # =====================================================
    # HEALTH SCORE
    # =====================================================

    health_score = min(
        100,
        round(final_cash / 100000)
    )

    st.subheader("🏥 Liquidity Health Score")

    st.progress(health_score / 100)

    st.metric(
        "Health Score",
        f"{health_score}/100"
    )

    if final_cash >= 7000000:

        st.success("""

🟢 Crisis Successfully Managed

Liquidity has improved significantly.

""")

    elif final_cash >= 4000000:

        st.warning("""

🟠 Situation Improved

Some risk still remains.

""")

    else:

        st.error("""

🔴 Severe Cash Stress

Immediate action required.

""")

    # =====================================================
    # VISUAL
    # =====================================================

    result_df = pd.DataFrame({

        "Stage":[

            "Initial Cash",

            "Final Cash"

        ],

        "Amount":[

            cash_balance,

            final_cash

        ]

    })

    fig = px.bar(

        result_df,

        x="Stage",

        y="Amount",

        title="Cash Position Improvement"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # DEALER DISCUSSION
    # =====================================================

    st.subheader("💡 Discussion Point")

    st.info("""

Many businesses focus on:

Sales ↑

But ignore:

Collections ↓

Inventory ↑

Cash ↓

The best dealers manage cash proactively.

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

Cash crisis வந்தால்:

• Collection improve செய்யுங்கள்

• Slow stock reduce செய்யுங்கள்

• Supplier உடன் பேசுங்கள்

• தேவையற்ற investment postpone செய்யுங்கள்

Cash தான் business-ஐ காப்பாற்றும்.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "If this happened in your dealership, what would be your first action?"
    )

    st.text_area(
        "Which area causes the biggest cash-flow stress today?"
    )

    st.success("""

Crisis Lesson:

Revenue creates business.

Profit creates wealth.

Cash creates survival.

""")
# =========================================================
# SEASONAL PLANNING SIMULATOR
# =========================================================

elif menu == "🌤️ Seasonal Planning":

    st.header("🌤️ Seasonal Planning Simulator")

    st.markdown("""

### Demand is not constant throughout the year.

Construction activity changes because of:

✅ Monsoon

✅ Festivals

✅ Government Projects

✅ Real Estate Cycles

Smart dealers prepare before demand changes.

""")

    # =====================================================
    # MONTHLY DEMAND
    # =====================================================

    months = [

        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"

    ]

    demand = [

        120,130,145,160,
        170,140,100,95,
        125,155,180,190

    ]

    season_df = pd.DataFrame({

        "Month": months,
        "Demand Index": demand

    })

    # =====================================================
    # VISUALIZATION
    # =====================================================

    st.subheader("📈 Annual Demand Pattern")

    fig = px.line(

        season_df,

        x="Month",

        y="Demand Index",

        markers=True,

        title="Seasonal Demand Trend"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # MONTH SELECTION
    # =====================================================

    selected_month = st.selectbox(

        "Select Planning Month",

        months

    )

    demand_value = season_df.loc[
        season_df["Month"] == selected_month,
        "Demand Index"
    ].values[0]

    st.metric(
        "Expected Demand Index",
        demand_value
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    if demand_value >= 170:

        st.success("""

🟢 Peak Demand Season

Increase:
- inventory
- manpower
- delivery readiness

""")

    elif demand_value >= 130:

        st.warning("""

🟠 Moderate Demand

Monitor inventory carefully.

""")

    else:

        st.error("""

🔴 Slow Demand Period

Focus on:
- collections
- inventory reduction
- customer engagement

""")

    # =====================================================
    # INVENTORY PLANNING
    # =====================================================

    st.subheader("📦 Inventory Planning")

    current_inventory = st.number_input(

        "Current Inventory (Bags)",

        value=5000

    )

    recommended_inventory = (

        demand_value * 50

    )

    st.metric(

        "Recommended Inventory",

        f"{recommended_inventory:,.0f} Bags"

    )

    gap = current_inventory - recommended_inventory

    if gap > 1000:

        st.warning("""

Inventory appears higher than recommended.

Working capital may be blocked.

""")

    elif gap < -1000:

        st.error("""

Inventory may be insufficient.

Risk of stockout exists.

""")

    else:

        st.success("""

Inventory level appears appropriate.

""")

    # =====================================================
    # SALES FORECAST
    # =====================================================

    st.subheader("📊 Sales Forecast")

    average_monthly_sales = st.number_input(

        "Average Monthly Sales (₹)",

        value=5000000

    )

    forecast_sales = (

        average_monthly_sales *

        demand_value /

        100

    )

    st.metric(

        "Forecast Sales",

        currency(forecast_sales)

    )

    # =====================================================
    # WHAT-IF SIMULATION
    # =====================================================

    st.subheader("🎮 What-If Simulation")

    monsoon_impact = st.slider(

        "Monsoon Severity",

        0,
        50,
        15

    )

    adjusted_forecast = (

        forecast_sales *

        (1 - monsoon_impact/100)

    )

    st.metric(

        "Adjusted Forecast Sales",

        currency(adjusted_forecast)

    )

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Logic")

    with st.expander("Seasonal Forecast Formula"):

        st.latex(r'''
Forecast\ Sales

=

Average\ Sales

\times

Demand\ Index

/
100
''')

        st.write(f"""

Forecast Sales

=

{average_monthly_sales:,.0f}

×

{demand_value}

÷

100

=

{forecast_sales:,.0f}

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

Season-க்கு ஏற்ப

• Stock plan செய்யுங்கள்

• Cash plan செய்யுங்கள்

• Demand forecast செய்யுங்கள்

Peak season-க்கு முன்பே தயாராக இருங்கள்.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(

        "Which months are strongest in your market?"

    )

    st.text_area(

        "How do you prepare for peak demand?"

    )

    st.success("""

Seasonal Planning Lesson:

Strong dealers do not react.

They prepare.

""")
# =========================================================
# SCHEME & TARGET PLANNER
# =========================================================

elif menu == "🎁 Scheme & Target Planner":

    st.header("🎁 Scheme & Target Planner")

    st.markdown("""

### Growth requires targets.

Dealers often receive:

✅ Volume Targets

✅ Incentive Schemes

✅ Growth Bonuses

The challenge is balancing:

Sales Growth
+
Profitability
+
Cash Flow

""")

    # =====================================================
    # INPUTS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        current_sales = st.number_input(
            "Current Monthly Sales (Bags)",
            value=5000
        )

        target_sales = st.number_input(
            "Target Monthly Sales (Bags)",
            value=6500
        )

    with col2:

        incentive_per_bag = st.number_input(
            "Scheme Incentive Per Bag (₹)",
            value=10.0
        )

        contribution_per_bag = st.number_input(
            "Contribution Per Bag (₹)",
            value=30.0
        )

    # =====================================================
    # GAP ANALYSIS
    # =====================================================

    additional_sales = max(
        target_sales - current_sales,
        0
    )

    achievement_pct = (

        current_sales /
        target_sales

    ) * 100

    st.subheader("📊 Target Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Target Achievement",
        f"{achievement_pct:.1f}%"
    )

    c2.metric(
        "Additional Bags Needed",
        f"{additional_sales:,.0f}"
    )

    c3.metric(
        "Growth Required",
        f"{((target_sales-current_sales)/current_sales)*100:.1f}%"
    )

    # =====================================================
    # INCENTIVE IMPACT
    # =====================================================

    incentive_income = (

        target_sales *
        incentive_per_bag

    )

    business_profit = (

        target_sales *
        contribution_per_bag

    )

    st.subheader("💰 Financial Impact")

    col1, col2 = st.columns(2)

    col1.metric(
        "Potential Incentive",
        currency(incentive_income)
    )

    col2.metric(
        "Contribution Generated",
        currency(business_profit)
    )

    # =====================================================
    # VISUALIZATION
    # =====================================================

    target_df = pd.DataFrame({

        "Category":[

            "Current Sales",
            "Target Sales"

        ],

        "Value":[

            current_sales,
            target_sales

        ]

    })

    fig = px.bar(

        target_df,

        x="Category",

        y="Value",

        title="Sales Target Comparison"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # SCHEME SIMULATOR
    # =====================================================

    st.subheader("🎮 Scheme Achievement Simulator")

    expected_achievement = st.slider(

        "Expected Achievement (%)",

        50,
        150,
        100

    )

    achieved_volume = (

        target_sales *
        expected_achievement /
        100

    )

    earned_incentive = (

        achieved_volume *
        incentive_per_bag

    )

    st.metric(
        "Expected Incentive Earned",
        currency(earned_incentive)
    )

    if expected_achievement >= 120:

        st.success("""
🟢 Outstanding Performance

Significant incentive opportunity exists.
""")

    elif expected_achievement >= 100:

        st.success("""
🟢 Target Achieved

Eligible for full incentive benefits.
""")

    else:

        st.warning("""
🟠 Target Not Fully Achieved

Potential incentive loss.
""")

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("Target Achievement Formula"):

        st.latex(r'''
Achievement\%

=

\frac{
Actual\ Sales
}
{
Target\ Sales
}

\times

100
''')

        st.write(f"""

Achievement %

=

{current_sales}

÷

{target_sales}

× 100

=

{achievement_pct:.1f}%

""")

    with st.expander("Incentive Formula"):

        st.latex(r'''
Incentive

=

Sales\ Volume

\times

Incentive\ Per\ Bag
''')

        st.write(f"""

Incentive

=

{target_sales}

×

{incentive_per_bag}

=

₹{incentive_income:,.0f}

""")

    # =====================================================
    # BUSINESS INSIGHT
    # =====================================================

    st.subheader("💡 Dealer Wisdom")

    st.info("""

The best dealers do not chase incentives alone.

They focus on:

✅ Sustainable growth

✅ Healthy margins

✅ Strong collections

✅ Customer retention

Incentives should support strategy,
not drive risky behaviour.

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

Target achieve செய்வது நல்லது.

ஆனால்:

• Margin sacrifice செய்யக்கூடாது

• Collection பாதிக்கக்கூடாது

• Inventory அதிகமாக வைத்துக்கொள்ளக்கூடாது

Smart growth தான் முக்கியம்.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What prevents your dealership from achieving higher targets?"
    )

    st.text_area(
        "How can growth be achieved without hurting profitability?"
    )

    st.success("""

Target Planning Lesson:

Growth is meaningful only when:

✔ Profit grows

✔ Cash flow remains healthy

✔ Customers stay loyal

""")
# =========================================================
# GROWTH DECISION SIMULATOR
# =========================================================

elif menu == "📈 Growth Decision Simulator":

    st.header("📈 Growth Decision Simulator")

    st.markdown("""

### Every growth opportunity requires investment.

The key question:

Will the investment create value?

Evaluate:

✅ Investment Cost

✅ Expected Benefits

✅ Payback Period

✅ Return on Investment (ROI)

""")

    # =====================================================
    # INVESTMENT OPTIONS
    # =====================================================

    investment_type = st.selectbox(

        "Choose Investment",

        [

            "New Warehouse",

            "Additional Delivery Truck",

            "Digital Transformation",

            "New Branch Expansion",

            "Sales Team Expansion"

        ]

    )

    # Suggested defaults

    defaults = {

        "New Warehouse": (5000000, 1500000),
        "Additional Delivery Truck": (2500000, 700000),
        "Digital Transformation": (1000000, 400000),
        "New Branch Expansion": (8000000, 2200000),
        "Sales Team Expansion": (1500000, 600000)

    }

    default_investment, default_benefit = defaults[investment_type]

    col1, col2 = st.columns(2)

    with col1:

        investment_cost = st.number_input(

            "Investment Cost (₹)",

            value=float(default_investment)

        )

    with col2:

        annual_benefit = st.number_input(

            "Expected Annual Benefit (₹)",

            value=float(default_benefit)

        )

    # =====================================================
    # CALCULATIONS
    # =====================================================

    roi = (

        annual_benefit

        /

        investment_cost

    ) * 100

    payback = (

        investment_cost

        /

        annual_benefit

    )

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.subheader("📊 Investment Dashboard")

    c1, c2 = st.columns(2)

    c1.metric(
        "ROI",
        f"{roi:.1f}%"
    )

    c2.metric(
        "Payback Period",
        f"{payback:.2f} Years"
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.subheader("🧠 Investment Assessment")

    if roi >= 25:

        st.success("""

🟢 Attractive Investment

Strong potential return.

Worth serious consideration.

""")

    elif roi >= 15:

        st.warning("""

🟠 Moderate Investment Opportunity

Needs further evaluation.

""")

    else:

        st.error("""

🔴 Weak Investment Return

Review assumptions carefully.

""")

    # =====================================================
    # VISUALIZATION
    # =====================================================

    growth_df = pd.DataFrame({

        "Category":[

            "Investment",

            "Annual Benefit"

        ],

        "Amount":[

            investment_cost,

            annual_benefit

        ]

    })

    fig = px.bar(

        growth_df,

        x="Category",

        y="Amount",

        title="Investment vs Annual Benefit"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # PAYBACK VISUAL
    # =====================================================

    years = list(range(1,6))

    cumulative = [

        annual_benefit * y

        for y in years

    ]

    payback_df = pd.DataFrame({

        "Year": years,

        "Cumulative Benefit": cumulative

    })

    fig2 = px.line(

        payback_df,

        x="Year",

        y="Cumulative Benefit",

        markers=True,

        title="Benefit Accumulation Over Time"

    )

    fig2.add_hline(

        y=investment_cost,

        line_dash="dash"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =====================================================
    # WHAT IF ANALYSIS
    # =====================================================

    st.subheader("🎮 Growth Scenario Analysis")

    benefit_change = st.slider(

        "Change Expected Benefits (%)",

        -50,
        50,
        0

    )

    revised_benefit = (

        annual_benefit *

        (1 + benefit_change/100)

    )

    revised_roi = (

        revised_benefit /

        investment_cost

    ) * 100

    st.metric(

        "Revised ROI",

        f"{revised_roi:.1f}%"

    )

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Formula")

    with st.expander("ROI Formula"):

        st.latex(r'''
ROI

=

\frac{
Annual\ Benefit
}
{
Investment
}

\times

100
''')

        st.write(f"""

ROI

=

{annual_benefit:,.0f}

÷

{investment_cost:,.0f}

× 100

=

{roi:.1f}%

""")

    with st.expander("Payback Formula"):

        st.latex(r'''
Payback

=

\frac{
Investment
}
{
Annual\ Benefit
}
''')

        st.write(f"""

Payback

=

{investment_cost:,.0f}

÷

{annual_benefit:,.0f}

=

{payback:.2f} years

""")

    # =====================================================
    # DEALER WISDOM
    # =====================================================

    st.info("""

Growth should create:

✅ Higher profits

✅ Better customer service

✅ Stronger cash flows

✅ Long-term competitive advantage

Not just bigger sales.

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

Investment செய்வதற்கு முன்:

• Return என்ன?

• Risk என்ன?

• Payback எவ்வளவு?

• Cash Flow பாதிக்குமா?

என்று யோசிக்க வேண்டும்.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(

        "What is the next major investment you are considering?"

    )

    st.text_area(

        "How will you evaluate whether it is worthwhile?"

    )

    st.success("""

Growth Lesson:

Not every opportunity should be accepted.

The best investments create sustainable value.

""")
# =========================================================
# DIGITAL TRANSFORMATION READINESS
# =========================================================

elif menu == "💻 Digital Transformation Readiness":

    st.header("💻 Digital Transformation Readiness")

    st.markdown("""

### The Future Dealer is Data Driven

Digital tools can improve:

✅ Sales Tracking

✅ Collections

✅ Inventory Management

✅ Customer Relationships

✅ Decision Making

Evaluate your dealership's digital readiness.

""")

    # =====================================================
    # DIGITAL READINESS INPUTS
    # =====================================================

    st.subheader("📊 Digital Assessment")

    erp = st.slider(
        "ERP Usage",
        0,
        10,
        5
    )

    crm = st.slider(
        "Customer Relationship Management",
        0,
        10,
        4
    )

    analytics = st.slider(
        "Data & Analytics Usage",
        0,
        10,
        3
    )

    digital_payments = st.slider(
        "Digital Payment Adoption",
        0,
        10,
        8
    )

    whatsapp_orders = st.slider(
        "Digital Ordering / WhatsApp Orders",
        0,
        10,
        7
    )

    dashboard_usage = st.slider(
        "Management Dashboard Usage",
        0,
        10,
        2
    )

    # =====================================================
    # SCORE
    # =====================================================

    digital_score = (

        erp +
        crm +
        analytics +
        digital_payments +
        whatsapp_orders +
        dashboard_usage

    ) / 60 * 100

    st.subheader("📈 Digital Readiness Score")

    st.progress(digital_score / 100)

    st.metric(
        "Digital Readiness",
        f"{digital_score:.1f}%"
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    if digital_score >= 80:

        st.success("""

🟢 Digital Leader

Your dealership is highly digitized.

Focus on analytics and automation.

""")

    elif digital_score >= 60:

        st.warning("""

🟠 Digital Adopter

Good progress.

Several opportunities still exist.

""")

    else:

        st.error("""

🔴 Traditional Operations

Significant digital transformation opportunity exists.

""")

    # =====================================================
    # RADAR CHART
    # =====================================================

    categories = [

        "ERP",
        "CRM",
        "Analytics",
        "Payments",
        "Orders",
        "Dashboards"

    ]

    values = [

        erp,
        crm,
        analytics,
        digital_payments,
        whatsapp_orders,
        dashboard_usage

    ]

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            name="Digital Readiness"

        )

    )

    fig.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # DIGITAL PRIORITY
    # =====================================================

    st.subheader("🎯 Recommended Next Step")

    weakest_area = categories[
        values.index(min(values))
    ]

    st.info(f"""

Your biggest digital improvement opportunity is:

✅ {weakest_area}

Improving this area may create the highest business impact.

""")

    # =====================================================
    # DIGITAL ROI SIMULATION
    # =====================================================

    st.subheader("🎮 Digital Investment Simulation")

    digital_investment = st.slider(

        "Digital Investment (₹ Lakhs)",

        1,
        50,
        10

    )

    efficiency_gain = digital_investment * 1.8

    st.metric(
        "Estimated Efficiency Gain (%)",
        f"{efficiency_gain:.1f}%"
    )

    # =====================================================
    # FORMULA LEARNING
    # =====================================================

    st.subheader("📘 Learn the Logic")

    with st.expander("Digital Readiness Score"):

        st.write("""

Digital Score

=

(Total Digital Capability Score)

÷

(Maximum Possible Score)

× 100

Higher score indicates better preparedness
for future business growth.

""")

    # =====================================================
    # DEALER WISDOM
    # =====================================================

    st.info("""

The future competitive advantage will not be:

❌ Bigger warehouse

❌ More paperwork

It will be:

✅ Better data

✅ Faster decisions

✅ Strong customer insights

✅ Digital execution

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

இனி business வளர:

• ERP

• CRM

• Analytics

• Digital Payments

• Dashboard

முக்கியம்.

Data வைத்து decision எடுத்தால்
growth வேகம் அதிகரிக்கும்.

""")
 # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Dealer Reflection")

    st.text_area(
        "What is the biggest digital challenge in your dealership?"
    )

    st.text_area(
        "What digital tool would create the highest impact?"
    )

    st.success("""

Digital Lesson:

Technology alone does not create value.

Using data for better decisions creates value.

""")

   
# =========================================================
# NEXTGEN LEADERSHIP
# =========================================================

elif menu == "🌟 NextGen Leadership":

    st.header("🌟 NextGen Leadership")

    st.markdown("""

### The next generation dealer must be more than a business operator.

Future leaders must:

✅ Build teams

✅ Use data

✅ Drive innovation

✅ Manage finances

✅ Create customer relationships

✅ Think long term

Evaluate your leadership readiness.

""")

    # =====================================================
    # LEADERSHIP ASSESSMENT
    # =====================================================

    delegation = st.slider(
        "Delegation Ability",
        0,
        10,
        6
    )

    innovation = st.slider(
        "Innovation Mindset",
        0,
        10,
        7
    )

    financial_discipline = st.slider(
        "Financial Discipline",
        0,
        10,
        8
    )

    customer_focus = st.slider(
        "Customer Orientation",
        0,
        10,
        8
    )

    team_building = st.slider(
        "Team Development",
        0,
        10,
        6
    )

    learning_agility = st.slider(
        "Continuous Learning",
        0,
        10,
        7
    )

    # =====================================================
    # LEADERSHIP SCORE
    # =====================================================

    leadership_score = (

        delegation +
        innovation +
        financial_discipline +
        customer_focus +
        team_building +
        learning_agility

    ) / 60 * 100

    st.subheader("📈 Leadership Readiness Score")

    st.progress(leadership_score / 100)

    st.metric(
        "Leadership Readiness",
        f"{leadership_score:.1f}%"
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    if leadership_score >= 80:

        st.success("""

🟢 Future-Ready Leader

You demonstrate strong leadership potential.

Focus on scaling your impact.

""")

    elif leadership_score >= 60:

        st.warning("""

🟠 Emerging Leader

Strong foundation exists.

Further development can create significant growth.

""")

    else:

        st.error("""

🔴 Leadership Development Opportunity

Focus on building management and leadership capabilities.

""")

    # =====================================================
    # RADAR CHART
    # =====================================================

    leadership_categories = [

        "Delegation",
        "Innovation",
        "Finance",
        "Customer",
        "Team",
        "Learning"

    ]

    leadership_values = [

        delegation,
        innovation,
        financial_discipline,
        customer_focus,
        team_building,
        learning_agility

    ]

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=leadership_values,

            theta=leadership_categories,

            fill='toself',

            name='Leadership Profile'

        )

    )

    fig.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # LEADERSHIP STYLE
    # =====================================================

    st.subheader("🎯 Leadership Strength")

    strongest_area = leadership_categories[
        leadership_values.index(max(leadership_values))
    ]

    weakest_area = leadership_categories[
        leadership_values.index(min(leadership_values))
    ]

    col1, col2 = st.columns(2)

    col1.success(f"""
Strongest Area:

✅ {strongest_area}
""")

    col2.warning(f"""
Development Area:

⚠️ {weakest_area}
""")

    # =====================================================
    # NEXTGEN CHALLENGE
    # =====================================================

    st.subheader("🎮 Leadership Scenario")

    scenario = st.radio(

        "A senior employee resists a new digital system. What would you do?",

        [

            "Force implementation immediately",

            "Explain benefits and train employees",

            "Drop the initiative"

        ]

    )

    if st.button("Evaluate Leadership Decision"):

        if scenario == "Explain benefits and train employees":

            st.success("""

Excellent leadership choice.

Change succeeds when people understand
and support the vision.

""")

        elif scenario == "Force implementation immediately":

            st.warning("""

Results may come quickly,
but employee resistance may increase.

""")

        else:

            st.error("""

Avoiding change may reduce competitiveness.

""")

    # =====================================================
    # LEADERSHIP PRINCIPLES
    # =====================================================

    st.subheader("📘 Leadership Principles")

    st.info("""

Successful NextGen Dealers typically:

1. Use data before making decisions

2. Build systems instead of depending on individuals

3. Develop future leaders within the team

4. Focus on customer relationships

5. Continuously learn and adapt

""")

    # =====================================================
    # TAMIL LEARNING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

அடுத்த தலைமுறை Dealer:

• Data பார்க்க வேண்டும்

• Team உருவாக்க வேண்டும்

• Technology பயன்படுத்த வேண்டும்

• Customer relationship வளர்க்க வேண்டும்

• நீண்டகால vision வைத்திருக்க வேண்டும்

Leadership என்பது பதவி அல்ல.

Influence மற்றும் Direction.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Leadership Reflection")

    st.text_area(
        "What leadership quality would you most like to improve?"
    )

    st.text_area(
        "What kind of dealership leader do you want to become?"
    )

    st.success("""

Leadership Lesson:

Businesses grow because of systems.

Great businesses grow because of leaders.

""")
# =========================================================
# DEALER REFLECTION & FINANCIAL SCORECARD
# =========================================================

elif menu == "📊 Dealer Reflection & Financial Scorecard":

    st.header("📊 Dealer Reflection & Financial Scorecard")

    st.markdown("""

### Your Dealership Health Check

Evaluate:

✅ Profitability

✅ Cost Efficiency

✅ Collections

✅ Inventory Management

✅ Supplier Credit

✅ Cash Flow Efficiency

""")

    # =====================================================
    # INPUTS
    # =====================================================

    annual_sales = st.number_input(
        "Annual Sales (₹)",
        value=60000000.0
    )

    annual_profit = st.number_input(
        "Annual Profit (₹)",
        value=6000000.0
    )

    receivables = st.number_input(
        "Receivables (₹)",
        value=5000000.0
    )

    inventory = st.number_input(
        "Inventory (₹)",
        value=7000000.0
    )

    payables = st.number_input(
        "Payables (₹)",
        value=4000000.0
    )

    cogs = st.number_input(
        "Annual Cost of Goods Sold (₹)",
        value=45000000.0
    )

    operating_expenses = st.number_input(
        "Operating Expenses (₹)",
        value=8000000.0
    )

    # =====================================================
    # CALCULATIONS
    # =====================================================

    profit_margin = (
        annual_profit / annual_sales
    ) * 100

    expense_ratio = (
        operating_expenses / annual_sales
    ) * 100

    receivable_days = (
        receivables / annual_sales
    ) * 365

    inventory_days = (
        inventory / cogs
    ) * 365

    payable_days = (
        payables / cogs
    ) * 365

    cash_conversion_cycle = (
        receivable_days +
        inventory_days -
        payable_days
    )

    # =====================================================
    # KPI DASHBOARD
    # =====================================================

    st.subheader("📈 Financial Scorecard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )

    c2.metric(
        "Expense Ratio",
        f"{expense_ratio:.2f}%"
    )

    c3.metric(
        "Receivable Days",
        f"{receivable_days:.1f}"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Inventory Days",
        f"{inventory_days:.1f}"
    )

    c5.metric(
        "Payable Days",
        f"{payable_days:.1f}"
    )

    c6.metric(
        "Cash Conversion Cycle",
        f"{cash_conversion_cycle:.1f}"
    )

    # =====================================================
    # VISUALIZATION
    # =====================================================

    scorecard_df = pd.DataFrame({

        "Ratio":[

            "Profit Margin",
            "Expense Ratio",
            "Receivable Days",
            "Inventory Days",
            "Payable Days",
            "CCC"

        ],

        "Value":[

            profit_margin,
            expense_ratio,
            receivable_days,
            inventory_days,
            payable_days,
            cash_conversion_cycle

        ]

    })

    fig = px.bar(

        scorecard_df,

        x="Ratio",

        y="Value",

        title="Dealer Financial Scorecard"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # FORMULA EXPLANATION
    # =====================================================

    st.subheader("📘 How Are These Ratios Calculated?")

    with st.expander("Profit Margin Formula"):

        st.latex(r'''
Profit\ Margin

=

\frac{
Profit
}
{
Sales
}

\times

100
''')

        st.write(f"""
= {annual_profit:,.0f}
÷
{annual_sales:,.0f}
×100

= {profit_margin:.2f}%
""")

    with st.expander("Receivable Days Formula"):

        st.latex(r'''
Receivable\ Days

=

\frac{
Receivables
}
{
Sales
}

\times

365
''')

        st.write(f"""
= {receivables:,.0f}
÷
{annual_sales:,.0f}
×365

= {receivable_days:.1f} days
""")

    with st.expander("Inventory Days Formula"):

        st.latex(r'''
Inventory\ Days

=

\frac{
Inventory
}
{
COGS
}

\times

365
''')

        st.write(f"""
= {inventory:,.0f}
÷
{cogs:,.0f}
×365

= {inventory_days:.1f} days
""")

    with st.expander("Cash Conversion Cycle Formula"):

        st.latex(r'''
CCC

=

Receivable\ Days

+

Inventory\ Days

-

Payable\ Days
''')

        st.write(f"""
CCC

=

{receivable_days:.1f}

+

{inventory_days:.1f}

-

{payable_days:.1f}

=

{cash_conversion_cycle:.1f} days
""")

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.subheader("🧠 Interpretation")

    if profit_margin >= 10:
        st.success("🟢 Strong Profitability")

    elif profit_margin >= 5:
        st.warning("🟠 Moderate Profitability")

    else:
        st.error("🔴 Weak Profitability")

    if receivable_days <= 45:
        st.success("🟢 Collections Healthy")
    elif receivable_days <= 90:
        st.warning("🟠 Collections Need Monitoring")
    else:
        st.error("🔴 Collection Risk High")

    if inventory_days <= 60:
        st.success("🟢 Inventory Efficient")
    elif inventory_days <= 120:
        st.warning("🟠 Inventory Build-up Exists")
    else:
        st.error("🔴 Excess Inventory Blocking Cash")

    if cash_conversion_cycle <= 45:
        st.success("🟢 Excellent Cash Flow Cycle")
    elif cash_conversion_cycle <= 90:
        st.warning("🟠 Moderate Cash Flow Pressure")
    else:
        st.error("🔴 Significant Working Capital Stress")

    # =====================================================
    # OVERALL DEALER HEALTH SCORE
    # =====================================================

    health_score = 100

    if profit_margin < 5:
        health_score -= 20

    if receivable_days > 90:
        health_score -= 20

    if inventory_days > 120:
        health_score -= 20

    if cash_conversion_cycle > 90:
        health_score -= 20

    health_score = max(0, health_score)

    st.subheader("🏆 Dealer Health Score")

    st.progress(health_score/100)

    st.metric(
        "Overall Score",
        f"{health_score}/100"
    )

    # =====================================================
    # TAMIL INSIGHT
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

💡 தமிழ் விளக்கம்

ஒரு நல்ல dealership:

✅ நல்ல profit

✅ வேகமான collection

✅ குறைந்த inventory blockage

✅ நல்ல cash flow

இவற்றை maintain செய்ய வேண்டும்.

""")

    # =====================================================
    # REFLECTION
    # =====================================================

    st.subheader("📝 Reflection")

    st.text_area(
        "What is the biggest financial challenge in your dealership?"
    )

    st.text_area(
        "Which ratio would you like to improve first?"
    )

    st.success("""

Financial Excellence =
Profitability
+
Cash Flow
+
Discipline
+
Continuous Improvement

""")
# =========================================================
# 90-DAY ACTION PLAN
# =========================================================

elif menu == "📝 90-Day Action Plan":

    st.header("📝 My 90-Day Dealer Action Plan")

    st.markdown("""

### Congratulations!

You have completed the NextGen Dealer Finance Lab.

Now convert learning into action.

Choose a few practical improvements that you will implement over the next 90 days.

""")

    # =====================================================
    # BUSINESS IMPROVEMENT PRIORITIES
    # =====================================================

    st.subheader("🎯 Top Business Priorities")

    priority1 = st.text_input(
        "Priority 1"
    )

    priority2 = st.text_input(
        "Priority 2"
    )

    priority3 = st.text_input(
        "Priority 3"
    )

    # =====================================================
    # COLLECTION TARGET
    # =====================================================

    st.subheader("💰 Working Capital Improvement")

    current_receivable_days = st.number_input(

        "Current Receivable Days",

        value=60

    )

    target_receivable_days = st.number_input(

        "Target Receivable Days",

        value=45

    )

    receivable_improvement = (

        current_receivable_days -
        target_receivable_days

    )

    st.metric(

        "Improvement Target",

        f"{receivable_improvement:.0f} Days"

    )

    # =====================================================
    # INVENTORY TARGET
    # =====================================================

    st.subheader("📦 Inventory Improvement")

    current_inventory_days = st.number_input(

        "Current Inventory Days",

        value=70

    )

    target_inventory_days = st.number_input(

        "Target Inventory Days",

        value=55

    )

    inventory_improvement = (

        current_inventory_days -
        target_inventory_days

    )

    st.metric(

        "Inventory Reduction Target",

        f"{inventory_improvement:.0f} Days"

    )

    # =====================================================
    # SALES TARGET
    # =====================================================

    st.subheader("📈 Growth Target")

    current_sales = st.number_input(

        "Current Monthly Sales (Bags)",

        value=5000

    )

    target_sales = st.number_input(

        "90-Day Sales Target (Bags)",

        value=5500

    )

    growth_pct = (

        (target_sales - current_sales)

        /

        current_sales

    ) * 100

    st.metric(

        "Sales Growth Target",

        f"{growth_pct:.1f}%"

    )

    # =====================================================
    # LEADERSHIP GOAL
    # =====================================================

    st.subheader("🌟 Leadership Goal")

    leadership_goal = st.text_area(

        "What leadership capability do you want to improve?"

    )

    # =====================================================
    # DIGITAL GOAL
    # =====================================================

    st.subheader("💻 Digital Transformation Goal")

    digital_goal = st.text_area(

        "What digital initiative will you implement?"

    )

    # =====================================================
    # PERSONAL COMMITMENT
    # =====================================================

    st.subheader("✍️ Personal Commitment")

    commitment = st.text_area(

        "Write a commitment statement for the next 90 days"

    )

    # =====================================================
    # ACTION PLAN SUMMARY
    # =====================================================

    st.subheader("📋 My 90-Day Action Plan")

    summary = f"""

BUSINESS PRIORITIES

1. {priority1}

2. {priority2}

3. {priority3}

WORKING CAPITAL

• Reduce Receivable Days from
{current_receivable_days}
to
{target_receivable_days}

• Reduce Inventory Days from
{current_inventory_days}
to
{target_inventory_days}

GROWTH

• Increase Monthly Sales from
{current_sales}
to
{target_sales}

LEADERSHIP

• {leadership_goal}

DIGITAL TRANSFORMATION

• {digital_goal}

PERSONAL COMMITMENT

• {commitment}

"""

    st.text_area(

        "Action Plan Summary",

        summary,

        height=350

    )

    # =====================================================
    # FINAL MESSAGE
    # =====================================================

    st.success("""

🎉 Congratulations!

You have completed the

Ramco Cement
NextGen Dealer Finance Lab.

Remember:

✔ Profit matters

✔ Cash flow matters

✔ Customers matter

✔ Leadership matters

✔ Continuous learning matters

The future belongs to dealers who:

Run Smarter.
Grow Stronger.
Lead the Future.

""")

    # =====================================================
    # TAMIL CLOSING
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

🎯 இறுதி செய்தி

வெற்றி பெறும் Dealer:

• Profit பார்க்க வேண்டும்

• Cash Flow பார்க்க வேண்டும்

• Customer relationship வளர்க்க வேண்டும்

• Technology பயன்படுத்த வேண்டும்

• Leadership வளர்க்க வேண்டும்

சிறந்த எதிர்காலம்
திட்டமிடுபவர்களுக்கே சொந்தம்.

நன்றி!

""")

    # =====================================================
    # PROGRAMME CLOSING
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
### Developed and Designed by

**Prof. Shalini Velappan**  
Indian Institute of Management Tiruchirappalli

*Ramco Cement – NextGen Dealer Finance Lab*
"""
    )
# =========================================================
# GRADUATION CERTIFICATE
# =========================================================

elif menu == "🏆 Graduation Certificate":

    st.header("🏆 Graduation Certificate")

    st.markdown("""

### Congratulations!

You have successfully completed the

# Ramco Cement — NextGen Dealer Finance Lab

Management Development Programme

""")

    # =====================================================
    # PARTICIPANT DETAILS
    # =====================================================

    participant_name = st.text_input(
        "Participant Name"
    )

    dealer_name = st.text_input(
        "Dealership Name"
    )

    city = st.text_input(
        "City"
    )

    # =====================================================
    # SELF-ASSESSMENT
    # =====================================================

    st.subheader("📊 Self Assessment")

    finance_score = st.slider(
        "Finance Understanding",
        0,
        100,
        80
    )

    leadership_score = st.slider(
        "Leadership Readiness",
        0,
        100,
        75
    )

    digital_score = st.slider(
        "Digital Readiness",
        0,
        100,
        70
    )

    overall_score = round(
        (
            finance_score +
            leadership_score +
            digital_score
        ) / 3,
        1
    )

    # =====================================================
    # BADGE
    # =====================================================

    if overall_score >= 85:

        badge = "🥇 Gold Dealer Leader"

    elif overall_score >= 70:

        badge = "🥈 Silver Growth Leader"

    else:

        badge = "🥉 Emerging NextGen Leader"

    # =====================================================
    # CERTIFICATE
    # =====================================================

    st.markdown(f"""

<div style='
background:linear-gradient(135deg,#FFF8DC,#F5DEB3);
padding:40px;
border-radius:20px;
border:5px solid #B22222;
text-align:center;
'>

<h1>🏆 Certificate of Completion</h1>

<h2>{participant_name}</h2>

<p>
has successfully completed
</p>

<h2>
Ramco Cement
NextGen Dealer Finance Lab
</h2>

<p>
Management Development Programme
</p>

<p>
Representing
</p>

<h3>{dealer_name}</h3>

<p>
{city}
</p>



<p>
Developed and Designed by
</p>

<h3>
Prof. Shalini Velappan
</h3>

<p>
Indian Institute of Management Tiruchirappalli
</p>

</div>

""", unsafe_allow_html=True)

    # =====================================================
    # LEADERSHIP PLEDGE
    # =====================================================

    st.subheader("🌟 NextGen Dealer Pledge")

    st.success("""

I commit to:

✅ Building a profitable dealership

✅ Managing cash flow responsibly

✅ Using technology effectively

✅ Developing my team

✅ Serving customers with excellence

✅ Creating long-term sustainable growth

""")

    # =====================================================
    # TAMIL MESSAGE
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

🎉 வாழ்த்துக்கள்!

நீங்கள் வெற்றிகரமாக

Ramco Cement
NextGen Dealer Finance Lab

நிகழ்ச்சியை முடித்துள்ளீர்கள்.

அடுத்த தலைமுறை Dealer ஆக:

• Profit உருவாக்குங்கள்

• Cash Flow காப்பாற்றுங்கள்

• Technology பயன்படுத்துங்கள்

• Team வளர்த்திடுங்கள்

• Customer நம்பிக்கையை வெல்லுங்கள்

உங்கள் எதிர்காலத்திற்கு வாழ்த்துக்கள்!

""")

    # =====================================================
    # FINAL QUOTE
    # =====================================================

    st.markdown("""
---
### 🌱 Final Thought

**"A successful dealer does not merely sell cement.  
A successful dealer builds trust, relationships, systems, and a lasting business legacy."**
""")
# =========================================================
# HALL OF FAME
# =========================================================

elif menu == "🏆 Hall of Fame":

    st.header("🏆 NextGen Dealer Hall of Fame")

    st.markdown("""

### Discover Your Dealer Leadership Persona

Rate yourself on the following dimensions.

There are no right or wrong answers.

""")

    # =====================================================
    # SELF-ASSESSMENT
    # =====================================================

    finance = st.slider(
        "Finance & Profitability Focus",
        1,
        10,
        7
    )

    growth = st.slider(
        "Growth Orientation",
        1,
        10,
        7
    )

    digital = st.slider(
        "Digital Adoption",
        1,
        10,
        6
    )

    customer = st.slider(
        "Customer Relationship Focus",
        1,
        10,
        8
    )

    leadership = st.slider(
        "Leadership & Team Building",
        1,
        10,
        7
    )

    innovation = st.slider(
        "Innovation Mindset",
        1,
        10,
        6
    )

    # =====================================================
    # SCORES
    # =====================================================

    scores = {

        "📈 Finance Strategist":
        finance * 2 + leadership,

        "🦁 Growth Champion":
        growth * 2 + innovation,

        "💻 Digital Transformer":
        digital * 2 + innovation,

        "🤝 Relationship Builder":
        customer * 2 + leadership,

        "🌟 NextGen Visionary":
        leadership + innovation + growth

    }

    persona = max(
        scores,
        key=scores.get
    )

    # =====================================================
    # RADAR CHART
    # =====================================================

    categories = [

        "Finance",
        "Growth",
        "Digital",
        "Customer",
        "Leadership",
        "Innovation"

    ]

    values = [

        finance,
        growth,
        digital,
        customer,
        leadership,
        innovation

    ]

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill='toself'

        )

    )

    fig.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # RESULT
    # =====================================================

    st.subheader("🎖 Your Hall of Fame Identity")

    st.success(
        f"You are a: {persona}"
    )

    # =====================================================
    # PERSONA EXPLANATION
    # =====================================================

    if persona == "📈 Finance Strategist":

        st.info("""

You think like a CFO.

Strengths:

✅ Profitability

✅ Cash Flow

✅ Risk Management

✅ Financial Discipline

""")

    elif persona == "🦁 Growth Champion":

        st.info("""

You focus on expansion.

Strengths:

✅ Market Growth

✅ Business Development

✅ Ambition

✅ Opportunity Recognition

""")

    elif persona == "💻 Digital Transformer":

        st.info("""

You believe technology creates advantage.

Strengths:

✅ Automation

✅ Data

✅ Digital Innovation

✅ Modernization

""")

    elif persona == "🤝 Relationship Builder":

        st.info("""

You win through trust.

Strengths:

✅ Customer Relationships

✅ Dealer Networks

✅ Team Collaboration

✅ Loyalty

""")

    else:

        st.info("""

You are a future-focused leader.

Strengths:

✅ Vision

✅ Leadership

✅ Innovation

✅ Strategic Thinking

""")

    # =====================================================
    # LEADERBOARD
    # =====================================================

    st.subheader("🌟 World-Class Dealer Traits")

    hof_df = pd.DataFrame({

        "Trait":[

            "Financial Discipline",

            "Customer Focus",

            "Leadership",

            "Digital Adoption",

            "Growth Mindset"

        ],

        "Importance Score":[

            95,
            95,
            90,
            85,
            90

        ]

    })

    fig2 = px.bar(

        hof_df,

        x="Trait",

        y="Importance Score",

        title="Traits of Successful NextGen Dealers"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =====================================================
    # TAMIL VERSION
    # =====================================================

    if language == "English + தமிழ்":

        st.info("""

🏆 உங்கள் Dealer Style

📈 Finance Strategist
= Profit மற்றும் Cash Flow கவனம்

🦁 Growth Champion
= Business Expansion கவனம்

💻 Digital Transformer
= Technology கவனம்

🤝 Relationship Builder
= Customer & Trust கவனம்

🌟 NextGen Visionary
= Future Leadership கவனம்

""")

    # =====================================================
    # FINAL MESSAGE
    # =====================================================

    st.success("""

Every successful dealer is unique.

The best dealers combine:

✔ Financial Discipline

✔ Customer Trust

✔ Digital Capability

✔ Leadership

✔ Growth Mindset

""")

