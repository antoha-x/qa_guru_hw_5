import os

from selene import browser, have


def test_fill_form_and_check_result_table():
    browser.open('')
    browser.element('#firstName').send_keys("Vasiliy")
    browser.element('#lastName').send_keys("Pupkin")
    browser.element('#userEmail').send_keys("test@test.ts")
    browser.element('#gender-radio-1 + label').click()
    browser.element('#userNumber').send_keys("9876543210")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element("[value='0']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1990']").click()
    browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').send_keys("Maths")
    browser.element('#react-select-2-option-0').click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element('#uploadPicture').send_keys(f"{os.getcwd()}/resources/m527697.jpg")
    browser.element('#currentAddress').send_keys("Royal Road, Mont Choisy Mauritius, Mont Choisy, Mauritius Island")
    browser.element("#submit").hover()
    browser.element("#state").click()
    browser.element("#react-select-3-option-0").click()
    browser.element("#city").click()
    browser.element("#react-select-4-option-2").click()
    browser.element("#submit").click()

    browser.all(".modal-body tbody > tr > td:last-child").element(0).should(have.text("Vasiliy Pupkin"))
    browser.all(".modal-body tbody > tr > td:last-child").element(1).should(have.text("test@test.ts"))
    browser.all(".modal-body tbody > tr > td:last-child").element(2).should(have.text("Male"))
    browser.all(".modal-body tbody > tr > td:last-child").element(3).should(have.text("9876543210"))
    browser.all(".modal-body tbody > tr > td:last-child").element(4).should(have.text("01 January,1990"))
    browser.all(".modal-body tbody > tr > td:last-child").element(5).should(have.text("Maths"))
    browser.all(".modal-body tbody > tr > td:last-child").element(6).should(have.text("Reading"))
    browser.all(".modal-body tbody > tr > td:last-child").element(7).should(have.text("m527697.jpg"))
    browser.all(".modal-body tbody > tr > td:last-child").element(8).should(have.text("Royal Road, Mont Choisy "
                                                                                      "Mauritius, Mont Choisy, "
                                                                                      "Mauritius Island"))
    browser.all(".modal-body tbody > tr > td:last-child").element(9).should(have.text("NCR Noida"))
