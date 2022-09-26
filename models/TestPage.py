
class TestPage():
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(3500)



    def navigate(self):
        self.page.goto("https://scan-interfax.ru/")
        self.page.locator('button.button.button--fill-blue.button--lightning').click()

    @property
    def user_form(self):
        return self.page.wait_for_selector('div.lp-content')

    @property
    def name_field(self):
        return self.user_form.wait_for_selector('input[name=\'name\']')

    @property
    def company_field(self):
        return self.user_form.wait_for_selector('input[name=\'company\']')

    @property
    def division_select(self):
        return self.user_form.wait_for_selector('select.lp-input')

    @property
    def email_field(self):
        return self.user_form.wait_for_selector('input[name=\'email\']')

    @property
    def phone_field(self):
        return self.user_form.wait_for_selector('input[name=\'phone\']')

    @property
    def submit_button(self):
        return self.user_form.wait_for_selector('button.lp-submit.lp-submit-forward')

    @property
    def confirm_checkbox(self):
        return self.user_form.wait_for_selector('input[name=\'confirm\']')

    @property
    def sub_checkbox(self):
        return self.user_form.wait_for_selector('input[name=\'subscribe\']')

    @property
    def confirm_message(self):
        return self.page.wait_for_selector("div.lp-html.lp-description")

    @property
    def fin_message(self):
        return self.page.wait_for_selector("div.lp-content-wrapper")
