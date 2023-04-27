# Calculate Relevant Tax on Share Options (RTSO) Portugal
import sys

def stock_options_calculator(strike_price, market_value, share_count):
  gross_profit = (market_value * share_count) - (strike_price * share_count)
  tax_liability = gross_profit * 0.14 # https://www.newco.pro/en/blog/tax-alert-taxation-of-stock-options-in-portugal
  net_profit = gross_profit - tax_liability
  return gross_profit, tax_liability, net_profit

# Get command line arguments
strike_price = float(sys.argv[1])
market_value = float(sys.argv[2])
share_count = float(sys.argv[3])

# Calculate income gain
gross_profit, tax_liability, net_profit = stock_options_calculator(strike_price, market_value, share_count)
print("Gross profit:", gross_profit)
print("Tax liability:", tax_liability)
print("Net profit:", net_profit)
