from playwright.sync_api import Page
import pytest
import allure
from models.TestPage import TestPage


@allure.step
def fill_register(test_page: TestPage, **data):


    for key, value in data.items():
        if key == "name" and value is not None: test_page.name_field.fill(value)
        if key == "company" and value is not None: test_page.company_field.fill(value)
        if key == "division" and value is not None: test_page.division_select.select_option(value=value)
        if key == "email" and value is not None: test_page.email_field.fill(value)
        if key == "phone" and value is not None: test_page.phone_field.fill(value)
        if key == "confirm" and value:test_page.confirm_checkbox.click(force=True)
        if key == "subscribe" and value: test_page.sub_checkbox.click(force=True)

    try:
        test_page.submit_button.click()
        assert test_page.confirm_message.inner_text() == "Мы свяжемся с вами с 10 до 19 в будний день.",\
                                                         "Неправильно заполненные данные"
    except:
        assert False, "Неправильно заполненные данные"
        pass

    test_page.fin_message.screenshot(path="screenshots/screenshot.png")
    allure.attach.file('./screenshots/screenshot.png', "Test Screenshot", allure.attachment_type.PNG)



@pytest.mark.parametrize('Name', ["Макс", None], ids=['Правильное имя "Макс"', 'Незаполненное поле'])
@pytest.mark.parametrize('Company', ["ООО \"Макс\"", None], ids=['Правильное имя компании "ООО \"Макс\""',
                                                                 'Незаполненное поле'])
@pytest.mark.parametrize('Division', ["PR", None], ids=['Выбран пункт меню', 'Не выбран ни один пункт меню'])
@pytest.mark.parametrize('Email', ["Maks@Maks.ru", "maks@", None], ids=['Правильно введенный email', 'Введено "maks@"',
                                                                                'Ничего не введено'])
@pytest.mark.parametrize('Phone', ["79009009090", "123", None], ids=['Введен телефон правильного формата',
                                                                     'Введен набор цифр "123"', 'Ничего не введено'])
@pytest.mark.parametrize('Confirm', [True, False], ids=['Галочка поставленна в поле соглашения','Ничего не поставлено'])
@pytest.mark.parametrize('Subscribe', [True, False], ids=['Галочка поставленна в поле рассылки','Ничего не поставлено'])
def test_register(page: Page, Name, Company, Division, Email, Phone, Confirm, Subscribe):
    test_page = TestPage(page)
    test_page.navigate()
    fill_register(test_page, name=Name, company=Company, division=Division, email=Email, phone=Phone, confirm=Confirm,
                  subscribe=Subscribe)

