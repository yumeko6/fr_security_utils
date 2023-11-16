from os import getenv

from utils.event_dates import EventDates
from utils.variables import (
	LASTWEEK,
	CUSTOM,
	STAFFCOP,
	HEADHUNTER,
	VACANCY_URL,
	FILTERS,
	FACTS_URL,
	BACKEND,
	DIM,
	DIR,
	API_KEY,
	DIM_FILTERS,
	FILTER_HH,
	TIME_FROM,
	TIME_FROM_END,
	TIME_TO,
	TIME_TO_END, AMOUNT, AGGREGATE_URL, DRILL, YESTERDAY
)


def prepare_url_to_request(
		chosen_dates: str | None,
		chosen_event: str,
		filters=None
) -> str:
	"""
	Функция формирует ссылку для GET запроса на основе переданных в неё данных.
	:param chosen_dates: Тип дат (кастомный или за прошлую неделю).
	:param chosen_event: Тип события.
	:param filters: Кастомные фильтры.
	:return: Ссылка для GET запроса.
	"""

	facts = getenv(FACTS_URL)
	aggregate = getenv(AGGREGATE_URL)
	back = getenv(BACKEND)
	dim = getenv(DIM)
	drill = getenv(DRILL)
	dir_ = getenv(DIR)
	key = getenv(API_KEY)
	dim_f = getenv(DIM_FILTERS)
	hh = getenv(FILTER_HH)
	start, end = None, None

	if chosen_dates == LASTWEEK:
		start, end = EventDates.get_last_week()
	elif chosen_dates == CUSTOM:
		start, end = EventDates.get_custom_dates()
	elif chosen_dates == YESTERDAY:
		start = EventDates.get_yesterday()
		end = start

	time_from = f'{TIME_FROM}{start}{TIME_FROM_END}'
	time_to = f'{TIME_TO}{end}{TIME_TO_END}'

	url_formats = {
		STAFFCOP: f'{facts}{back}{dim}{dir_}{hh}{time_from}{time_to}{key}',
		HEADHUNTER: VACANCY_URL,
		FILTERS: f'{facts}{back}{dim_f}{dir_}{filters}{time_from}{time_to}{key}',
		AMOUNT: f'{aggregate}{back}{drill}{time_from}{time_to}{key}'
	}

	url = url_formats.get(chosen_event)

	return url
