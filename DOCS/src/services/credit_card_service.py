from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from ultils.Config import Config

def analyze_credit_card(card_url):
    try:
        # Configuração do cliente
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentAnalysisClient(endpoint=Config.ENDPOINT, credential=credential)

        # Análise do documento usando URL
        poller = document_client.begin_analyze_document_from_url("prebuilt-id", card_url)
        result = poller.result()

        # Extração de informações do cartão
        for document in result.documents:
            return {
                "card_name": document.fields.get('CardHolderName', {}).value,
                "card_number": document.fields.get('CardNumber', {}).value,
                "expiration_date": document.fields.get('ExpirationDate', {}).value,
                "bank_name": document.fields.get('BankName', {}).value,
            }

    except Exception as e:
        print(f"Erro ao analisar o cartão de crédito: {e}")
        return None
