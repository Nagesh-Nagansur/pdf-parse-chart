import plotly.graph_objects as go
import pandas as pd
from utils.util import read_from_mongo
import pandas as pd
import plotly.express as px





def create_bar_chart(transactions):

    df = pd.DataFrame(transactions)

    # Convert the 'amount' column from string to numeric by removing currency symbols and commas
    df['amount'] = df['amount'].replace({'₹': '', ',': ''}, regex=True).astype(float)

    # Group the data by 'category' and sum the 'amount'
    grouped_df = df.groupby('category')['amount'].sum().reset_index()

    # Create a pie chart using Plotly
    fig = px.pie(grouped_df, values='amount', names='category', title='Spending by Category')

    # Show the pie chart
    fig.show()

  