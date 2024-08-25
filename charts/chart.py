from 



transactions = data["transactions"]
dates = [transaction["date"] for transaction in transactions]
amounts = [float(transaction["amount"].replace('₹', '').replace(',', '')) for transaction in transactions]
types = [transaction["type"] for transaction in transactions]

# Create a bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=dates,
    y=amounts,
    marker_color=['green' if t == 'CREDIT' else 'red' for t in types],
    text=[f'₹{amount}' for amount in amounts],
    textposition='outside'
))

# Update layout
fig.update_layout(
    title='Bank Transactions',
    xaxis_title='Date',
    yaxis_title='Amount (₹)',
    barmode='group'
)

# Show the figure
fig.show()