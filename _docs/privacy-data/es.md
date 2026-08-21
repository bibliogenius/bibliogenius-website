---
title: Dónde se guardan mis datos
description: Lo que se queda en tu dispositivo, lo que sale de él y cómo mantienes el control
order: 12
group: data
---

BiblioGenius es local primero: tu biblioteca vive en una base de datos de tu dispositivo, y la aplicación funciona sin cuenta y sin conexión. Lo que sale del dispositivo sale porque tú lo has pedido, y esta página dice exactamente qué, cuándo y hacia dónde.

## En tu dispositivo

Tus libros, estanterías, colecciones, etiquetas, ejemplares, préstamos y contactos se guardan en local. Puedes usar toda la aplicación sin conexión: añadir libros a mano, organizarlos, seguir tus lecturas.

## Lo que sale del dispositivo, y cuándo

- **Las búsquedas en catálogos externos.** Cuando escaneas un ISBN o buscas un título, la consulta sale hacia las fuentes activadas (BNF, OpenLibrary, Inventaire y otras). Esas fuentes ven, por tanto, lo que buscas. Tú eliges cuáles consultar en Configuración > Fuentes de búsqueda.
- **Las portadas y los metadatos** se descargan de esas mismas fuentes y luego se quedan en tu dispositivo.
- **Lo que compartes con tus contactos.** Cuando una biblioteca conectada consulta tu catálogo, tu dispositivo le responde directamente, cifrado de extremo a extremo. En una red wifi local el intercambio no sale de esa red. A distancia pasa por un relé que solo ve datos cifrados.
- **El directorio en línea**, si lo activas con "Hacer visible mi biblioteca para otras bibliotecas". Puedes exigir tu aprobación antes de que un nuevo seguidor acceda a tus libros compartidos. Tu ciudad sigue siendo una preferencia local mientras no elijas compartirla.
- **La cuenta cifrada**, si creas una. El servidor solo guarda bloques cifrados, ilegibles para él. Consulta [Cuenta cifrada y varios dispositivos](../../en/docs/account-sync.html) (en inglés).

Nada de esto se activa en tu lugar.

## Elegir lo que ven los demás

Activa "Libros privados" en la configuración para desbloquear la opción Privado en cada libro: un libro privado se queda en tu biblioteca pero nunca aparece ante los demás, ni en tu perfil público ni en las búsquedas de la red.

Para comprobarlo en vez de fiarte, abre **"Lo que ven las otras bibliotecas"**: esa lista es la respuesta exacta que tu dispositivo envía a una biblioteca que consulta tu catálogo, producida por el mismo código, sin ningún recálculo de fachada.

## Copias de seguridad

Puedes sacar tus datos cuando quieras desde **Configuración > Copia de seguridad y recuperación**: exportación portátil, exportación CSV legible en una hoja de cálculo, o archivo cifrado restaurable. Consulta [Guardar y exportar](../../en/docs/export-backup.html) (en inglés).

## Cifrado

Los intercambios entre bibliotecas están cifrados de extremo a extremo. La cuenta cifrada y las copias completas también, con una clave derivada de tu frase secreta: no tenemos ningún medio técnico de leer tus datos.

## Borrar mis datos

En el dispositivo, la configuración permite borrar tus libros o empezar de cero. Para eliminar una cuenta en línea, sigue el procedimiento descrito en la página [Eliminación de datos](../data-deletion.html).
