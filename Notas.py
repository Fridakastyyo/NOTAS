from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token de autenticación de tu bot (reemplaza con el token que obtuviste de BotFather)
TOKEN = '7587654794:AAElkV2yJUplL8gWZwHxxf9jurEuN9hVpGI'

# Respuestas según las palabras clave
RESPUESTAS = {
    'CPA04010': '****Esta nota aplica para transitorios y permanentes**** se envía en un tiempo límite de 10 minutos después del disparo. \n *12 de enero de 2025* \n A las *00:00:00* horas, sale de operación el circuito *04010*, de la subestación *Coapan (CPA)*, *afectando a 14 sistemas de agua potable* del municipio de San Antonio Cañada, Ajalpan, Altepexi y Tehuacán en el Estado de Puebla, y *7.0 MW* de demanda y a *11,278* usuarios. El recierre fue a las *00:00:00* horas. \n Saludos. \n ________________________________________________________________________________ \n En caso de Permanente aplicar esta nota a los 10 minutos de mandar la primera nota  \n *12 de enero de 2025* \n *Informar sobre la afectación del suministro de energía eléctrica por la salida operación del circuito de media tensión 04010, de la subestación Coapan (CPA), afectando a 14 sistemas de agua potable y usuarios de San Antonio Cañada, Ajalpan, Altepexi y Tehuacán, en el estado de Puebla.* \n  *Antecedentes:* \n En la Zona de Distribución Tehuacán de la División Centro Oriente, el 12 de enero de 2025 a las XXXX horas se interrumpió el suministro de energía eléctrica por la salida de operación del circuito de media tensión *04010*, de la subestación *Coapan (CPA)*, afectando *7.0 MW* de demanda y a *11,278 usuarios*, del *municipio de San Antonio Cañada, Ajalpan, Altepexi y Tehuacán, estado de Puebla.* \n Los usuarios importantes afectados son: *14 sistemas de agua potable* \n La colonia importante es: San Esteban Necoxcalco y Santa Cruz Acapa, Puebla.\n *Situación actual:* \n Se envía personal para detectar y corregir la causa de salida del circuito de media tensión 04010. \n Con horario de las XX:XX:XX horas, se restablecieron xx usuarios afectados, lo que representa un avance del XXX%. Con esta maniobra se recuperaron X sistemas de agua potable y X Centros de Salud. \n La causa se investiga. \n *Acciones para emprender:*\n Continuar con el restablecimiento hasta recuperar el 100% de los usuarios afectados.',
    'CPA04020': '',
    'CPA04030': '',
    'CPA04040': '¡Me alegro de que estés bien! 🙌',
    'CPA04050': 'Lamento escuchar eso. 😔 ¿En qué puedo ayudarte?',
    'CPA04060':'',
    'CPA53010':'',
    'CPA53020':'',
    'THN04410':'',
    'THN04420':'',
    'THN04430':'',
    'THN04440':'',
    'THN04450':'',
    'THN04460':'',
    'THN04470':'',
    'THN04480':'',
    'THN04490':'',
    'THN05460':'',
    'THN05470':'',
    'THN05480':'',
    'TTP04010':'',
    'TTP04020':'',
    'TTP04030':'',
    'TTP04040':'',
    'SNG04010':'',
    'SNG04020':'',
    'SNG04030':'',
    'ZIP04010':'',
    'ZIP04020':'',
    'ZIP04030':'',
    'ZIP04040':'',
    'ZIP04050':'',
    'ZIP04060':'',

}

# Función para manejar el comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! escribe qué nota necesitas')

# Función para manejar los mensajes del usuario
def responder_palabra(update: Update, context: CallbackContext) -> None:
    # Obtiene el texto del mensaje
    mensaje = update.message.text.lower()

    # Responde según la palabra dada
    respuesta = RESPUESTAS.get(mensaje, 'Lo siento, no entiendo esa palabra.')

    # Enviar la respuesta
    update.message.reply_text(respuesta)

# Función principal para configurar el bot
def main():
    # Crear el Updater y el Dispatcher para manejar los mensajes
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Registrar el manejador para el comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Registrar el manejador para los mensajes de texto
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, responder_palabra))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
