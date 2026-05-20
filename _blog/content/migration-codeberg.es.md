+++
title = "BiblioGenius se muda de GitHub a Codeberg"
slug = "de-github-a-codeberg"
description = "Nuestra cuenta de GitHub fue suspendida de un día para otro, sin aviso. El código del proyecto vive ahora en Codeberg, una plataforma sin ánimo de lucro y open source. Esto es lo que pasó, y lo que cambia (o no) para ti."
date = 2026-05-20
updated = 2026-05-20
template = "blog/page.html"

[extra]
tags = ["anuncio"]
+++

BiblioGenius repite una idea sencilla desde el primer día: tus libros te pertenecen, tus datos se quedan contigo. El 4 de mayo recibimos un recordatorio muy concreto de por qué ese principio importa.

## Lo esencial primero: tu aplicación no se mueve

Si usas BiblioGenius para gestionar tu biblioteca, **todo está bien, puedes dejar de leer aquí**. Esta historia trata únicamente del lugar donde se guarda el *código fuente* del proyecto: la "receta" de la aplicación, la que los desarrolladores leen y mejoran. La aplicación, tus libros, tus préstamos, tus datos: nada se ve afectado, nada se pierde, no tienes que hacer nada.

El resto interesará sobre todo a los curiosos, y a las personas que contribuyen al proyecto.

## Qué pasó

Hasta ahora, el código de BiblioGenius estaba alojado en **GitHub**, la plataforma más conocida del mundo para almacenar código y colaborar en él. Un servicio gratuito, práctico, usado por millones de desarrolladores.

El 4 de mayo, **nuestra cuenta de GitHub fue suspendida**. Sin aviso previo, sin explicación, sin correo de advertencia. De un día para otro, todo el código del proyecto y su historial quedaron inaccesibles, para nosotros y para los contribuidores.

La causa más probable se reduce a una línea de las condiciones de uso: GitHub solo permite **una cuenta gratuita por persona**. Sin advertencia, sin plazo para regularizar: solo un interruptor apagado.

Consecuencia: los **tickets** (la lista de errores conocidos y de tareas pendientes) desaparecieron junto con la cuenta. Era ante todo una lista de trabajo interna, y se está reconstruyendo en la nueva plataforma.

## La lección

Hay una pequeña ironía en todo esto. BiblioGenius es un proyecto que defiende la soberanía digital: no depender de una plataforma única, capaz de cambiar sus reglas, encerrarte o cortarte el acceso sin rendir cuentas. Y acabamos de vivirlo, de verdad, con nuestro propio código.

Una única puerta de entrada, controlada por una sola empresa, es un punto de fragilidad. La respuesta correcta no es quejarse: es elegir un alojamiento coherente con los valores del proyecto.

## El nuevo hogar: Codeberg

BiblioGenius vive ahora en **Codeberg**.

Codeberg es el equivalente de GitHub (un lugar para alojar código y colaborar), pero con una diferencia de fondo: lo gestiona una **asociación sin ánimo de lucro**, con sede en Alemania, y no una multinacional. El software que hace funcionar Codeberg, *Forgejo*, es a su vez open source: se puede inspeccionar, copiar e instalar en otro sitio.

Dicho de otro modo: BiblioGenius es open source, y también lo es la plataforma que ahora aloja su código. Es más coherente, y es incluso lo que deberíamos haber hecho antes.

El proyecto está aquí:

- **Organización**: <https://codeberg.org/bibliogenius>
- **Servidor** (Rust): <https://codeberg.org/bibliogenius/bibliogenius>
- **Aplicación** (Flutter): <https://codeberg.org/bibliogenius/bibliogenius-app>
- **Hub**: <https://codeberg.org/bibliogenius/bibliogenius-hub>
- **Entorno de desarrollo**: <https://codeberg.org/bibliogenius/bibliogenius-env>

## ¿Contribuyes al proyecto? (parte técnica)

Si tienes un clon local de un repositorio, basta con apuntarlo a la nueva dirección. Desde la carpeta del repositorio:

```
git remote set-url origin https://codeberg.org/bibliogenius/<repo>.git
```

Por ejemplo, para la aplicación:

```
git remote set-url origin https://codeberg.org/bibliogenius/bibliogenius-app.git
```

Para abrir un ticket o una *pull request*, necesitarás una **cuenta de Codeberg** (gratuita), y nada más. No hace falta que te añadan a la organización: haces un fork del repositorio, subes los cambios a tu fork, abres una pull request. El flujo open source clásico.

## ¿Contribuiste y perdimos el contacto?

Es la parte más delicada de esta migración. Como la cuenta de GitHub cayó sin avisar, **perdimos la forma de volver a contactar con algunas personas**, traductores sobre todo.

Si alguna vez nos enviaste una traducción, reportaste un error, propusiste una corrección o una idea, y estás leyendo estas líneas: **escríbenos**. Nos gustaría sinceramente retomar el contacto, y asegurarnos de que tu contribución no se perdió en la mudanza.

Un único punto de contacto: [contact@bibliogenius.org](mailto:contact@bibliogenius.org).

## ¿Y las descargas?

Las versiones instalables para **Linux y Windows** se distribuían a través de GitHub. Por lo tanto, están momentáneamente no disponibles, mientras se monta un nuevo canal de descarga. Las aplicaciones de iOS, Android y macOS pasan por la App Store y Google Play, y no se ven afectadas. ¿Necesitas una versión mientras tanto? Escríbenos y te ayudamos.

La migración está terminada: BiblioGenius funciona ahora por completo en Codeberg. Ahí es donde continúa el desarrollo, y donde puedes seguir el proyecto.
