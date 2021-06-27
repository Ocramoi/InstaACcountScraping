#!/usr/bin/env python3

# Bibliotecas utilizadas
from selenium import webdriver
import time
import platform
import pandas as pd
import re
import sys
import os

# Variáveis utilizadas
import env

# Link base de conta do instagram
linkBase = "https://www.instagram.com/{}/"

# Seleciona executável de driver correto por plataforma
if platform.system() == "Linux":
    seleniumDriver = 'geckodriver'
else:
    seleniumDriver = 'geckodriver.exe'

# Inicia webdriver
browser = webdriver.Firefox(executable_path=os.path.join(sys.path[0],
                                                         seleniumDriver))

# Compila regex de informações a serem lidas
regexSeguidores = re.compile('"edge_followed_by":{"count":([^,^}]+)')
regexPosts = re.compile('"edge_owner_to_timeline_media":{"count":([^,^}]+)')
regexSeguindo = re.compile('"edge_follow":{"count":([^,^}]+)')


def garanteLogin() -> None:
    """
    Abre página de login e aguarda confirmação
    """
    browser.get(linkBase.format("accounts/login"))
    input("Por favor, logue no instagram e aperte [ENTER] quando concluído...")


def main():
    garanteLogin()

    # Lê lista de usuários para conferência
    listaUsrs = []
    with open(env.NOME_ARQ_ENTRADA, "r") as arqLista:
        listaUsrs = [str(usr).strip() for usr in arqLista.readlines()]

    # Cria dataframe para inclusão das informações lidas
    df = pd.DataFrame({
        "Perfil": [],
        "Posts": [],
        "Seguidores": [],
        "Seguindo": []
    })

    # Para cada usuário da lista
    for usr in listaUsrs:
        # Gera link do perfil
        linkUsr = linkBase.format(usr)
        try:
            # Abre link do perfil
            browser.get(linkUsr)

            # Espera que página termina de carregar
            carregada = browser.execute_script("return document.readyState")
            while carregada != "complete":
                carregada = browser.execute_script(
                    "return document.readyState"
                )

            # Lê código fonte da página
            pagina = browser.page_source

            # Lê informações da página
            infos = {
                "Perfil": usr,
                "Posts": regexPosts.search(pagina).groups(0)[0],
                "Seguidores": regexSeguidores.search(pagina).groups(0)[0],
                "Seguindo": regexSeguindo.search(pagina).groups(0)[0]
            }

            # Adiciona informação à tabela
            df = df.append(infos,
                           ignore_index=True)
        except Exception:
            # Exibe usuários com erro de leitura
            print("Erro no usuário @{}!".format(usr))

        # Pausa para evitar bloqueio por spam
        time.sleep(env.PAUSA_REQUISICAO)

    # Salva tabela em excel
    df.to_excel(env.NOME_ARQ_SAIDA,
                sheet_name="Perfis")


if __name__ == "__main__":
    main()
