from setuptools import setup, find_packages

setup(
    name='class_schedul_manager', # Название вашей программы
    version='0.0.1', # Версия вашей программы.
    packages=find_packages("."),
    scripts=["bin/uni_schedule.py"], # Расположение главного исполняемого файла.
    url='https://github.com/LissavetaL8/Python_course/tree/main', # Адрес репозитория с вашей курсовой работой.
    license='Apache-2.0',
    author='Лопатинская Елизавета Сергеевна', # ФИО автора.
    author_email='elizavetalopatinskaa@gmail.com', # Электронная почта автора.
    description='...', # Описание вашей поделки. Что она может, для чего сделана.
    include_package_data=True,
    install_requires=[],
)




