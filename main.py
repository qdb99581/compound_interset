# # Set initial values
# init_principal = 0
# profit = 0.042
# monthly_fixed_purchase = 1000
# n_months = 14
# price_per_share = 16

# # Loop through each month and compound interest
# monthly_new_shares = {'compound': [], 'invest': []}
# principal = init_principal
# for i in range(n_months):
#     cash_dividend = profit * principal
    
#     monthly_new_shares['compound'].append(int(cash_dividend / price_per_share))
#     monthly_new_shares['invest'].append(monthly_fixed_purchase)

#     principal += monthly_new_shares['compound'][-1] + monthly_new_shares['invest'][-1]

# total_investment = sum(monthly_new_shares['invest'])
# # Print final result
# print(f"After {n_months} months, you will have {principal} shares.")
# print(f'From {init_principal} to {principal}, ROI is: {(principal - init_principal - total_investment)*price_per_share/total_investment:.2f}%')
# print(f'Earned {principal - init_principal - total_investment} shares = {(principal - init_principal - sum(monthly_new_shares["invest"])) * price_per_share} TWD')
# print(f'Invest: {total_investment}')


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class InvestmentCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Investment Calculator')
        self.setGeometry(100, 100, 500, 300)

        # Set initial values
        self.init_principal = 0
        self.profit = 0.042
        self.monthly_fixed_purchase = 1000
        self.n_months = 14
        self.price_per_share = 16

        # Create labels and line edits for inputs
        self.principal_label = QLabel('Initial Principal:', self)
        self.principal_label.move(50, 50)
        self.principal_input = QLineEdit(self)
        self.principal_input.move(200, 50)

        self.profit_label = QLabel('Profit:', self)
        self.profit_label.move(50, 80)
        self.profit_input = QLineEdit(self)
        self.profit_input.move(200, 80)

        self.monthly_label = QLabel('Monthly Fixed Purchase:', self)
        self.monthly_label.move(50, 110)
        self.monthly_input = QLineEdit(self)
        self.monthly_input.move(200, 110)

        self.months_label = QLabel('Number of Months:', self)
        self.months_label.move(50, 140)
        self.months_input = QLineEdit(self)
        self.months_input.move(200, 140)

        self.price_label = QLabel('Price per Share:', self)
        self.price_label.move(50, 170)
        self.price_input = QLineEdit(self)
        self.price_input.move(200, 170)

        # Create a button to calculate
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.move(200, 220)
        self.calculate_button.clicked.connect(self.calculate)

        # Create a label to display the result
        self.result_label = QLabel('', self)
        self.result_label.move(50, 250)

    def calculate(self):
        # Get the inputs from the line edits and convert them to floats
        try:
            self.init_principal = float(self.principal_input.text())
            self.profit = float(self.profit_input.text())
            self.monthly_fixed_purchase = float(self.monthly_input.text())
            self.n_months = float(self.months_input.text())
            self.price_per_share = float(self.price_input.text())
        except ValueError:
            self.result_label.setText('Invalid input(s). Please enter only floating-point numbers.')
            return

        # Loop through each month and compound interest
        monthly_new_shares = {'compound': [], 'invest': []}
        principal = self.init_principal
        for i in range(int(self.n_months)):
            cash_dividend = self.profit * principal

            monthly_new_shares['compound'].append(int(cash_dividend / self.price_per_share))
            monthly_new_shares['invest'].append(self.monthly_fixed_purchase)

            principal += monthly_new_shares['compound'][-1] + monthly_new_shares['invest'][-1]

        total_investment = sum(monthly_new_shares['invest'])
        # Set the result to the result label
        self.result_label.setText(f"After {self.n_months} months, you will have {principal} shares.\n"
                                  f'From {self.init_principal} to {principal}, ROI is: {(principal - self.init_principal - total_investment)*self.price_per_share/total_investment:.2f}%\n'
                                  f'Earned {principal - self.init_principal - total_investment} shares = {(principal - self.init_principal - sum(monthly_new_shares["invest"])) * self.price_per_share} TWD\n'
                                  f'Invest: {total_investment}')

if __name__ == '__main__':
    # Create the application and show the main window
    app = QApplication(sys.argv)
    window = InvestmentCalculator()
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
