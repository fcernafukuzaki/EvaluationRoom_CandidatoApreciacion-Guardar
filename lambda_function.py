from dynamodb_config import dynamodb
from autorizador_service import AutorizadorService
from candidato_apreciacion_service import CandidatoApreciacionService

autorizador_service = AutorizadorService()
candidato_apreciacion_service = CandidatoApreciacionService()


def lambda_handler(event, context):

    token = event['headers']['Authorization']
    email = event['headers']['correoelectronico']
    flag, respuesta, codigo = autorizador_service.reclutador_identificador_validar(token, email)
    if not flag:
        return {
            'statusCode': codigo,
            'body': respuesta
        }

    idcandidato = event['idcandidato']
    idcliente_idpuestolaboral = event['idcliente_idpuestolaboral']
    idcliente = event['idcliente']
    idpuestolaboral = event['idpuestolaboral']
    idreclutador = event['idreclutador']
    apreciacion = event['apreciacion']

    flag, respuesta, codigo = candidato_apreciacion_service.registrar_apreciacion_candidato(idcandidato, idcliente_idpuestolaboral, idcliente,
                                      idpuestolaboral, idreclutador, apreciacion, dynamodb)
    if flag:
        return {
            'statusCode': codigo,
            'body': respuesta
        }

    return {
        'statusCode': 500,
        'body': 'Error al registrar apreciación del candidato.'
    }
