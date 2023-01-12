import os
from selene.support.shared import browser
from selene import have

def test_input_and_authorization(size_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').click().type('Test')
    browser.element('#lastName').click().type('Testovych')
    browser.element('#userEmail').click().type('test123@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').click().type('9001112233')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1996"]').click()
    browser.element('.react-datepicker__month-select>[value="7"]').click()
    browser.element('.react-datepicker__week>.react-datepicker__day--020').click()
    browser.element('#subjectsInput').click().type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '\media\pic.jpeg')))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'Test Testovych',
        'test123@mail.ru',
        'Male',
        '9001112233',
        '20 August,1996',
        'English',
        'Reading',
        'pic.jpeg',
        'Moscow',
        'Rajasthan Jaipur'
    ))

