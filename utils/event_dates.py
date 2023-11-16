from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, SU

from utils.variables import ENTER_DATE_FROM, ENTER_DATE_TO, INPUT_ERROR


class EventDates:
	"""
	Класс для формирования дат для запросов.
	"""
	@staticmethod
	def get_current_year() -> int:
		"""
		Получаем текущий год.
		:return: Текущий год, тип данных int.
		"""
		today = date.today()
		return today.year

	@staticmethod
	def get_today() -> datetime:
		"""
		Получаем текущий день.
		:return: Текущий день, тип данных datetime.
		"""
		return datetime.today()

	@staticmethod
	def get_yesterday() -> str:
		today = EventDates.get_today()
		yesterday = today - timedelta(days=1)
		return yesterday.strftime('%Y-%m-%d')

	@staticmethod
	def get_custom_dates() -> tuple[str, str]:
		"""
		Функция позволяет расчитать произвольные даты.
		:return: Кортеж из стартовой и конечной дат.
		"""
		year = EventDates.get_current_year()
		start = input(ENTER_DATE_FROM)
		end = input(ENTER_DATE_TO)

		match len(start), len(end):
			case 4, 4:
				start_date = f'{year}-{start[2:4]}-{start[0:2]}'
				end_date = f'{year}-{end[2:4]}-{end[0:2]}'
				return start_date, end_date
			case _:
				print(INPUT_ERROR)
				EventDates.get_custom_dates()

	@staticmethod
	def get_last_week() -> tuple[str, str]:
		"""
		Функция считает даты начала и конца предыдущей недели.
		:return: Кортеж из стартовой и конечной дат предыдущей недели.
		"""

		today = EventDates.get_today()
		today_weekday = today.weekday()

		last_monday = today + relativedelta(
			days=-1, weekday=MO(-(1+today_weekday))
		)
		last_sunday = today + relativedelta(
			weekday=SU(-1)
		)

		return last_monday.strftime('%Y-%m-%d'), last_sunday.strftime('%Y-%m-%d')
