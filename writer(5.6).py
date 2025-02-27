def process_book_sales():
    
    sales = []
    while True:
        author = input("Enter author's name (or 'stop' to finish): ")
        if author.lower() == 'stop':
            break

        title = input("Enter book title: ")
        publication_year = int(input("Enter publication year: "))
        quantity = int(input("Enter number of copies sold: "))

        sales.append({
            "author": author,
            "title": title,
            "publication_year": publication_year,
            "quantity": quantity
        })

    sales_totals = {}
    for sale in sales:
        author = sale["author"]
        quantity = sale["quantity"]

        if author in sales_totals:
            sales_totals[author] += quantity
        else:
            sales_totals[author] = quantity

    authors = sorted(sales_totals.keys())

    print("\nTotal number of copies sold by author (in alphabetical order):")
    for author in authors:
        print(f"{author}: {sales_totals[author]}")

process_book_sales()