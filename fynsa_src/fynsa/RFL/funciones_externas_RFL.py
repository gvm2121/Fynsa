from RFL.models import tr,risk,bonos,lva_vector
from django.core.exceptions import ObjectDoesNotExist


def truncar(numero,decimales):
    if ',' in numero:
        numero_aux=numero.split(',')
        lado_derecho=numero_aux[1]
        lado_izquierdo=numero_aux[0]
        if decimales==0:
            return lado_izquierdo
        if len(lado_derecho)>=decimales:
            lado_derecho=lado_derecho[:decimales]
            numero_final=lado_izquierdo+'.'+lado_derecho
        else:
            numero_final=lado_izquierdo+'.'+lado_derecho
        return numero_final
    elif '.' in numero:
        numero_aux=numero.split('.')
        lado_derecho=numero_aux[1]
        lado_izquierdo=numero_aux[0]
        if decimales==0:
            return lado_izquierdo
        if len(lado_derecho)>=decimales:
            lado_derecho=lado_derecho[:decimales]
            numero_final=lado_izquierdo+'.'+lado_derecho
        else:
            numero_final=lado_izquierdo+'.'+lado_derecho
        return numero_final
    else:
        numero_final=numero
        return numero_final

def actualiza_riesgo():
    for h in tr.objects.all():
        try:
            
            riesgo_bono = bonos.objects.get(instrumento=h.instrumento)
            objeto = tr.objects.filter(instrumento=h.instrumento)
            objeto.update(rating = riesgo_bono.rating)
        except bonos.DoesNotExist:
            print('Bono no encontrado : {}'.format(h.instrumento))
            pass        

    return True
    
def actualiza_tipo():
    for h in tr.objects.all():
        try:            
            riesgo_bono = bonos.objects.get(instrumento=h.instrumento)
            objeto = tr.objects.filter(instrumento=h.instrumento)
            objeto.update(tipo = riesgo_bono.tipo)
        except bonos.DoesNotExist:
            print('Bono no encontrado : {}'.format(h.instrumento))
            pass        

    return True

def limpia_risk():
    for h in tr.objects.all():
        try:            
            objeto = risk.objects.filter(nemo=h.instrumento)
            objeto.delete()
        except bonos.DoesNotExist:
            print('Bono no encontrado : {}'.format(h.instrumento))
            pass        

    return True

def actualiza_riesgo_lva():
    for h in lva_vector.objects.all():
        try:
            
            riesgo_bono = bonos.objects.get(instrumento=h.nemo)
            #objeto = lva_vector.objects.filter(nemo=h.instrumento)
            #objeto.update(riesgo = riesgo_bono.rating)
            h.riesgo = riesgo_bono.rating
            h.save()

        except bonos.DoesNotExist:
            print('Bono no encontrado : {}'.format(h.nemo))
            pass        

    return True



    
