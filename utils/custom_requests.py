from asyncio import create_task, gather
from typing import Any, Generator

from aiohttp import ClientSession
from requests import get
from requests.exceptions import JSONDecodeError

from utils.custom_exeptions import CustomExceptions as CE
from utils.variables import HEADERS, VACANCY_URL


class CustomRequests:
	@staticmethod
	def get_staffcop_response(
			url: str,
			headers: dict = None,
			params: dict = None,
			query: str = None
	) -> dict:
		"""
		Функция выполняет GET запрос по переданным в неё настройкам.
		:param params: Параметры запроса.
		:param url: Ссылка.
		:param headers: Заголовки запроса.
		:param query: Ключевое слово для получения конкретных результатов.
		:return: Словарь с кастомными событиями.
		"""
		try:
			response = get(url, headers=headers, params=params)
			response_json = response.json()
			match query:
				case None:
					return response_json
				case 'items':
					return response_json
				case _:
					return response_json.get(query)
		except ConnectionError as err:
			raise CE(err).conn_error()
		except KeyError as err:
			raise CE(err).key_error()
		except JSONDecodeError as err:
			raise CE(err).json_error()

	@staticmethod
	async def one_request(chosen_event: str, url_id: str | int) -> None:
		hh_url: str = VACANCY_URL
		headers: dict = HEADERS[chosen_event]

		async with ClientSession(headers=headers) as session:
			url = f'{hh_url}{url_id}'
			try:
				async with session.get(url=url,	headers=headers) as result:
					return await result.json()
			except ConnectionError as err:
				raise CE(err).conn_error()
			except KeyError as err:
				raise CE(err).key_error()
			except JSONDecodeError as err:
				raise CE(err).json_error()

	@staticmethod
	async def prepare_async_tasks(
			chosen_event: str,
			gen_data: Generator[list, Any, Any]
	) -> list:
		tasks, temp = [], []
		for data in gen_data:
			tasks.append(
				create_task(
					CustomRequests.one_request(
						chosen_event=chosen_event, url_id=data[0]
					)
				)
			)
			temp.append([data[1], data[2]])

		results = await gather(*tasks)

		final: list = [[i, y] for i, y in zip(temp, results)]

		return final
