import json

def lambda_handler(event, context):
    """
    Simula o processamento principal (executado apenas se APROVADO).
    """
    
    print(f"Iniciando o processamento do pedido para o cliente ID: {event['data'].get('cliente_id')}")
    
    # Simulação de um processamento de 5 segundos
    # time.sleep(5) 
    
    return {
        "status": "CONCLUIDO",
        "detail": f"Pedido processado com sucesso para o Cliente ID: {event['data'].get('cliente_id')}",
        "final_data": event['data']
    }
