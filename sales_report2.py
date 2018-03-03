"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
melon_sales_by_salesperson = {}

sales_data = open('sales-report.txt')

for record in sales_data:
    record = record.rstrip().split("|")
    if record[0] in melon_sales_by_salesperson:
        melon_sales_by_salesperson[record[0]] += int(record[2])
    else:
        melon_sales_by_salesperson[record[0]] = int(record[2])

for salesperson, melons_sold in melon_sales_by_salesperson.items():
    print "{} sold {} melons.".format(salesperson, melons_sold)

# IMPROVEMENTS ADDED:
# - Use a dictionary to group salesperson name & sales figures together (also
#   avoids confusion about matching each index to its pair between lists)
# - Directly add content to dictionary using index of each iteration instead
#   of binding it to a variable first (can also typecast to int this way)
# - Print by iterating over dictionary & using key & value pulled using .items()
#   method instead of attempting to reconstruct association of name & sales number
#   values from disparate list indices.