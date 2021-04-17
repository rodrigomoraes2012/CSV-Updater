import csv

# Main List, where all records will be stored
csv_list = []
# Output List, where duplicated rows will be replaced and updated by the last one
output_csv_list = []

replacingColumns = [2, 3, 4]
output_writer = csv.writer(open("output.csv", "w"), delimiter=';')

print('----------------------')

with open('first_file.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        csv_list.append(row)

with open('second_file.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_index = 0 
    for row in csv_reader:
        if line_index > 0:
            csv_list.append(row)
        line_index += 1

#print('Records: ' + str(len(csv_list)) )

index = 0
for row in csv_list:

    # Get the header
    if index == 0: 
        output_writer.writerow(row)

    # Get the rows
    else:

        # Primary Key column
        key_column_temp = str.strip( row[0])
        found = False # Detect duped rows

        temp_row = []
        for row_output in output_csv_list:
            key_column = str.strip( row_output[0] )
            
            if key_column == key_column_temp:
                found = True
                temp_row = row_output
                break

        if found: # Update
            # Replace specific columns
            for colNumber in replacingColumns:
                temp_row[colNumber] = row[colNumber]
        else: # Get new
            output_csv_list.append(row)

        # Log
        log = 'Processing: ' + key_column_temp
        if found:
            log += " - updating"
        print(log)

    index += 1

# Write output.csv file
for row_output in output_csv_list:
    output_writer.writerow(row_output)
    
print('----------------------')