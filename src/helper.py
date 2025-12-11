import time
from datetime import datetime
from g_sheets import sheets

date     = datetime.now().strftime("%Y-%m-%d")

def measure_perf(base_fn):
    """A decorator for measuring code execution time of a function"""
    def wrapper(*args):
        
        start_time   = time.perf_counter()
        result = base_fn(*args)
        end_time     = time.perf_counter()
        elasped_time = end_time - start_time
        
        print(f"Execution time for {base_fn.__name__}: {elasped_time:.3f} Seconds")
        return result
       
    return wrapper



def view_expense() -> str:
    """View today's expenses with vertical price column in Telegram using monospace."""
    
    expenses = sheets.get_expenses_at(date)
    if expenses == []:
        return "```\n" + "\n" "Log something down..."+ "\n```"
    # Header
    lines = [" "]

    # Fixed column widths
    index_width = 3
    category_width = 10
    name_width = 15
    price_width = 6  # right-aligned

    # Build lines
    for index, row in enumerate(expenses, start=1):
        category:str = row[3]
        name:str = row[4]
        price:str = row[5]
        line = f"{index:<{index_width}} {category.capitalize():<{category_width}} {name.capitalize():<{name_width}} {price:>{price_width}}"
        lines.append(line)

    # Join lines and wrap in monospace formatting
    result = "```\n" + "\n" .join(lines)+ "\n```"
    return result

def find_id(args: int) -> tuple[bool|str] :
    """ Given an index find the corresponding ID returns false if not found"""
    expense = sheets.get_expenses_at(date)
    
    max_index = len(expense)
    index = int(args) - 1
    index_range = [i for i in range (max_index)]
    
    if index not in index_range: 
        return False
        
    id  =  int(expense[index][0])
    return id

def get_item(id: int) -> str:
    """ Given an id returns a string consists of the item's category name and price"""
    expense  =  sheets.get_item(id)

    category: str   =  expense[0]
    name:     str   =  expense[1]
    price:    float =  expense[2]
    
    return f"{category.capitalize()} {name.capitalize()} {price}" 


if __name__ == '__main__':
    print(get_item(1))
    pass