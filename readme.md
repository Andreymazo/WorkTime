Пользователи - admin (администратор), employee (сотрудник). Джанго проект учета рабочего времени. Календарь datepicker,
формы джанго. Предусмотрено логирование пользователя. У пользователя - сотрудника считается рабочее время.
В проекте предусмотрена валюта, для расчета заработной платы. Валюта привязана к .....(сотруднику)?
Сотрудник не может видеть информацию кроме своей.

Пользователь сотрудник логируется и попадает на персональную информацию, может

    - посмотреть сколько времени осталось до конца рабочего дня, прошло рабочего дня, и до конца рабочей недели,
    - начать течение рабочего времени,
    - прекратить течение рабочего времени

    - посмотреть сколько заработная плата за день, за неделю

    В случае нажатия на продолжение/прекращение течения рабочего дня пользоатель сотрудник попадает на ...

Пользователь администратор логируется и попадает на список сотрудников, может

    - посмотреть список сотрудников с из параментрами (Имя, Фамилия, e-mail, длительность трудового дня, состав рабочей недели,

    В случае нажатия на добавить/изменить сотрудника пользоатель администратор попадает на окно добавить/изменить сотрудника

        В случае нажатия на добавить/изменить сотрудника пользоатель администратор попадает на ...

    В случае нажатия на удалить сотрудника пользоатель администратор попадает на ...


Запуск.
  - Скопируйте проект
    - git clone git@github.com:Andreymazo/WorkingTime.git
  - Установите зависимости
    - pip install -r requirements.txt
  - Установите базу. Файл .env_sample поможет с параметрами.
  - Загрузите базу (одна команда из двух должна загрузить)
    - python manage.py loaddata db.json/python manage.py loaddata db.json_foreign_user
  - Запуск
    - python manage.py runserver
  - Командные файлы в папке workingtime/management/commands с создания суперюзера create_super_user.py и поочереди create_employer.py, create_employee.py, create_timesheet.py
  - можно через админку работать (суперюзер изсстафф должно быть тру)
