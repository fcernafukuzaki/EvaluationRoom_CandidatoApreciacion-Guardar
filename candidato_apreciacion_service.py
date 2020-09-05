from datetime import datetime
from botocore.exceptions import ClientError


class CandidatoApreciacionService():

    def registrar_apreciacion_candidato(self, idcandidato, idcliente_idpuestolaboral, idcliente,
                                      idpuestolaboral, idreclutador, apreciacion, dynamodb=None):

        try:
            tabla = dynamodb.Table('Candidato_Apreciacion')
            response = tabla.put_item(
                Item={
                    'idcandidato': idcandidato,
                    'idcliente_idpuestolaboral': idcliente_idpuestolaboral,
                    'idcliente': idcliente,
                    'idpuestolaboral': idpuestolaboral,
                    'idreclutador': idreclutador,
                    'apreciacion': apreciacion,
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
            return False, e.response['Error']['Message'], 500
        else:
            return True, 'Respuesta guardada con éxito.', 200