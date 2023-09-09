Запуск проекта:

Cоздаем образы контейнеров, запускаем их и наполняем базу тестовыми данными:


      docker-compose up

Проект доступен по ссылкам:
   
    api docs - http://127.0.0.1:7777/docs
 
    admin - http://127.0.0.1:7777/admin


Если потребуется стереть и заново создать тестовые данные:

    docker exec backend python initial_db.py 

Подключение к postgres:

    psql -U postgres -d bookingsDB -h 0.0.0.0 -p 6543
    пароль - bookings_pass132