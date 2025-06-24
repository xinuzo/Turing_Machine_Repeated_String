def calculate(input, rules):
    symbols = ["L"] + list(input) + ["R"]
 
    pos = 0
    state = 1
    counter = 0
 
    while True:
        found = False
 
        for old_symbol, old_state, new_symbol, new_state, action in rules:
            if symbols[pos] == old_symbol and state == old_state:
                found = True
                counter += 1
 
                symbols[pos] = new_symbol
                state = new_state
 
                if action == "RIGHT": pos += 1
                if action == "LEFT": pos -= 1
                if action == "ACCEPT": return True
                if action == "REJECT": return False
 
                if pos < 0 or pos >= len(symbols):
                    return False
 
                break
 
        if not found or counter == 1000:
            return False
