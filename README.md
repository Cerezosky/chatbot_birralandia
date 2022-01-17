# chatbot_birralandia
Trabajo para la asignatura de Programación de Inteligencia Artificial

En este repositorio se encuentra por un lado un cuaderno de Jupiter Notebook donde podremos ejecutar la combinación del archivo AIML con el modelo de python obtenido de ML4K. Además, dentro de la carpeta, tenemos el archivo charbot.py que se obtiene como resultado de ML4K.

Para poder ejecutar este cuaderno, es necesario que se ejecuten todas las celdas para que se instale el paquete programy y se carguen los paquetes y variables necesarias. La primera línea que instala programy solo hay que ejecutarla si no se tiene instalado este paquete.

Este chatbot está pensado para una web que se dedique a vender cerveza, y que sirva de guía para aquellos que no sepan qué cerveza quieren.

En primer lugar, te pregunta si necesitas ayuda. Si dices que si, te pregunta el tipo de cerveza que quieres entre tres tipos, y una vez indicado, te pregunta si quieres una nacional o de importación. Una vez que le has indicado la procedencia de la cerveza, te devuelve de forma aleatoria una de las cervezas que cumple estas propiedades.

La capa de ML4K hace que las respuestas no tengan que ser exactamente idénticas a las esperadas, y si el porcentaje de parecido está por denajo del 75%, lanza un mensaje diciendo que no te entiende y que por favor, respondas otra cosa.

Además, una vez que has indicado el tipo de cerveza que te gusta, te mete en un topic para garantizar que si indicas que la quieres de importación, es de ese tipo de cerveza y no de ninguna otra.

Eso es todo. Espero que cumpla las espectativas esperadas.
