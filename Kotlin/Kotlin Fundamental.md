_Based on material by Eko Kurniawan Khannedy_

---

## 📑 Table of Contents

### Fundamentals

- [[#🎯 About Kotlin]]
- [[#🛠️ Setup & Installation]]
- [[#👋 Hello World]]

### Data Types

- [[#🔢 Number Types]]
- [[#🔤 Character]]
- [[#✅ Boolean]]
- [[#📝 String]]
- [[#📊 Array]]
- [[#📏 Range]]

### Variables

- [[#💾 Variable Declaration]]
- [[#❓ Nullable Types]]
- [[#🔒 Constants]]

### Operators

- [[#➕ Mathematical Operations]]
- [[#⚖️ Comparison Operations]]
- [[#🔀 Boolean Operations]]

### Control Flow

- [[#🔀 If Expression]]
- [[#🔄 When Expression]]
- [[#🔁 For Loop]]
- [[#⏰ While Loop]]
- [[#⛔ Break & Continue]]

### Functions

- [[#⚙️ Function Basics]]
- [[#📥 Function Parameters]]
- [[#📤 Return Types]]
- [[#🔧 Extension Functions]]
- [[#λ Lambda Expressions]]
- [[#🎯 Higher-Order Functions]]
- [[#⚡ Inline Functions]]
- [[#🔄 Recursive Functions]]

### Advanced Topics

- [[#🏷️ Labels]]
- [[#📦 Package & Import]]
- [[#💬 Comments]]
- [[#🎭 Anonymous Functions]]
- [[#🔐 Closure]]
- [[#🎯 Function Scope]]
- [[#🔗 Infix Notation]]
- [[#🚀 Main Function Parameters]]

---

## 🎯 About Kotlin

**History:**

- Introduced by JetBrains in 2011
- Runs on JVM (Java Virtual Machine)
- Designed to integrate with Java
- Official Android development language (2017)

**Why Kotlin?**

- More elegant and simpler than Java
- Full Java ecosystem compatibility
- Primary language for Android development
- Supported by Spring Framework

[[#📑 Table of Contents|← Back to Contents]]

---

## 🛠️ Setup & Installation

**Requirements:**

- Java Development Kit (JDK) 8 or higher
- IntelliJ IDEA (recommended IDE)

**Installation:**

```bash
# Linux/Mac - Add to .bashrc or .zshrc
export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_241.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 👋 Hello World

```kotlin
fun main() {
    println("Hello World")
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔢 Number Types

### Integer Numbers

|Type|Size (bits)|Range|
|---|---|---|
|`Byte`|8|-128 to 127|
|`Short`|16|-32,768 to 32,767|
|`Int`|32|-2,147,483,648 to 2,147,483,647|
|`Long`|64|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|

### Floating Point Numbers

|Type|Size (bits)|Decimal Digits|
|---|---|---|
|`Float`|32|6-7|
|`Double`|64|15-16|

### Examples

```kotlin
val age: Int = 25
val distance: Long = 1000000L
val price: Float = 99.99F
val pi: Double = 3.14159

// Literals with underscore for readability
val million = 1_000_000

// Conversion
val int: Int = 100
val long: Long = int.toLong()
val double: Double = int.toDouble()
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔤 Character

```kotlin
val firstLetter: Char = 'A'
val newLine: Char = '\n'
val tab: Char = '\t'
```

[[#📑 Table of Contents|← Back to Contents]]

---

## ✅ Boolean

```kotlin
val isActive: Boolean = true
val isComplete: Boolean = false
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📝 String

### Basic String

```kotlin
// Single line
val name: String = "Kotlin"

// Multi-line
val address: String = """
    Jalan ABC
    Jakarta
    Indonesia
"""

// Multi-line with trim margin
val formatted: String = """
    |Line 1
    |Line 2
    |Line 3
""".trimMargin()
```

### String Concatenation

```kotlin
val firstName = "John"
val lastName = "Doe"
val fullName = firstName + " " + lastName
```

### String Template

```kotlin
val name = "Kotlin"
val version = 1.4

// Simple expression
println("Hello $name")

// Complex expression
println("Version ${version + 1}")
println("Name length: ${name.length}")
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📊 Array

### Creating Arrays

```kotlin
val numbers: Array<Int> = arrayOf(1, 2, 3, 4, 5)
val names: Array<String> = arrayOf("John", "Jane", "Bob")

// Array with specific size and initializer
val squares = Array(5) { i -> i * i }  // [0, 1, 4, 9, 16]
```

### Array Operations

```kotlin
val names = arrayOf("Eko", "Kurniawan", "Khannedy")

// Get size
println(names.size)  // 3

// Access element
println(names[0])        // Eko
println(names.get(1))    // Kurniawan

// Modify element
names[0] = "John"
names.set(1, "Doe")
```

### Index in Array

|Index|Data|
|---|---|
|0|Eko|
|1|Kurniawan|
|2|Khannedy|

### Array Nullable

```kotlin
// Array with nullable elements
val names: Array<String?> = arrayOf("John", null, "Jane")
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📏 Range

### Creating Ranges

```kotlin
val range1 = 0..10        // 0 to 10 (inclusive)
val range2 = 1..100       // 1 to 100
val rangeChar = 'a'..'z'  // a to z
```

### Range Operations

```kotlin
val range = 1..10

println(range.count())      // 10
println(range.contains(5))  // true
println(5 in range)         // true
println(range.first)        // 1
println(range.last)         // 10
println(range.step)         // 1

// Reverse range
val reverse = 10 downTo 1

// Range with step
val step = 1..10 step 2  // 1, 3, 5, 7, 9
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 💾 Variable Declaration

### Mutable Variable (var)

```kotlin
var name: String = "John"
name = "Jane"  // Can be changed
```

### Immutable Variable (val)

```kotlin
val pi: Double = 3.14
// pi = 3.15  // Error! Cannot be reassigned
```

**Declaration Format:**

```kotlin
val/var variableName: DataType = data
```

**Recommendation:** Use `val` (immutable) by default

[[#📑 Table of Contents|← Back to Contents]]

---

## ❓ Nullable Types

```kotlin
// Non-nullable (default)
var name: String = "John"
// name = null  // Error!

// Nullable
var nullableName: String? = "John"
nullableName = null  // OK

// Array with nullable elements
val names: Array<String?> = arrayOf("John", null, "Jane")
```

**Note:** Use nullable types sparingly, only when absolutely necessary.

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔒 Constants

```kotlin
const val MAX_AGE = 100
const val APP_NAME = "MyApp"
const val PI = 3.14159
```

**Convention:** Use UPPER_CASE for constant names.

[[#📑 Table of Contents|← Back to Contents]]

---

## ➕ Mathematical Operations

### Basic Operators

```kotlin
val a = 10
val b = 3

println(a + b)  // 13 - Addition
println(a - b)  // 7  - Subtraction
println(a * b)  // 30 - Multiplication
println(a / b)  // 3  - Division
println(a % b)  // 1  - Modulus (remainder)
```

### Augmented Assignments

```kotlin
var a = 10

a += 5   // a = a + 5
a -= 3   // a = a - 3
a *= 2   // a = a * 2
a /= 4   // a = a / 4
a %= 3   // a = a % 3
```

### Unary Operators

```kotlin
var a = 10

++a  // Increment (a = 11)
--a  // Decrement (a = 10)
-a   // Negative (-10)
+a   // Positive (10)
!true  // Boolean negation (false)
```

[[#📑 Table of Contents|← Back to Contents]]

---

## ⚖️ Comparison Operations

```kotlin
val a = 10
val b = 5

println(a > b)   // true  - Greater than
println(a < b)   // false - Less than
println(a >= b)  // true  - Greater than or equal
println(a <= b)  // false - Less than or equal
println(a == b)  // false - Equal to
println(a != b)  // true  - Not equal to
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔀 Boolean Operations

### Logical Operators

```kotlin
val a = true
val b = false

println(a && b)  // false - AND
println(a || b)  // true  - OR
println(!a)      // false - NOT
```

### Truth Tables

**AND (&&):**

|Value 1|Operator|Value 2|Result|
|---|---|---|---|
|true|&&|true|true|
|true|&&|false|false|
|false|&&|true|false|
|false|&&|false|false|

**OR (||):**

|Value 1|Operator|Value 2|Result|
|---|---|---|---|
|true|\||true|true|
|true|\||false|true|
|false|\||true|true|
|false|\||false|false|

**NOT (!):**

|Operator|Value|Result|
|---|---|---|
|!|true|false|
|!|false|true|

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔀 If Expression

### Basic If

```kotlin
val score = 85

if (score >= 80) {
    println("Excellent")
}
```

### If-Else

```kotlin
val age = 17

if (age >= 18) {
    println("Adult")
} else {
    println("Minor")
}
```

### If-Else If

```kotlin
val score = 75

if (score >= 90) {
    println("A")
} else if (score >= 80) {
    println("B")
} else if (score >= 70) {
    println("C")
} else {
    println("D")
}
```

### If as Expression

```kotlin
val max = if (a > b) a else b

val grade = if (score >= 90) {
    "A"
} else if (score >= 80) {
    "B"
} else {
    "C"
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔄 When Expression

### Basic When

```kotlin
val grade = "A"

when (grade) {
    "A" -> println("Excellent")
    "B" -> println("Good")
    "C" -> println("Average")
    else -> println("Poor")
}
```

### Multiple Options

```kotlin
when (grade) {
    "A", "B" -> println("Good job!")
    "C" -> println("Not bad")
    else -> println("Need improvement")
}
```

### When with In

```kotlin
val score = 85

when (score) {
    in 90..100 -> println("A")
    in 80..89 -> println("B")
    in 70..79 -> println("C")
    else -> println("D")
}
```

### When with Is

```kotlin
val value: Any = "Hello"

when (value) {
    is String -> println("It's a string")
    is Int -> println("It's an integer")
    is Boolean -> println("It's a boolean")
    else -> println("Unknown type")
}
```

### When as If-Else Replacement

```kotlin
when {
    score >= 90 -> println("A")
    score >= 80 -> println("B")
    score >= 70 -> println("C")
    else -> println("D")
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔁 For Loop

### Loop Through Array

```kotlin
val names = arrayOf("John", "Jane", "Bob")

for (name in names) {
    println(name)
}
```

### Loop Through Range

```kotlin
for (i in 1..5) {
    println(i)  // 1, 2, 3, 4, 5
}

// Reverse
for (i in 5 downTo 1) {
    println(i)  // 5, 4, 3, 2, 1
}

// With step
for (i in 1..10 step 2) {
    println(i)  // 1, 3, 5, 7, 9
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## ⏰ While Loop

### While

```kotlin
var i = 1

while (i <= 5) {
    println(i)
    i++
}
```

### Do-While Loop

```kotlin
var i = 1

do {
    println(i)
    i++
} while (i <= 5)
```

**Note:** Do-While executes the block at least once before checking the condition.

[[#📑 Table of Contents|← Back to Contents]]

---

## ⛔ Break & Continue

### Break

```kotlin
for (i in 1..10) {
    if (i == 5) {
        break  // Stop the loop
    }
    println(i)  // Prints 1, 2, 3, 4
}
```

### Continue

```kotlin
for (i in 1..5) {
    if (i == 3) {
        continue  // Skip this iteration
    }
    println(i)  // Prints 1, 2, 4, 5
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## ⚙️ Function Basics

### Simple Function

```kotlin
fun sayHello() {
    println("Hello!")
}

// Call the function
sayHello()
```

### Function with Parameters

```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}

greet("Kotlin")  // Hello, Kotlin!
```

### Function with Multiple Parameters

```kotlin
fun sum(a: Int, b: Int) {
    println(a + b)
}

sum(5, 3)  // 8
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📥 Function Parameters

### Default Parameters

```kotlin
fun greet(name: String, greeting: String = "Hello") {
    println("$greeting, $name!")
}

greet("John")              // Hello, John!
greet("John", "Hi")        // Hi, John!
```

### Named Arguments

```kotlin
fun createUser(name: String, age: Int, country: String) {
    println("$name, $age, $country")
}

// With named arguments (order doesn't matter)
createUser(age = 25, name = "John", country = "USA")
```

### Varargs Parameters

```kotlin
fun sum(vararg numbers: Int): Int {
    var total = 0
    for (number in numbers) {
        total += number
    }
    return total
}

println(sum(1, 2, 3))           // 6
println(sum(1, 2, 3, 4, 5))     // 15
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📤 Return Types

### Unit (No Return Value)

```kotlin
fun sayHello(): Unit {
    println("Hello")
}

// Unit can be omitted
fun sayGoodbye() {
    println("Goodbye")
}
```

### Function with Return Value

```kotlin
fun add(a: Int, b: Int): Int {
    return a + b
}

val result = add(5, 3)  // 8
```

### Single Expression Function

```kotlin
// Traditional
fun multiply(a: Int, b: Int): Int {
    return a * b
}

// Single expression (return type inferred)
fun multiply(a: Int, b: Int) = a * b

// With explicit return type
fun divide(a: Int, b: Int): Int = a / b
```

### Return If/When

```kotlin
fun getGrade(score: Int): String = if (score >= 90) {
    "A"
} else if (score >= 80) {
    "B"
} else {
    "C"
}

fun getStatus(code: Int) = when (code) {
    200 -> "OK"
    404 -> "Not Found"
    500 -> "Server Error"
    else -> "Unknown"
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔧 Extension Functions

```kotlin
// Extend String class
fun String.hello(): String {
    return "Hello $this"
}

val name = "Kotlin"
println(name.hello())  // Hello Kotlin

// Extension with parameters
fun Int.times(message: String) {
    for (i in 1..this) {
        println(message)
    }
}

3.times("Hello")  // Prints "Hello" 3 times
```

**Note:** Use extension functions wisely as they can make code harder to understand if overused.

[[#📑 Table of Contents|← Back to Contents]]

---

## λ Lambda Expressions

### Basic Lambda

```kotlin
val message = { println("Hello Lambda") }
message()  // Execute lambda

// Lambda with parameters
val sum = { a: Int, b: Int -> a + b }
println(sum(5, 3))  // 8
```

### Lambda in Variable

```kotlin
val multiply: (Int, Int) -> Int = { a, b -> a * b }
println(multiply(4, 5))  // 20
```

### It Keyword

```kotlin
// When lambda has single parameter, use 'it'
val numbers = arrayOf(1, 2, 3, 4, 5)
numbers.forEach { println(it) }

// Explicit parameter name
numbers.forEach { number -> println(number) }
```

### Method References

```kotlin
fun isEven(number: Int): Boolean = number % 2 == 0

val numbers = arrayOf(1, 2, 3, 4, 5)
val evenNumbers = numbers.filter(::isEven)
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🎯 Higher-Order Functions

### Function as Parameter

```kotlin
fun calculate(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
    return operation(a, b)
}

val result1 = calculate(5, 3) { a, b -> a + b }  // 8
val result2 = calculate(5, 3) { a, b -> a * b }  // 15
```

### Trailing Lambda

```kotlin
// If lambda is last parameter, it can be outside parentheses
numbers.forEach { println(it) }

// Instead of
numbers.forEach({ println(it) })
```

[[#📑 Table of Contents|← Back to Contents]]

---

## ⚡ Inline Functions

```kotlin
inline fun repeat(times: Int, action: () -> Unit) {
    for (i in 1..times) {
        action()
    }
}

repeat(3) {
    println("Hello")
}

// Noinline parameter
inline fun process(
    inline action1: () -> Unit,
    noinline action2: () -> Unit
) {
    action1()
    action2()
}
```

**Benefits:** Avoids creating lambda objects repeatedly, improving performance.

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔄 Recursive Functions

### Basic Recursion

```kotlin
fun factorial(n: Int): Int {
    return if (n == 1) {
        1
    } else {
        n * factorial(n - 1)
    }
}

println(factorial(5))  // 120
```

### Tail Recursive Function

```kotlin
tailrec fun factorialTail(n: Int, result: Int = 1): Int {
    return if (n == 1) {
        result
    } else {
        factorialTail(n - 1, result * n)
    }
}

println(factorialTail(5))  // 120
```

**Note:** Tail recursion prevents stack overflow by converting recursion to loop.

**Execution Flow:**

```
// Regular recursion (builds stack)
factorial(5) => 5 * factorial(4) => 4 * factorial(3) => ...

// Tail recursion (optimized to loop)
factorialTail(5, 1) => factorialTail(4, 5) => factorialTail(3, 20) => ...
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 🏷️ Labels

### Creating Labels

```kotlin
loop@ for (i in 1..3) {
    for (j in 1..3) {
        println("$i $j")
        if (i == 2) break@loop  // Break outer loop
    }
}
```

### Break to Label

```kotlin
outer@ for (i in 1..3) {
    for (j in 1..3) {
        if (j == 2) break@outer
        println("$i $j")
    }
}
```

### Continue to Label

```kotlin
outer@ for (i in 1..3) {
    for (j in 1..3) {
        if (j == 2) continue@outer
        println("$i $j")
    }
}
```

### Return to Label

```kotlin
fun printNumbers() {
    listOf(1, 2, 3, 4, 5).forEach lit@{
        if (it == 3) return@lit  // Continue forEach
        println(it)
    }
    println("Done")
}
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📦 Package & Import

### Declaring Package

```kotlin
// File: com/example/utils/Helper.kt
package com.example.utils

fun sayHello() {
    println("Hello")
}
```

### Importing

```kotlin
// Import specific function
import com.example.utils.sayHello

// Import all from package
import com.example.utils.*

// Import with alias
import com.example.utils.sayHello as greet

fun main() {
    sayHello()
    greet()
}
```

**Convention:** Package names use lowercase letters, separated by dots for sub-packages.

[[#📑 Table of Contents|← Back to Contents]]

---

## 💬 Comments

```kotlin
// Single line comment

/*
   Multi-line comment
   Can span multiple lines
*/

/**
 * Documentation comment
 * Used for generating documentation
 * @param name The name parameter
 * @return The greeting string
 */
fun greet(name: String): String {
    return "Hello, $name"
}
```

**Best Practice:** The best comment is the code itself. Write self-documenting code.

[[#📑 Table of Contents|← Back to Contents]]

---

## 🎭 Anonymous Functions

```kotlin
val multiply = fun(a: Int, b: Int): Int {
    return a * b
}

println(multiply(4, 5))  // 20

// As parameter
fun calculate(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
    return operation(a, b)
}

val result = calculate(10, 5, fun(a, b) = a - b)
```

**Difference from Lambda:** Anonymous functions allow explicit return statements anywhere, while lambdas treat the last line as the return value.

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔐 Closure

```kotlin
fun createCounter(): () -> Int {
    var count = 0
    return {
        count++
        count
    }
}

val counter = createCounter()
println(counter())  // 1
println(counter())  // 2
println(counter())  // 3
```

**Definition:** Closure is the ability of a function/lambda to interact with data in the surrounding scope.

[[#📑 Table of Contents|← Back to Contents]]

---

## 🎯 Function Scope

```kotlin
fun outer() {
    val x = 10
    
    // Inner function (local function)
    fun inner() {
        println(x)  // Can access outer variable
    }
    
    inner()
}
```

**Scope Rules:**

- Functions at file level can be accessed from anywhere
- Functions inside other functions have limited scope
- Inner functions can access outer function variables

[[#📑 Table of Contents|← Back to Contents]]

---

## 🔗 Infix Notation

```kotlin
infix fun Int.times(str: String) = str.repeat(this)

println(3 times "Hello ")  // Hello Hello Hello 

// Without infix
println(3.times("Hello "))
```

**Requirements for Infix:**

- Must be member function or extension function
- Must have single parameter
- Parameter cannot be varargs or have default value

[[#📑 Table of Contents|← Back to Contents]]

---

## 🚀 Main Function Parameters

```kotlin
fun main(args: Array<String>) {
    if (args.isNotEmpty()) {
        println("Arguments: ${args.joinToString()}")
    }
}
```

**Run with arguments:**

```bash
kotlin MyProgram arg1 arg2 arg3
```

[[#📑 Table of Contents|← Back to Contents]]

---

## 📚 Next Topics

- **Kotlin Object Oriented Programming** - Classes, objects, inheritance
- **Kotlin Generic** - Generic types and functions
- **Kotlin Collection** - Lists, sets, maps
- **Kotlin Coroutine** - Asynchronous programming

---

## 🔗 Resources

- **Documentation:** [kotlinlang.org](https://kotlinlang.org/)
- **Playground:** [play.kotlinlang.org](https://play.kotlinlang.org/)
- **Tutorial by:** Eko Kurniawan Khannedy
    - Website: [programmerzamannow.com](https://www.programmerzamannow.com/)
    - YouTube: [Programmer Zaman Now](https://youtube.com/c/ProgrammerZamanNow)

---

_This cheat sheet is based on "Kotlin Dasar" by Eko Kurniawan Khannedy_

[[#📑 Table of Contents|← Back to Top]]