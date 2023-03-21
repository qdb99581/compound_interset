# Set initial values
init_principal = 1000
profit = 0.042
monthly_fixed_purchase = 1000
n_months = 14
price_per_share = 16

# Loop through each month and compound interest
monthly_new_shares = {'compound': [], 'invest': []}
principal = init_principal
for i in range(n_months):
    cash_dividend = profit * principal
    
    monthly_new_shares['compound'].append(int(cash_dividend / price_per_share))
    monthly_new_shares['invest'].append(monthly_fixed_purchase)

    principal += monthly_new_shares['compound'][-1] + monthly_new_shares['invest'][-1]

total_investment = sum(monthly_new_shares['invest'])
# Print final result
print(f"After {n_months} months, you will have {principal} shares.")
print(f'From {init_principal} to {principal}, ROI is: {(principal - init_principal - total_investment)*price_per_share/total_investment:.2f}%')
print(f'Earned {principal - init_principal - total_investment} shares = {(principal - init_principal - sum(monthly_new_shares["invest"])) * price_per_share} TWD')
