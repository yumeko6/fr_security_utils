from utils.variables import NO_SALARY, SALARY_FROM, SALARY_TO, TO


class Salary:
	"""
	Класс для формирования текстовых данных о зарплате.
	"""
	@staticmethod
	def match_salary(temp_salary: dict | None) -> str:
		"""
		Функция сравнивает переданные в неё данные о зарплате и разбивает на
		зарплату до и зарплату после в зависимости от данных.
		:param temp_salary: Данные о зарплате
		:return: NO_SALARY если переданное в функцию значение равно None
		"""
		match temp_salary:
			case None:
				return NO_SALARY
			case _:
				salary_from: int = temp_salary.get('from', '')
				salary_to: int = temp_salary.get('to', '')
				match salary_from, salary_to:
					case None, _:
						return Salary.__get_salary_to(str(salary_to))
					case _, None:
						return Salary.__get_salary_from(str(salary_from))
					case _, _:
						return Salary.__get_salary_from_to(
							str(salary_from), str(salary_to)
						)

	@staticmethod
	def __get_salary_from(s_from: str) -> str:
		"""
		Функция формирует текстовые данные о зарплате.
		:param s_from: Запрлата от.
		:return: Текстовые данные о зарплате.
		"""
		return f'{SALARY_FROM}{s_from}'

	@staticmethod
	def __get_salary_to(s_to: str) -> str:
		"""
		Функция формирует текстовые данные о зарплате.
		:param s_to: Зарплата до.
		:return: Текстовые данные о зарплате.
		"""
		return f'{SALARY_TO}{s_to}'

	@staticmethod
	def __get_salary_from_to(s_from: str, s_to: str) -> str:
		"""
		Функция формирует текстовые данные о зарплате.
		:param s_from: Зарплата от.
		:param s_to: Зарплата до.
		:return: Текстовые данные о зарплате.
		"""
		return f'{SALARY_FROM}{s_from}{TO}{s_to}'
