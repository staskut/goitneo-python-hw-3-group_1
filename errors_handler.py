# error handler decorator to these commands https://github.com/staskut/goitneo-python-hw-1-group_1/blob/main/main.py

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return None
        except KeyError:
            return None
        except IndexError:
            return None

    return inner

