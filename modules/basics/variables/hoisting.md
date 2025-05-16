# 🪁 Hoisting en JavaScript

**Hoisting** (en español: “elevación” o “alzado”) es un comportamiento peculiar de JavaScript:  
Antes de que tu código se ejecute, **las declaraciones de variables y funciones se mueven (internamente) hacia arriba del archivo o bloque**.

Pero ojo: **sólo las declaraciones**, no las asignaciones.

---

## ¿Qué significa eso en la práctica?

Que podés usar una función o una variable **antes** de declararla... pero con matices.

---

## Hoisting con funciones

Las funciones declaradas con `function` sí se "hoistean" completamente: declaración y contenido.

<pre>
saludar(); // Funciona

function saludar() {
  console.log("Hola desde una función hoisteada");
}
</pre>

---

## Hoisting con `var`

Las variables declaradas con `var` también se hoistean, pero solo su **declaración**, no el valor.

<pre>
console.log(nombre); // undefined, no error

var nombre = "Getti";
</pre>

Lo que realmente interpreta JavaScript es como si hicieras esto:

<pre>
var nombre;
console.log(nombre); // undefined
nombre = "Getti";
</pre>

---

## `let` y `const` NO se comportan igual

Aunque también son "hoisteadas", **no pueden ser usadas antes de su declaración**. Si lo hacés, da error.

<pre>
console.log(edad); // ❌ ReferenceError

let edad = 25;
</pre>

Esto pasa porque están en lo que se llama **zona muerta temporal** (temporal dead zone), un período en el que la variable existe pero no es accesible.

---

## Entonces… ¿es malo el hoisting?

No es malo, simplemente **hay que entenderlo**.

Evitás la mayoría de los problemas si:

- Declarás tus variables y funciones **antes de usarlas**.
- Usás `let` y `const` en lugar de `var`.

---

## Consejo de Getti

No te apoyes en el hoisting para escribir "magia negra".  
Declarar todo al principio de tus bloques y funciones hace que tu código sea más claro y fácil de mantener.

---

> _Hoisting es como si JavaScript dijera: “Voy a ordenar tu casa antes de que empieces a vivir en ella”, pero no siempre como esperás._
