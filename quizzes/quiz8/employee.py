class Employee:
    # class attribute
    figure = "regular"

    # constructor
    def __init__(self, name, position, start_salary, annual_rate, contract_years):
        self.name = name
        self.position = position
        self.start_salary = start_salary
        self.annual_rate = annual_rate
        self.contract_years = contract_years

    # instance method
    def get_cumulative_salary(self):
        """
        This function calculates the cumulative salary after
        @param contract_years: 
        @return: 
        """
        yearly_salary = self.start_salary
        cumulated_salary = self.start_salary
        if self.contract_years <= 1:
            return yearly_salary
        else:
            for year in range(1, self.contract_years):
                yearly_salary += yearly_salary * (self.annual_rate / 100)
                cumulated_salary += yearly_salary

        return round(cumulated_salary, 2)


def print_employees(employees):
    """
    Prints employees records given a list of employee objects
    @param employees: 
    @return: 
    """
    print(f"\n{'Name':<20}{'Position':<20}{'Start salary':<20}{'Annual rate':<20}{'Cumulative salary':<20}")
    for employee in employees:
        cumulative_salary = employee.get_cumulative_salary()
        print(
            f"{employee.name:<20}{employee.position:<20}{employee.start_salary:<20}{employee.annual_rate:<20}{cumulative_salary:<20}")


def main():
    """
    Prompts for the number of employees. Reads the employee records comma-separated. Calls the print_employees() function.
    @return:
    """
    number_of_employees = int(input("Enter the number of employees: "))
    employees = []
    for employee in range(number_of_employees):
        record = input("name, position, start salary, annual rate, contract years: ").split(',')
        name = record[0]
        position = record[1]
        start_salary = float(record[2])
        annual_rate = float(record[3])
        contract_years = int(record[4])
        employees.append(Employee(name, position, start_salary, annual_rate, contract_years))
    print_employees(employees)


if __name__ == '__main__':
    main()
