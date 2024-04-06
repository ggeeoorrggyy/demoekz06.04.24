import flet as ft
from src.database.models import *  
from src.client.auth_component import AuthComponent

def main(page: ft.Page):
    doctor_id = [0]

    def on_login_click(event: ft.ControlEvent):
        user = UserLogin.get_or_none(
            UserLogin.login == auth_component.login_field.value,
            UserLogin.password == auth_component.password_field.value
        )
        if user:
            doctor_id[0] = user.id 
            auth_component.visible = False
            patient_data_component.visible = True
            page.update()
        else:
            print('Неверные данные')
            

    def show_client_data(event: ft.ControlEvent):
        data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
        alert_dialog = ft.AlertDialog(content=ft.Text(str(data.__dict__['model_data'])))
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    def show_records(event: ft.ControlEvent):
        if doctor_id[0] == 0:
            return
        data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
        doctor = Staff.get_by_id(doctor_id[0])
        record = Services.select().where(Services.doctor == doctor, Services.patient_id == data)
        d = []
        for r in record:
            d.append(r.__dict__['model_data'])  # Исправлено обращение к атрибутам записи
        alert_dialog = ft.AlertDialog(content=ft.Text(str(d)))
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    auth_component = AuthComponent()
    auth_component.login_button.on_click = on_login_click

    patient_data_component = ft.Column(
        controls=[
            ft.TextField(label='Имя пациента'),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.FilledButton(text='Показать информацию', on_click=show_client_data)
                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.FilledButton(text='Просмотр записей пациентов', on_click=show_records)
                ]
            ),
        ],
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(
        ft.Column(
            controls=[auth_component, patient_data_component]
        )
    )

ft.app(target=main)
