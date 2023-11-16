from os import getenv

from dotenv import load_dotenv


load_dotenv()

# Env keys

FACTS_URL = 'FACTS_URL'
AGGREGATE_URL = 'AGGREGATE_URL'
BACKEND = 'BACKEND'
DIM = 'DIM'
DRILL = 'DRILL'
DIR = 'DIR'
API_KEY = 'API_KEY'
DIM_FILTERS = 'DIM_FILTERS'
FILTER_HH = 'FILTER_HH'

# Date choices

LASTWEEK = 'lastweek'
YESTERDAY = 'yesterday'
CUSTOM = 'custom'

# User inputs

ENTER_DATE_FROM = 'Введите дату начала в формате ДДММ:\n'
ENTER_DATE_TO = 'Введите дату окончания в формате ДДММ:\n'
INPUT_ERROR = 'Ошибка ввода, попробуйте еще раз.'

# Events

STAFFCOP = 'staffcop'
HEADHUNTER = 'hh'
FILTERS = 'filters'
AMOUNT = 'amount'

# HeadHunter settings

VACANCY_URL = 'https://api.hh.ru/vacancies/'
VACANCY_SEARCH_FIELDS = 'name'
AREA = 1
INDUSTRY = 5
PROFESSIONAL_ROLE = 120
TEXT = 'Экономическая безопасность'
NO_MAGIC = 'true'
NO_VACANCY_TEXT = 'Подходящих вакансий не найдено'
VACANCY_URL_PATTERN = 'ru/vacancy/'

# Custom filters

STAFFCOP_FILTERS = {
	'custom': {
		'Head Hunter': getenv('FILTER_HH')
	},
	'general': {
		'Автомобильные порталы': getenv('FILTER_ANALYTIC_1'),
		'Видеохостинг': getenv('FILTER_ANALYTIC_2'),
		'Файлообменники': getenv('FILTER_ANALYTIC_3'),
		'Торговые площадки и доски объявлений': getenv('FILTER_ANALYTIC_4'),
		'Новостные ресурсы': getenv('FILTER_ANALYTIC_5'),
		'Развлекательные ресурсы': getenv('FILTER_ANALYTIC_6')
	}
}

# Exceptions text

KEY_ERROR = 'Ошибка получения по ключу'
CONNECTION_ERROR = 'Ошибка соединения'
JSON_ERROR = 'Ошибка валидации JSON'


# Save to file settings

EXT = '.csv'

FIELDS = {
	'staffcop':
		[
			'Дата',
			'Сотрудник',
			'Название вакансии',
			'Компания',
			'Город',
			'Зарплата',
			'Ссылка'
		],
	'hh':
		[
			'Название вакансии',
			'Компания',
			'Зарплата',
			'Ссылка'
		],
	'filters':
		[
			'Пользователь',
			'Компьютер',
			'Время',
			'Ссылка',
			'Заголовок'
		],
	'amount':
		[
			'Пользователь',
			'Количество событий'
		]
}

FILENAMES = {
	'staffcop': 'Отчет по НН за',
	'hh': 'Вакансии СБ',
	'amount': 'Количество событий'
}

PATHS = {
	'staffcop': 'files/weekly_staffcop_hh/',
	'hh': 'files/weekly_hh_security/',
	'filters': 'files/weekly_staffcop_filters/',
	'amount': 'files/weekly_amount_events/'
}

# Salary text

NO_SALARY = 'Зарплата не указана'
SALARY_FROM = 'Зарплата от '
SALARY_TO = 'Зарплата до '
TO = ' до '

# Requests settings

ITEMS = 'items'
OBJECT_LIST = 'object_list'

TIME_FROM = 'time_from='
TIME_FROM_END = 'T00:00:00.000&'
TIME_TO = 'time_to='
TIME_TO_END = 'T23:59:59.999&'

PARAMS = {
	'hh': {
			'vacancy_search_fields': VACANCY_SEARCH_FIELDS,
			'area': AREA,
			'industry': INDUSTRY,
			'professional_role': PROFESSIONAL_ROLE,
			'text': TEXT,
			'no_magic': NO_MAGIC
	}
}

HEADERS = {
	'staffcop': {
		'Authorization': getenv('HH_ACCESS_TOKEN')
	}
}

# JSON keys

AGENT_WEB_URL = 'agent_web.url'
LOCAL_TIME = 'local_time'
WINDOW_TITLE = 'window_title'
AGENT_ACCOUNT_USER_NAME = 'agent_account.user_name'
AGENT_ACCOUNT_COMPUTER_NAME = 'agent_agent.computer_name'
NAME = 'name'
EMPLOYER = 'employer'
SALARY = 'salary'
ALTERNATE_URL = 'alternate_url'
AREA_JSON = 'area'

# Csv hyperlink text

HYPERLINK = 'ГИПЕРССЫЛКА'
CLICK = 'Клик'
