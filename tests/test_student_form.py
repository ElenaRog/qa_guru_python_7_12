import allure
from classes.registration_page import RegistrationPage
from classes.user_registration import Student, Gender, Hobbies, Birthday


def test_student_registration():
    student = Student(
        first_name='Elena',
        last_name='Rogozina',
        email='elenarog@mail.ru',
        gender=Gender.female,
        number='5554678578',
        date_of_birth=Birthday('27 June,1997'),
        subject='Biology',
        hobbies=Hobbies.sports,
        picture='image.png',
        address='Baker st. 221B',
        state='Uttar Pradesh',
        city='Agra')

    registration_page = RegistrationPage()

    with allure.step('Open registration form'):
        registration_page.open()
    with allure.step('Fill form'):
        registration_page.register(student)
    with allure.step('Check results'):
        registration_page.should_have_registered(student)
