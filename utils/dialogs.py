from colorama import init, Fore


init()


class Dialog:
	@staticmethod
	def info():
		print(
			Fore.LIGHTGREEN_EX +
			'Добро пожаловать в консоль обработки запросов '
			'Staffcop и HeadHunter!\n'
			'На данный момент реализованы функции 1-3, а также 4, выполняющая \n'
			'полноценный отчет по всем трём категориям.'
		)

	@staticmethod
	def choices():
		print(
			Fore.LIGHTYELLOW_EX +
			'Выберите необходимое действие:\n'
			'1 - Еженедельный отчет по HH\n'
			'2 - Еженедельный отчет по вакансиям СБ\n'
			'3 - Еженедельный отчет по непродуктивности\n'
			'4 - Еженедельный отчет по количеству событий\n'
			'5 - Ежедневный отчет по количеству событий\n'
			'6 - Полный еженедельный отчет (включая пункты 1-4)\n'
			'7 - Еженедельный отчет по HH за произвольную дату\n'
			'8 - Еженедельный отчет по непродуктивности за произвольную дату\n'
			'9 - Завершить работу'
		)

	@staticmethod
	def success():
		print(Fore.GREEN + f'Отчет выполнен успешно!')

	@staticmethod
	def failure(error):
		print(
			Fore.RED +
			f'Во время выполнения отчета произошла ошибка!\n'
			f'{error}'
		)
