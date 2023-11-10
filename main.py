from utils.dialogs import Dialog
from utils.pipelines import Pipeline


if __name__ == '__main__':
	Dialog.info()

	while True:
		Dialog.choices()
		user_choice = input()

		match user_choice:
			case '1':
				try:
					Pipeline.pipeline_weekly_hh()
					Dialog.success()
				except Exception as error:
					Dialog.failure(error)

			case '2':
				try:
					Pipeline.pipeline_weekly_security()
					Dialog.success()
				except Exception as error:
					Dialog.failure(error)

			case '3':
				try:
					Pipeline.pipeline_weekly_filters()
					Dialog.success()
				except Exception as error:
					Dialog.failure(error)
			case '4':
				try:
					Pipeline.pipeline_weekly_hh()
					Pipeline.pipeline_weekly_security()
					Pipeline.pipeline_weekly_filters()
					Dialog.success()
				except Exception as error:
					Dialog.failure(error)
			case '7':
				break
			case _:
				print('В разработке...')
