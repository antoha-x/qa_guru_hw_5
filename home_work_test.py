import os

from selene import browser, have


def test_fill_form_and_check_result_table():
    browser.open('/automation-practice-form')

    # Заполняем имя
    browser.element('#firstName').send_keys('Vasiliy')

    # Заполняем фамилию
    browser.element('#lastName').send_keys('Pupkin')

    # Заполняем почту
    browser.element('#userEmail').send_keys('test@test.ts')

    # Выбираем пол
    browser.element('#gender-radio-1 + label').click()

    # Заполняем телефон
    browser.element('#userNumber').send_keys('9876543210')

    # Заполняем дату рождения
    browser.element('#dateOfBirthInput').click()

    # Выбираем январь
    browser.element('.react-datepicker__month-select').click().element("[value='0']").click()

    # Выбираем 1990 год
    browser.element('.react-datepicker__year-select').click().element("[value='1990']").click()

    # Выбираем 1 число
    browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()

    # Заполняем предмет
    browser.element('#subjectsInput').send_keys('Maths')
    browser.element('#react-select-2-option-0').click()

    # Выбираем чтение
    browser.element("[for='hobbies-checkbox-2']").click()

    # Загружаем фото
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/m527697.jpg'))

    # Заполняем адрес
    browser.element('#currentAddress').send_keys('Royal Road, Mont Choisy Mauritius, Mont Choisy, Mauritius Island')

    # Прокручиваем страницу ниже
    browser.element('#submit').hover()

    # Выбираем штат
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    # Выбираем город
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()

    # Отправляем форму
    browser.element('#submit').click()

    # Проверяем корректность сохраненных данных на форме
    browser.all('.modal-body tbody > tr > td').even.should(have.exact_texts((
        'Vasiliy Pupkin',
        'test@test.ts',
        'Male',
        '9876543210',
        '01 January,1990',
        'Maths',
        'Reading',
        'm527697.jpg',
        'Royal Road, Mont Choisy Mauritius, Mont Choisy, Mauritius Island',
        'NCR Noida'
    )))
