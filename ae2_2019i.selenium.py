# -*- coding: utf-8 -*-
import time
from selenium import webdriver


def ir_mef_web(cod_ejec, expedient):
    browser = webdriver.Chrome()
    # Definimos nuestra página objetivo
    site = "http://apps2.mef.gob.pe/consulta-vfp-webapp/consultaExpediente.jspx"
    browser.get(site)
    browser.maximize_window()
    browser.find_element_by_xpath(
        "//select[@name='anoEje']/option[text()='2016']").click()
    # Obtenemos la caja de texto donde se ingresa el codigo unidad ejecutora
    documento = browser.find_element_by_name("secEjec")
    # Escribimos el codigo
    documento.send_keys(cod_ejec)
    # Obtenemos la caja de texto donde se ingresa el numero de expediente
    expediente = browser.find_element_by_name("expediente")
    # Escribimos el expediente
    expediente.send_keys(expedient)
    # Obtenemos el texto del captcha
    captcha_web = "hola"
    # pytesseract.image_to_string(img_recortada)
    # Obtenemos la caja de texto donde se escribe el texto del captcha
    codigo = browser.find_element_by_name("j_captcha")
    # Escribimos el texto
    codigo.send_keys(captcha_web)
    # Capturamos el botón de búsqueda
    boton = browser.find_element_by_class_name("button")
    # Click en el botón de búsqueda
    boton.click()
    # driver.quit()


def main():
    # Ingresar expediente
    expediente = 1
    cod_ejec = 301848
    ir_mef_web(cod_ejec, expediente)


main()
