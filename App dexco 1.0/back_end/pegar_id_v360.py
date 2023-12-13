from back_end.bibliotecas import *

usuario1 = []


class pegar_id:
    def pegar():
        
        try:
            options = webdriver.ChromeOptions() 
            options.add_argument(f"user-data-dir=C:\\Users\\{usuario1[0]}\\AppData\\Local\\Google\\Chrome\\User Data")
            time.sleep(2)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            driver.get("https://dexco.virtual360.io/nf/tax_documents/") 
            
            while len(driver.find_elements(By.XPATH,'//a[contains(text(),  "Login Dexco")]')) < 1 :
                pass
            driver.find_element(By.XPATH,'//a[contains(text(),  "Login Dexco")]').click()
            time.sleep(3)

            
            # Abrir tabela exel
            tabela = pd.read_excel("Bases/base_pegar_id/pegar_id.xlsx")
           
  
            
            for linha in tabela.index:
                
                try:  
                    time.sleep(2)
                    chave = tabela.loc[linha, "CHAVE"]
                
                    link = f"https://dexco.virtual360.io/nf/tax_documents?filters%5Bcompleted%5D=&filters%5Baccess_key%5D%5B%5D={chave}&filters%5Bautomatic_debit%5D=&filters%5Bhas_document_pdf%5D=&filters%5Bhas_document_xml%5D=&filters%5Bhas_bank_slips%5D=&filters%5Bprovider%5D=&filters%5Breceipt_status%5D=&filters%5Breceipt_confirmed%5D=&filters%5Bsimples_nacional_from_robot%5D=&filters%5Bsupplier_opting_for_simples_nacional%5D=&filters%5Bsupplier_cepom_registration%5D=&commit=Aplicar+filtros"
                    driver.get(link)
                
                    while len(driver.find_elements(By.XPATH,'//*[@id="table_list"]/div[1]/h2')) < 1 :
                        pass
                    
                    
                    pyautogui.click(500, 2000 )
                    img = pyautogui.locateCenterOnScreen('imgs/btn_v360.png')
                    pyautogui.click(img.x +100, img.y )
                    

                    while len(driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/div/div/div[1]/div[1]/h2/u')) < 1 :
                        pass
                    
                    id_nota = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/div/div/div[1]/div[1]/h2/u').text
                    

                    tabela.loc[tabela["CHAVE"] == chave, "ID"] = id_nota
                    
                
                    print(id_nota)
                    tabela.to_excel("Bases/base_pegar_id/pegar_id2.xlsx", index = False)
            
                
                except:
                    print("Erro no for")
                    break
            os.startfile("Bases/base_pegar_id/pegar_id2.xlsx")
        except:
            print("erro abrir navegador")
            pass    
        
        
    