# 🧱 `const`: Constantes en JavaScript

`const` se usa para declarar **constantes**, es decir, valores que **no pueden ser reasignados** una vez definidos.

Pero ojo: **const no significa inmutable**, sólo que no podés cambiar lo que guarda la variable… aunque lo que guarda sí puede cambiar (si es un objeto o array, por ejemplo).

---

## ¿Cuándo usar `const`?

Usá `const` cuando **sabés que una variable no va a cambiar** nunca después de asignarla.

<pre>
const pi = 3.1416;
console.log(pi); // 3.1416

pi = 3; // ❌ Error: Assignment to constant variable
</pre>

---

## Ventajas de `const`

- Hace que tu intención como programador sea clara: *esto no va a cambiar*.  
- Evita errores accidentales de reasignación.  
- Ayuda a mantener el código más estable y predecible.

---

## Objetos y `const`

Esto confunde a muchos: **con `const` no podés cambiar la referencia, pero sí el contenido si es un objeto o array.**

<pre>
const persona = { nombre: "Getti" };
persona.nombre = "Otro nombre"; // ✅ Válido

persona = {}; // ❌ Error: no podés reasignar la referencia
</pre>

---

## Buenas prácticas

- Usá `const` **por defecto**.  
- Si sabés que vas a reasignar el valor, entonces usá `let`.  
- Evitá `var`.

---

## Comparación rápida

| Tipo   | ¿Se puede reasignar? | ¿Respeta scope de bloque? |
|--------|----------------------|----------------------------|
| `const` | ❌ No               | ✅ Sí                      |
| `let`   | ✅ Sí               | ✅ Sí                      |
| `var`   | ✅ Sí               | ❌ No (usa scope de función) |

---

## Consejo de Getti

Usar `const` es como poner un cartel de **"esto no se toca"**.  
Hace que tu código hable más claro, y eso es clave para pensar, leer y trabajar sin miedo.

---

> _La constante no es rígida, es una promesa de no cambiar la etiqueta._  
