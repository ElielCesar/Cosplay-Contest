from playwright.sync_api import sync_playwright
from time import sleep

usuarios_fantasy = [
    # ('Pedro', 'Felipe', 'pedro', 'pedro@gmail.com', 'teste123','teste123', 'Goku', r'C:\Users\eliel\Downloads\cosplay\goku.png'),
    # ('Danilo', 'Escudeiro', 'danilo', 'danilo@gmail.com', 'teste123','teste123', 'Escanor', r'C:\Users\eliel\Downloads\cosplay\escanor.jpg'),
    # ('Charles', 'Passos', 'charles', 'charles@gmail.com', 'teste123','teste123', 'Natsu', r'C:\Users\eliel\Downloads\cosplay\satoru.jpg'),
    ('Teste1', 'teste1', 'teste1', 'teste1@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste2', 'teste2', 'teste2', 'teste2@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste3', 'teste3', 'teste3', 'teste3@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste4', 'teste4', 'teste4', 'teste4@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste5', 'teste5', 'teste5', 'teste5@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste6', 'teste6', 'teste6', 'teste6@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste7', 'teste7', 'teste7', 'teste7@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),

]

usuarios_makeyourself = [
    # ('Cleide', 'Lacheski', 'cleide', 'cleide@gmail.com',
    #  'teste123', 'teste123', 'Gon freaks'),
    # ('Eliel', 'Cesar', 'eliel', 'eliel@gmail.com',
    #  'teste123', 'teste123', 'Yujiro Hamna'),
    ('Teste1', 'teste1', 'teste1', 'teste1@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste2', 'teste2', 'teste2', 'teste2@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste3', 'teste3', 'teste3', 'teste3@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste4', 'teste4', 'teste4', 'teste4@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste5', 'teste5', 'teste5', 'teste5@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste6', 'teste6', 'teste6', 'teste6@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
    ('Teste7', 'teste7', 'teste7', 'teste7@gmail.com', 'teste123', 'teste123', 'python', r'C:\Users\eliel\Downloads\cosplay\python.png'),
]


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()

    def inscrever_fantasy():
        for usuario in usuarios_fantasy:
            # login
            pagina.goto("http://127.0.0.1:8000/auth/login/")
            pagina.fill('xpath=//*[@id="username"]', usuario[2])
            pagina.fill('xpath=//*[@id="password"]', usuario[4])
            pagina.click('xpath=/html/body/main/div/div[3]/form/input[4]')
            sleep(2)

            # inscrever-se
            pagina.goto('http://127.0.0.1:8000/home/inscrever_fantasy/')

            # preencher formulário
            pagina.fill('xpath=//*[@id="id_nome_completo"]', usuario[0])
            pagina.fill('xpath=//*[@id="id_email"]', usuario[3])
            pagina.fill('xpath=//*[@id="id_telefone"]', '69 99268-5784')
            pagina.fill('xpath=//*[@id="id_personagem"]', usuario[6])
            pagina.set_input_files(
                'xpath=//*[@id="id_imagem_principal"]', usuario[7])
            sleep(2)
            pagina.click('xpath=/html/body/div/div[2]/div/form/button')
            sleep(2)

            # sair
            pagina.goto("http://127.0.0.1:8000/auth/logout/")
            
    def inscrever_makeyourself():
        for usuario in usuarios_makeyourself:
            # login
            pagina.goto("http://127.0.0.1:8000/auth/login/")
            pagina.fill('xpath=//*[@id="username"]', usuario[2])
            pagina.fill('xpath=//*[@id="password"]', usuario[4])
            pagina.click('xpath=/html/body/main/div/div[3]/form/input[4]')
            sleep(2)

            # inscrever-se
            pagina.goto('http://127.0.0.1:8000/home/inscrever_makeyourself/')

            # preencher formulário
            pagina.fill('xpath=//*[@id="id_nome_completo"]', usuario[0])
            pagina.fill('xpath=//*[@id="id_email"]', usuario[3])
            pagina.fill('xpath=//*[@id="id_telefone"]', '69 99268-5784')
            pagina.fill('xpath=//*[@id="id_personagem"]', usuario[6])
            pagina.set_input_files(
                'xpath=//*[@id="id_imagem_principal"]', usuario[7])
            sleep(2)
            pagina.click('xpath=/html/body/div/div[2]/div/form/button')
            sleep(2)

            # sair
            pagina.goto("http://127.0.0.1:8000/auth/logout/")

    # executando
    inscrever_fantasy()
    inscrever_makeyourself()
