from utils.variables import CONNECTION_ERROR, JSON_ERROR, KEY_ERROR


class CustomExceptions:
	"""
	Небольшой класс, отвечающий за передачу текста ошибки в вызов raise.
	"""
	def __init__(self, text):
		self.text = text

	def key_error(self):
		"""
		Текст для события KeyError Exception.
		:return: Текст ошибки.
		"""
		return f'{KEY_ERROR} {self.text}'

	def conn_error(self):
		"""
		Текст для события ConnectionError Exception.
		:return: Текст ошибки.
		"""
		return f'{CONNECTION_ERROR} {self.text}'

	def json_error(self):
		"""
		Текст для события JSONError Exception.
		:return: Текст ошибки.
		"""
		return f'{JSON_ERROR} {self.text}'
