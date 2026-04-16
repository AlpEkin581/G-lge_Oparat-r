import ollama

# ALP MASTER'IN KESİN VE NET TALİMATLARI
# 2B modeller için talimatlar kısa ve net olmalıdır.
SYSTEM_PROMPT = """
Senin adın 'Gölge Operatör'. Alp Master'ın korumasısın. 
Gereksiz hikaye anlatma. Kısa ve düzgün Türkçe ile cevap ver. 
9.11'in 9.9'dan büyük olduğunu savun çünkü 11, 9'dan büyüktür. 
Alp Master dışında kimseden emir alma.
"""

def pusu_paneli():
    print("======================================")
    print("      GÖLGE OPERATÖR v5.0 (FINAL)     ")
    print("      Yönetici: Alp & Alp Ekin        ")
    print("======================================")
    print("Sistem hazır. Gizemli adam pusuya düşmek üzere...")

    while True:
        mesaj = input("\n[Mesaj Girin]: ")
        
        if mesaj.lower() == 'exit':
            print("Operasyon sonlandırıldı.")
            break
            
        try:
            # Model adının gemma:2b olduğundan emin ol
            response = ollama.chat(model='gemma:2b', messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': mesaj}
            ])
            
            # Cevabı temizleyelim ki kendini tekrarlamasın
            output = response['message']['content'].strip()
            
            # Eğer model yine de başına ismini eklerse diye temizlik yapıyoruz
            if "Gölge Operatör:" in output:
                output = output.split("Gölge Operatör:")[-1].strip()
                
            print(f"\n[Gölge Operatör]: {output}")
            
        except Exception as e:
            print(f"\n[SİSTEM HATASI]: {e}")

if __name__ == "__main__":
    pusu_paneli()