import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
  st.title('Upload de Arquivos Azure Fake Docs')
  upload_file = st.file_uploader("Upload de Arquivos", type = ["png", "jpg", "jpeg"])

  if upload_file is not None:
    fileName = upload_file.name
    #Enviar para o blob
    blob_url = upload_blob(upload_file, fileName)
    if blob_url:
        st.write(f"Arquivo {fileName} enviado com sucesso!")
        credit_card_info = "" #Chamar função de cartão de crédito
        show_image_and_validate = (blob_url, credit_card_info) #Chamar função de imagem
    else:
        st.write(f"Erro ao enviar o arquivo {fileName}")



  def show_image_and_validate(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem do documento enviada", use_column_width=True)
    st.write("Resultado da validação")
    if credit_card_info and credit_card_info["card_name"]:
      st.markdown(f"<h1 style='color: green;'>Cartão de Crédito:</h1>", unsafe_allow_html= True) 
      st.write(f"Nome do titular: {credit_card_info['card_name']}")
      st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
      st.write(f"Data de validade: {credit_card_info['expiration_date']}")
    else:
      st.markdown("<h1 style='color: red;'>Cartão de Inválido:</h1>", unsafe_allow_html= True) 
      st.write("Cartão de crédito inválido")


  if __name__ == "__main__":
    configure_interface()
