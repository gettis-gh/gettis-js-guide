# 🧪 `var`: El viejo modo de declarar variables

Antes de que existieran `let` y `const`, la única forma de declarar variables en JavaScript era usando `var`.

Aunque todavía funciona, **no se recomienda usarlo hoy** salvo que estés manteniendo código viejo o aprendiendo sobre cómo funcionaba JS antes de ES6 (2015).

---

## ¿Cómo se usa?

<pre>
var nombre = "Getti";
console.log(nombre); // Getti
</pre>

Funciona igual que `let`, pero tiene un par de comportamientos raros que pueden causar errores inesperados.

---

## Problemas con `var`

### 1. No respeta el scope de bloque

`var` ignora las llaves `{}` de los bloques.  
Sólo respeta el scope de función.

<pre>
if (true) {
  var fruta = "banana";
}
console.log(fruta); // banana (aunque está fuera del if)
</pre>

Con `let` o `const`, eso daría un error porque `fruta` estaría limitada al bloque.

---

### 2. Puede ser redeclarada sin error

<pre>
var animal = "gato";
var animal = "perro"; // no da error
console.log(animal); // perro
</pre>

Con `let` o `const`, intentar redeclarar una variable en el mismo scope lanza un error.

---

### 3. Está afectada por hoisting (de forma peligrosa)

Las variables declaradas con `var` son **"hoisteadas"** pero su valor inicial es `undefined`.

<pre>
console.log(edad); // undefined
var edad = 30;
</pre>

La declaración se mueve arriba, pero la asignación no.  
Con `let` y `const` esto daría un error (y eso es bueno).

---

## ¿Cuándo usar `var`?

- Si estás manteniendo código viejo.
- Si estás aprendiendo sobre cómo funcionaba JS antes de ES6.
- Para entender conceptos como hoisting y scope antiguo.

---

## Consejo de Getti

No uses `var` en código nuevo.  
Aprendelo para entender la historia del lenguaje y por qué `let` y `const` existen.  
Pero en la práctica diaria, usá `let` si va a cambiar el valor, y `const` si no.

---

> _`var` fue útil en su tiempo, pero hoy es como usar una cámara analógica: útil para aprender, pero poco práctica para lo moderno._
