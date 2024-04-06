import flet as ft

class AuthComponent(ft.UserControl):
    def __init__(self):
        self.login_button = ft.FilledButton(text='Войти')
        self.login_field = ft.TextField(label='Логин')
        self.password_field = ft.TextField(label='Пароль', password=True, can_reveal_password=True)
    
    def build(self):
        def on_create_account_click(e):
            print("Функция создания аккаунта пока не реализована")

        create_account_button = ft.TextButton(
            text='Создать аккаунт',
            on_click=on_create_account_click
        )

        login_page = ft.Column(
            controls=[
                self.login_field,
                self.password_field,
                ft.Row(
                    controls=[
                        self.login_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        create_account_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
        return login_page
