from back_end.bibliotecas import *

usuario4 = []


class analizar_in:
    def analisar():
        
        
        print(usuario4[0])
        options = webdriver.ChromeOptions() 
        options.add_argument(f"user-data-dir=C:\\Users\\{usuario4[0]}\\AppData\\Local\\Google\\Chrome\\User Data")
        time.sleep(2)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://dexco.virtual360.io/nf/tax_documents/") 
        
        while len(driver.find_elements(By.XPATH,'//a[contains(text(),  "Login Dexco")]')) < 1 :
            pass
        driver.find_element(By.XPATH,'//a[contains(text(),  "Login Dexco")]').click()
        time.sleep(6)

        
        # Abrir tabela exel
        tabela = pd.read_excel("Bases/base_analisar_inbound/base_analisar_inbound.xlsx")

        for linha in tabela.index:
            
            try:  
            
                codigoid = tabela.loc[linha, "ID"]
                link = f"https://dexco.virtual360.io/nf/tax_documents/{codigoid}"
                driver.get(link)
                
                while len(driver.find_elements(By.XPATH,'//*[@id="process-instance-progressbar"]/ul/li[2]/div')) < 1 :
                    pass
                processo = driver.find_element(By.XPATH,'//*[@id="process-instance-progressbar"]/ul/li[2]/div').text
                
                print(processo)
                
                tabela.loc[tabela["ID"] == codigoid, "PROCESSO"] = processo
            
                tabela.to_excel("Bases/base_analisar_inbound/base_analisar_inbound2.xlsx", index = False)
            
            
            except:
                print("//////////////////////ERRO//////////////////////")
                break
        
        
        
    