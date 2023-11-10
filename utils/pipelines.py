from asyncio import run

from utils.custom_requests import CustomRequests as CR
from utils.event_dates import EventDates
from utils.events import Events
from utils.save_to_file import SaveToFile
from utils.variables import STAFFCOP, LASTWEEK, HEADHUNTER, STAFFCOP_FILTERS, \
	FILTERS, PATHS


class Pipeline:
	@staticmethod
	def pipeline_weekly_hh():
		"""
		Пайплайн для выполнения еженедельной задачи по фильтру hh.ru в staffcop.
		:return: Файл csv в папке files/weekly_staffcop_hh
		"""
		chosen_event = STAFFCOP
		chosen_dates = LASTWEEK
		all_events = Events.get_all_staffcop_events(
			chosen_dates=chosen_dates,
			chosen_event=chosen_event
		)
		all_hh_urls = Events.get_generator_of_all_staffcop_events(
			all_events
		)
		all_hh_events = run(
			CR.prepare_async_tasks(
				chosen_event=chosen_event, gen_data=all_hh_urls
			)
		)
		data_to_file = Events.prepare_data_to_save_in_csv(all_hh_events)
		start, end = EventDates.get_last_week()
		SaveToFile.save_event_to_csv(
			chosen_event=chosen_event,
			start=start,
			end=end,
			data=[event for event in data_to_file],
			path=PATHS[chosen_event]
		)

	@staticmethod
	def pipeline_weekly_security():
		chosen_event = HEADHUNTER
		start = EventDates.get_today()
		end = start
		all_events = Events.get_security_vacancies(
			chosen_event=chosen_event
		)
		all_events_gen = Events.get_generator_of_security_vacancies(
			all_events
		)
		SaveToFile.save_event_to_csv(
			chosen_event=chosen_event,
			start=start,
			end=end,
			data=[event for event in all_events_gen],
			path=PATHS[chosen_event]
		)

	@staticmethod
	def pipeline_weekly_filters():
		chosen_event = FILTERS
		chosen_dates = LASTWEEK

		for policy, sc_filter in STAFFCOP_FILTERS['general'].items():
			all_events = Events.get_analytics_filters(
				chosen_dates=chosen_dates,
				chosen_event=chosen_event,
				chosen_filter=sc_filter
			)

			match len(all_events):
				case 0:
					continue
				case _:
					all_events_gen = Events.get_generator_of_analytics_filters(
						all_events
					)
					start, end = EventDates.get_last_week()
					SaveToFile.save_event_to_csv(
						chosen_event=chosen_event,
						start=start,
						end=end,
						data=[event for event in all_events_gen],
						custom_filter=policy,
						path=PATHS[chosen_event]
					)
