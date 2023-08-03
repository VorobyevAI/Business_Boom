
<h1>Начало</h1>
<p>Следуя этим инструкциям, вы получите копию проекта, которая будет запущена на вашем локальном компьютере для разработки и тестирования.</p>

<h2>Версии</h2>
<code>python== 3.11 и django==4.2.3</code>

<h2>Установка</h2>
<pre>Откройте терминал и введите:</pre>
<code>git clone https://github.com/VorobyevAI/Business_Boom</code><br><br>

<pre>Или просто скачайте, используя приведенный ниже URL:</pre>
<code>https://github.com/VorobyevAI/Business_Boom</code><br>
<pre>Создайте виртуальное окружение</pre>
<code>Для windows: python -m venv venv</code><br>
<code>Для linux: python3 -m venv venv</code><br>

<pre>Активируйте виртуальное окружение:</pre>
<code>Для windows: venv\Scripts\activate.bat</code><br>
<code>Для linux: source venv/bin/activate</code><br>

<pre>Установите зависимости:</pre>
<code>pip install -r requirements.txt</code><br>

<h2>Чтобы перенести базу данных, откройте терминал в каталоге проекта и введите:</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>Чтобы использовать панель администратора, вам необходимо создать суперпользователя с помощью этой команды: </h2>
<code>python manage.py createsuperuser</code>


<h2> Чтобы запустить программу на локальном сервере, используйте следующую команду: </h2>
<code>python manage.py runserver</code>

<h2>Затем перейдите по URL: http://127.0.0.1:8000 в вашем браузере<h2>
