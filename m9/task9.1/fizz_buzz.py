def get_info(servers,size):

	if servers>30 and size>400:
		return 'FizzBuzz/Vip'
	elif size>400 and servers<30:
		return 'Fizz/Medium'
	elif servers<30 and size<400:
		return 'Buzz/Demo'
	else:
		return ''
