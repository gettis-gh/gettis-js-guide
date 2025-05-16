# 🔧 `let`: Tu variable de confianza

`let` es una de las formas modernas y recomendadas para declarar variables en JavaScript.  
Es flexible, segura y respeta el scope de bloque.

---

## ¿Qué hace `let`?

Declara una variable cuyo valor **puede cambiar** a lo largo del tiempo.  
A diferencia de `const`, no es constante, y a diferencia de `var`, no se comporta raro con el scope ni con hoisting.

<pre>
let nombre = "Getti";
nombre = "Otro Getti"; // ✅ válido
</pre>

---

## Ventajas de usar `let`

- Tiene **scope de bloque**, lo que evita errores.
- No permite declarar la misma variable dos veces en el mismo bloque.
- Es más predecible que `var`.

---

## Scope de bloque con `let`

<pre>
if (true) {
  let mensaje = "Hola desde dentro";
  console.log(mensaje); // Funciona
}

console.log(mensaje); // ❌ Error: mensaje no está definida
</pre>

Esto te ayuda a mantener tu código limpio y controlado.

---

## Reasignación sí, redeclaración no

<pre>
let fruta = "banana";
fruta = "manzana"; // ✅ Ok

let fruta = "pera"; // ❌ Error: ya está declarada en este bloque
</pre>

---

## Diferencia clave con `var`

`let` no se hoistea como `var`, o mejor dicho, sí se hoistea, pero **no se inicializa automáticamente con `undefined`**.  
Intentar usar una variable `let` antes de declararla lanza error.

<pre>
console.log(nombre); // ❌ ReferenceError
let nombre = "Getti";
</pre>

Esto se llama **zona muerta temporal (TDZ)**: el tiempo entre que se entra al scope y se declara la variable.

---

## Consejo de Getti

Siempre que necesites una variable que pueda cambiar, usá `let`.  
Vas a evitarte muchos dolores de cabeza comparado con `var`.

---

> _Pensá en `let` como una caja que podés abrir y cambiar, pero que nadie puede confundir con otra caja del mismo nombre._
