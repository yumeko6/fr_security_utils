from re import search
from typing import Any, Generator

from utils.custom_requests import CustomRequests as CR
from utils.custom_exeptions import CustomExceptions as CE
from utils.salaries import Salary
from utils.urls import prepare_url_to_request
from utils.variables import *


class Events:
	"""
	Класс для получения кастомных событий.
	"""

	@staticmethod
	def get_all_staffcop_events(chosen_dates: str, chosen_event: str) -> dict:
		"""
		Функция обращается к базе данных staffcop для получения всех фактов
		по заданному фильтру(посещение сайта hh.ru за предыдущую неделю или
		за произвольный отрезок времени).
		:param chosen_dates: Тип дат (кастомный или за прошлую неделю).
		:param chosen_event: Тип события.
		:return: Словарь с кастомными событиями.
		"""
		url = prepare_url_to_request(
			chosen_dates=chosen_dates, chosen_event=chosen_event
		)
		return CR.get_staffcop_response(url=url, query=OBJECT_LIST)

	@staticmethod
	def get_generator_of_all_staffcop_events(
			data: dict) -> Generator[list, Any, Any]:
		"""
		Функция создает генератор списков на основе полученных данных.
		:param data: Список событий.
		:return: Генератор списков.
		"""

		for event in data:
			url = event.get(AGENT_WEB_URL, '')
			if VACANCY_URL_PATTERN in url:
				vac_id_match = search(r"\d+", url)
				if vac_id_match:
					vac_id = vac_id_match.group()
					event_date: str = event.get(LOCAL_TIME, '').split('+')[0]
					user: str = event.get(AGENT_ACCOUNT_USER_NAME, '')

					yield [vac_id, event_date, user]

	@staticmethod
	def prepare_data_to_save_in_csv(
			data: list
	) -> Generator[list, Any, Any]:
		"""
		Функция подготовливает необходимые данные для записи в файл.
		:param data: Список входных данных.
		:return: Генератор списков подготовленных данных.
		"""
		for value in data:
			job_data = value[1]
			name: str = job_data.get(NAME, '')
			employer: str = job_data.get(EMPLOYER, {}).get(NAME, '')
			area: str = job_data.get(AREA_JSON, {}).get(NAME, '')
			temp_salary: dict = job_data.get(SALARY, {})
			salary: str = Salary.match_salary(temp_salary)
			alternate_url: str = job_data.get(ALTERNATE_URL, '')
			url: str = f'={HYPERLINK}("{alternate_url}"; "{CLICK}")'

			yield [value[0][0], value[0][1], name, employer, area, salary, url]

	@staticmethod
	def get_security_vacancies(chosen_event: str) -> dict:
		"""
		Функция с помощью подключения к api hh.ru получает список вакансий
		по заранее заданным фильтрам в словаре params.
		:param chosen_event: Тип события.
		:return: Словарь с кастомными событиями.
		"""
		params = PARAMS[chosen_event]

		url = prepare_url_to_request(
			chosen_dates=None, chosen_event=chosen_event
		)

		return CR.get_staffcop_response(url=url,	params=params, query=ITEMS)

	@staticmethod
	def get_generator_of_security_vacancies(
			data: dict
	) -> Generator[list[str], Any, str]:
		"""
		Функция создает генератор списков на основе полученных данных.
		:param data: Список событий.
		:return: Генератор списков.
		"""
		match len(data) > 0:
			case True:
				for vacancy in data.get('items', []):
					try:
						name: str = vacancy.get(NAME, '')
						employer: str = vacancy.get(EMPLOYER, {}).get(NAME, '')
						temp_salary: dict = vacancy.get(SALARY, {})
						salary: str = Salary.match_salary(temp_salary)
						alternate_url: str = vacancy.get(ALTERNATE_URL, '')
						url: str = f'={HYPERLINK}("{alternate_url}"; "{CLICK}")'

						yield [name, employer, salary, url]
					except KeyError as err:
						raise CE(err).key_error()
			case False:
				return NO_VACANCY_TEXT

	@staticmethod
	def get_analytics_filters(
			chosen_dates: str,
			chosen_event: str,
			chosen_filter: str
	) -> dict:
		"""
		Функция для получения событий по встроенным в staffcop фильтрам.
		:param chosen_dates: Тип дат (кастомный или за прошлую неделю).
		:param chosen_event: Тип события.
		:param chosen_filter: Тип фильтра.
		:return: Словарь с кастомными событиями.
		"""

		url = prepare_url_to_request(
			chosen_dates=chosen_dates,
			chosen_event=chosen_event,
			filters=chosen_filter
		)

		return CR.get_staffcop_response(url=url, query=OBJECT_LIST)

	@staticmethod
	def get_generator_of_analytics_filters(
			data: dict
	) -> Generator[list[str], Any, Any]:
		"""
		Функция создает генератор списков на основе полученных данных.
		:param data: Список событий.
		:return: Генератор списков.
		"""
		for filter_data in data:
			try:
				name: str = filter_data.get(AGENT_ACCOUNT_USER_NAME, '')
				computer: str = filter_data.get(AGENT_ACCOUNT_COMPUTER_NAME, '')
				local_time: str = filter_data.get(LOCAL_TIME, '').split('+')[0]
				url: str = filter_data.get(AGENT_WEB_URL, '')
				title: str = filter_data.get(WINDOW_TITLE, '')

				yield [name, computer, local_time, url, title]
			except KeyError as err:
				raise CE(err).key_error()
