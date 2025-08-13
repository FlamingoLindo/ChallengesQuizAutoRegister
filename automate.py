"""
Module for selenium driver automation
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def automate_quiz_registration(master_url, master_login, master_password, df):
    """
    Function to automate quiz registration.

    Args:
        master_url (str): URL of the master login page
        master_login (str): Login email for the master account
        master_password (str): Password for the master account
        df (DataFrame): DataFrame containing quiz data
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    driver.get(master_url)

    email = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    email.send_keys(master_login)

    password = wait.until(
        EC.presence_of_element_located((By.NAME, 'password')))
    password.send_keys(master_password)
    password.submit()

    time.sleep(3)

    driver.get(
        'https://challenges-quiz-master.netlify.app/perguntas/cadastrar/Challenges')

    for index, row in df.iterrows():
        # Print das perguntas para debug
        print(f"Pergunta: {row['PERGUNTA']}\n")

        # Abre o select de categoria
        categ = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/form/div[2]/fieldset[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]')))
        categ.click()

        # Seleciona a categoria de vendas
        vendas = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="react-select-category-option-0"]')))
        vendas.click()

        # Abre o select de módulo
        module_select = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/form/div[2]/fieldset[1]/div/div[2]/div/div[2]/div/div[1]/div[2]')))
        module_select.click()

        # Seleciona o módulo (TEM QUE SEMPRE ALTERAR ALI O ID)
        module = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="react-select-module-option-9"]')))
        driver.execute_script("arguments[0].click();", module)

        # Abre o select de dificuldade
        dif_select = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/form/div[2]/fieldset[1]/div/div[3]/div/div[2]/div/div[1]/div[2]')))
        dif_select.click()

        # Seleciona a dificuldade
        if row['NÍVEL DE DIFICULDADE'] == 'Fácil':
            dif = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-select-difficult-option-0"]')))
            dif.click()
        elif row['NÍVEL DE DIFICULDADE'] == 'Médio':
            dif = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-select-difficult-option-1"]')))
            dif.click()
        else:
            dif = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="react-select-difficult-option-2"]')))
            dif.click()

        # Preenche a data de início
        start_date = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'start_date')))
        start_date.send_keys('13082025')

        # Preenche a hora de início
        start_time = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'start_hour')))
        start_time.send_keys('1500')

        # Preenche a data final
        final_date = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/form/div[2]/fieldset[2]/div/div[3]/div[2]/label[2]')))
        final_date.click()

        # Preenche a hora final
        final_time = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'max_time')))
        final_time.send_keys('300')

        # Preenche a pergunta
        question = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'question')))
        question.send_keys(row['PERGUNTA'])

        # Preenche as alternativa
        # (A ordem das alternativas é A, B, C, D)
        alternative_a = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'alternative1')))
        alternative_a.send_keys(row['ALTERNATIVA 1'])

        alternative_b = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'alternative2')))
        alternative_b.send_keys(row['ALTERNATIVA 2'])

        alternative_c = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'alternative3')))
        alternative_c.send_keys(row['ALTERNATIVA 3'])

        alternative_d = wait.until(EC.presence_of_element_located(
            (By.NAME,
             'alternative4')))
        alternative_d.send_keys(row['ALTERNATIVA 4'])

        # Seleciona a alternativa correta
        if row['ALTERNATIVA CORRETA'] == 'a':
            correct_alternative = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/main/div/form/div[2]/fieldset[4]/div/div[1]/button')))
            correct_alternative.click()
        elif row['ALTERNATIVA CORRETA'] == 'b':
            correct_alternative = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/main/div/form/div[2]/fieldset[4]/div/div[2]/button')))
            correct_alternative.click()
        elif row['ALTERNATIVA CORRETA'] == 'c':
            correct_alternative = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/main/div/form/div[2]/fieldset[4]/div/div[3]/button')))
            correct_alternative.click()
        else:
            correct_alternative = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/main/div/form/div[2]/fieldset[4]/div/div[4]/button')))
            correct_alternative.click()

        # Salva a pergunta
        save_btn = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/form/div[1]/div[2]/button')))
        save_btn.click()

        # Clica no modal de sucesso
        success = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '.hEgsAm')))
        success.click()

        # Abre a aba do challenges
        challenges_btn = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '.bjMlEC')))
        challenges_btn.click()

        # Clica no botão de registrar
        register = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '.cXYdXT')))
        register.click()
    driver.quit()
