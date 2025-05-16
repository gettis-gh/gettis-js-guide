# 🧩 ¿Qué es una variable realmente?

Una variable es, en esencia, un **contenedor con nombre** donde guardamos información que puede cambiar mientras tu programa corre.

Pero no pienses en variables como cajas rígidas o cosas aburridas; son más bien como etiquetas que pones en tus ideas para poder usarlas y transformarlas cuando quieras.

---

## Concepto básico

Imagina que estás en la cocina y tienes diferentes ingredientes en frascos.  
Cada frasco tiene una etiqueta (variable) y puede contener diferentes cosas (valores).  

Puedes cambiar lo que hay dentro sin perder la etiqueta. Por ejemplo:

<pre>
let fruta = "manzana";  // la variable "fruta" tiene la manzana
fruta = "banana";       // ahora "fruta" tiene una banana
</pre>

---

## Tipos de variables en JavaScript

En JS, puedes declarar variables con `let`, `const` o `var`.  
Aquí te dejo lo esencial para que entiendas la diferencia:

- **let**: variable que puede cambiar su valor a lo largo del programa.  
- **const**: variable que no cambia una vez asignada (constante).  
- **var**: la forma antigua, no recomendable hoy, pero aún existe.

Para entender mejor los tipos de variables, mira:  
- [let](let.md)  
- [const](const.md)  
- [var](var.md)

---

## ¿Por qué usar variables?

- Para **guardar datos** que tu programa necesita, como nombres, números, resultados.  
- Para **hacer tu código legible**, usando nombres que tengan sentido.  
- Para **poder modificar y reutilizar información** sin repetir código.

---

## Para profundizar: Alcance y Hoisting

Antes de ver ejemplos prácticos, te recomiendo que sepas que hay dos conceptos importantes relacionados con las variables, que no vamos a explicar en detalle aquí para no complicar la introducción:

- **Alcance (Scope):** Se refiere a *dónde* y *cuándo* tus variables existen y pueden ser usadas dentro del código. Es clave para entender cómo funcionan tus variables en diferentes partes del programa.  
  Puedes profundizar más en el archivo [Alcance de variables](scope.md).

- **Hoisting:** Es un comportamiento especial de JavaScript donde las declaraciones de variables y funciones se "suben" al inicio del código antes de que se ejecute. Esto puede causar resultados inesperados si no se conoce bien.  
  Para entenderlo mejor, revisa [Hoisting en JavaScript](hoisting.md).

Estos temas pueden parecer un poco avanzados para arrancar, por eso los dejamos en archivos separados para que los consultes cuando estés listo.

---

## Ejemplo práctico

<pre>
let edad = 25;
console.log(edad); // 25

edad = 26;
console.log(edad); // 26
</pre>

Aquí `edad` es la variable que cambia conforme pasa el tiempo, justo como en la vida real.

---

## Variables y tipos de datos

Las variables pueden contener diferentes tipos de datos: números, texto, booleanos (verdadero/falso), objetos, funciones y más.

<pre>
let nombre = "Getti";
let esEstudiante = true;
let altura = 1.75;
</pre>

---

## Consejo de Getti

No te obsesiones con memorizar reglas al principio.  
Piensa en variables como tus “herramientas para guardar ideas” y usa nombres claros para que tu código sea un lenguaje para vos y para otros.

---

> _Una variable es más que una caja: es una idea con nombre que evoluciona en tu programa._
