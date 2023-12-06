from back_end.bibliotecas import *

usuario1 = []


class pegar_id:
    def pegar():
        
        
        print(usuario[0])
        options = webdriver.ChromeOptions() 
        options.add_argument(f"user-data-dir=C:\\Users\\{usuario[0]}\\AppData\\Local\\Google\\Chrome\\User Data")
        time.sleep(2)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://dexco.virtual360.io/nf/tax_documents/") 
        
        while len(driver.find_elements(By.XPATH,'//a[contains(text(),  "Login Dexco")]')) < 1 :
            pass
        driver.find_element(By.XPATH,'//a[contains(text(),  "Login Dexco")]').click()
        time.sleep(6)

        
        # Abrir tabela exel
        tabela = pd.read_excel("Bases/base_pegar_id/base_pegar_id.xlsx")

        for linha in tabela.index:
            
            try:  
            
                numero = tabela.loc[linha, "numero"]
            
                link = f"https://dexco.virtual360.io/nf/tax_documents?filters%5Bcompleted%5D=&filters%5Baccess_key%5D%5B%5D={numero}&filters%5Bautomatic_debit%5D=&filters%5Bhas_document_pdf%5D=&filters%5Bhas_document_xml%5D=&filters%5Bhas_bank_slips%5D=&filters%5Bprovider%5D=&filters%5Breceipt_status%5D=&filters%5Breceipt_confirmed%5D=&filters%5Bsimples_nacional_from_robot%5D=&filters%5Bsupplier_opting_for_simples_nacional%5D=&filters%5Bsupplier_cepom_registration%5D=&commit=Aplicar+filtros"
                driver.get(link)
            
                while len(driver.find_elements(By.XPATH,'//*[@id="table_list"]/div[1]/h2')) < 1 :
                    pass
            
                pyautogui.click(698,424, duration=0.2)
            
                while len(driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/div/div/div[1]/div[1]/h2/u')) < 1 :
                    pass
            
                id_nota = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/div/div/div[1]/div[1]/h2/u').text
                
                num = re.compile(r'\d')
                num2 =num.findall(id_nota)
                
                tabela.loc[tabela["numero"] == numero, "id"] = num2
                tabela.loc[tabela["numero"] == numero, "link"] = f"https://dexco.virtual360.io/nf/tax_documents/{id_nota}"
            
                print(id_nota)
                print("feito")
            
                tabela.to_excel("Bases/base_pegar_id/base_pegar_id2.xlsx", index = False)
            
            
            except:
                print("//////////////////////ERRO//////////////////////")
                break
        
        
        
    