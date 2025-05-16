# 🌐 Alcance (Scope) en JavaScript

El **alcance** o *scope* determina **dónde** y **cuándo** una variable o función puede ser accedida dentro del código.

Entender el scope es clave para evitar errores y escribir código claro y mantenible.

---

## Tipos de Scope

En JavaScript hay principalmente dos tipos de scope:

- **Scope Global:** Las variables declaradas fuera de cualquier función o bloque, accesibles desde cualquier parte del código.  
- **Scope Local:** Las variables declaradas dentro de una función o bloque, accesibles solo dentro de ese contexto.

---

## Scope Global

Las variables globales son accesibles desde cualquier parte de tu programa.

<pre>
let mensaje = "Hola desde el scope global";

function saludar() {
  console.log(mensaje); // Puede acceder a "mensaje"
}

saludar(); // Imprime: Hola desde el scope global
</pre>

Pero cuidado: abusar de variables globales puede generar problemas y conflictos.

---

## Scope Local

Las variables declaradas dentro de funciones o bloques sólo existen ahí.

<pre>
function saludoLocal() {
  let mensaje = "Hola desde el scope local";
  console.log(mensaje); // Funciona bien aquí
}

saludoLocal();

console.log(mensaje); // Error: mensaje no está definida aquí
</pre>

---

## Scope de Bloque (Block Scope)

Con `let` y `const`, las variables tienen scope limitado al bloque `{ ... }` donde se declaran.

<pre>
if (true) {
  let secreto = "Sólo estoy aquí dentro";
  console.log(secreto); // Funciona
}

console.log(secreto); // Error: secreto no está definido aquí
</pre>

En cambio, `var` no respeta el scope de bloque, sino el de función.

---

## ¿Por qué es importante el scope?

- Evita conflictos entre variables con el mismo nombre.  
- Mejora la legibilidad y mantenimiento del código.  
- Controla la vida útil y visibilidad de los datos.

---

## Consejo de Getti

Siempre usa `let` y `const` para aprovechar el scope de bloque y escribir código más seguro y predecible.  

Entender el scope te dará poder para organizar tu código y evitar errores comunes.

---

> _El scope es el mapa que te dice dónde tus variables pueden vivir y respirar._
