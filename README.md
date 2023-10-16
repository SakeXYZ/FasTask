# FasTask

Certainly, here is a README for the provided Python code that creates Trello cards and an input prompt:

# Trello Card Creator / Создатель карточек в Trello

## English / Английский

This Python script allows you to create Trello cards with specific details by providing the department and a description of the issue. It serves as a handy tool for automating the card creation process in Trello.

### How to Use

1. **Bot Setup:**
   - Before using the script, ensure you have the necessary libraries and dependencies installed. You can install required dependencies by using the command `pip install requests`.

2. **Configuration:**
   - In the `config.py` file, provide the values for `ID`, `API_KEY`, `TOKEN`, and `URL`. These values are essential for interacting with the Trello API.

3. **Creating Trello Cards:**
   - Run the script, and it will prompt you to enter the department and a description of the issue.
   - Enter the department and description as requested. The script will then create a Trello card with the specified details.

4. **Card Details:**
   - The script will construct the card name by adding "Отдел" before the department name.
   - The provided description will be added to the card as a description.

5. **Output:**
   - The script will print the response received from the Trello API, which will include details of the created card.

6. **Repeat Usage:**
   - The script will keep prompting you to create additional cards. You can exit the script when you're done.

This script simplifies the process of creating Trello cards for various departments and issues. It can be used for various task management purposes.

## Русский / Russian

Этот скрипт на Python позволяет создавать карточки Trello с указанными подробностями, предоставляя информацию о департаменте и описании проблемы. Он служит удобным инструментом для автоматизации процесса создания карточек в Trello.

### Инструкция по использованию

1. **Настройка скрипта:**
   - Перед использованием скрипта убедитесь, что у вас установлены необходимые библиотеки и зависимости. Вы можете установить требуемые зависимости с помощью команды `pip install requests`.

2. **Настройка:**
   - В файле `config.py` укажите значения для `ID`, `API_KEY`, `TOKEN` и `URL`. Эти значения необходимы для взаимодействия с API Trello.

3. **Создание карточек Trello:**
   - Запустите скрипт, и он попросит вас ввести департамент и описание проблемы.
   - Введите департамент и описание, как указано. Затем скрипт создаст карточку Trello с указанными данными.

4. **Детали карточки:**
   - Скрипт создаст имя карточки, добавив перед названием "Отдел".
   - Предоставленное описание будет добавлено в карточку как описание.

5. **Вывод:**
   - Скрипт распечатает ответ, полученный от API Trello, включая детали созданной карточки.

6. **Повторное использование:**
   - Скрипт будет предлагать создавать дополнительные карточки. Вы можете завершить выполнение скрипта, когда закончите.

Этот скрипт упрощает процесс создания карточек Trello для различных департаментов и задач. Его можно использовать для управления задачами в различных целях.
