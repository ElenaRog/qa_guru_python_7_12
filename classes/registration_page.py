import os
from pathlib import Path

from selene.support.shared import browser
from selene import have, be, command
from classes.user_registration import Student


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.element('#app > footer').perform(command.js.remove)
        browser.element('#fixedban').click()
        browser.element('#fixedban').perform(command.js.remove)

    @staticmethod
    def register(student: Student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.all('[name=gender]').element_by(have.value(student.gender.value)).element('..').click()
        browser.element('#userNumber').type(student.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(student.date_of_birth.month)
        browser.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        browser.element(
            f'.react-datepicker__day--0{student.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(student.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(student.hobbies.value)).click()
        browser.element('#uploadPicture').locate().send_keys(
            str(Path(__file__).absolute().parent.parent.joinpath('tests', 'resources', student.picture))
        )
        browser.element('#currentAddress').type(student.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.city)
        ).click()
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').should(be.visible).click()

    @staticmethod
    def should_have_registered(student: Student):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender.female.value,
                student.number,
                student.date_of_birth.bday,
                student.subject,
                student.hobbies.sports.value,
                student.picture,
                student.address,
                f'{student.state} {student.city}'
            )
        )
