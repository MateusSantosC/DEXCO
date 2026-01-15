from back_end.bibliotecas import *

usuario3 = []


class mover_processo:
    def mover():
        
        try:   
            options = webdriver.ChromeOptions() 
            options.add_argument(f"user-data-dir=C:\\Users\\{usuario3[0]}\\AppData\\Local\\Google\\Chrome\\User Data")
            time.sleep(2)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            driver.get("https://dexco.virtual360.io/nf/tax_documents/") 
            
            while len(driver.find_elements(By.XPATH,'//a[contains(text(),  "Login Dexco")]')) < 1 :
                pass
            driver.find_element(By.XPATH,'//a[contains(text(),  "Login Dexco")]').click()
            time.sleep(6)

            
            # Abrir tabela exel
            tabela = pd.read_excel("Bases/Base_mover_processo/mover_processo.xlsx")

            for linha in tabela.index:
                
                try:  
                    
                    # Pesquisar ID
                    codigoid = tabela.loc[linha, "ID"]
                    processo = tabela.loc[linha, "PROCESSO"]
                    
                    link = f"https://dexco.virtual360.io/nf/tax_documents/{codigoid}"
                    print(codigoid)
                    driver.get(link)
                                
                                
                    while len(driver.find_elements(By.XPATH,'//div[contains(text(),  "Mover Processo")]')) < 1 :
                        pass
                    driver.find_element(By.XPATH,'//div[contains(text(),  "Mover Processo")]').click()
                    time.sleep(4)

                    try:
                        driver.find_element(By.CLASS_NAME,'select2-selection__arrow').click()
                    except:
                        pass


                    time.sleep(1)
                    while len(driver.find_elements(By.XPATH,'/html/body/span/span/span[1]/input')) < 1 :
                        pass
                    driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input').send_keys(processo)
                    time.sleep(1)


                    while len(driver.find_elements(By.XPATH,'/html/body/span/span/span[2]/ul/li[1]')) < 1 :
                        pass
                    driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[1]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div/div[2]/form/div[2]/input').click()
                    time.sleep(1)

                        
                    tabela.loc[tabela["ID"] == codigoid, "STATUS"] = "Feito"
                    
                    tabela.to_excel("Bases\Base_mover_processo\mover_processo2.xlsx", index = False)    
                
                except:
                    print("//////////////////////ERRO//////////////////////")
                    break
            os.startfile("Bases\Base_mover_processo\mover_processo2.xlsx")
        except:
            pass    
        
        
    