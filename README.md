# test_task
Тестовое задание

С использованием fastapi необходимо сделать веб-страницу состоящую из:
1. Формы с текстовым полем
2. Списком сообщений пронумерованных с 1

Страница подключается к серверу по WebSocket.
С помощью формы вы можете отправить сообщение на сервер, где оно будет принято и добавлен порядковый номер этого сообщения.
Далее сообщение с порядковым номером отправляется на страницу и отображается в списке.

При перезагрузке страницы данные о номерации теряются и начинается с 1.

Страница должна быть динамической, обрабатывать все действия без перезагрузки. Имеется ввиду что при отправке сообщения на сервер через вебсокет страница не должна перезагружаться.
Взаимодействие с сервером по вебсокет нужно реализовать с использованием JSON.

Тестовое задание выполнено на Python 3.9
Все необходимые зависимости перечислены в requirements.txt
