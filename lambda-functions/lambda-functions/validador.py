import json

def lambda_handler(event, context):
    """
    Simula a validação de dados.
    Verifica se o campo 'cliente_id' está presente.
    """
    
    # Simula a lógica de falha se o ID do cliente não for fornecido
    if 'cliente_id' not in event:
        # Retorna o status REJEITADO e uma mensagem de erro
        return {
            "status": "REJEITADO",
            "error_message": "Erro de validação: 'cliente_id' não encontrado na entrada.",
            "original_input": event
        }
    
    # Se a validação passar
    if event.get('cliente_id') in ['123', '456']: # Exemplo de IDs aprovados
        return {
            "status": "APROVADO",
            "message": "Dados válidos. Pronto para processamento.",
            "data": event # Passa os dados adiante
        }
    else:
        # Se o cliente ID estiver lá, mas for inválido
        return {
            "status": "REJEITADO",
            "error_message": f"Erro de validação: Cliente ID {event.get('cliente_id')} é desconhecido.",
            "original_input": event
        }
