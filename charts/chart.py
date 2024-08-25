import plotly.graph_objects as go
import pandas as pd
from utils.util import read_from_mongo


data = read_from_mongo()

import pdb 
pdb.set_trace()

transactions = data.get("transactions", []).to_dict()[0]

def create_bar_chart():

    import pdb
    pdb.set_trace()
    # Convert to pandas DataFrame

    df = pd.DataFrame(transactions)
    df['amount'] = df['amount'].str.replace('₹', '').str.replace(',', '').astype(float)

    # Separate tables for DEBIT, CREDIT, and TRANSFER
    debit_df = df[df['type'] == 'DEBIT']
    credit_df = df[df['type'] == 'CREDIT']
    transfer_df = df[df['type'] == 'TRANSFER']

    # Calculate sums
    debit_total = debit_df['amount'].sum()
    credit_total = credit_df['amount'].sum()
    transfer_total = transfer_df['amount'].sum()

    # Add total row to each DataFrame
    debit_df = debit_df._append({'date': 'TOTAL', 'description': '', 'amount': debit_total, 
                                'transaction_id': '', 'utr_no': '', 'paid_by': ''}, ignore_index=True)
    credit_df = credit_df._append({'date': 'TOTAL', 'description': '', 'amount': credit_total, 
                                'transaction_id': '', 'utr_no': '', 'paid_by': ''}, ignore_index=True)
    transfer_df = transfer_df._append({'date': 'TOTAL', 'description': '', 'amount': transfer_total, 
                                    'transaction_id': '', 'utr_no': '', 'paid_by': ''}, ignore_index=True)

    # Create Plotly Table for DEBIT
    debit_table = go.Figure(data=[go.Table(
        header=dict(values=['Date', 'Description', 'Amount', 'Transaction ID', 'UTR No', 'Paid By'],
                    fill_color='red',
                    align='left'),
        cells=dict(values=[debit_df['date'], debit_df['description'], debit_df['amount'], 
                        debit_df['transaction_id'], debit_df['utr_no'], debit_df['paid_by']],
                fill_color=['lavender' if i < len(debit_df) - 1 else 'lightcoral' for i in range(len(debit_df))],
                align='left'))
    ])

    # Create Plotly Table for CREDIT
    credit_table = go.Figure(data=[go.Table(
        header=dict(values=['Date', 'Description', 'Amount', 'Transaction ID', 'UTR No', 'Paid By'],
                    fill_color='green',
                    align='left'),
        cells=dict(values=[credit_df['date'], credit_df['description'], credit_df['amount'], 
                        credit_df['transaction_id'], credit_df['utr_no'], credit_df['paid_by']],
                fill_color=['lavender' if i < len(credit_df) - 1 else 'lightcoral' for i in range(len(credit_df))],
                align='left'))
    ])

    # Create Plotly Table for TRANSFER
    transfer_table = go.Figure(data=[go.Table(
        header=dict(values=['Date', 'Description', 'Amount', 'Transaction ID', 'UTR No', 'Paid By'],
                    fill_color='blue',
                    align='left'),
        cells=dict(values=[transfer_df['date'], transfer_df['description'], transfer_df['amount'], 
                        transfer_df['transaction_id'], transfer_df['utr_no'], transfer_df['paid_by']],
                fill_color=['lavender' if i < len(transfer_df) - 1 else 'lightcoral' for i in range(len(transfer_df))],
                align='left'))
    ])

    # Show tables
    debit_table.show()
    credit_table.show()
    transfer_table.show()