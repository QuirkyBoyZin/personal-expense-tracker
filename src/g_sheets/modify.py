from datetime import datetime

def add_row (sheet, type, name, price):
    
    print("In progress...")
    data = sheet.get_all_records()
    id=len(data)+1
    item=[id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]
    new=sheet.append_row(item)
    print("Done")
    return new
    
def remove_row(sheet, row_id ):
    
    print('Removing...')
    sheet.delete_rows(row_id + 1)
    print("Done")
    
    # Updating ID and formatting row after deletion
    sheet_data = sheet.get_all_records()
    for new_id, row in enumerate(sheet_data, start=1):
        sheet.update_cell(new_id + 1, 1, new_id)

def update_row(sheet, row_id, new_type = None, new_name = None, new_price = None):
    print("Updating...")
    row_index = row_id + 1
    data = sheet.get_all_records()
    row_data = data[row_id - 1]
    
    if new_name is not None:
        row_data["Name"] = new_name

    if new_type is not None:
        row_data["Category"] = new_type
    
    if new_price is not None:
        row_data["Price"] = new_price

    new_row = [row_id,  row_data["Date"],  row_data["Time"], row_data["Category"],row_data["Name"],row_data["Price"]]

    sheet.update(f"A{row_index}:F{row_index}", [new_row])
    print("Done")
    return new_row

if __name__ == "__main__":
   pass


    


