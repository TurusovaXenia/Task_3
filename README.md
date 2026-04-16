# Task_3

Данный проект содержит набор автоматизированных UI-тестов для сервиса "Stellar Burgers". Тесты написаны на
**Python** c применением **Pytest** и **Selenium**.
Проект реализован с использованием паттерна **Page Object Model**:

- locators/ - описание локаторов страниц
- pages/ - описание методов страниц
- tests/ - сами тестовые методы
- utils/ - вспомогательные методы для генерации данных
- conftest.py - фикстуры для тестов
- data.py - тестовые данные
- urls.py - URL ресурсы

### Покрытые кейсы:

1. **Восстановление пароля (test_forgot_password.py + test_reset_password.py):**  
   test_click_forgot_password_link_redirects_to_page - переход на страницу восстановления пароля по кнопке «Восстановить пароль;  
   test_click_show_password_button_highlights_password_field - проверка подсвечивания поля 'Пароль' при нажатии на кнопку 'показать/скрыть пароль'.  


2. **Личный кабинет (test_profile_page.py):**  
   test_click_profile_button_redirects_to_page - переход по клику на 'Личный кабинет';  
   test_click_order_history_button_redirects_to_page - переход в раздел 'История заказов';  
   test_click_logout_button_redirects_to_login - проверка выхода из аккаунта.  


3. **Проверка основного функционала (test_constructor_page.py):**  
   test_click_constructor_button_redirects_to_constructor_page - переход по клику на 'Конструктор';  
   test_click_ingredient_card_opens_ingredient_modal - при клике на ингредиент появляется всплывающее окно с деталями;  
   test_click_cross_closes_ingredient_modal - при клике на крестик закрывается всплывающее окно с деталями ингредиента;  
   test_add_ingredient_increases_counter - при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента;  
   test_authorized_user_creates_order_successfully - залогиненный пользователь может оформить заказ.  

   
4. **Раздел 'Лента заказов' (test_order_feed_page.py):**  
   test_click_order_feed_button_redirects_to_page - переход по клику на 'Лента заказов';  
   test_click_order_card_opens_modal - при клике на заказ появляется всплывающее окно с деталями;  
   test_order_history_item_appears_in_feed - заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов';    
   test_created_order_appears_in_work_list - после оформления заказа его номер появляется в разделе 'В работе';  
   test_create_order - при создании нового заказа счётчик 'Выполнено за всё время'/'Выполнено за сегодня' увеличивается.    


### Запуск тестов

1. Установите зависимости:</br>
   pip install -r requirements.txt
2. Запустите тесты:</br>
   pytest tests

### Генерация отчета Allure

1. Запустите тесты с генерацией данных для отчета:  
   pytest --alluredir=allure-results
2. Сгенерируйте отчет и откройте его в браузере:
   allure serve allure-results