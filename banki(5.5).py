def process_bank_operations():
    

    account_balances = {}  

    while True:
        try:
            operation = input("Введите номер счета и сумму операции (например, 12345 100 или 67890 -50).  Для завершения введите 'стоп': ")

            if operation.lower() == 'стоп':
                break

            account_number, amount = operation.split()
            account_number = int(account_number)
            amount = float(amount)

            
            if account_number in account_balances:
                account_balances[account_number] += amount
            else:
                account_balances[account_number] = amount

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите номер счета и сумму через пробел.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    
    sorted_accounts = sorted(account_balances.items())  

    1
    print("\nИтоговые суммы на счетах (по возрастанию номера счета):")
    for account_number, balance in sorted_accounts:
        print(f"Счет: {account_number}, Итоговая сумма: {balance}")



if __name__ == "__main__":
    process_bank_operations()