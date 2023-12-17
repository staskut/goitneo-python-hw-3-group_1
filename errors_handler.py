# error handler decorator to these commands https://github.com/staskut/goitneo-python-hw-1-group_1/blob/main/main.py

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner

