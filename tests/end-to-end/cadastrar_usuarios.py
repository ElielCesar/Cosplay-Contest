from playwright.sync_api import sync_playwright
from time import sleep

usuarios_teste = [
    ('Pedro', 'Felipe', 'pedro', 'pedro@gmail.com', 'teste123', 'teste123'),
    ('Danilo', 'Escudeiro', 'danilo', 'danilo@gmail.com', 'teste123', 'teste123'),
    ('Charles', 'Passos', 'charles', 'charles@gmail.com', 'teste123', 'teste123'),
    ('Cleide', 'Lacheski', 'cleide', 'cleide@gmail.com', 'teste123', 'teste123'),
    ('Eliel', 'Cesar', 'eliel', 'eliel@gmail.com', 'teste123', 'teste123'),
]

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    def cadastrar_usuarios():
        for usuario in usuarios_teste:
            pagina.goto("http://127.0.0.1:8000/auth/cadastro/")
            pagina.fill('xpath=//*[@id="nome"]', usuario[0])
            pagina.fill('xpath=//*[@id="sobrenome"]', usuario[1])
            pagina.fill('xpath=//*[@id="username"]', usuario[2])
            pagina.fill('xpath=//*[@id="email"]', usuario[3])
            pagina.fill('xpath=//*[@id="senha"]', usuario[4])
            pagina.fill('xpath=//*[@id="confirmar_senha"]', usuario[5])
            pagina.click('xpath=/html/body/main/div/div[3]/form/input[6]')
            sleep(5)
            
    def testar_login_usuarios():
        for usuario in usuarios_teste:
            pagina.goto("http://127.0.0.1:8000/auth/login/")
            pagina.fill('xpath=//*[@id="username"]', usuario[2])
            pagina.fill('xpath=//*[@id="password"]', usuario[4])
            pagina.click('xpath=/html/body/main/div/div[3]/form/input[4]')
            sleep(3)
            pagina.click('xpath=/html/body/div/div[1]/div/div[4]/ul/li[9]/a')


    # executar
    testar_login_usuarios()
