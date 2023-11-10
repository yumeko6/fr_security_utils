from csv import writer
import datetime

from utils.event_dates import EventDates
from utils.variables import FIELDS, FILENAMES, STAFFCOP, HEADHUNTER, FILTERS, \
	EXT


class SaveToFile:
	"""
	Класс для формирования полей и имени файла и сохранения в файл.
	"""

	@staticmethod
	def __prepare_fields_and_filename(
			chosen_event: str,
			path: str,
			start: datetime = None,
			end: datetime = None,
			today: datetime = None,
			custom_filter: str = None,
	) -> tuple[list[str], str]:
		"""
		Функция готовит поля для таблицы и название файла выгрузки из
		предоставленных данных.
		:param chosen_event: Выбранный тип данных для выгрузки.
		:param path: Путь до папки с выгрузками событий.
		:param start: Дата начала событий.
		:param end: Дата окончания событий.
		:param today: Дата сегодня.
		:param custom_filter: Кастомный фильтр.
		:return: Поля для таблицы и название файла.
		"""

		fields = FIELDS[chosen_event]
		filename = None

		if chosen_event == STAFFCOP:
			filename = f'{path}{FILENAMES[chosen_event]} {start}-{end}{EXT}'
		elif chosen_event == HEADHUNTER:
			filename = f'{path}{FILENAMES[chosen_event]} {today}{EXT}'
		elif chosen_event == FILTERS:
			filename = f'{path}{custom_filter} {start}-{end}{EXT}'

		return fields, filename

	@staticmethod
	def save_event_to_csv(
			chosen_event: str,
			start: datetime,
			end: datetime,
			data: list,
			path: str,
			custom_filter: str = None
	) -> None:
		"""
		Функция сохраняет в файл переданные в неё данные.
		:param chosen_event: Тип события.
		:param start: Начало событий.
		:param end: Окончание событий.
		:param data: Список данных.
		:param path: Путь до папки с выгрузками событий.
		:param custom_filter: Кастомный фильтр.
		:return: Сохраянет данные в файл csv.
		"""

		today = EventDates.get_today().date()
		fields, filename = SaveToFile.__prepare_fields_and_filename(
			chosen_event, path, start, end, today, custom_filter
		)

		with open(filename, 'w', newline='', encoding='utf_8_sig') as f:
			write = writer(f, delimiter=';')
			write.writerow(fields)
			write.writerows(data)
