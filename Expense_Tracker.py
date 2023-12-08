class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(self.expenses)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense['category'] == category]

    def get_expenses_by_month(self, month):
        return [expense for expense in self.expenses if expense['month'] == month]

    def get_expenses_by_year(self, year):
        return [expense for expense in self.expenses if expense['year'] == year]

    def get_expenses_by_date_range(self, start_date, end_date):
        return [expense for expense in self.expenses if start_date <= expense['date'] <= end_date]

    def delete_expense(self, expense):
        self.expenses.remove(expense)
