from playwright.sync_api import sync_playwright
from time import sleep

usuarios_makeyourself = [
    ('Cleide', 'Lacheski', 'cleide', 'cleide@gmail.com',
     'teste123', 'teste123', 'Gon freaks', r'C:\Users\eliel\Downloads\cosplay\gon.png'),
    ('Eliel', 'Cesar', 'eliel', 'eliel@gmail.com',
     'teste123', 'teste123', 'Yujiro Hamna', r'C:\Users\eliel\Downloads\cosplay\yujiro.jpg'),
]


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()

    def inscrever_makeyourself():
        for usuario in usuarios_makeyourself:
            # login
            pagina.goto("http://127.0.0.1:8000/auth/login/")
            pagina.fill('xpath=//*[@id="username"]', usuario[2])
            pagina.fill('xpath=//*[@id="password"]', usuario[4])
            pagina.click('xpath=/html/body/main/div/div[3]/form/input[4]')
            sleep(3)

            # inscrever-se
            pagina.click('xpath=/html/body/div/div[1]/div/div[4]/ul/li[1]/a')
            pagina.click(
                'xpath=/html/body/div/div[2]/div/div/div[1]/div/div[2]/a')

            # preencher formulário
            pagina.fill('xpath=//*[@id="id_nome_completo"]', usuario[0])
            pagina.fill('xpath=//*[@id="id_email"]', usuario[3])
            pagina.fill('xpath=//*[@id="id_telefone"]', '69 99268-5784')
            pagina.fill('xpath=//*[@id="id_personagem"]', usuario[6])
            pagina.set_input_files(
                'xpath=//*[@id="id_imagem_principal"]', usuario[7])
            sleep(3)
            pagina.click('xpath=/html/body/div/div[2]/div/form/button')
            sleep(3)

            # sair
            pagina.click('xpath=/html/body/div/div[1]/div/div[4]/ul/li[9]/a')

    # executando
    inscrever_makeyourself()
