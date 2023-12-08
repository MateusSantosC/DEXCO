from back_end.bibliotecas import *

usuario2 = []


class extrair_descri:
    def extrair():
        
        try:
            options = webdriver.ChromeOptions() 
            options.add_argument(f"user-data-dir=C:\\Users\\{usuario2[0]}\\AppData\\Local\\Google\\Chrome\\User Data")
            time.sleep(2)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            driver.get("https://dexco.virtual360.io/nf/tax_documents/") 
            
            while len(driver.find_elements(By.XPATH,'//a[contains(text(),  "Login Dexco")]')) < 1 :
                pass
            driver.find_element(By.XPATH,'//a[contains(text(),  "Login Dexco")]').click()
            time.sleep(6)

            
            # Abrir tabela exel
            tabela = pd.read_excel("Bases/base_extrair_descri/base_extrair_descrição.xlsx")

            for linha in tabela.index:
                
                try:  
                
                    # Pesquisar ID
                    codigoid = tabela.loc[linha, "id"]
                    link = f"https://dexco.virtual360.io/nf/tax_documents/{codigoid}"
                    driver.get(link)
        
        
                    # Extrair valor
                    while len(driver.find_elements(By.XPATH,'//*[@id="tax_document_invoice_items_attributes_0_validation_errors_messages"]')) < 1 :
                        pass
                    valor = driver.find_element(By.XPATH,'//*[@id="tax_document_invoice_items_attributes_0_validation_errors_messages"]').text
                    print(codigoid, valor)
        
        
                    # Preencher tabela
                    tabela.loc[tabela["id"] == codigoid, "valor"] = valor
        
                    tabela.to_excel("Bases/base_extrair_descri/base_extrair_descrição2.xlsx", index = False)
    
                
                except:
                    print("//////////////////////ERRO//////////////////////")
                    break
            os.startfile("Bases/base_extrair_descri/base_extrair_descrição2.xlsx")
        except:
            print("//////////////////////ERRO2//////////////////////")
            pass        
      