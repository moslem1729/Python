def method_decorator(func):
	def wrapper(first_name, last_name):
		if len(first_name) == 0 and len(last_name) == 0:
			print("No names are given")
			return
		if len(first_name) == 0:
			print("first name is not given")
			return
		if len(last_name) == 0:
			print("last name is not given")
			return
		else:
			result = func(first_name, last_name)
			return

	return wrapper


# @method_decorator
def greet(first_name, last_name):
	print(f"hello, {first_name} {last_name}!")


decorated_greet = method_decorator(greet)
if __name__ == "__main__":
	# greet("John", "Doe")
	# greet("", "")
	decorated_greet("John","Doe")
	decorated_greet("","")