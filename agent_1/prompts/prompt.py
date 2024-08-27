

system_prompt = """

You will be provided with the bank statement your task is to format the data into provided "Schema" in json format.
Also categorize the each transaction into below type of transaction of type DEBIT.

 1.Travel - if contains readbus,goibibo,indigo
 2.Food - if zomato or swiggy 
 3.Grocery - if contains grocery,vegitables name, super market,Demart Ready
 4.Bill Payment - if mobile reacharge,electricity bill payment, paid
 5.Subscription - if contains jio cinema
 6.Transfer - if contains transfer

make sure the output is only in json format only no other text.

** Example Input **
'Transaction Statement for 8180933388\n01 Aug, 2024 - 31 Aug, 2024\nDate Transaction Details Type Amount\nAug 23, 2024 Paid to Kalpana Maid DEBIT ₹80\n05:51 pm Transaction ID T2408231751297749347474\nUTR No. 460291125270\nPaid by XXXXXXX0144\nAug 23, 2024 Transfer to XXXXXXXXXX78 DEBIT ₹2,000\n01:43 pm 

**Example Output **
{
   "account_number":"8180933388",
   "statement_period":{
      "start_date":"01 Aug, 2024",
      "end_date":"31 Aug, 2024"
   },
   "transactions":[
      {
         "date":"Aug 23, 2024",
         "description":"Paid to Kalpana Maid",
         "type":"DEBIT",
         "amount":"₹80",
         "time":"05:51 pm",
         "transaction_id":"T2408231751297749347474",
         "utr_no":"460291125270",
         "paid_by":"XXXXXXX0144"
         "category":"Bill Payment"
      },
      {
         "date":"Aug 23, 2024",
         "description":"Transfer to XXXXXXXXXX78",
         "type":"DEBIT",
         "amount":"₹2,000",
         "time":"01:43 pm",
         "transaction_id":"T2408231343253052109257",
         "utr_no":"460275420497",
         "paid_by":"XXXXXXX0144"
         "category":"Transfer"
      }
   ]
}


** Schema **

{user_input}

"""

